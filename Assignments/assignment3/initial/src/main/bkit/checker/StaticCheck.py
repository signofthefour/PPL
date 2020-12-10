
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
   
    def getNameOfSymbol(self, envi, a: Symbol):
        return None 
            

    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, c):
        #decl : List[Decl]
        #c = [[],[]] #mpType and action (for funciton)
            
        [self.visit(x,c) for x in ast.decl]
        
    
    def visitVarDecl(self, ast, envi):
        #variable : Id
        #varDimen : List[int] # empty list for scalar variable
        #varInit  : Literal   # null if no initial

        name  = self.visit(ast.variable)
        enviList = [idx.name for idx in envi] if envi else []
        if name in enviList:                                    # Check if variable name used 
            rasie Redeclared(Identifier(), ast.variable)

        dimen   = []
        varType = Unknown()
        if varDimen:                                            # Check if this variable is a arraycell
            [dimen.append(x) for x in ast.varDimen]
            varType = self.visit(ast.varInit) if varInit else Unknown()
            var     = Symbol(name , ArrayType(dimen, varType))
            envi.append(var)
            return

        varType = self.visit(ast.varInit) if varInit else Unknown()
        var     = Symbol(name, varType)
        envi.append(var)
        return

    
    def visitFuncDecl(self, ast, envi):
        # name: Id
        # param: List[VarDecl]
        # body: Tuple[List[VarDecl],List[Stmt]]

        name = self.visit(ast.name)
        if name in envi[0]:
            rasie Redeclared(Function(), name)
        else 


        return None
    
    def visitBinaryOp(self, ast, envi):
        # op:str
        # left:Expr
        # right:Expr
        return None
    
    def visitUnaryOp(self, ast, envi):
        # op:str
        # body:Expr
        return None
    
    def visitCallExpr(self, ast, envi):
        # method:Id
        # param:List[Expr]

        return None
    
    def visitId(self, ast, envi):
        #name : str
        return ast.name
    
    def visitArrayCell(self, ast, envi):
        # arr:Expr
        # idx:List[Expr]
        return None
    
    def visitAssign(self, ast, envi):
        # lhs: LHS
        # rhs: Expr
        return None
    
    def visitIf(self, ast, envi):   
        # ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
        # elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else

        return None
    
    def visitFor(self, ast, envi):
        # idx1: Id
        # expr1:Expr
        # expr2:Expr
        # expr3:Expr
        # loop: Tuple[List[VarDecl],List[Stmt]]
        return None
    
    def visitContinue(self, ast, envi):

        
        return None
    
    def visitBreak(self, ast, envi):
        return None
    
    def visitReturn(self, ast, envi):
        return None
    
    def visitDowhile(self, ast, envi):
        # sl:Tuple[List[VarDecl],List[Stmt]]
        # exp: Expr
        return None

    def visitWhile(self, ast, envi):
        # exp: Expr
        # sl:Tuple[List[VarDecl],List[Stmt]]
        return None

    def visitCallStmt(self, ast, envi):
        # method:Id
        # param:List[Expr]
        name = self.visit(ast.method)

        if name not in envi[0]:
            raise Undeclared(Function(), name)
        if name in envi[0] and getType(name) != Function()
            rasie Undeclared(Function(), name)

        

        return None
    
    def visitIntLiteral(self, ast, envi):
        # value: int
        return IntType()
    
    def visitFloatLiteral(self, ast, envi):
        # value: float
        return FloatType()
    
    def visitBooleanLiteral(self, ast, envi):
        # value: boolean
        return BoolType()
    
    def visitStringLiteral(self, ast, envi):
        # value: string
        return StringType()

    def visitArrayLiteral(self, ast, envi):
        # value:List[Literal]
        return [self.visit(idx) for idx in ast.value] else Unknown()
        

