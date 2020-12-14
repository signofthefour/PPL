
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
        global_scope = reduce(lambda env, x: [self.visitGlobal(x, env)] + env, ast.decl, c)
        self.env = global_scope
        self.hasEntryPoint = False
        [self.visit(x,self.env) for x in ast.decl]
        if self.hasEntryPoint == False:
            raise NoEntryPoint()

    def visitVarDecl(self, ast, c):
        """
        Visit each global var top-down
        """
        symbol = self.visit(ast.variable, c)
        if symbol is None:
            symbol = Symbol(ast.variable.name, None)
        if symbol.mtype is not None:
            raise Redeclared(Variable(), symbol.name)
        symbol.mtype = Unknown()
        dimen = list(ast.varDimen)
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
                return symbol
            else:
                symbol.mtype = ArrayType(dimen, Unknown())
                return symbol
        else:
            if isinstance(init_type.mtype, ArrayType):
                raise TypeMismatchInStatement(ast)
            symbol.mtype = init_type.mtype
            
            return symbol

    def visitFuncDecl(self, ast, env):
        """
        docstring
        """
        symbol = self.visit(ast.name, env)
        if symbol.name == 'main':
            self.hasEntryPoint = True
        param = []
        try:
            param = reduce(lambda env, x: [self.visit(x, env)] +  env, ast.param, [])
        except Redeclared as e:
            raise Redeclared(Parameter(), e.n)
        if len(symbol.mtype.intype) != len(param):
            raise TypeMismatchInExpression(ast)
        if len(symbol.mtype.intype):
            if symbol.mtype.intype[0]:
                print(len(param))
                print(ast)
                # Was inferred (was inferred in somewhere before visit)
                for idx in range(len(param)):
                    if isinstance(symbol.mtype.intype[idx].mtype, MType):
                        param[idx].mtype = symbol.mtype.intype[idx].mtype.restype 
                    else:
                        param[idx].mtype = symbol.mtype.intype[idx].mtype

        scope_env = reduce(lambda env, x: [self.visit(x, env)] + env, ast.body[0], param)
        cur_env = scope_env + env

        res_type_list = [self.visit(x, cur_env) for x in ast.body[1]]
        res_type = VoidType()
        for (idx, typ) in enumerate(res_type_list):
            if typ is not None:
                if not symbol.mtype.restype:
                    symbol.mtype.restype = typ
                if type(symbol.mtype.restype) != type(typ):
                    raise TypeMismatchInStatement(ast.body[1])
        
        param_list = cur_env[len(scope_env) - len(param): len(scope_env)]
        
        symbol.mtype.intype = param_list
        # print('sym_name: {}, sym_type: {}'.format(symbol.name, symbol.mtype))

    def visitArrayCell(self, ast, env):
        """
        For an array indexing E[E1]...[En], -
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
                raise TypeMismatchInExpression(ast)
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
                raise TypeMismatchInExpression(ast)
            
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
                raise TypeMismatchInExpression(ast)
            
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
                raise TypeMismatchInExpression(ast)
            
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
                raise TypeMismatchInExpression(ast)
            
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
        if func is None or not isinstance(func.mtype, MType):
            raise Undeclared(Function(), ast.method.name)
        if len(func.mtype.intype) != len(ast.param):
            raise TypeMismatchInStatement(ast)
        args = [self.visit(arg, env) for arg in ast.param]
        for (idx, arg) in enumerate(ast.param):
            arg_sym = self.visit(arg, env) # arg_type: Symbol
            arg_type = Unknown()
            is_arr = False
            if isinstance(arg_sym.mtype, (Prim, Unknown)):
                arg_type = arg_sym.mtype
            if isinstance(arg_sym.mtype, MType):
                arg_type = arg_sym.mtype.restype
            if isinstance(arg_sym.mtype, ArrayType):
                arg_type = arg_sym.mtype.eletype
                is_arr = True
            if isinstance(arg_type, Unknown):
                if func.mtype.intype[idx] == None:
                    raise TypeCannotBeInferred(ast)
                if isinstance(func.mtype.intype[idx].mtype, Prim):
                    if isinstance(func.mtype.intype[idx].mtype, Unknown):
                        raise TypeCannotBeInferred(ast)
                    arg_type = func.mtype.intype[idx].mtype
                if isinstance(func.mtype.intype[idx].mtype, MType):
                    if isinstance(func.mtype.intype[idx].mtype.restype, Unknown):
                        raise TypeCannotBeInferred(ast)
                    arg_type = func.mtype.intype[idx].mtype.restype
                if isinstance(func.mtype.intype[idx].mtype, ArrayType):
                    if not is_arr:
                        raise TypeMismatchInExpression(ast)
                    if isinstance(func.mtype.intype[idx].mtype.eletype, Unknown):
                        raise TypeCannotBeInferred(ast)
                    arg_type = func.mtype.intype[idx].mtype.eletype
                    
            else: # arg_type is known
                # print(func.mtype.intype[idx])
                # print(arg_sym)
                if func.mtype.intype[idx] == None:
                    func.mtype.intype[idx] = arg_sym
                if isinstance(func.mtype.intype[idx].mtype, (Unknown,Prim)):
                    if isinstance(func.mtype.intype[idx].mtype, Unknown):
                        func.mtype.intype[idx].mtype = arg_type
                    if type(func.mtype.intype[idx].mtype) != type(arg_type):
                        raise TypeMismatchInExpression(ast)
                if isinstance(func.mtype.intype[idx].mtype, MType):
                    if isinstance(func.mtype.intype[idx].mtype.restype, Unknown):
                        func.mtype.intype[idx].mtype.restype = arg_type
                    if type(func.mtype.intype[idx].mtype.restype) != type(arg_type):
                        raise TypeMismatchInExpression(ast)
                if isinstance(func.mtype.intype[idx].mtype, ArrayType):
                    if not is_arr:
                        raise TypeMismatchInExpression(ast)
                    if isinstance(func.mtype.intype[idx].mtype.eletype, Unknown):
                        func.mtype.intype[idx].mtype.eletype = arg_type
                    if type(func.mtype.intype[idx].mtype.eletype) != type(arg_type):
                        raise TypeMismatchInExpression(ast)
                    if type(func.mtype.intype[idx]) != type(arg_sym):
                        # array type not match
                        raise TypeMismatchInExpression(ast)
                
            if isinstance(arg_sym.mtype, (Prim, Unknown)):
                arg_sym.mtype =  arg_type
            if isinstance(arg_sym.mtype, MType):
                arg_sym.mtype.restype = arg_type
            if isinstance(arg_sym.mtype, ArrayType):
                arg_sym.mtype.eletype = arg_type
        if func.mtype.restype == None:
            func.mtype.restype = Unknown()
        return func
        
    def visitIntLiteral(self, ast, env):
        return Symbol('', IntType())

    def visitStringLiteral(self, ast, env):
        return Symbol('', StringType())

    def visitBooleanLiteral(self, ast, env):
        return Symbol('', BoolType())
    
    def visitFloatLiteral(self, ast, env):
        return Symbol('', FloatType())

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
            curr_dimen = [len(type_of_arr)]
            last_dimen = type_of_arr[0].mtype.dimen if isinstance(type_of_arr[0].mtype, ArrayType) else []
            dimen = curr_dimen + last_dimen
            typ = type_of_arr[0].mtype.eletype if isinstance(type_of_arr[0].mtype, ArrayType) else type_of_arr[0].mtype
            return Symbol('',ArrayType(dimen, typ))
        else:
            raise InvalidArrayLiteral(ast)

    def visitAssign(self, ast, env):
        """
        lhs = rhs
        <Symbol> = <Symbol>
        Can we assign VoidType to VoidType
        """
        rtype = ltype = None
        rhs = self.visit(ast.rhs, env)
        if rhs is None:
            raise Undeclared(Identifier(), rhs.name)

        lhs = self.visit(ast.lhs, env)
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
            if type(lhs.mtype.restype) != type(rhs.mtype.restype):
                raise TypeMismatchInStatement(ast)
        
        # ARRAY = MTYPE
        if isinstance(lhs.mtype, ArrayType) and isinstance(rhs.mtype, MType):
            if isinstance(rhs.mtype.restype, Unknown):
                rhs.mtype.restype = lhs.mtype.eletype
            if isinstance(lhs.mtype.eletype, Unknown):
                lhs.mtype.eletype = rhs.mtype.restype
            if isinstance(lhs.mtype.eletype, Unknown):
                raise TypeCannotBeInferred(ast)
            if type(lhs.mtype.eletype) != type(rhs.mtype.restype):
                raise TypeMismatchInStatement(ast)
        
        # PRIM = MTYPE
        if isinstance(lhs.mtype, (Prim, Unknown)) and isinstance(rhs.mtype, MType):
            if isinstance(rhs.mtype.restype, Unknown):
                rhs.mtype.restype = lhs.mtype
            if isinstance(lhs.mtype, Unknown):
                lhs.mtype = rhs.mtype.restype
            if isinstance(lhs.mtype, Unknown):
                raise TypeCannotBeInferred(ast)
            if type(lhs.mtype) != type(rhs.mtype.restype):
                raise TypeMismatchInStatement(ast)
        
        # MTYPE = ARRAY
        if isinstance(lhs.mtype, MType) and isinstance(rhs.mtype, ArrayType):
            if isinstance(lhs.mtype.restype, Unknown):
                lhs.mtype.restype = rhs.mtype.eletype
            if isinstance(rhs.mtype.eletype):
                rhs.mtype.eletype = lhs.mtype.restype
            if isinstance(lhs.mtype.restype, Unknown):
                raise TypeCannotBeInferred(ast)
            if type(lhs.mtype.restype) != type(rhs.mtype.eletype):
                raise TypeMismatchInStatement(ast)
        
        # ARRAY = ARRAY
        if isinstance(lhs.mtype, ArrayType) and isinstance(rhs.mtype, ArrayType):
            if isinstance(lhs.mtype.eletype, Unknown):
                lhs.mtype.eletype = rhs.mtype.eletype
            if isinstance(rhs.mtype.eletype, Unknown):
                rhs.mtype.eletype = lhs.mtype.eletype
            if isinstance(rhs.mtype.eletype, Unknown):
                raise TypeCannotBeInferred(ast)
            if type(rhs.mtype.eletype) != type(lhs.mtype.eletype):
                raise TypeMismatchInStatement(ast)
        
        # PRIM = ARRAY
        if isinstance(lhs.mtype, (Prim, Unknown)) and isinstance(rhs.mtype, ArrayType):
            if isinstance(lhs.mtype, Unknown):
                lhs.mtype = rhs.mtype.eletype
            if isinstance(rhs.mtype.eletype, Unknown):
                rhs.mtype.eletype = lhs.mtype
            if isinstance(lhs.mtype, Unknown):
                raise TypeCannotBeInferred(ast)
            if type(lhs.mtype) != type(rhs.mtype.eletype):
                raise TypeMismatchInStatement(ast)
        
        # MTYPE = PRIM
        if isinstance(lhs.mtype, MType) and isinstance(rhs.mtype, (Prim, Unknown)):
            if isinstance(lhs.mtype.restype, Unknown):
                lhs.mtype.restype = rhs.mtype
            if isinstance(rhs.mtype, Unknown):
                rhs.mtype =  lhs.mtype.restype
            if isinstance(rhs.mtype, Unknown):
                raise TypeCannotBeInferred(ast)
            if type(lhs.mtype.restype) != type(rhs.mtype):
                raise TypeMismatchInStatement(ast)
        
        # ARRAY = PRIM
        if isinstance(lhs.mtype, ArrayType) and isinstance(rhs.mtype, (Prim, Unknown)):
            if isinstance(lhs.mtype.eletype, Unknown):
                lhs.mtype.eletype = rhs.mtype
            if isinstance(rhs.mtype, Unknown):
                rhs.mtype = lhs.mtype.eletype
            if isinstance(rhs.mtype, Unknown):
                raise TypeCannotBeInferred(ast)
            if type(lhs.mtype.eletype) != type(rhs.mtype):
                raise TypeMismatchInStatement(ast)
        
        # PRIM = PRIM
        if isinstance(lhs.mtype, (Prim, Unknown)) and isinstance(rhs.mtype, (Prim, Unknown)):
            if isinstance(lhs.mtype, Unknown):
                lhs.mtype = rhs.mtype
            if isinstance(rhs.mtype, Unknown):
                rhs.mtype = lhs.mtype
            if isinstance(lhs.mtype, Unknown):
                raise TypeCannotBeInferred(ast)
            if type(rhs.mtype) != type(lhs.mtype):
                raise TypeMismatchInStatement(ast)
        
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
        
        return_type = None
        scope = reduce(lambda y, x: [self.visit(x, y)] + y, ast.ifthenStmt[0][1], []) 
        if_env = scope + env
        res_list = [self.visit(stmt, if_env) for stmt in ast.ifthenStmt[1]]
        env = if_env[len(scope):]
        for res in res_list:
            if res:
                return_type = res
        if len(ast.elseStmt):
            scope = reduce(lambda env, x: env + [self.visit(x, env)], ast.elseStmt[0], [])
            else_env = env + scope
            res_list = [self.visit(stmt, else_env) for stmt in ast.elseStmt]
            for res in res_list:
                if res:
                    return_type = res
            env = else_env[len(scope):]
        return return_type

    def visitFor(self, ast):
        """
        Check if all has the same type as spec
        """
        idx1 = self.visit(ast.idx1, env)
        idx1_val = None
        if idx1 is None:
            raise Undeclared(Identifier(), ast.idx1.name)
        if isinstance(idx1.mtype, (Prim, Unknown)):
            if isinstance(idx1.mtype, Unknown):
                idx1.mtype = IntType()
            idx1_val = idx1.mtype
        if isinstance(idx1.mtype, ArrayType):
            if isinstance(idx1.mtype.eletype, Unknown):
                idx1.mtype.eletype = IntType()
            idx1_val = idx1.mtype.eletype
        if isinstance(idx1.mtype, MType):
            if isinstance(idx1.mtype.restype, Unknown):
                idx1.mtype.restype = IntType()
            idx1_val = idx1.mtype.restype
        if not isinstance(idx1_val, IntType):
            raise TypeMismatchInStatement(ast)

        init_expr = self.visit(ast.expr1, env)
        init_val = None
        if init_expr is None:
            raise Undeclared(Identifier(), ast.expr1.name)
        if isinstance(init_expr.mtype, (Prim, Unknown)):
            if isinstance(init_expr.mtype, Unknown):
                init_expr.mtype = IntType()
            init_val = init_expr.mtype
        if isinstance(init_expr.mtype, ArrayType):
            if isinstance(init_expr.mtype.eletype, Unknown):
                init_expr.mtype.eletype = IntType()
            init_val = init_expr.mtype.eletype
        if isinstance(init_expr.mtype, MType):
            if isinstance(init_expr.mtype.restype, Unknown):
                init_expr.mtype.restype = IntType()
            init_val = init_expr.mtype.restype
        if not isinstance(init_val, IntType):
            raise TypeMismatchInStatement(ast)

        con_expr = self.visit(ast.expr2, env)
        con_val = None
        if con_expr is None:
            raise Undeclared(Identifier(), ast.expr2.name)
        if isinstance(con_expr.mtype, (Prim, Unknown)):
            if isinstance(con_expr.mtype, Unknown):
                con_expr.mtype = BoolType()
            con_val = con_expr.mtype
        if isinstance(con_expr.mtype, ArrayType):
            if isinstance(con_expr.mtype.eletype, Unknown):
                con_expr.mtype.eletype = BoolType()
            con_val = con_expr.mtype.eletype
        if isinstance(con_expr.mtype, MType):
            if isinstance(con_expr.mtype.restype, Unknown):
                con_expr.mtype.restype = BoolType()
            con_val = con_expr.mtype.restype
        if not isinstance(con_val, BoolType):
            raise TypeMismatchInStatement(ast)
        
        update_expr = self.visit(ast.expr3, env)
        update_val = None
        if update_expr is None:
            raise Undeclared(Identifier(), ast.expr1.name)
        if isinstance(update_expr.mtype, (Prim, Unknown)):
            if isinstance(update_expr.mtype, Unknown):
                update_expr.mtype = IntType()
            update_val = update_expr.mtype
        if isinstance(update_expr.mtype, ArrayType):
            if isinstance(update_expr.mtype.eletype, Unknown):
                update_expr.mtype.eletype = IntType()
            update_val = update_expr.mtype.eletype
        if isinstance(update_expr.mtype, MType):
            if isinstance(update_expr.mtype.restype, Unknown):
                update_expr.mtype.restype = IntType()
            update_val = update_expr.mtype.restype
        if not isinstance(update_val, IntType):
            raise TypeMismatchInStatement(ast)

        scope = reduce(lambda env, x: [self.visit(x, env)] + env, ast.loop[0], [])
        cur_env = scope + env
        res_list = [self.visit(x, cur_env) for x in ast.loop[1]]
        env = cur_env[len(scope) :]
        for res in res_list:
            if res:
                return res
        return None
                
    def visitBreak(self, ast, env):
        """
        Do not care about unreachablestmt
        """
        return None

    def visitReturn(self, ast, env):
        """
        TODO: check the type of this return stmt and the type of function return
        return type has the type if None we handled in FuncDecl
        """
        return self.visit(ast.expr, env).mtype if ast.expr else VoidType()

    def visitDowhile(self, ast, env):
        """
        Do stmt before
        """
        scope = reduce(lambda env, x: [self.visit(x, env)] + env, ast.sl[0], [])
        cur_env = scope + env
        res_list = [self.visit(x, cur_env) for x in ast.sl[1]]
        expr = self.visit(ast.exp, env)
        expr_val = None
        if expr is None:
            raise Undeclared(Identifier(), ast.exp.name)
        if isinstance(expr.mtype, (Prim, Unknown)):
            if isinstance(expr.mtype, Unknown):
                expr.mtype = BoolType()
            expr_val = expr.mtype
        if isinstance(expr.mtype, ArrayType):
            if isinstance(expr.mtype.eletype, Unknown):
                expr.mtype.eletype = BoolType()
            expr_val = expr.mtype.eletype
        if isinstance(expr.mtype, MType):
            if isinstance(expr.mtype.restype, Unknown):
                expr.mtype.restype = BoolType()
            expr_val = expr.mtype.restype
        if not isinstance(expr_val, BoolType):
            raise TypeMismatchInStatement(ast)
        
        env = cur_env[len(scope) :]
        for res in res_list:
            if res:
                return res
        return None
        

    def visitWhile(self, ast):
        """
        Same with Dowhile?
        """
        expr = self.visit(ast.exp, env)
        expr_val = None
        if expr is None:
            raise Undeclared(Identifier(), ast.exp.name)
        if isinstance(expr.mtype, (Prim, Unknown)):
            if isinstance(expr.mtype, Unknown):
                expr.mtype = BoolType()
            expr_val = expr.mtype
        if isinstance(expr.mtype, ArrayType):
            if isinstance(expr.mtype.eletype, Unknown):
                expr.mtype.eletype = BoolType()
            expr_val = expr.mtype.eletype
        if isinstance(expr.mtype, MType):
            if isinstance(expr.mtype.restype, Unknown):
                expr.mtype.restype = BoolType()
            expr_val = expr.mtype.restype
        if not isinstance(expr_val, BoolType):
            raise TypeMismatchInStatement(ast)

        scope = reduce(lambda env, x: [self.visit(x, env)] + env, ast.sl[0], [])
        cur_env = scope + env
        res_list = [self.visit(x, cur_env) for x in ast.sl[1]]
        
        env = cur_env[len(scope) :]
        for res in res_list:
            if res:
                return res
        return None

    def visitCallStmt(self, ast, env):
        """
        Callee must have the VoidType as its return type
        """
        func = self.visit(ast.method, env)
        if func is None or not isinstance(func.mtype,  MType):
            raise Undeclared(Function(), ast.method.name)
        
        if not isinstance(func.mtype.restype, VoidType):
            raise TypeMismatchInStatement(ast)

        if len(func.mtype.intype) != len(ast.param):
            raise TypeMismatchInStatement(ast)
        
        # args = [self.visit(arg, env) for arg in ast.param]
        for (idx, arg) in enumerate(ast.param):
            arg_sym = self.visit(arg, env) # arg_type: Symbol
            arg_type = Unknown()
            is_arr = False
            if isinstance(arg_sym.mtype, (Prim, Unknown)):
                arg_type = arg_sym.mtype
            if isinstance(arg_sym.mtype, MType):
                arg_type = arg_sym.mtype.restype
            if isinstance(arg_sym.mtype, ArrayType):
                arg_type = arg_sym.mtype.eletype
                is_arr = True

            if isinstance(arg_type, Unknown):
                if func.mtype.intype[idx] == None:
                    raise TypeCannotBeInferred(ast)
                if isinstance(func.mtype.intype[idx].mtype, Prim):
                    if isinstance(func.mtype.intype[idx].mtype, Unknown):
                        raise TypeCannotBeInferred(ast)
                    arg_type = func.mtype.intype[idx].mtype
                if isinstance(func.mtype.intype[idx].mtype, MType):
                    if isinstance(func.mtype.intype[idx].mtype.restype, Unknown):
                        raise TypeCannotBeInferred(ast)
                    arg_type = func.mtype.intype[idx].mtype.restype
                if isinstance(func.mtype.intype[idx].mtype, ArrayType):
                    if not is_arr:
                        raise TypeMismatchInStatement(ast)
                    if isinstance(func.mtype.intype[idx].mtype.eletype, Unknown):
                        raise TypeCannotBeInferred(ast)
                    arg_type = func.mtype.intype[idx].mtype.eletype
                    
            else: # arg_type is known
                if func.mtype.intype[idx] == None:
                    func.mtype.intype[idx] = arg_sym
                if isinstance(func.mtype.intype[idx].mtype, Prim):
                    if isinstance(func.mtype.intype[idx].mtype, Unknown):
                        func.mtype.intype[idx].mtype = arg_type
                    if type(func.mtype.intype[idx].mtype) != type(arg_type):
                        raise TypeMismatchInStatement(ast)
                if isinstance(func.mtype.intype[idx].mtype, MType):
                    if isinstance(func.mtype.intype[idx].mtype.restype, Unknown):
                        func.mtype.intype[idx].mtype.restype = arg_type
                    if type(func.mtype.intype[idx].mtype.restype) != type(arg_type):
                        raise TypeMismatchInStatement(ast)
                if isinstance(func.mtype.intype[idx].mtype, ArrayType):
                    if not is_arr:
                        raise TypeMismatchInStatement(ast)
                    if isinstance(func.mtype.intype[idx].mtype.eletype, Unknown):
                        func.mtype.intype[idx].mtype.eletype = arg_type
                    if type(func.mtype.intype[idx].mtype.eletype) != type(arg_type):
                        raise TypeMismatchInStatement(ast)
                    if type(func.mtype.intype[idx].mtype) != type(arg_sym):
                        # array type not match
                        raise TypeMismatchInStatement(ast)
                
            if isinstance(arg_sym.mtype, (Prim, Unknown)):
                arg_sym.mtype =  arg_type
            if isinstance(arg_sym.mtype, MType):
                arg_sym.mtype.restype = arg_type
            if isinstance(arg_sym.mtype, ArrayType):
                arg_sym.mtype.eletype = arg_type

        return None

    def visitId(self, ast, c):
        """
        return: Symbol(name=id.name, mtype=None)
        """
        for sym in c:
            if sym.name == ast.name:
                return sym
        return None

    def is_same_type(self, a, b):
        # print(a.mtype)
        # print(b.mtype)
        if type(a.mtype) != type(b.mtype):
            return False
        else:
            if isinstance(a.mtype, ArrayType):
                if len(a.mtype.dimen) != len(b.mtype.dimen) or a.mtype.eletype != b.mtype.eletype:
                    return False
            if isinstance(a.mtype, MType):
                if a.mtype.intype != b.mtype.intype or a.mtype.restype != b.mtype.restype:
                    return False
        return True
    
    def visitGlobal(self,ast,c):
        if isinstance(ast, FuncDecl):
            for x in c:
                if x.name == ast.name.name:
                    raise Redeclared(Function(), x.name)
            return Symbol(ast.name.name, MType([None]*len(ast.param), None))
        if isinstance(ast, VarDecl):
            for x in c:
                if x.name == ast.variable.name:
                    raise Redeclared(Variable(), x.name)
            return Symbol(ast.variable.name, None)

    def update_scope(self, scope, var):
        """
        stack-like
        """
        return [var] + scope
        """
        Rang comment them de co du 1000 dong
        """
