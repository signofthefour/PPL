
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_of_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType()))]                           
   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, c):
        [self.visit(x,c) for x in ast.decl]

    def visitVarDecl(self, ast, env):
        """
        Visit each global var top-down
        first layer in stack
        """
        name = self.visit(ast.variable, env)
        if name is not None:
            raise Redeclared(Variable(), name)
        dimen = ast.varDimen
        init_type = self.visit(ast.varInit, []) if ast.varInit else Unknown()
        if len(dimen):
            if not isinstance(init_type, (ArrayType, Unknown)):
                """
                Declaration of array with mismatch type is TypeMismatch
                or Type can not be infered
                """
                raise TypeMismatchInStatement(ast)
            
            if isinstance(init_type, ArrayType):
                if dimen != init_type.dimen:
                    raise TypeMismatchInStatement(ast)
                env = self.update_scope(env, Symbol(name, init_type))
            else:
                env = self.update_scope(env, Symbol(name, ArrayType(dimen, Unknown())))
        else:
            if isinstance(init_type, ArrayType):
                raise TypeMismatchInStatement(ast)
            env = self.update_scope(env, Symbol(name, init_type))

    def visitFuncDecl(self, ast, env):
        """
        docstring
        """
        name = self.visit(ast.name, env)
        if name is not None:
            raise Redeclared(Function(), name)
        try:
            param = reduce(lambda env, x: self.visit(x, env), ast.param, [])
        except Redeclared as e:
            raise Redeclared(Parameter(), e.n)

        scope_env = reduce(lambda env, x: self.visit(x, env), ast.body[0], param)
        cur_env = scope_env + env

        res_type = Unknown()
        [self.visit(x, cur_env) for x in ast.body[1]]
        param_list = [p for p in \
                        [x for x in cur_env if x.name in \
                            [y.name for y in param]]]

        function = Symbol(name, MType(param_list, res_type)) 
        self.update_scope(env, function)

    def visitArrayCell(self, ast, env):
        """
        For an array indexing E[E1]...[En], 
            E must be in array type with n dimensions and E1...En must be integer.
        """
        e = self.visit(ast.arr, env)
        if not isinstance(e, ArrayType):
            raise TypeMismatchInExpr(ast)
        e_i = [self.visit(x, env) for x in ast.idx]
        if any([not isinstance(x, IntType) for x in e_i]):
            raise TypeMismatchInExpr(ast)

    def visitBinaryOp(self, ast, env):
        """
        docstring
        """
        pass

    def visitUnaryOp(self, ast, env):
        """
        docstring
        """
        pass

    def visitCallExpr(self, ast, env):
        """
        docstring
        """
        func = self.visit(ast.method, env)
        if func is None:
            raise Undeclared(Function(), func)
        
        if len(func.mtype.intype) != len(ast.param):
            raise TypeMismatchInStmt(ast)
        
        args = [self.visit(arg, env) for arg in ast.param]
        match_type = list(map(lambda x, y: type(x) == type(y), args, func.mtype.intype))
        if any([not match for match in match_type]):
            raise TypeMismatchInStmt(ast)
        
    def visitIntLiteral(self, ast, env):
        return IntType()

    def visitStringLiteral(self, ast, env):
        return StringType()

    def visitBooleanLiteral(self, ast, env):
        return BoolType()

    def visitArrayLiteral(self, ast, env):
        type_of_arr = [self.visit(x,[]) for x in ast.value]
        if not len(type_of_arr):
            return ArrayType([0], Unknown())
        num_of_type = reduce(lambda count, x: count if self.is_same_type(x, type_of_arr[0]) else count + 1,\
            type_of_arr, 1)
        print(num_of_type)
        if  num_of_type == 1:
            """
            Same type for all elements in array
            """
            dimen = [len(type_of_arr)] if not isinstance(type_of_arr[0], ArrayType) else \
                    [len(type_of_arr)] + type_of_arr[0].dimen
            return ArrayType(dimen, type(type_of_arr[0]))
        else:
            raise InvalidArrayLiteral(ast)

    def visitAssign(self, ast, env):
        """
        lhs = rhs
        <Symbol> = <MType>
        """
        rhs = self.visit(rhs, env) # lhs is a Symbol
        lhs = self.visit(lhs, env) # rhs is a Mtype
        if type(rhs) == type(lhs.mtype):
            if isinstance(rhs, Unknown()):
                raise TypeCannotBeInferred(ast)
        else:
            if isinstance(lhs.mtype, Unknown()):
                lhs.mtype = rhs
            else:
                raise TypeMismatchInStmt(ast)

    def visitIf(self, ast, env):
        """
        docstring
        """
        con_expr = self.visit(ast.ifthenStmt[0][0]) # if condition
        scope = reduce(lambda env, x: self.visit(x, env), ast.ifthenStmt[0][1], []) # decl of if - idk why we need it for if :(
        if_env = env + scope
        [self.visit(stmt, if_env) for stmt in ast.ifthenStmt[1]]
        if len(ast.elseStmt):
            scope = reduce(lambda env, x: self.visit(x, env), ast.elseStmt[0], [])
            else_env = env + scope
            [self.visit(stmt, else_env) for stmt in ast.elseStmt]

    def visitFor(self, ast, env):
        """
        docstring
        """
        idx1 = self.visit(ast.idx1, env)
        if not isinstance(idx1, (IntType, Unknown)):
            raise TypeMismatchInStmt(ast)
        if isinstance(idx1, Unknown):
            idx1.mtype = IntType()

        init_expr = self.visit(ast.expr1, env)
        
                
    def visitBreak(self, ast, env):
        """
        docstring
        """
        pass

    def visitReturn(self, ast, env):
        """
        docstring
        """
        pass

    def visitDowhile(self, ast, env):
        """
        docstring
        """
        pass

    def visitWhile(self, ast, env):
        """
        docstring
        """
        pass

    def visitCallStmt(self, ast, env):
        """
        docstring
        """
        pass

    def visitId(self, ast, env):
        """
        docstring
        """
        id_list = [sym.name for sym in env]
        if id_list == []:
            return None
        else:
            return id_list[0]

    def is_same_type(self, a, b):
        if type(a) != type(b):
            return False
        else:
            if isinstance(a, ArrayType):
                if a.dimen != b.dimen:
                    return False
        return True

    def update_scope(self, scope, var):
        """
        stack-like
        """
        return [var] + scope