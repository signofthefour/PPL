'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from abc import ABC, abstractmethod

from Visitor import BaseVisitor
from Emitter import Emitter
from Frame import Frame
from AST import *   
from functools import reduce

class MethodEnv():
    def __init__(self, frame, sym):
        self.frame = frame
        self.symbol = sym
class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
class CName:
    def __init__(self,n):
        self.value = n
class Index:
    def __init__(self,n):
        self.value = n
class Type(ABC): pass
class IntType(Type): pass
class FloatType(Type): pass
class VoidType(Type): pass
class ClassType(Type):
    def __init__(self,n):
        self.cname = n
class StringType(Type):pass
class BoolType(Type): pass
class MType(Type):
    def __init__(self,i,o):
        self.partype = i #List[Type]
        self.rettype = o #Type	
class ArrayType(Type):
    def __init__(self,et,*s):
        self.eleType = et #Type
        self.dimen = s   #List[int]  

class SubBody():
    def __init__(self, frame_, symlist_):
        self.frame = frame_
        self.symbol = symlist_
        self.body = []
        self.ret = VoidType()
    
    def printout(self, code_):
        self.body += [code_]
    
    def emitPrintout(self, emiter):
        [emiter.emit.printout(code) for code in self.body]

    def setRet(self, rettype_):
        self.ret = rettype_
    
    def getRet(self):
        return self.ret

class Access():
    def __init__(self, frame_, sym_, isLeft=False):
        self.frame = frame_
        self.symbol = sym_
        self.isLeft = isLeft
        self.body = []
        self.ret = None
    
    def printout(self, code_):
        self.body += [code_]
    
    def getCode(self):
        return self.body
    
    def setRet(self, rettype_):
        self.ret = rettype_

    def getRet(self):
        return self.ret

class StaticAttribute():
    def __init__(self, className, name, ast):
        self.className = className
        self.name = name
        self.ast = ast
    def init(self, frame, codegen):
        a = Access(frame, [], isLeft=False)
        init_code, typ = codegen.visit(self.ast.varInit, a)
        codegen.emit.printAt(codegen.emit.emitATTRIBUTE(self.name, typ, False, ''), codegen.emit.getBuffLen() - 1   )
        codegen.emit.printout(init_code)
        codegen.emit.printout(codegen.emit.emitPUTSTATIC(self.className + '.' + self.name, typ, frame))
        return Symbol(self.name, typ, CName(self.className))

class CodeGenerator():
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("read", MType([], StringType()), CName(self.libName)),
                    Symbol("printLn", MType([], VoidType()), CName(self.libName)),
                    Symbol("printStrLn", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("print", MType([StringType()], VoidType()), CName(self.libName)),
		    Symbol("string_of_int", MType([IntType()], StringType()), CName(self.libName))
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)



class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.static = []
        self.initVar = []
        self.ret = []

    def visitProgram(self, ast:Program, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = MethodEnv(None, self.env)
        c = [self.visit(decl, e) for decl in ast.decl]
        # self.genMain(e) 
        # generate default constructor
        self.genInit()
        # generate class init if necessary
        self.emit.emitEPILOG()
        return c
    
    # We do not need to save the signature of all the function due to
    # the assumption that there is no semantic error!
    # In the callee we only need to infer the type it self
    # def visitGlobal(self,ast,c):
    #     if isinstance(ast, FuncDecl):
    #         return Symbol(ast.name.name, MType([None]*len(ast.param), None))
    #     if isinstance(ast, VarDecl):
    #         return Symbol(ast.variable.name, None)

    def genInit(self):
        methodname,methodtype = "<init>",MType([],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,False,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "this",ClassType(self.className),frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        self.emit.printout(self.emit.emitREADVAR(varname, vartype, varindex, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        # printout the init_code of the static field
        [var.init(frame, self) for var in self.static]
        # _________
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

    """
    * In var decl, this should add the symbol to frame for later work
    TODOs: 
    @param: self
    @param: 
    """
    def visitVarDecl(self,ctx:VarDecl,o):
        var_name = ctx.variable.name
        dimen = ctx.varDimen
        a = Access(o.frame, o.symbol, isLeft=False)
        if ctx.varInit:
            # handle normal declarations with the assumption of the ass4
            if o.frame == None:
                self.static.append(StaticAttribute(self.className, var_name, ctx))
            else:
                init_code, typ = self.visit(ctx.varInit, a)
                if len(dimen):
                    typ = ArrayType(typ, dimen)
                idx = o.frame.getNewIndex()
                start_label = o.frame.getStartLabel()
                end_label = o.frame.getEndLabel()
                self.emit.printout(self.emit.emitVAR(idx, var_name, typ, start_label, end_label, o.frame))
                init_code += self.emit.emitWRITEVAR(var_name, typ, idx, o.frame)
                self.initVar.append(init_code)
                return Symbol(var_name, typ, Index(idx))
        else:
            # for param in functions
            pass
    
    def visitFuncDecl(self,ctx:FuncDecl,o):
        frame = Frame(ctx.name.name, VoidType())
        subBody = SubBody(frame, o.symbol)
        frame.enterScope(True)
        begin_pos = self.emit.getBuffLen() 
        [self.visit(p, subBody) for p in ctx.param]
        [self.visit(p, subBody) for p in ctx.body[0]]
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        [self.emit.printout(p) for p in self.initVar]
        self.initVar = []
        [self.visit(p, subBody) for p in ctx.body[1]]
        # after visit all stmt inside the body
        # there a trick to printout the method decl
        typ = MType([decl.typ for decl in ctx.param], subBody.getRet())
        # for the Main function: it should be public static void main(String[] args)
        if ctx.name.name == 'main':
            typ = MType([ArrayType(StringType(), [1])], VoidType())
        self.emit.printAt(self.emit.emitMETHOD(ctx.name.name, typ, True, o.frame), self.emit.getBuffLen() - begin_pos)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        [self.emit.printout(code) for code in self.ret]
        self.emit.printout(self.emit.emitRETURN(typ.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return Symbol(ctx.name, typ, CName(self.className))

    def visitAssign(self,ctx:Assign,o):
        o.isLeft = False
        rhs_code, _ = self.visit(ctx.rhs, o)
        o.isLeft = True
        lhs_code, _ = self.visit(ctx.lhs, o)
        self.emit.printout(rhs_code)
        self.emit.printout(lhs_code)

    def visitIf(self, ctx:If, o):
        access = Access(o.frame, o.sym, False)
        expr_code, _ = self.visit(ctx.ifthenStmt[0][0], access)
        l1 = o.frame.getNewLabel()
        l2 = o.frame.getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(l1, o.frame))
        [self.visit(decl, access) for decl in ctx.ifthenStmt[0][1]]
        [self.visit(stmt, access) for stmt in ctx.ifthenStmt[0][2]]
        self.emit.printout(self.emit.emitGOTO(l2, o.frame))
        self.emit.printout(self.emit.emitLABEL(l1, o.frame))
        if ctx.elseStmt:
            [self.visit(decl, access) for decl in ctx.elseStmt[0]]
            [self.visit(stmt, access) for stmt in ctx.elseStmt[1]]
        self.emit.printout(self.emit.emitLABEL(l2, o.frame))
    
    def visitWhile(self, ctx:While, o):
        access = Access(o.frame, o.sym, False)
        o.frame.enterLoop()
        inL, outL = o.frame.getContinueLabel(), o.frame.getBreakLabel()
        self.emit.printout(self.emit.emitLABEL(inL, o.frame))
        # condition
        expr_code, _ = self.visit(ctx.expr, access)
        self.emit.printout(expr_code)
        self.emit.printout(self.emit.emitIFFALSE(outL, o.frame))
        # declaration
        [self.visit(decl) for decl in ctx.sl[0]]
        # enter loop
        [self.visit(stmt) for stmt in ctx.sl[1]]
        self.emit.printout(self.emit.emitGOTO(inL, o.frame))
        self.emit.printout(self.emit.emitLABEL(outL, o.frame))
        o.frame.exitLoop()
    
    def visitFor(self, ctx:For, o):
        o.frame.enterLoop()
        inL, outL = o.frame.getContinueLabel(), o.frame.getBreakLabel()
        o_ = Access(o.frame, o.sym, False)
        # init
        expr1_code, _ = self.visit(ctx.expr1, o_)
        o_.isLeft = True
        idx1_code, _ = self.visit(ctx.idx1, o_)
        o_.isLeft = False
        expr2_code, _ = self.visit(ctx.expr2, o_)
        expr3_code, _ = self.visit(ctx.expr3, o_)
        # decl
        [self.visit(decl) for decl in ctx.loop[0]]
        self.emit.printout(self.emit.emitLABEL(inL, o.frame))
        # condition
        self.emit.printout(expr2_code)
        self.emit.printout(self.emit.emitIFFALSE(outL, o.frame))
        # loop stmt
        [self.visit(stmt) for stmt in ctx.loop[1]]
        # update
        self.emit.printout(expr3_code)
        self.emit.printout(idx1_code)
        self.emit.printout(self.emit.emitGOTO(inL, o.frame))
        self.emit.printout(self.emit.emitLABEL(outL, o.frame))
        o.frame.exitLoop()

    def visitBreak(self, ctx:Break, o):
        outL = o.frame.getBreakLabel()
        self.emit.printout(self.emit.emitGOTO(outL, o.frame))
    
    def visitContinue(self, ctx:Continue, o):
        inL = o.frame.getContinueLabel()
        self.emit.printout(self.emit.emitGOTO(inL, o.frame))
    
    def visitReturn(self, ctx:Return, o):
        typ = VoidType()
        if ctx.expr:
            expr_code, typ = self.visit(ctx.expr, o)
            o.frame.rettype = typ
            self.ret.append(expr_code)
        # self.emit.printout(self.emit.emitRETURN(typ, o.frame))
        o.setRet(typ)
    
    def visitDowhile(self, ctx:Dowhile, o):
        access = Access(o.frame, o.sym, False)
        expr_code, _ = self.visit(ctx.expr, access)
        o.frame.enterLoop()
        inL, outL = o.frame.getContinueLabel(), o.frame.getBreakLabel()
        # declaration
        [self.visit(decl) for decl in ctx.sl[0]]
        # enter loop
        self.emit.printout(self.emit.emitLABEL(inL, o.frame))
        [self.visit(stmt) for stmt in ctx.sl[1]]
        # condition
        self.emit.printout(expr_code)
        self.emit.printout(self.emit.emitIFFALSE(outL, o.frame))
        self.emit.printout(self.emit.emitGOTO(inL, o.frame))
        self.emit.printout(self.emit.emitLABEL(outL, o.frame))
        o.frame.exitLoop()
    
    def visitCallStmt(self, ctx:CallStmt, o):
        method_sym = None
        for sym in o.sym:
            if sym.name == ctx.method.name:
                method_sym = sym
                break
        access = Access(o.frame, o.sym, isLeft=False)
        expr_codes = [self.visit(expr, access) for expr in ctx.param]
        [self.emit.printout(code) for code in [ret[0] for ret in expr_codes]]
        typ = [ret[1] for ret in expr_codes]
        self.emit.printout(self.emit.emitINVOKESTATIC(method_sym.name, method_sym.mtype, o.frame))
    
    """
    ! I dont know if we can use emitREADVAR for this
    TODOs: try some experiences
    """
    def visitArrayCell(self, ctx, o):
        access = Access(o.frame, o.symbol, isLeft=True)
        self.visit(ctx.arr, access)
        exprs = [self.visit(expr, access) for expr in ctx.idx]
        [self.emit.printout(expr[0] + self.emit.printout(self.emit.emitALOAD(ArrayType(), o.frame))) for expr in exprs]
        self.emit.printout(self.emit)
    
    def visitUnaryOp(self, ctx, o):
        expr, typ = self.visit(ctx.body)
        if ctx.op in ['!']:
            code = expr + self.emit.emitNOT(BoolType(), o.frame)
            return code, BoolType()
        elif ctx.op in ['-']:
            code = expr + self.emit.emitNEGOP(typ, o.frame)
            return code, typ
    
    def visitBinaryOp(self, ctx, o):
        l, typ = self.visit(ctx.left, o)
        r, typ = self.visit(ctx.right, o)
        code, rettyp = None, None

        if ctx.op in ['+', '-', '+.', '-.']:
            if ctx.op in ['+', '+.']:
                code =  l + r + self.emit.emitADDOP('+', typ, o.frame)
                rettyp = typ
            else:
                code = l + r + self.emit.emitADDOP('-', typ, o.frame)
                rettyp = typ
        elif ctx.op in ['*', '*.', '\\', '\\.', '%']:
            if ctx.op in ['*', '*.']:
                code = l + r + self.emit.emitMULOP('*', typ, o.frame)
                rettyp = typ
            elif ctx.op in ['\\', '\\.']:
                code = l + r + self.emit.emitMULOP('\\', typ, o.frame)
                rettyp = typ
            else:
                code = l + r + self.emit.emitMOD(o.frame)
                rettyp = typ
        elif ctx.op in ['&&', '||']:
            if ctx.op in ['&&']:
                code = l + r + self.emit.emitANDOP(o.frame)
                rettyp = BoolType()
            else:
                code = l + r + self.emit.emitOROP(o.frame)
                rettyp = BoolType()
        elif ctx.op in ['==', '!=', '<', '>', '<=', '>=', '=/=', '<.', '>.', '<=.', '>=.']:
            if ctx.op in ['==']:
                code = l + r + self.emit.emitREOP('==', typ, o.frame)
            elif ctx.op in ['!=', '=/=']:
                code = l + r + self.emit.emitREOP('!=', typ, o.frame)
            elif ctx.op in ['<', '<.']:
                code = l + r + self.emit.emitREOP('<', typ, o.frame)
            elif ctx.op in ['>', '>.']:
                code = l + r + self.emit.emitREOP('>', typ, o.frame)
            elif ctx.op in ['<=', '<=.']:
                code = l + r + self.emit.emitREOP('<=', typ, o.frame)
            elif ctx.op in ['>=', '>=.']:
                code = l + r + self.emit.emitREOP('>=', typ, o.frame)
            rettyp = BoolType()
        return code, rettyp
    
    def visitIntLiteral(self, ctx, o):
        code = self.emit.emitPUSHICONST(ctx.value, o.frame)
        return code, IntType()
    def visitFloatLiteral(self,ctx,o):
        code  = self.emit.emitPUSHFCONST(ctx.value, o.frame)
        return code, FloatType()
    def visitStringLiteral(self, ctx, o):
        code = self.emit.emitPUSHCONST(ctx.value, StringType(), o.frame)
        return code, StringType()
    def visitBooleanLiteral(self, ctx, o):
        code = self.emit.emitPUSHICONST(str(ctx.value).lower(), o.frame)
        return code, BoolType()
    def visitArrayLiteral(self, ctx, o):
        pass

    def visitId(self, ctx, o):
        id_sym = None
        for _sym in o.symbol:
            if _sym.name == ctx.name:
                id_sym = _sym
                break
        if o.isLeft:
            if isinstance(id_sym.value, Index):
                code = self.emit.emitWRITEVAR(id_sym.name, id_sym.mtype, id_sym.value.value, o.frame)
                self.emit.printout(code)
                return 1, id_sym.mtype
            else:
                code = self.emit.emitPUTSTATIC(id_sym.value.value + '.' + ctx.name, id_sym.mtype, o.frame)
                self.emit.printout(code)
                return 1, id_sym.mtype
        else:
            if isinstance(id_sym.value, Index):
                code = self.emit.emitREADVAR(id_sym.name, id_sym.mtype, id_sym.value.value, o.frame)
                self.emit.printout(code)
                return 1, id_sym.mtype
            else:
                code = self.emit.emitGETSTATIC(id_sym.value.value + '.' + ctx.name, id_sym.mtype, o.frame)
                self.emit.printout(code)
                return 1, id_sym.mtype

    
