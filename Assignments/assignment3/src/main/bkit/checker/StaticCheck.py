
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
    

    def visitProgram(self,ast,c):
        """
        Phase 1:
            -> visit all declaration -> create a stack base frame
            ERROR: Redeclared, NoEntryPoint
        Phase 2:
            -> inference the type by visit function.scope
            ERROR: Undeclare, TypeMismatchInExpression, TypeMismatchInStatement
                    TypeCannotBeInferred
        """
        global_scope = reduce(lambda env, x: env + [self.visitGlobal(x, env)], ast.decl, c)
        self.env = global_scope
        [self.visit(x,self.env) for x in ast.decl]

    def visitVarDecl(self, ast, c):
        """
        Visit each global var top-down
        first layer in stack
        """
        symbol = self.visit(ast.variable, c)
        if symbol is None:
            symbol = Symbol(ast.variable.name, Unknown())
        if symbol.mtype is not None:
            raise Redeclared(Variable(), symbol.name)
        dimen = ast.varDimen
        init_type = self.visit(ast.varInit, []) if ast.varInit else Symbol('', Unknown())
        if len(dimen):
            if not isinstance(init_type.mtype, (ArrayType, Unknown)):
                """
                Declaration of array with mismatch type is TypeMismatch
                or Type can not be infered
                """
                raise TypeMismatchInStatement(ast)
            
            if isinstance(init_type.mtype, ArrayType):
                if dimen != init_type.mtype.dimen:
                    raise TypeMismatchInStatement(ast)
                symbol.mtype = init_type.mtype
                c = self.update_scope(c, symbol)
            else:
                symbol.mtype = ArrayType(dimen, Unknown())
                c = self.update_scope(c, symbol)
        else:
            if isinstance(init_type.mtype, ArrayType):
                raise TypeMismatchInStatement(ast)
            symbol.mtype = init_type.mtype
            c = self.update_scope(c, symbol)

    def visitFuncDecl(self, ast, env):
        """
        docstring
        """
        symbol = self.visit(ast.name, env)
        param = []
        if symbol is None:
            raise Undeclared(Function(), ast.name)
        try:
            param = reduce(lambda env, x: env + [self.visit(x, env)], ast.param, [])
        except Redeclared as e:
            raise Redeclared(Parameter(), e.n)

        scope_env = reduce(lambda env, x: env + [self.visit(x, env)], ast.body[0], param)
        cur_env = scope_env + env

        res_type_list = [self.visit(x, cur_env) for x in ast.body[1]]
        res_type = VoidType()
        for typ in res_type_list:
            if typ is not None:
                res_type = typ
                break
        param_list = [p for p in \
                        [x for x in cur_env if x.name in \
                            [y.name for y in param]]]

        symbol.mtype = MType(param_list, res_type)

    def visitArrayCell(self, ast, env):
        """
        For an array indexing E[E1]...[En], 
            E must be in array type with n dimensions and E1...En must be integer.
        Input: All arraycell must be declared in vardecl, so there no redeclared
        """
        e = self.visit(ast.arr, env)
        if e is None:
            raise Undeclared(Identifier(), ast.arr)
        if not isinstance(e.mtype, (ArrayType,MType)):
            raise TypeMismatchInExpression(ast)
        if isinstance(e.mtype, ArrayType):
            if len(e.mtype.dimen) != len(ast.idx):
                raise TypeMismatchInExpression(ast)
        if isinstance(e.mtype, MType):
            if isinstance(e.mtype.restype, type(None)):
                e.mtype.restype = ArrayType([0]*len(ast.idx), Unknown())
            if len(e.mtype.restype.dimen) != len(ast.idx):
                raise TypeMismatchInExpression(ast)
        e_i = [self.visit(x, env) for x in ast.idx]
        if any([not isinstance(x.mtype, IntType) for x in e_i]):
            raise TypeMismatchInExpression(ast)
        
        return e
        

    def visitBinaryOp(self, ast, env):
        """
        ==, ! =, <, >, <=, >=, = / =, < ., > ., <= ., >= .
        """
        # RELATIONAL
        ## Int
        ltype = rtype = None
        if ast.op in ['==', '!=', '<', '>', '>=', '<=']:
            l = self.visit(ast.left, env)
            if l is None:
                raise Undeclared(Identifer(), ast.left.name)
            if isinstance(l.mtype, Unknown):
                l.mtype = IntType()
            ltype = l.mtype
            if isinstance(l.mtype, ArrayType):
                if isinstance(l.mtype.eletype, Unknown):
                    l.mtype.eletype = IntType()
                ltype = l.mtype.eletype
            if isinstance(l.mtype, MType):
                if isinstance(l.mtype.retype, Unknown):
                    l.mtype.restype = IntType()
                ltype = l.mtype.restype
            r = self.visit(ast.right, env)
            if r is None:
                raise Undeclared(Identifier(), ast.right.name)
            if isinstance(r.mtype, Unknown):
                r.type = IntType()
            rtype = r.mtype
            if isinstance(r.mtype, ArrayType):
                if isinstance(r.mtype.eletype, Unknown):
                    r.mtype.eletype = IntType()
                rtype = r.mtype.eletype
            if isinstance(r.mtype, MType):
                if isinstance(r.mtype.restype, Unknown):
                    r.mtype.restype = IntType()
                rtype = r.mtype.restype
            if not isinstance(ltype, IntType) or not isinstance(rtype, IntType):
                raise TypeMismatchInExpr(ast)
            return Symbol('', BoolType())
        ## Float
        if ast.op in ['=/=', '<.', '>.', '>=.', '<=.']: 
            l = self.visit(ast.left, env)
            if l is None:
                raise Undeclared(Identifer(), ast.left.name)
            if isinstance(l.mtype, Unknown):
                l.mtype = FloatType()
            ltype = l.mtype
            if isinstance(l.mtype, ArrayType):
                if isinstance(l.mtype.eletype, Unknown):
                    l.mtype.eletype = FloatType()
                ltype = l.mtype.eletype
            if isinstance(l.mtype, MType):
                if isinstance(l.mtype.retype, Unknown):
                    l.mtype.restype = FloatType()
                ltype = l.mtype.restype

            r = self.visit(ast.right, env)
            if r is None:
                raise Undeclared(Identifier(), ast.right.name)
            if isinstance(r.mtype, Unknown):
                r.type = FloatType()
            rtype = r.mtype
            if isinstance(r.mtype, ArrayType):
                if isinstance(r.mtype.eletype, Unknown):
                    r.mtype.eletype = FloatType()
                rtype = r.mtype.eletype
            if isinstance(r.mtype, MType):
                if isinstance(r.mtype.restype, Unknown):
                    r.mtype.restype = FloatType()
                rtype = r.mtype.restype
            if not isinstance(ltype, FloatType) or not isinstance(rtype, FloatType):
                raise TypeMismatchInExpr(ast)
            
            return Symbol('', BoolType())
        
        # BOOLEAN
        if ast.op in ['&&' , '||']:
            l = self.visit(ast.left, env)
            if l is None:
                raise Undeclared(Identifer(), ast.left.name)
            if isinstance(l.mtype, Unknown):
                l.mtype = BoolType()
            ltype = l.mtype
            if isinstance(l.mtype, ArrayType):
                if isinstance(l.mtype.eletype, Unknown):
                    l.mtype.eletype = BoolType()
                ltype = l.mtype.eletype
            if isinstance(l.mtype, MType):
                if isinstance(l.mtype.retype, Unknown):
                    l.mtype.restype = BoolType()
                ltype = l.mtype.restype
            r = self.visit(ast.right, env)
            if r is None:
                raise Undeclared(Identifier(), ast.right.name)
            if isinstance(r.mtype, Unknown):
                r.type = BoolType()
            rtype = r.mtype
            if isinstance(r.mtype, ArrayType):
                if isinstance(r.mtype.eletype, Unknown):
                    r.mtype.eletype = BoolType()
                rtype = r.mtype.eletype
            if isinstance(r.mtype, MType):
                if isinstance(r.mtype.restype, Unknown):
                    r.mtype.restype = BoolType()
                rtype = r.mtype.restype
            if not isinstance(ltype, BoolType) or not isinstance(rtype, BoolType):
                raise TypeMismatchInExpr(ast)
            
            return Symbol('', BoolType())
        
        # ARITHMETIC
        ## Int
        if ast.op in ['-' , '+', '*', '\\']:
            l = self.visit(ast.left, env)
            if l is None:
                raise Undeclared(Identifer(), ast.left.name)
            if isinstance(l.mtype, Unknown):
                l.mtype = IntType()
            ltype = l.mtype
            if isinstance(l.mtype, ArrayType):
                if isinstance(l.mtype.eletype, Unknown):
                    l.mtype.eletype = IntType()
                ltype = l.mtype.eletype
            if isinstance(l.mtype, MType):
                if isinstance(l.mtype.retype, Unknown):
                    l.mtype.restype = IntType()
                ltype = l.mtype.restype
            r = self.visit(ast.right, env)
            if r is None:
                raise Undeclared(Identifier(), ast.right.name)
            if isinstance(r.mtype, Unknown):
                r.type = IntType()
            rtype = r.mtype
            if isinstance(r.mtype, ArrayType):
                if isinstance(r.mtype.eletype, Unknown):
                    r.mtype.eletype = IntType()
                rtype = r.mtype.eletype
            if isinstance(r.mtype, MType):
                if isinstance(r.mtype.restype, Unknown):
                    r.mtype.restype = IntType()
                rtype = r.mtype.restype
            if not isinstance(ltype, IntType) or not isinstance(rtype, IntType):
                raise TypeMismatchInExpr(ast)
            
            return Symbol('', IntType())
        
        ## Float
        if ast.op in ['-.' , '+.', '*.', '\\.']:
            l = self.visit(ast.left, env)
            if l is None:
                raise Undeclared(Identifer(), ast.left.name)
            if isinstance(l.mtype, Unknown):
                l.mtype = FloatType()
            ltype = l.mtype
            if isinstance(l.mtype, ArrayType):
                if isinstance(l.mtype.eletype, Unknown):
                    l.mtype.eletype = FloatType()
                ltype = l.mtype.eletype
            if isinstance(l.mtype, MType):
                if isinstance(l.mtype.retype, Unknown):
                    l.mtype.restype = FloatType()
                ltype = l.mtype.restype
                
            r = self.visit(ast.right, env)
            if r is None:
                raise Undeclared(Identifier(), ast.right.name)
            if isinstance(r.mtype, Unknown):
                r.type = FloatType()
            rtype = r.mtype
            if isinstance(r.mtype, ArrayType):
                if isinstance(r.mtype.eletype, Unknown):
                    r.mtype.eletype = FloatType()
                rtype = r.mtype.eletype
            if isinstance(r.mtype, MType):
                if isinstance(r.mtype.restype, Unknown):
                    r.mtype.restype = FloatType()
                rtype = r.mtype.restype

            if not isinstance(ltype, FloatType) or not isinstance(rtype, FloatType):
                raise TypeMismatchInExpr(ast)
            
            return Symbol('', FloatType())

    def visitUnaryOp(self, ast, env):
        """
        docstring
        """
        # ARITHMETIC
        ## Int
        otype = None
        if ast.op in ['-']:
            operand = self.visit(ast.body, env)
            if operand is None:
                raise Undeclared(Identifier, ast.body.name)
            if isinstance(operand.mtype, Unknown):
                operand.mtype = IntType()
            otype = operand.mtype
            if isinstance(operand.mtype, ArrayType):
                if isinstance(operand.mtype.eletype, Unknown):
                    operand.mtype.eletype = IntType()
                otype = operand.mtype.eletype
            if isinstance(operand.mtype, MType):
                if isinstance(operand.mtype.retype, Unknown):
                    operand.mtype.restype = IntType()
                otype = operand.mtype.restype
            if not isinstance(otype, IntType):
                raise TypeMismatchInExpression(ast)
            return Symbol('', IntType())
        ## Float
        if ast.op in ['-.']:
            operand = self.visit(ast.body, env)
            if operand is None:
                raise Undeclared(Identifier, ast.body.name)
            if isinstance(operand.mtype, Unknown):
                operand.mtype = FloatType()
            otype = operand.mtype
            if isinstance(operand.mtype, ArrayType):
                if isinstance(operand.mtype.eletype, Unknown):
                    operand.mtype.eletype = FloatType()
                otype = operand.mtype.eletype
            if isinstance(operand.mtype, MType):
                if isinstance(operand.mtype.retype, Unknown):
                    operand.mtype.restype = FloatType()
                otype = operand.mtype.restype
            if not isinstance(otype, FloatType):
                raise TypeMismatchInExpression(ast)

            return Symbol('', FloatType())

        # BOOLEAN
        if ast.op in ['!']:
            operand = self.visit(ast.body, env)
            if operand is None:
                raise Undeclared(Identifier, ast.body.name)
            if isinstance(operand.mtype, Unknown):
                operand.type = BoolType()
            otype = operand.mtype
            if isinstance(operand.mtype, ArrayType):
                if isinstance(operand.mtype.eletype, Unknown):
                    operand.mtype.eletype = BoolType()
                otype = operand.mtype.eletype
            if isinstance(operand.mtype, MType):
                if isinstance(operand.mtype.retype, Unknown):
                    operand.mtype.restype = BoolType()
                otype = operand.mtype.restype

            if isinstance(otype, BoolType):
                raise TypeMismatchInExpression(ast)
            return Symbol('', BoolType())

    def visitCallExpr(self, ast, env):
        """
        Return type of call expr is inferred when it call by the 
            parent operand (can be infer from op)
            assignment (can be infer from assign statement)
        """
        func = self.visit(ast.method, env)
        if func is None or not isinstance(func.mtype,  (MType, type(None))):
            raise Undeclared(Function(), ast.method.name)
        if func.mtype is None:
            args = [self.visit(arg, env) for arg in ast.param]
            if any([isinstance(arg, (Unknown, type(None))) for arg in args]):
                raise TypeCannotBeInferred(ast)
            func.mtype = MType(args, Unknown())
            return func

        if len(func.mtype.intype) != len(ast.param):
            raise TypeMismatchInStatement(ast)
         
        args = [self.visit(arg, env) for arg in ast.param]
        if any([isinstance(arg, (Unknown, type(None))) for arg in args]):
            raise TypeCannotBeInferred(ast)
        match_type = list(map(lambda x, y: type(x) == type(y), args, func.mtype.intype))
        if any([not match for match in match_type]):
            raise TypeMismatchInStatement(ast)
        return func
        
    def visitIntLiteral(self, ast, env):
        return Symbol('', IntType())

    def visitStringLiteral(self, ast, env):
        return Symbol('', StringType())

    def visitBooleanLiteral(self, ast, env):
        return Symbol('', BoolType())
    
    def visitFloatLiteral(self, ast, env):
        return Symbol('', BoolType())

    def visitArrayLiteral(self, ast, env):
        type_of_arr = [self.visit(x,[]) for x in ast.value]
        if not len(type_of_arr):
            return Symbol('',ArrayType([0], Unknown()))
        num_of_type = reduce(lambda count, x: count if self.is_same_type(x, type_of_arr[0]) else count + 1,\
            type_of_arr, 1)
        if  num_of_type == 1:
            """
            Same type for all elements in array
            """
            dimen = [len(type_of_arr)] if not isinstance(type_of_arr[0], ArrayType) else \
                    [len(type_of_arr)] + type_of_arr[0].dimen
            return Symbol('',ArrayType(dimen, type(type_of_arr[0])))
        else:
            raise InvalidArrayLiteral(ast)

    def visitAssign(self, ast, env):
        """
        lhs = rhs
        <Symbol> = <Symbol>
        Can we assign VoidType to VoidType
        """
        rtype = ltype = None
        rhs = self.visit(rhs, env)
        if rhs is None:
            raise Undeclared(Identifier(), rhs.name)

        lhs = self.visit(lhs, env)
        if lhs is None:
            raise Undeclared(Identifier(), lhs.name)
        
        # there will be 9 case:

        # MTYPE = MTYPE
        if isinstance(lhs.mtype, MType) and isinstance(rhs.mtype, MType):
            if isinstance(rhs.mtype.restype, Unknown):
                rhs.mtype.restype = lhs.mtype
            if isinstance(lhs.mtype.restype, Unknown):
                lhs.mtype.restype = rhs.mtype
            if isinstance(lhs.mtype.restype, Unknown):
                raise TypeCannotBeInferred(ast)
        
        # ARRAY = MTYPE
        if isinstance(lhs.mtype, ArrayType) and isinstance(rhs.mtype, MType):
            if isinstance(rhs.mtype.restype, Unknown):
                rhs.mtype.restype = lhs.mtype.eletype
            if isinstance(lhs.mtype.eletype, Unknown):
                lhs.mtype.eletype = rhs.mtype.restype
            if isinstance(lhs.mtype.eletype, Unknown):
                raise TypeCannotBeInferred(ast)
        
        # PRIM = MTYPE
        if isinstance(lhs.mtype, (Prim, Unknown)) and isinstance(rhs.mtype, MType):
            if isinstance(rhs.mtype.restype, Unknown):
                rhs.mtype.restype = lhs.mtype
            if isinstance(lhs.mtype, Unknown):
                lhs.mtype = rhs.mtype.restype
            if isinstance(lhs.mtype, Unknown):
                raise TypeCannotBeInferred(ast)
        
        # MTYPE = ARRAY
        if isinstance(lhs.mtype, MType) and isinstance(rhs.mtype, ArrayType):
            if isinstance(lhs.mtype.restype, Unknown):
                lhs.mtype.restype = rhs.mtype.eletype
            if isinstance(rhs.mtype.eletype):
                rhs.mtype.eletype = lhs.mtype.restype
            if isinstance(lhs.mtype.restype, Unknown):
                raise TypeCannotBeInferred(ast)
        
        # ARRAY = ARRAY
        if isinstance(lhs.mtype, ArrayType) and isinstance(rhs.mtype, ArrayType):
            if isinstance(lhs.mtype.eletype, Unknown):
                lhs.mtype.eletype = rhs.mtype.eletype
            if isinstance(rhs.mtype.eletype, Unknown):
                rhs.mtype.eletype = lhs.mtype.eletype
            if isinstance(rhs.mtype.eletype, Unknown):
                raise TypeCannotBeInferred(ast)
        
        # PRIM = ARRAY
        if isinstance(lhs.mtype, (Prim, Unknown)) and isinstance(rhs.mtype, ArrayType):
            if isinstance(lhs.mtype, Unknown):
                lhs.mtype = rhs.mtype.eletype
            if isinstance(rhs.mtype.eletype, Unknown):
                rhs.mtype.eletype = lhs.mtype
            if isinstance(lhs.mtype, Unknown):
                raise TypeCannotBeInferred(ast)
        
        # MTYPE = PRIM
        if isinstance(lhs.mtype, MType) and isinstance(rhs.mtype, (Prim, Unknown)):
            if isinstance(lhs.mtype.restype, Unknown):
                lhs.mtype.restype = rhs.mtype
            if isinstance(rhs.mtype, Unknown):
                rhs.mtype =  lhs.mtype.restype
            if isinstance(rhs.mtype, Unknown):
                raise TypeCannotBeInferred(ast)
        
        # ARRAY = PRIM
        if isinstance(lhs.mtype, ArrayType) and isinstance(rhs.mtype, (Prim, Unknown)):
            if isinstance(lhs.mtype.eletype, Unknown):
                lhs.mtype.eletype = rhs.mtype
            if isinstance(rhs.mtype, Unknown):
                rhs.mtype = lhs.mtype.eletype
            if isinstance(rhs.mtype, Unknown):
                raise TypeCannotBeInferred(ast)
        
        # PRIM = PRIM
        if isinstance(lhs.mtype, (Prim, Unknown)) and isinstance(rhs.mtype, (Prim, Unknown)):
            if isinstance(lhs.mtype, Unknown):
                lhs.mtype = rhs.mtype
            if isinstance(rhs.mtype, Unknown):
                rhs.mtype = lhs.mtype
            if isinstance(lhs.mtype, Unknown):
                raise TypeCannotBeInferred(ast)
            rtype = rhs.mtype.restype
        
        return None

    def visitIf(self, ast, env):
        """
        scope_type statement
        """
        con_expr = self.visit(ast.ifthenStmt[0][0]) # if condition
        con_val = None
        if con_expr is None:
            if isinstance(ast.ifthenStmt[0][0], Id):
                raise Undeclared(Identifier(), ast.ifthenStmt[0][0].name)
            # for call_expr and call_stmt: it raise exception when visit call_
            # so we do not need to handle it here

        if isinstance(con_expr.mtype, (Prim, Unknown)):
            if isinstance(con_expr.mtype, Unknown):
                con_expr.mtype = BoolType()
            con_val = con_expr.mtype

        if isinstance(con_expr.mtype, ArrayType):
            if isinstance(con_expr.mtype.eletype, Unknown):
                con_expr.mtype.eletype = BoolType()
            con_val = con_expr.mtype.eletype
            
        if isinstance(con_expr.mtype, Mtype):
            if isinstance(con_expr.mtype.restype, Unknown):
                con_expr.mtype.restype = BoolType()
            con_val = con_expr.mtype.restype

        if not isinstance(con_val, BoolType):
            raise TypeMismatchInStatement(ast)

        scope = reduce(lambda y, x: y + [self.visit(x, y)], ast.ifthenStmt[0][1], []) 
        if_env = scope + env
        [self.visit(stmt, if_env) for stmt in ast.ifthenStmt[1]]
        env = if_env[len(scope):]
        if len(ast.elseStmt):
            scope = reduce(lambda env, x: env + [self.visit(x, env)], ast.elseStmt[0], [])
            else_env = env + scope
            [self.visit(stmt, else_env) for stmt in ast.elseStmt]
            env = else_env[len(scope):]

    def visitFor(self, ast, env):
        """
        Check if all has the same type as spec
        """
        idx1 = self.visit(ast.idx1, env)
        if idx1 is None:
            raise Undeclared(Identifier(), ast.idx1.name)
        if isinstance(idx1.mtype, ""
        /
        /''):
            raise TypeMismatchInStatement(ast)
        if isinstance(idx1.mtype, Unknown):
            idx1.mtype = IntType()

        init_expr = self.visit(ast.expr1, env)
        if init_expr is None:
            raise Undeclared(Identifier(), ast.expr1.name)
        if not isinstance(init_expr.mtype, (IntType, Unknown)):
            raise TypeMismatchInStatment(ast)
        if isinstance(init_expr.mtype, Unknown):
            init_expr.mtype = IntType()

        con_expr = self.visit(ast.expr2, env)
        if con_expr is None:
            raise Undeclared(Identifier(), ast.expr2.name)
        if not isinstance(con_expr.mtype, (BoolType, Unknown)):
            raise TypeMismatchInStatement(ast)
        if isinstance(con_expr.mtype, Unknown):
            con_expr.mtype = BoolType()
        
        update_expr = self.visit(ast.expr3, env)
        if update_expr is None:
            raise Undeclared(Identifier(), ast.expr3.name)
        if not isinstance(update_expr.mtype, (IntType, Unknown)):
            raise TypeMismatchInStatement(ast)
        if isinstance(update_expr.mtype, Unknown):
            update_expr.mtype = IntType()

        scope = reduce(lambda env, x: env + [self.visit(x, env)], ast.loop[0], [])
        cur_env = scope + env
        [(idx, self.visit(x, cur_env)) for (idx, x) in enumerate(ast.loop[1])]
        env = cur_env[len(scope) :]
                
    def visitBreak(self, ast, env):
        """
        Do not care about unreachablestmt
        """
        return None

    def visitReturn(self, ast, env):
        """
        TODO: check the type of this return stmt and the type of function return
        """
        return self.visit(ast.expr, env)

    def visitDowhile(self, ast, env):
        """
        docstring
        """
        scope = reduce(lambda env, x: env + [self.visit(x, env)], ast.sl[0], [])
        cur_env = scope + env
        [self.visit(x, cur_env) for x in ast.sl[1]]
        expr = self.visit(ast.exp, env)
        if expr is None:
            raise Undeclared(Identifier(), ast.exp.name)
        if isinstance(expr.mtype, Unknown()):
            expr.mtype = BoolType()
        if not isinstance(expr, BoolType()):
            raise TypeMismatchInStatement(ast)
        
        env = cur_env[len(scope) :]
        return None
        

    def visitWhile(self, ast, env):
        """
        Same with Dowhile?
        """
        expr = self.visit(ast.exp, env)
        if expr is None:
            raise Undeclared(Identifier(), ast.exp.name)
        if isinstance(expr.mtype, Unknown()):
            expr.mtype = BoolType()
        if not isinstance(expr.mtype, BoolType()):
            raise TypeMismatchInStatement(ast)
        scope = reduce(lambda env, x: env + [self.visit(x, env)], ast.sl[0], [])
        cur_env = scope + env
        [self.visit(x, cur_env) for x in ast.sl[1]]
        env = cur_env[len(scope) :]
        return None

    def visitCallStmt(self, ast, env):
        """
        docstring
        """
        method_ref = self.visit(ast.method, env)
        if method_ref == None or not isinstance(method_ref.mtype, MType):
            raise Undeclared(Function(), ast.method.name)
        args_type = [self.visit(x, env) for x in ast.param] # from call statement
        param_type = method_ref.intype # from function declaration
        both_unknown_type = list(map(lambda x, y: isinstance(x, Unknown) and isinstance(y,Unknown),\
                                    args_type, param_type))
        if any(both_unknown_type):
            raise TypeCannotBeInferred(ctx)
        # inference type of param & args
        args_type = list(map(lambda x: args_type[x[0]] if isinstance(args_type[x[0]], Unknown) \
                                    else param_type[x[0]], list(enumerate(args_type))))
        
        param_type = list(map(lambda x: param_type[x[0]] if isinstance(args_type[x[0]], Unknown) \
                                    else args_type[x[0]], list(enumerate(args_type))))

        unmatch_type = list(map(lambda x, y: type(x) != type(y), args_type, param_type))
        if any(unmatch_type):
            raise TypeMismatchInStatement(ast)

    def visitId(self, ast, c):
        """
        return: Symbol(name=id.name, mtype=None)
        """
        for sym in c:
            if sym.name == ast.name:
                return sym
        return None

    def is_same_type(self, a, b):
        if type(a) != type(b):
            return False
        else:
            if isinstance(a, ArrayType):
                if a.dimen != b.dimen:
                    return False
        return True
    
    def visitGlobal(self,ast,c):
        if isinstance(ast, FuncDecl):
            for x in c:
                if x.name == ast.name.name:
                    raise Redeclared(Function(), x.name)
            return Symbol(ast.name.name, None)
        if isinstance(ast, VarDecl):
            for x in c:
                if x.name == ast.variable.name:
                    raise Redeclared(Variable(), x.name)
            return Symbol(ast.variable.name, MType([], None)))

    def update_scope(self, scope, var):
        """
        stack-like
        """
        return [var] + scope