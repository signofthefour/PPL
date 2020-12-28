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
from functools import reduce

class MethodEnv():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym
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
        self.sym = symlist_
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
        self.sym = sym_
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

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = MethodEnv(None, self.env)
        c = [self.visit(decl) for decl in ast.decl]
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
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

    # The following code is just for initial, students should remove it and write your visitor from here
    # def genMain(self,o):
    #     methodname,methodtype = "main",MType([ArrayType(StringType())],VoidType())
    #     frame = Frame(methodname, methodtype.rettype)
    #     self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,True,frame))
    #     frame.enterScope(True)
    #     varname,vartype,varindex = "JasminCodeargs",methodtype.partype[0],frame.getNewIndex()
    #     startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
    #     self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
    #     self.emit.printout(self.emit.emitLABEL(startLabel,frame))
    #     self.emit.printout(self.emit.emitPUSHICONST(10, frame))
    #     sym = next(filter(lambda x: x.name == "string_of_int",o.sym))
    #     self.emit.printout(self.emit.emitINVOKESTATIC(sym.value.value+"/string_of_int",sym.mtype,frame))
    #     sym = next(filter(lambda x: x.name == "print",o.sym))
    #     self.emit.printout(self.emit.emitINVOKESTATIC(sym.value.value+"/print",sym.mtype,frame))
    #     self.emit.printout(self.emit.emitLABEL(endLabel, frame))
    #     self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
    #     self.emit.printout(self.emit.emitENDMETHOD(frame))

    def visitVarDecl(self,ctx,o):
        if o.frame == None:
            self.emit.printout(self.emit.emitATTRIBUTE(ctx.name, ctx.typ, False, ''))
            return Symbol(ctx.name, ctx.typ, CName(self.className))
        else:
            idx = o.frame.getNewIndex()
            start_label = o.frame.getStartLabel()
            end_label = o.frame.getEndLabel()
            o.printout(self.emit.emitVAR(idx, ctx.name, ctx.typ, start_label, end_label))
            return Symbol(ctx.name, ctx.typ, Index(idx))
    
    def visitFuncDecl(self,ctx,o):
        frame = Frame(ctx.name, ctx.returnType)
        subBody = SubBody(frame, o.sym)
        frame.enterScope(True)
        param_code_len = reduce(lambda y, p: y + self.visit(p, subBody), ctx.param, 0)
        local_code_len = reduce(lambda y, p: y + self.visit(p, subBody), ctx.body[0], 0)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        stmt_code_len = reduce(lambda y, p: y + self.visit(p, subBody), ctx.body[1], 0)
        # after visit all stmt inside the body
        # there a trick to printout the method decl
        typ = MType([decl.typ for decl in ctx.param], subBody.getRet())
        self.emit.printAt(self.emit.printout(self.emit.emitMETHOD(ctx.name, typ, True)), param_code_len + local_code_len + stmt_code_len + 1)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        typ = MType([], ctx.returnType)
        return Symbol(ctx.name, typ, CName(self.className))

    def visitAssign(self,ctx,o):
        o.isLeft = False
        loc1, _ = self.visit(ctx.rhs, o)
        o.isLeft = True
        loc2, _ = self.visit(ctx.lhs, o)
        return loc1 + loc2

    def visitIf(self, ctx, o):
        new_o = Access(o.frame, o.sym, False)
        loc, _ = self.visit(ctx.ifthenStmt[0][0], new_o)
        l1 = o.frame.getNewLabel()
        l2 = o.frame.getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(l1, o.frame))
        loc += 1
        loc += sum([self.visit(decl, new_o) for decl in ctx.ifthenStmt[0][1]])
        loc += sum([self.visit(stmt, new_o) for stmt in ctx.ifthenStmt[0][2]])
        self.emit.printout(self.emit.emitGOTO(l2, o.frame))
        loc += 1
        self.emit.printout(self.emit.emitLABEL(l1, o.frame))
        loc += 1
        if ctx.estmt:
            loc += sum([self.visit(decl, new_o) for decl in ctx.elseStmt[0]])
            loc += sum([self.visit(stmt, new_o) for stmt in ctx.elseStmt[1]])
        self.emit.printout(self.emit.emitLABEL(l2, o.frame))
        loc += 1
        return loc
    
    def visitWhile(self, ctx, o):
        new_o = Access(o.frame, o.sym, False)
        o.frame.enterLoop()
        inL, outL = o.frame.getContinueLabel(), o.frame.getBreakLabel()
        self.emit.printout(self.emit.emitLABEL(inL, o.frame)); loc=1
        # condition
        loc += self.visit(ctx.expr, new_o)[0]
        self.emit.printout(self.emit.emitIFFALSE(outL, o.frame)); loc+=1
        # declaration
        loc += sum([self.visit(decl) for decl in ctx.sl[0]])
        # enter loop
        loc += sum([self.visit(stmt) for stmt in ctx.sl[1]])
        self.emit.printout(self.emit.emitGOTO(inL, o.frame)); loc+=1
        self.emit.printout(self.emit.emitLABEL(outL, o.frame)); loc+=1
        o.frame.exitLoop()
        return loc
    
    def visitFor(self, ctx, o):
        loc = 0
        o.frame.enterLoop()
        inL, outL = o.frame.getContinueLabel(), o.frame.getBreakLabel()
        o_ = Access(o.frame, o.sym, False)
        # init
        loc = self.visit(ctx.expr1, o_)
        o_.isLeft = True
        loc += self.visit(ctx.idx1, o_)
        o_.isLeft = False
        # decl
        loc += sum([self.visit(decl) for decl in ctx.loop[0]])
        self.emit.printout(self.emit.emitLABEL(inL, o.frame)); loc+=1
        # condition
        loc += self.visit(ctx.expr2, o_)
        self.emit.printout(self.emit.emitIFFALSE(outL, o.frame)); loc+=1
        # loop stmt
        loc += sum([self.visit(stmt) for stmt in ctx.loop[1]])
        # update
        loc += self.visit(ctx.expr3, o_)
        o_.isLeft = True
        loc += self.visit(ctx.idx1, o_)
        self.emit.printout(self.emit.emitGOTO(inL, o.frame)); loc+=1
        self.emit.printout(self.emit.emitLABEL(outL, o.frame)); loc+=1
        o.frame.exitLoop()
        return loc

    def visitBreak(self, ctx, o):
        outL = o.frame.getBreakLabel()
        self.emit.printout(self.emit.emitGOTO(outL, o.frame))
        return 1
    
    def visitContinue(self, ctx, o):
        inL = o.frame.getContinueLabel()
        self.emit.printout(self.emit.emitGOTO(inL, o.frame))
        return 1
    
    def visitReturn(self, ctx, o):
        loc = 0
        if ctx.expr:
            loc_, typ = self.visit(ctx.expr, o)
            loc += loc_
        self.emit.printout(self.emit.emitRETURN(typ, o.frame)); loc+=1
        return loc
    
    def visitDowhile(self, ctx, o):
        new_o = Access(o.frame, o.sym, False)
        o.frame.enterLoop()
        inL, outL = o.frame.getContinueLabel(), o.frame.getBreakLabel()
        self.emit.printout(self.emit.emitLABEL(inL, o.frame)); loc=1
        # declaration
        loc += sum([self.visit(decl) for decl in ctx.sl[0]])
        # enter loop
        loc += sum([self.visit(stmt) for stmt in ctx.sl[1]])
        # condition
        loc += self.visit(ctx.expr, new_o)[0]
        self.emit.printout(self.emit.emitIFFALSE(outL, o.frame)); loc+=1
        self.emit.printout(self.emit.emitGOTO(inL, o.frame)); loc+=1
        self.emit.printout(self.emit.emitLABEL(outL, o.frame)); loc+=1
        o.frame.exitLoop()
        return loc
    
    def visitCallStmt(self, ctx, o):
        method_sym = None
        for sym in o.sym:
            if sym.name == ctx.method.name:
                method_sym = sym
                break
        loc = [self.visit(expr, o)[0] for expr in ctx.param]
        self.emit.printout(self.emit.emitINVOKESTATIC(method_sym.name, method_sym.mtype, o.frame)); loc +=1
        return loc
    
    def visitArrayCell(self, ctx, o):
        


    def visitId(self, ctx, o):
        id_sym = None
        for _sym in o.sym:
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
            
    

    
