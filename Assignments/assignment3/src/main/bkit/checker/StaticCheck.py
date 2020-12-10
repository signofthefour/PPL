
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

    class ControlFlow:
        def __init__(self, ast):
            self.flow = []

        def add(self, summary:Summary):
            self.flow.append(summary)

        def type_inference(self):
            pass
    
    class Summary(AST):
        @abstractmethod
        def infer(self):
            pass
        @abstractmethod
        def propagate(self):
            pass
        @abstractmethod
        def receive(self):
            pass
    @dataclass
    class Type(Summary):
        # mean type of this is <TYPE>
        symbol: Symbol
        kind: Kind # for raising
        ast: AST

        def infer(self, scope_stack1):
            for symbol in global_scope:
                if symbol.name == symbol.name:
                    raise Redeclared(Kind, symbol.name)
            self.propagate(symbol, inner_most_scope, global_scope)

        def propagate(self, inner_most_scope, global_scope):
            for summary in inner_most_scope:
                    summary.receive(Symbol, same_scope=True)

        def receive(self, _symbol, same_scope=False):
            if same_scope == True:
                if symbol.name ==  _symbol.name:
                    raise Redeclared(kind, name)
                else: return
            if symbol.name ==  _symbol.name:
                if symbol.mtype == Unknown():
                    symbol.mtype = _symbol.mtype
                else:
                    raise TypeMismatchInStatement(None)

    @dataclass
    class Scope(Summary):
        scope_type: str # 'Function', 'For', 'If', 'Do'
        symbol: Symbol
        scope_summarise: List[Summary] # Without first param
        in_type: List[Summary] # in param of scope
        ast: AST

        def infer(self, inner_most_scope, global_scope):
            for symbol in global_scope:
                if name == symbol.name:
                    raise Redeclared(kind, name)
            self.propagate(name, inner_most_scope, global_scope)
            symbol.mtype = return_type.mtype

        def propagate(self, inner_most_scope, global_scope):
            # inner most scope means current scope in this situation
            # for summary in inner_most_scope:
            #     summary.receive(name, self, same_scope=True)
            # for summary in global_scope
            pass
        
        def receive(self, _name, scope, same_scope=False):
            if same_scope:
                if _name ==  name:
                    raise Redeclared(kind, name)
                else:
                    return 

    @dataclass
    class Operation(Summary):
        # mean: in this operation, we need name as Symbol
        # when infer type, this need a param named ecpected
        name: str
        in_type: List[Summary]
        ret: Symbol
        ast: AST

        def infer(self):
            pass
            # # RELATIONAL
            # ## Int
            # if ast.op in ['==', '!=', '<', '>', '>=', '<=']:
            #     l = self.visit(ast.left, env)
            #     if isinstance(l, Symbol) and isinstance(l.type, Unknown):
            #         l.type = IntType()
            #     r = self.visit(ast.right, env)
            #     if isinstance(r, Symbol) and isinstance(r.type, Unknown):
            #         r.type = IntType()

            #     if isinstance(l, IntType) and isinstance(r, IntType):
            #         raise TypeMismatchInExpr(ast)
            #     return BoolType()
            # ## Float
            # if ast.op in ['=/=', '<.', '>.', '>=.', '<=.']:
            #     l = self.visit(ast.left, env)
            #     if isinstance(l, Symbol) and isinstance(l.type, Unknown):
            #         l.type = FloatType()
            #     r = self.visit(ast.right, env)
            #     if isinstance(r, Symbol) and isinstance(r.type, Unknown):
            #         r.type = FloatType()
                
            #     if isinstance(l, FloatType) and isinstance(r, FloatType):
            #         raise TypeMismatchInExpr(ast)
            #     return BoolType()
            
            # # BOOLEAN
            # if ast.op in ['&&' , '||']:
            #     l = self.visit(ast.left, env)
            #     if isinstance(l, Symbol) and isinstance(l.type, Unknown):
            #         l.type = BoolType()
            #     r = self.visit(ast.right, env)
            #     if isinstance(r, Symbol) and isinstance(r.type, Unknown):
            #         r.type = BoolType()

            #     if isinstance(l, BoolType) and isinstance(r, BoolType):
            #         raise TypeMismatchInExpr(ast)
            #     return BoolType()
            
            # # ARITHMETIC
            # ## Int
            # if ast.op in ['-' , '+', '*', '\\']:
            #     l = self.visit(ast.left, env)
            #     if isinstance(l, Symbol) and isinstance(l.type, Unknown):
            #         l.type = IntType()
            #     r = self.visit(ast.right, env)
            #     if isinstance(r, Symbol) and isinstance(r.type, Unknown):
            #         r.type = IntType()

            #     if isinstance(l, IntType) and isinstance(r, IntType):
            #         raise TypeMismatchInExpr(ast)
            #     return IntType()
            
            # ## Float
            # if ast.op in ['-.' , '+.', '*.', '\\.']:
            #     l = self.visit(ast.left, env)
            #     if isinstance(l, Symbol) and isinstance(l.type, Unknown):
            #         l.type = FloatType()
            #     r = self.visit(ast.right, env)
            #     if isinstance(r, Symbol) and isinstance(r.type, Unknown):
            #         r.type = FloatType()

            #     if isinstance(l, FloatType) and isinstance(r, FloatType):
            #         raise TypeMismatchInExpr(ast)
            #     return FloatType()
            
            # if ast.op in ['-']:
            #     operand = self.visit(ast.body, env)
            #     if isinstance(operand, Symbol) and isinstance(operand.type, Unknown):
            #         operand.type = IntType()

            #     if isinstance(operand, IntType):
            #         raise TypeMismatchInExpr(ast)
            #     return IntType()
            # ## Float
            # if ast.op in ['-.']:
            #     operand = self.visit(ast.body, env)
            #     if isinstance(operand, Symbol) and isinstance(operand.type, Unknown):
            #         operand.type = FloatType()

            #     if isinstance(operand, FloatType):
            #         raise TypeMismatchInExpr(ast)
            #     return FloatType()

            # # BOOLEAN
            # if ast.op in ['!']:
            #     operand = self.visit(ast.body, env)
            #     if isinstance(operand, Symbol) and isinstance(operand.type, Unknown):
            #         operand.type = BoolType()

            #     if isinstance(operand, BoolType):
            #         raise TypeMismatchInExpr(ast)
            #     return BoolType()

    @dataclass
    class Equivalent(Summary):
        # between two Symbol mean x = y mean equivalent type
        # mean two thing that do not know type in current context, need more summaries.
        name: str
        lhs: List[Summary]
        rhs: List[Summary]
        ast: AST
    
    @dataclass
    class Call(Summary):
        # Special for BKIT because of function type can be infer before use
        # 
        name: str
        in_type: List[Summary]
        return_type: Symbol
        ast: AST
    
    @dataclass
    class FuncReturn(Summary):
        # Get the return type of the function with rule that it do
        # not change the return type in program
        name: str
        return_type: Summary

  
    def check(self):
        """
        Depend on the idea from J. Aycock. Aggressive Type Inference...
        Divide this progess into two phase:
            1. Summarise: get informations as much as possible from the function (here is ast)
            2. Inference: the summary informations is repeatedly examined in order to propagate type information.
        """
        # Phase 1: Summarizing the informations from ast
        control_flow = self.visit(self.ast)

    def visitProgram(self,ast):
        summaries = [self.visit(x) for x in ast.decl]
        control_flow = ControlFlow()
        for block in summaries:
            for summary in block:
                control_flow.add(summary)
        return control_flow
        
    def visitVarDecl(self, ast):
        """
        Visit each global var top-down
        """
        var = self.visit(ast.variable)
        if ast.dimen:
            var.mtype = ArrayType(ast.dimen, Unknown())
        else:
            var.mtype = Unknown()
        init_val = self.visit(ast.varInit) if ast.varInit else Symbol('', Unknown())
        init = Operation('', [], init_val)
        return [Type(var.name, var, init, Variable(), ast)]

    def visitFuncDecl(self, ast):
        function = self.visit(ast.name)
        param_summary = self.flatten([self.visit(param) for param in ast.param])
        body_var_summary = self.flatten([self.visit(decl) for decl in ast.body[0]])
        body_summary = self.flatten([self.visit(stmt) for stmt in ast.body[1]])
        return [Type(function.name, function, init=None, kind=Function(),ast=ast), Scope(function.name, body_var_summary + body_summary, param_summary, ast)]

    def visitArrayCell(self, ast):
        """
        For an array indexing E[E1]...[En], -
            E must be in array type with n dimensions and E1...En must be integer.
        """
        e = self.visit(ast.arr)
        e.ast = ast
        e_n = [self.visit(x) for x in ast.idx]
        e_n = self.flatten(e_n)
        for e_i in e_n:
            e_i.return_type.mtype = IntType()
        return e + e_n

    def visitBinaryOp(self, ast):
        """
        ==, ! =, <, >, <=, >=, = / =, < ., > ., <= ., >= .
        """
        lhs = self.visit(ast.left)
        rhs = self.visit(ast.right)
        return [Operation(ast.op, lhs+rhs, Unknown(), ast)]

    def visitUnaryOp(self, ast):
        operand = self.visit(ast.body)
        return [Operation(ast.op, operand, Unknown(), ast)]

    def visitCallExpr(self, ast):
        op = self.visit(ast.method)
        param = [self.visit(exp) for exp in ast.param]
        param = self.flatten(param)
        return [Operation(op, param, Unknown(), ast)]
        
    def visitIntLiteral(self, ast):
        return [Type(None, Symbol('', IntType()), ast)]

    def visitStringLiteral(self, ast):
        return [Type(None, Symbol('', StringType()), ast)]

    def visitBooleanLiteral(self, ast):
        return [Type(None, Symbol('', BoolType()), ast)]
    
    def visitFloatLiteral(self, ast):
        return [Type(None, Symbol('', FloatType()), ast)]

    def visitArrayLiteral(self, ast):
        literal_summary = [self.visit(x) for x in ast.value]
        last_dimen = literal_summary[0].var.dimen if literal_summary[0].var.dimen else []
        return [Type(Symbol('', ArrayType([len(ast.value)] + last_dimen)), ast)]
        

    def visitAssign(self, ast):
        """
        lhs = rhs
        <Symbol> = <MType>
        """
        rhs = self.visit(rhs, env)
        lhs = self.visit(lhs, env)
        return [Equivalent(lhs, rhs, ast)]

    def visitIf(self, ast):
        con_expr = self.visit(ast.ifthenStmt[0][0]) # if condition
        scope_var = self.flatten([self.visit(x) for x in ast.ifthenStmt[0][1]])
        scope_body = self.flatten([self.visit(x) for x in ast.ifthenStmt[0][2]])
        if_scope = [Scope('If', con_expr + scope_var + scope_body, None, VoidType(), ast)]
        else_scope = []
        if len(ast.elseStmt):
            scope_var = self.flatten([self.visit(x) for x in ast.elseStmt[0]])
            scope_body = self.flatten([self.visit(x) for x in ast.elseStmt[1]])
            else_scope = [Scope('Else', scope_var + scope_body, None, VoidType()]
        return if_scope + else_scope

    def visitFor(self, ast):
        """
        Check if all has the same type as spec
        """
        idx = self.visit(ast.idx1)
        init_expr = self.visit(ast.expr1)
        con_expr = self.visit(ast.expr2)
        update_expr = self.visit(ast.expr3)
        scope_var = self.flatten(self.visit(ast.loop[0]))
        scope_body = self.flatten(self.visit(ast.loop[1]))
        return [Scope('For', idx + init_expr + con_expr + update_expr + scope_var + scope_body, None, VoidType())]
                
    def visitBreak(self, ast):
        return []

    def visitReturn(self, ast):
        return self.visit(ast.expr)

    def visitDowhile(self, ast):
        scope_var = self.flatten([self.visit(x) for x in ast.sl[0]])
        scope_body = self.flatten([self.visit(x) for x in ast.sl[1]])
        expr = self.visit(ast.exp)
        return [Scope('Do', scope_var + scope_body + expr, None, VoidType())]

    def visitWhile(self, ast):
        """
        Same with Dowhile?
        """
        scope_var = self.flatten([self.visit(x) for x in ast.sl[0]])
        scope_body = self.flatten([self.visit(x) for x in ast.sl[1]])
        expr = self.visit(ast.exp)
        return [Scope('While', expr + scope_var + scope_body, None, VoidType())]

    def visitCallStmt(self, ast, env):
        method = self.visit(ast.method)
        params = self.flatten([self.visit(x) for x in ast.param])
        return [Call(method.name, params, Symbol('', VoidType()),ast)]

    def visitId(self, ast, env, checking=False):
        """
        output: list of symbols that has the same name as the Id
        """
        return Symbol(ast.name, Unknown())

    def flatten(self, arr):
        return reduce(lambda arr, y: arr + [y], arr, [])