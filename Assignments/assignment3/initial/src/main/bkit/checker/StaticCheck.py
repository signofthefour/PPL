
"""
 * @author nhphung
"""
from Assignments.assignment3.initial.src.main.bkit.utils.AST import CallExpr
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
class UnInfer(Type):
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
Symbol("float_to_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("print",MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType()))]                           
   
    def getType(self, sym:Symbol, arrType:bool):
        """Return type of the param symbol""" 
        if type(sym.mtype) is MType:
            if type(sym.mtype.restype) is ArrayType:
                return sym.mtype.restype if arrType else sym.mtype.restype.eletype
        elif type(sym.mtype) is ArrayType:
            return sym.mtype if arrType else sym.mtype.eletype
        else:
            return sym.mtype

    def getSymbol(self, name, envi):
        for ctx in envi:
            if ctx.name == name:
                return ctx
        return None
    
    def getName(self, ast):
        if type(ast) == Id:
            return ast.name
        elif isinstance(ast, ArrayCell):
            if isinstance(ast.arr, CallExpr):
                return ast.arr.method.name
            else:
                return ast.arr.name
        elif isinstance(ast, CallExpr):
            return ast.method.name

    def updateType(self, symName, envi, newType: Type):
        """update type of a symbol in envi"""
        for idx in envi:
            if idx.name == symName:
                idx.mtype = newType
        return

    def buildEnvi(self, inEnvi, outEnvi): 
        # make enviroment for a function, include function and variable
        for ele in outEnvi:
            if type(ele.mtype) is MType:
                inEnvi.append(ele)
        inVar = [ele.name for ele in inEnvi]
        for ele in outEnvi:
            if type(ele.mtype) != MType and ele.name not in inVar:
                inEnvi.append(ele)
        return inEnvi

    def updateOutEnvi(self, inEnvi, outEnvi, tempEnvi):
        # Update variable after run out a function or a block 
        outName  = [idx.name for idx in outEnvi]
        tempName = [idx.name for idx in tempEnvi]
        for idx in inEnvi:
            if idx.name in outName and idx.name not in tempName and type(idx.type) != MType:
                self.updateType(idx.name, outEnvi, idx.mtype)

    def funcTraverser(self, ast, o):
        # name: Id
        # param: List[VarDecl]
        # body: Tuple[List[VarDecl],List[Stmt]]
        name = ast.name.name
        enviList = [idx.name for idx in o]
        if name in enviList:                                    # Check if function declared 
            raise Redeclared(Function(), name)
        tempEnvi  = []
        [self.visit(idx, tempEnvi) for idx  in ast.param]
        return tempEnvi

    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, c):
        #decl : List[Decl]
        #trevease function
        c = []
        [self.visit(x,c) for x in ast.decl if type(x) is VarDecl]
        for idx in ast.decl:
            if type(idx) is FuncDecl:
                param = self.funcTraverser(idx, c)
                name = idx.name.name
                c.append(Symbol(name, MType(param, Unknown())))
        #check main func
        funcList = [idx.name for idx in c]
        if 'main' not in funcList:
            raise NoEntryPoint()
        #visit decl
        [self.visit(x,c) for x in ast.decl if type(x) is FuncDecl]
        
    def visitVarDecl(self, ast, envi):
        #variable : Id
        #varDimen : List[int] # empty list for scalar variable
        #varInit  : Literal   # null if no initial
        name  = ast.variable.name
        enviList = [idx.name for idx in envi]
        if name in enviList:                                    # Check if variable name used 
            raise Redeclared(Identifier(), ast.variable)
        dimen   = []
        varType = Unknown()
        if ast.varDimen:                                            # Check if this variable is a arraycell
            [dimen.append(x) for x in ast.varDimen]
            varType = self.visit(ast.varInit) if ast.varInit else Unknown()
            envi.append(Symbol(name , ArrayType(dimen, varType)))
            return
        else:
            varType = self.visit(ast.varInit) if ast.varInit else Unknown()
            envi.append(Symbol(name, varType))
            return
        
    def visitFuncDecl(self, ast, envi):
        # name: Id
        # param: List[VarDecl]
        # body: Tuple[List[VarDecl],List[Stmt]]
        #set up enviroment for a function
        tempEnvi  = []
        varList = ast.param + ast.body[0]
        [self.visit(idx, tempEnvi) for idx  in varList]
        funcEnvi = self.buildEnvi(tempEnvi, envi)
        #run statement
        [self.visit(idx, funcEnvi) for idx in ast.body[1]]
        #check Return:
        self.getSymbol(ast.name.name, funcEnvi)
        for stmt in ast.body[1]:
            if type(stmt) is Return:
                restype = self.visit(stmt)
        #update type
        self.updateOutEnvi(funcEnvi, envi, tempEnvi)

    def visitBinaryOp(self, ast, envi):
        # op:str
        # left:Expr
        # right:Expr
        left  = self.visit(ast.left, envi)
        right = self.visit(ast.right, envi)
        #Check UnInfer
        if type(left) is UnInfer or type(right) is UnInfer:
            return UnInfer()
        #If not Uninfer, check operator
        if ast.op in ['+','-','*','\\','%']:
            if type(left) is Unknown:
                self.updateType(self.getName(ast.left), envi, IntType())
            if type(right) is Unknown:
                self.updateType(self.getName(ast.right), envi, IntType())
            left  = self.visit(ast.left, envi)
            right = self.visit(ast.right, envi)
            if type(left) != IntType or type(right) != IntType:
                raise TypeMismatchInExpression(ast)
            else:
                return IntType()       
        elif ast.op in ['+.','-.','*.','\\.','%.']:
            if type(left) is Unknown:
                self.updateType(self.getName(ast.left), envi, FloatType())
            if type(right) is Unknown:
                self.updateType(self.getName(ast.right), envi, FloatType())
            left  = self.visit(ast.left, envi)
            right = self.visit(ast.right, envi)
            if type(left) != FloatType or type(right) != FloatType:
                raise TypeMismatchInExpression(ast)
            else:
                return FloatType()
        elif ast.op in ['==','!=','<','>','<=','>=']:
            if type(left) is Unknown:
                self.updateType(self.getName(ast.left), envi, IntType())
            if type(right) is Unknown:
                self.updateType(self.getName(ast.right), envi, IntType())
            left  = self.visit(ast.left, envi)
            right = self.visit(ast.right, envi)
            if type(left) != IntType or type(right) != IntType:
                raise TypeMismatchInExpression(ast)
            else:
                return BoolType()
        elif ast.op in ['=/=','<.','>.','<=.','>=.']:
            if type(left) is Unknown:
                self.updateType(self.getName(ast.left), envi, FloatType())
            if type(right) is Unknown:
                self.updateType(self.getName(ast.right), envi, FloatType())
            left  = self.visit(ast.left, envi)
            right = self.visit(ast.right, envi)
            if type(left) != FloatType or type(right) != FloatType:
                raise TypeMismatchInExpression(ast)
            else:
                return BoolType()
        elif ast.op in  ['&&','||']:
            if type(left) is Unknown:
                self.updateType(self.getName(ast.left), envi, BoolType())
            if type(right) is Unknown:
                self.updateType(self.getName(ast.right), envi, BoolType())
            left  = self.visit(ast.left, envi)
            right = self.visit(ast.right, envi)
            if type(left) != BoolType or type(right) != BoolType:
                raise TypeMismatchInExpression(ast)
            else:
                return BoolType()
    
    def visitUnaryOp(self, ast, envi):
        # op:str
        # body:Expr
        exp = self.visit(ast.body, envi)
        sign = ast.op
        
        if sign == '-':
            if type(exp) is Unknown:
                self.updateType(self.getName(ast.body), envi, IntType())
            exp = self.visit(ast.body, envi)
            if type(exp) != IntType:
                raise TypeMismatchInExpression(ast)
            else:
                return IntType()
        elif sign == '-.':
            if type(exp) is Unknown:
                self.updateType(self.getName(ast.body), envi, FloatType())
            exp = self.visit(ast.body, envi)
            if type(exp) != FloatType:
                raise TypeMismatchInExpression(ast)
            else:
                return FloatType()
        elif sign == '!':
            if type(exp) is Unknown:
                self.updateType(self.getName(ast.body), envi, BoolType())
            exp = self.visit(ast.body, envi)
            if type(exp) != BoolType:
                raise TypeMismatchInExpression(ast)
            else:
                return BoolType()

    def visitCallExpr(self, ast, envi):
        # method:Id
        # param:List[Expr]
        # method:Id
        # param:List[Expr]
        # Check if function not exist
        funcName = ast.method.name
        funcList = [idx.name for idx in envi if type(idx.mtype) is MType]
        if funcName not in funcList:
            raise Undeclared(Function(), funcName)
        for decl in envi:
            if decl.name == funcName and type(decl.mtype) != MType:
                raise Undeclared(Function(), funcName)
        #check parameter
        paraList = funcSym.mtype.intype
        if len(paraList) != len(ast.param):
            raise TypeMismatchInStatement(ast)

        for idx in range(len(ast.param)):
            para = self.visit(idx)
            if type(para) is UnInfer or type(paraList[idx]) is UnInfer:
                raise TypeCannotBeInferred(ast)
            elif type(para) is Unknown and type(paraList[idx]) is Unknown:
                raise TypeCannotBeInferred(ast)
            elif type(para) is Unknown and type(ast.param[idx]) is CallExpr and type(paraList[idx]) is ArrayType:
                if paraList[idx].dimen and type(paraList[idx].eletype) != Unknown:
                    self.updateType(self.getName(ast.param[idx]), envi, paraList[idx])
                else: 
                    raise TypeCannotBeInferred(ast)
            elif type(paraList[idx]) is Unknown and type(para) not in [Unknown, ArrayType]:
                paraList[idx] = para
            elif type(para) is Unknown and type(paraList[idx]) not in [Unknown, ArrayType]:
                para = paraList[idx]
                self.updateType(self.getName(ast.param[idx]), envi, para)
            elif type(paraList[idx]) is ArrayType and type(para) is ArrayType:
                if paraList[idx].dimen != para.dimen:
                    raise TypeMismatchInStatement(ast)
                else:
                    if type(paraList[idx].eletype) is Unknown and type(para.eletype) is Unknown:
                        raise TypeCannotBeInferred(ast)
                    elif type(paraList[idx].eletype) is Unknown:
                        paraList[idx].eletype =  para.eletype
                    elif type(para.eletype)  is Unknown:
                        para.eletype = paraList[idx].eletype
                    elif type(paraList[idx].eletype) != type(para.eletype):
                        raise TypeMismatchInStatement(ast)
            elif type(paraList[idx]) !=  type(para):
                raise TypeMismatchInStatement(ast)

    
    def visitId(self, ast, envi):
        #name : str
        name = ast.name
        lst = [idx.name for idx in envi]
        if ast.name not in lst:
            raise Undeclared(Identifier(), name)
        else:
            return self.getType(self.getSymbol(name, envi), True)

    def visitArrayCell(self, ast, envi):
        # arr:Expr
        # idx:List[Expr]
        if not ast.idx:
            raise TypeMismatchInExpression(ast)
        else:
            for exp in ast.idx:
                value = self.visit(exp, envi)
                if type(value) is UnInfer:
                    return UnInfer()
                elif type(value) is Unknown:
                    self.updateType(self.getName(ast), envi, IntType())
                value = self.visit(exp, envi)
                if type(exp) != IntType:
                    raise TypeMismatchInExpression(ast)
            arrType = self.visit(ast.arr)
            if type(arrType) is Unknown or type(arrType) is UnInfer:
                if isinstance(ast.arr, CallExpr):
                    return UnInfer()
                else: 
                    raise TypeMismatchInExpression(ast)
            elif type(arrType) != ArrayType:
                raise TypeMismatchInExpression(ast)        
            else:
                return arrType.eletype 

    def visitAssign(self, ast, envi):
        # lhs: LHS
        # rhs: Expr
        lhs = self.visit(ast.lhs, envi)
        rhs = self.visit(ast.rhs, envi)
        if type(rhs) is UnInfer and type(lhs) is UnInfer:
            raise TypeCannotBeInferred(ast)
        elif type(lhs) is Unknown and type(rhs) is Unknown:
            raise TypeCannotBeInferred(ast)
        elif type(lhs) is VoidType or type(rhs) is VoidType:
            raise TypeMismatchInStatement(ast)
        elif type(lhs) is Unknown and type(ast.lhs) is CallExpr and type(rhs) is ArrayType:
            if rhs.dimen and type(rhs.eletype) != Unknown:
                self.updateType(self.getName(ast.lhs), envi, rhs)
            else:
                raise TypeCannotBeInferred(ast)
        elif type(rhs) is Unknown and type(ast.rhs) is CallExpr and type(lhs) is ArrayType:
            if lhs.dimen and type(lhs.eletype) != Unknown:
                self.updateType(self.getName(ast.rhs), envi, lhs)
            else:
                raise TypeCannotBeInferred(ast)
        elif type(lhs) is Unknown and type(rhs) not in [Unknown, ArrayType]:
            lhs = rhs
            self.updateType(self.getName(ast.lhs), envi, rhs)  
        elif type(rhs) is Unknown and type(lhs) not in [Unknown, ArrayType]:
            rhs = lhs
            self.updateType(self.getName(ast.rhs), envi, lhs)
        elif (type(lhs) is ArrayType and type(rhs) is ArrayType):
            if lhs.dimen == rhs.dimen:
                if type(lhs.eletype) is Unknown and type(rhs.eletype) is Unknown:
                    raise TypeCannotBeInferred(ast)
                elif type(lhs.eletype) is Unknown:
                    lhs = rhs
                    self.updateType(self.getName(ast.lhs), envi, rhs)
                elif type(rhs.eletype) is Unknown:
                    rhs = lhs
                    self.updateType(self.getName(ast.rhs), envi, lhs)
                elif type(lhs.eletype) != type(rhs.eletype):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)
        elif type(lhs) != type(rhs):
            raise TypeMismatchInStatement(ast)
    def visitIf(self, ast, envi):   
        # ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
        # elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else
        for stmt in ast.ifthenStmt:
            exp = self.visit(stmt[0])
            if type(exp) is UnInfer:
                raise TypeCannotBeInferred(ast)
            #Check and infer type of the expr
            elif type(exp) is Unknown:
                self.updateType(self.getName(ast.stmt[0]), envi, BoolType)
            exp = self.visit(stmt[0])
            if type(exp) != BoolType:
                raise  TypeMismatchInStatement(ast)
            #Run statemnets in scope
            tempEnvi = []
            [self.visit(idx, tempEnvi) for idx in ast.stmt[1]]
            inEnvi = self.buildEnvi(tempEnvi, envi)
            [self.visit(idx, inEnvi) for idx in ast.stmt[2]]
            self.updateOutEnvi(inEnvi, envi, tempEnvi) 
        if ast.esleStmt:
            tempEnvi = []
            [self.visit(idx, tempEnvi) for idx in ast.esleStmt[0]]
            inEnvi = self.buildEnvi(tempEnvi, envi)
            [self.visit(idx, inEnvi) for idx in ast.esleStmt[1]]
            self.updateOutEnvi(inEnvi, envi, tempEnvi)

    def visitFor(self, ast, envi):
        # idx1: Id
        # expr1:Expr
        # expr2:Expr
        # expr3:Expr
        # loop: Tuple[List[VarDecl],List[Stmt]]
        scalar = self.visit(ast.idx1)
        exp1   = self.visit(ast.expr1)
        exp2   = self.visit(ast.expr2)
        exp3   = self.visit(ast.expr3)r
        if UnInfer in [type(scalar), type(exp1), type(exp2), type(exp3)]:
            raise TypeCannotBeInferred(ast)
        #Infer and check type of idx1 and exp1
        if type(scalar) is Unknown:
            self.updateType(ast.idx1.name, envi,IntType())
        if type (exp1) is Unknown:
            self.updateType(self.getName(ast.expr1), envi, IntType())
        scalar = self.visit(ast.idx1)
        exp1   = self.visit(ast.expr1)
        if type(scalar)  != IntType or type(exp1) != IntType:
            raise TypeMismatchInStatement(ast)
        #Infer and check type of exp2
        if type(exp2) is Unknown:
            self.updateType(self.getName(ast.expr2), envi, BoolType())
        exp2   = self.visit(ast.expr2)
        if type(exp2) != BoolType:
            raise TypeMismatchInStatement(ast)
        #Infer and check type of exp3
        if type(exp3) is Unknown:
            self.updateType(self.getName(ast.expr3), envi, IntType())
        exp3   = self.visit(ast.expr3)
        if type(exp2) != IntType:
            raise TypeMismatchInStatement(ast)
        #run statement in scope
        tempEnvi = []
        [self.visit(idx, tempEnvi) for idx in ast.loop[0]]
        inEnvi = self.buildEnvi(tempEnvi, envi)
        [self.visit(idx, inEnvi) for idx in ast.loop[1]]
        self.updateOutEnvi(inEnvi, envi, tempEnvi)     

    def visitContinue(self, ast, envi):
        return None
    
    def visitBreak(self, ast, envi):
        return None

    def visitReturn(self, ast, envi):
        #expr:Expr
        return self.visit(ast.expr, envi) if ast.expr else VoidType()
    
    def visitDowhile(self, ast, envi):
        # sl:Tuple[List[VarDecl],List[Stmt]]
        # exp: Expr
        tempEnvi = []
        [self.visit(idx, tempEnvi) for idx in ast.sl[0]]
        inEnvi = self.buildEnvi(tempEnvi, envi)
        [self.visit(idx, inEnvi) for idx in ast.sl[1]]
        expr = self.visit(ast.exp, envi)
        if type(expr) is Unknown:
            self.updateType(ast.exp.name, envi, BoolType())
        elif type(expr) is UnInfer:
            raise TypeCannotBeInferred(ast.exp)
        elif type(expr) is not BoolType:
            raise TypeMismatchInExpression(ast.exp)
        self.updateOutEnvi(inEnvi, envi, tempEnvi)

    def visitWhile(self, ast, envi):
        # exp: Expr
        # sl:Tuple[List[VarDecl],List[Stmt]]
        expr = self.visit(ast.exp, envi)
        if type(expr) is Unknown:
            self.updateType(ast.exp.name, envi, BoolType())
        elif type(expr) is UnInfer:
            raise TypeCannotBeInferred(ast.exp)
        elif type(expr) is not BoolType:
            raise TypeMismatchInExpression(ast.exp)
        tempEnvi = []
        [self.visit(idx, tempEnvi) for idx in ast.sl[0]]
        inEnvi = self.buildEnvi(tempEnvi, envi)
        [self.visit(idx, inEnvi) for idx in ast.sl[1]]
        self.updateOutEnvi(inEnvi, envi, tempEnvi)

    def visitCallStmt(self, ast, envi):
        # method:Id
        # param:List[Expr]
        # Check if function not exist
        funcName = ast.method.name
        funcList = [idx.name for idx in envi if type(idx.mtype) is MType]
        if funcName not in funcList:
            raise Undeclared(Function(), funcName)
        for decl in envi:
            if decl.name == funcName and type(decl.mtype) != MType:
                raise Undeclared(Function(), funcName)
        #check type of function
        funcSym = self.getSymbol(ast.method.name, envi)
        if type(funcSym.mtype.restype) is Unknown:
            funcSym.mtype.restype = VoidType()
        if type(funcSym.mtype.restype) != VoidType:
            raise TypeMismatchInStatement(ast)
        #check parameter
        paraList = funcSym.mtype.intype
        if len(paraList) != len(ast.param):
            raise TypeMismatchInStatement(ast)

        for idx in range(len(ast.param)):
            para = self.visit(idx)
            if type(para) is UnInfer or type(paraList[idx]) is UnInfer:
                raise TypeCannotBeInferred(ast)
            elif type(para) is Unknown and type(paraList[idx]) is Unknown:
                raise TypeCannotBeInferred(ast)
            elif type(para) is Unknown and type(ast.param[idx]) is CallExpr and type(paraList[idx]) is ArrayType:
                if paraList[idx].dimen and type(paraList[idx].eletype) != Unknown:
                    self.updateType(self.getName(ast.param[idx]), envi, paraList[idx])
                else: 
                    raise TypeCannotBeInferred(ast)
            elif type(paraList[idx]) is Unknown and type(para) not in [Unknown, ArrayType]:
                paraList[idx] = para
            elif type(para) is Unknown and type(paraList[idx]) not in [Unknown, ArrayType]:
                para = paraList[idx]
                self.updateType(self.getName(ast.param[idx]), envi, para)
            elif type(paraList[idx]) is ArrayType and type(para) is ArrayType:
                if paraList[idx].dimen != para.dimen:
                    raise TypeMismatchInStatement(ast)
                else:
                    if type(paraList[idx].eletype) is Unknown and type(para.eletype) is Unknown:
                        raise TypeCannotBeInferred(ast)
                    elif type(paraList[idx].eletype) is Unknown:
                        paraList[idx].eletype =  para.eletype
                    elif type(para.eletype)  is Unknown:
                        para.eletype = paraList[idx].eletype
                    elif type(paraList[idx].eletype) != type(para.eletype):
                        raise TypeMismatchInStatement(ast)
            elif type(paraList[idx]) !=  type(para):
                raise TypeMismatchInStatement(ast)

            
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
        return [self.visit(idx) for idx in ast.value] if ast.value else Unknown()