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
    def init(self, a, codegen):
        init_code, typ = codegen.visit(self.ast.varInit, a)
        codegen.emit.printAt(codegen.emit.emitATTRIBUTE(self.name, typ, False, ''), codegen.emit.getBuffLen() - 1   )
        # codegen.emit.printout(init_code)
        # codegen.emit.printout(codegen.emit.emitPUTSTATIC(self.className + '.' + self.name, typ, a.frame))

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
        self.envFuncNum = 0
        self.staticFunction = []
        self.initStatic = []
        self.clinitStackSize = 0

    def visitProgram(self, ast:Program, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = MethodEnv(None, self.env)
        self.envFuncNum = len(self.env)
        # self.env = [self.visit(decl, e) for decl in ast.decl] + self.env
        for decl in ast.decl:
            s = self.visit(decl, e)
            e.symbol.append(s)
        # reduce(lambda e, decl: e.symbol + [self.visit(decl, e)], ast.decl, e)
        # self.genMain(e) 
        # generate default constructor
        self.genInit()
        self.genClinit()
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
        a = Access(frame, self.env, isLeft=False)
        [static.init(a, self) for static in self.static]
        self.clinitStackSize = a.frame.getMaxOpStackSize()
        # _________
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
    
    def genClinit(self):
        methodname,methodtype = "<clinit>",MType([],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,True,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "this",ClassType(self.className),frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        # self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        # self.emit.printout(self.emit.emitREADVAR(varname, vartype, varindex, frame))
        # self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        # printout the init_code of the static field
        [self.emit.printout(p) for p in self.initStatic]
        self.initStatic = []
        frame.maxOpStackSize = self.clinitStackSize
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
        dimen = list(ctx.varDimen)
        if isinstance(dimen, tuple):
            dimen = dimen[0]
        a = Access(o.frame, o.symbol, isLeft=False)
        if ctx.varInit:
            # handle normal declarations with the assumption of the ass4
            if o.frame == None:
                self.static.append(StaticAttribute(self.className, var_name, ctx))
                methodname,methodtype = "<init>",MType([],VoidType())
                a.frame = Frame(methodname, methodtype.rettype)
                init_code, typ = self.visit(ctx.varInit, a)
                init_code += self.emit.emitPUTSTATIC(self.className + '.' + var_name, typ, a.frame)
                self.initStatic.append(init_code)
                return Symbol(var_name, typ, CName(self.className))
            else:
                init_code, typ = self.visit(ctx.varInit, o)
                # if len(dimen):
                #     typ = ArrayType(typ, dimen)
                idx = o.frame.getNewIndex()
                start_label = o.frame.getStartLabel()
                end_label = o.frame.getEndLabel()
                self.emit.printout(self.emit.emitVAR(idx, var_name, typ, start_label, end_label, o.frame))
                init_code += self.emit.emitWRITEVAR(var_name, typ, idx, o.frame)
                self.initVar.append(init_code)
                # print('Index of {} in decl is {}'.format(var_name, idx))
                return Symbol(var_name, typ, Index(idx))
        else:
            # for param in functions
            idx = o.frame.getNewIndex()
            # self.emit.printout(self.emit.emitVAR(idx, var_name, typ, start_label, end_label, o.frame))
            if len(dimen):
                typ = ArrayType(None, dimen)
            else:
                typ = None
            return Symbol(var_name, typ, Index(idx))
    
    def visitFuncDecl(self,ctx:FuncDecl,o):
        frame = Frame(ctx.name.name, VoidType())
        subBody = SubBody(frame, o.symbol)
        frame.enterScope(True)
        begin_pos = self.emit.getBuffLen()
        partype = rettype = None
        for method in self.staticFunction:
            if method.name == ctx.name.name:
                # have invoked before its decl
                partype = method.mtype.partype
                rettype = method.mtype.rettype
        params = [self.visit(p, subBody) for p in ctx.param]
        if partype != None:
            params = list(map(lambda x, y: Symbol(x.name, y, x.value), params, partype))
        subBody.symbol = params + subBody.symbol
        # reduce(lambda e, decl: e.symbol + [self.visit(decl, e)], ctx.param, subBody)
        subBody.symbol = [self.visit(p, subBody) for p in ctx.body[0]] + subBody.symbol
        # reduce(lambda e, decl: e.symbol + [self.visit(decl, e)], ctx.body[0], subBody)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        [self.emit.printout(p) for p in self.initVar]
        self.initVar = []
        [self.visit(p, subBody) for p in ctx.body[1]]
        # after visit all stmt inside the body
        # there a trick to printout the method decl
        intype = []
        for name in [decl.variable.name for decl in ctx.param]:
            for sym in subBody.symbol:
                if sym.name == name:
                    start_label = subBody.frame.getStartLabel()
                    end_label = subBody.frame.getEndLabel()
                    if type(sym.mtype) is ArrayType:
                        if isinstance(sym.mtype.dimen, tuple):
                            sym.mtype.dimen = sym.mtype.dimen[0]
                    self.emit.printAt(self.emit.emitVAR(sym.value.value, name, sym.mtype, start_label, end_label, o.frame), self.emit.getBuffLen() - begin_pos)
                    intype.append(sym.mtype)
                    break
        typ = MType(intype, subBody.getRet())
        # for the Main function: it should be public static void main(String[] args)
        if ctx.name.name == 'main':
            start_label = subBody.frame.getStartLabel()
            end_label = subBody.frame.getEndLabel()
            self.emit.printAt(self.emit.emitVAR(frame.getNewIndex(), 'args', ArrayType(StringType(), [1]), start_label, end_label, o.frame), self.emit.getBuffLen() - begin_pos)
            typ = MType([ArrayType(StringType(), [1])], VoidType())
            print('come here')
        self.emit.printAt(self.emit.emitMETHOD(ctx.name.name, typ, True, o.frame), self.emit.getBuffLen() - begin_pos)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        # [self.emit.printout(code) for code in self.ret]
        # self.emit.printout(self.emit.emitRETURN(typ.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        o.symbol += [Symbol(ctx.name.name, typ, CName(self.className))]

    def visitAssign(self,ctx:Assign,o):
        access = Access(o.frame, o.symbol, isLeft=False)
        rhs_code, r_type = self.visit(ctx.rhs, access)
        access.isLeft = True
        lhs_code, l_type = self.visit(ctx.lhs, access)
        # Infer the type of unknown
        if rhs_code == None:
            self.infer(ctx.rhs, l_type, access)
            access.isLeft = False
            rhs_code, r_type = self.visit(ctx.rhs, access)
            # print(rhs_code)
        if lhs_code == None:
            self.infer(ctx.lhs, r_type, access)
            access.isLeft = True
            lhs_code, l_type = self.visit(ctx.lhs, access)
        # We must have the correct type after infered (instead of None)
        lines = lhs_code.split('\n')
        lines.insert(-2, rhs_code)
        self.emit.printout('\n'.join(lines))

    def visitIf(self, ctx:If, o):
        labels = list(map(lambda x: o.frame.getNewLabel(), range(len(ctx.ifthenStmt) + 1)))
        for idx in range(len(ctx.ifthenStmt)):
            access = Access(o.frame, o.symbol, False)
            expr_code, typ = self.visit(ctx.ifthenStmt[idx][0], access)
            if typ == None:
                self.inferId(ctx.ifthenStmt[idx][0], BoolType(), access)
                expr_code, typ = self.visit(ctx.ifthenStmt[idx][0], access)
            l1 = labels[idx]
            l2 = labels[-1]
            self.emit.printout(expr_code)
            self.emit.printout(self.emit.emitIFFALSE(l1, access.frame))
            access.symbol = [self.visit(decl, access) for decl in ctx.ifthenStmt[idx][1]] + access.symbol
            [self.emit.printout(p) for p in self.initVar]
            self.initVar = []
            [self.visit(stmt, access) for stmt in ctx.ifthenStmt[idx][2]]
            self.emit.printout(self.emit.emitGOTO(l2, access.frame))
            self.emit.printout(self.emit.emitLABEL(l1, access.frame))
        if ctx.elseStmt:
            access.symbol = [self.visit(decl, access) for decl in ctx.elseStmt[0]] + access.symbol
            [self.emit.printout(p) for p in self.initVar]
            self.initVar = []
            [self.visit(stmt, access) for stmt in ctx.elseStmt[1]]
        self.emit.printout(self.emit.emitLABEL(labels[-1], access.frame)) 
    
    def visitWhile(self, ctx:While, o):
        access = Access(o.frame, o.symbol, False)
        o.frame.enterLoop()
        inL, outL = o.frame.getContinueLabel(), o.frame.getBreakLabel()
        self.emit.printout(self.emit.emitLABEL(inL, o.frame))
        # condition
        expr_code, typ = self.visit(ctx.exp, access)
        if expr_code == None:
            self.infer(ctx.exp, BoolType(), access)
            expr_code, typ = self.visit(ctx.exp, access)
        self.emit.printout(expr_code)
        self.emit.printout(self.emit.emitIFFALSE(outL, access.frame))
        # declaration
        access.symbol = [self.visit(decl, access) for decl in ctx.sl[0]] + access.symbol
        [self.emit.printout(p) for p in self.initVar]
        self.initVar = []
        # enter loop
        [self.visit(stmt, access) for stmt in ctx.sl[1]]
        self.emit.printout(self.emit.emitGOTO(inL, access.frame))
        self.emit.printout(self.emit.emitLABEL(outL, access.frame))
        o.frame.exitLoop()
    
    def visitFor(self, ctx:For, o):
        o.frame.enterLoop()
        inL, outL = o.frame.getContinueLabel(), o.frame.getBreakLabel()
        o_ = Access(o.frame, o.symbol, False)
        # init
        expr1_code, _ = self.visit(ctx.expr1, o_)
        if expr1_code == None:
            self.infer(ctx.expr1, IntType(), o_)
            expr1_code, _ = self.visit(ctx.expr1, o_)
        o_.isLeft = True
        idx1_code, _ = self.visit(ctx.idx1, o_)
        o_.isLeft = False
        expr2_code, _ = self.visit(ctx.expr2, o_)
        if expr2_code == None:
            self.infer(ctx.expr2, IntType(), o_)
            expr1_code, _ = self.visit(ctx.expr2, o_)
        expr3_code, _ = self.visit(ctx.expr3, o_)
        if expr3_code == None:
            self.infer(ctx.expr3, IntType(), o_)
            expr1_code, _ = self.visit(ctx.expr3, o_)
        # decl
        [self.visit(decl, o_) for decl in ctx.loop[0]]
        [self.emit.printout(p) for p in self.initVar]
        self.initVar = []
        self.emit.printout(self.emit.emitLABEL(inL, o.frame))
        # condition
        self.emit.printout(expr2_code)
        self.emit.printout(self.emit.emitIFFALSE(outL, o.frame))
        # loop stmt
        [self.visit(stmt, o_) for stmt in ctx.loop[1]]
        # update
        o_.isLeft = False
        idx1_code_load, _ = self.visit(ctx.idx1, o_)
        self.emit.printout(idx1_code_load)
        self.emit.printout(expr3_code)
        self.emit.printout(self.emit.emitADDOP('+', IntType(), o_.frame))
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
        a = Access(o.frame, o.symbol, isLeft=False)
        typ = VoidType()
        if ctx.expr:
            expr_code, typ = self.visit(ctx.expr, a)
            self.ret.append(expr_code)
            self.emit.printout(expr_code)
        self.emit.printout(self.emit.emitRETURN(typ, a.frame))
        o.setRet(typ)
    
    def visitDowhile(self, ctx:Dowhile, o):
        access = Access(o.frame, o.symbol, False)
        expr_code, _ = self.visit(ctx.exp, access)
        if expr_code == None:
            self.infer(ctx.expr, BoolType(), access)
            expr_code, _ = self.visit(ctx.exp, access)
        o.frame.enterLoop()
        inL, outL = o.frame.getContinueLabel(), o.frame.getBreakLabel()
        # declaration
        access.symbol = [self.visit(decl, access) for decl in ctx.sl[0]] + access.symbol
        [self.emit.printout(p) for p in self.initVar]
        self.initVar = []
        # enter loop
        self.emit.printout(self.emit.emitLABEL(inL, o.frame))
        [self.visit(stmt, access) for stmt in ctx.sl[1]]
        # condition
        self.emit.printout(expr_code)
        self.emit.printout(self.emit.emitIFFALSE(outL, o.frame))
        self.emit.printout(self.emit.emitGOTO(inL, o.frame))
        self.emit.printout(self.emit.emitLABEL(outL, o.frame))
        o.frame.exitLoop()
    
    def visitCallStmt(self, ctx:CallStmt, o):
        method_sym = None
        for sym in o.symbol:
            if sym.name == ctx.method.name:
                method_sym = sym
                break
        access = Access(o.frame, o.symbol, isLeft=False)
        expr_codes = []
        if method_sym != None:
            # infer the args in case the function has been inferred
            # print(list(map(lambda x,y: (x,y), ctx.param, method_sym.mtype.partype)))
            for (expr, expect) in list(map(lambda x,y: (x,y), ctx.param, method_sym.mtype.partype)):
                expr_code, typ = self.visit(expr, access)
                if expr_code == None:
                    self.infer(expr, expect, access)
                    expr_code, typ = self.visit(expr, access)
                expr_codes.append([expr_code, typ])
        else:
            name = ctx.method.name
            partype = [None]*len(ctx.param)
            rettype = VoidType()
            typ = MType(partype, rettype)
            self.staticFunction.append(Symbol(name, typ, CName(self.className)))
            method_sym = self.staticFunction[-1]
            expr_codes = [self.visit(expr, access) for expr in ctx.param]
        [self.emit.printout(code) for code in [ret[0] for ret in expr_codes]]
        typ = None
        className = self.className
        if method_sym == None:
            typ = MType([ret[1] for ret in expr_codes], VoidType())
            self.staticFunction.append(Symbol(ctx.method.name, typ, CName(self.className)))
        else:
            typ = method_sym.mtype
            className = method_sym.value.value
        self.emit.printout(self.emit.emitINVOKESTATIC(className +"."+ctx.method.name, typ, o.frame))
    
    def visitCallExpr(self, ctx:CallExpr, o):
        method_sym = None
        for sym in o.symbol:
            if sym.name == ctx.method.name:
                method_sym = sym
                break
        # Not yet go through
        if method_sym == None:
            for method in self.staticFunction:
                if method.name == ctx.method.name:
                    method_sym = method
                    break
        if method_sym == None:
            o.frame.push()
            return None, None
        access = Access(o.frame, o.symbol, isLeft=False)
        expr_codes = []
        if method_sym != None:
            if any([p == None for p in method_sym.mtype.partype]):
                # print('come here: ', method_sym.mtype.rettype)
                return None, None
            partype = method_sym.mtype.partype
            # infer the args in case the function has been inferred
            # print(list(map(lambda x,y: (x,y), ctx.param, method_sym.mtype.partype)))
            for (idx, p) in enumerate(ctx.param):
                code, typ = self.visit(p, access)
                if code == None:
                    if partype[idx] == None:
                        partype[idx] = IntType()
                    self.infer(p, partype[idx], access)
                    code, typ =self.visit(p, access)
                partype[idx] = typ
                expr_codes.append((code,typ))
        else:
            expr_codes = [self.visit(expr, access) for expr in ctx.param]
        code = ""
        if len(expr_codes) > 1:
            code = reduce(lambda x,y: x + y, [ret[0] for ret in expr_codes], "")
        elif len(expr_codes) == 1:
            code = expr_codes[0][0]
        print('the code: ', code)
        typ = method_sym.mtype
        className = method_sym.value.value
        # print('name of sym: {} and name of method: {}'.format(3method_sym.name, ctx.method.name))
        code += self.emit.emitINVOKESTATIC(className +"."+ctx.method.name, typ, o.frame)
        return code, method_sym.mtype.rettype
    
    """
    ! I dont know if we can use emitREADVAR for this
    TODOs: try some experiences
    """
    def visitArrayCell(self, ctx, o):
        access = Access(o.frame, o.symbol, isLeft=False)
        code, typ = self.visit(ctx.arr, access)
        if typ.eleType == None:
            return None, typ.eleType
        idxs_code = [self.visit(expr, access)[0] for expr in ctx.idx]
        for idx_code in idxs_code[:-1]:
            code += idx_code + self.emit.emitALOAD(ArrayType(typ, [1]), o.frame)
        if o.isLeft:
            code += idxs_code[-1] + self.emit.emitASTORE(typ.eleType, o.frame)
        else:
            code += idxs_code[-1] + self.emit.emitALOAD(typ.eleType, o.frame)
        return code, typ.eleType
    
    def visitUnaryOp(self, ctx, o):
        expr, typ = self.visit(ctx.body, o)
        if expr == None:
            self.infer(ctx.body, BoolType(), o)
            expr, typ = self.visit(ctx.body, o)
        if ctx.op in ['!']:
            code = expr + self.emit.emitNOT(BoolType(), o.frame)
            return code, BoolType()
        elif ctx.op in ['-', '-.']:
            code = expr + self.emit.emitNEGOP(typ, o.frame)
            return code, typ
    
    def visitBinaryOp(self, ctx, o):
        l, ltyp = self.visit(ctx.left, o)
        r, rtyp = self.visit(ctx.right, o)
        if ltyp == None:
            if ctx.op in ['+', '-', '*', '\\', '%', '==', '!=', '<', '>', '<=', '>=']:
                self.infer(ctx.left, IntType(), o)
            elif ctx.op in ['||', '&&']:
                self.infer(ctx.left, BoolType(), o)
            else:
                self.infer(ctx.left, FloatType(), o)
            l, ltyp = self.visit(ctx.left, o)
        elif rtyp == None:
            if ctx.op in ['+', '-', '*', '\\', '%', '==', '!=', '<', '>', '<=', '>=']:
                self.infer(ctx.right, IntType(), o)
            elif ctx.op in ['||', '&&']:
                self.infer(ctx.right, BoolType(), o)
            else:
                self.infer(ctx.right, FloatType(), o)
            r, rtyp = self.visit(ctx.right, o)
        typ = ltyp
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
        code  = self.emit.emitPUSHFCONST(str(ctx.value), o.frame)
        return code, FloatType()
    def visitStringLiteral(self, ctx, o):
        code = self.emit.emitPUSHCONST('"' + ctx.value + '"', StringType(), o.frame)
        return code, StringType()
    def visitBooleanLiteral(self, ctx, o):
        code = self.emit.emitPUSHICONST(str(ctx.value).lower(), o.frame)
        return code, BoolType()
    def visitArrayLiteral(self, ctx, o):
        access = o
        # lit_code = list(map(lambda x: self.visit(x, access), ctx.value))
        # lit_code = [ret[0] for ret in lit_code]
        # lit_code = list(map(lambda code, idx: self.emit.emitDUP(access.frame) + \
        #         self.emit.emitPUSHICONST(idx, access.frame) + code + \
        #         self.emit.emitASTORE(ele_type, access.frame), lit_code, range(len(lit_code))))
        init_code = ""
        ele_type = None
        for (idx, lit) in enumerate(ctx.value):
            init_code += self.emit.emitDUP(access.frame)
            init_code += self.emit.emitPUSHICONST(idx, access.frame)
            code, ele_type = self.visit(lit, access)
            init_code += code
            init_code += self.emit.emitASTORE(ele_type, access.frame)
        access.frame.maxOpStackSize += 1
        code = self.emit.emitANEWARRAY(ele_type, len(ctx.value), access.frame)
        code = code + init_code
        if isinstance(ele_type, ArrayType):
            # print(ele_type.dimen)
            if isinstance(ele_type.dimen, tuple):
                ele_type.dimen = ele_type.dimen[0]
            ele_type.dimen = [len(ctx.value)] + ele_type.dimen
        else:
            ele_type = ArrayType(ele_type, [len(ctx.value)])
        return code, ele_type
    def visitId(self, ctx, o):
        id_sym = None
        for _sym in o.symbol:
            if _sym.name == ctx.name:
                id_sym = _sym
                break
        if id_sym.mtype == None:
            return None, id_sym.mtype
        elif isinstance(id_sym.mtype, ArrayType) and id_sym.mtype.eleType == None:
            return None, id_sym.mtype
        # print('name: {}, mtype: {}, index: {}'.format(id_sym.name, id_sym.mtype, id_sym.value.value))
        if o.isLeft:
            if isinstance(id_sym.value, Index):
                # print('name: {}, mtype: {}, index: {}'.format(id_sym.name, id_sym.mtype, id_sym.value.value))
                code = self.emit.emitWRITEVAR(id_sym.name, id_sym.mtype, id_sym.value.value, o.frame)
                return code, id_sym.mtype
            else:
                code = self.emit.emitPUTSTATIC(id_sym.value.value + '.' + ctx.name, id_sym.mtype, o.frame)
                return code, id_sym.mtype
        else:
            if isinstance(id_sym.value, Index):
                code = self.emit.emitREADVAR(id_sym.name, id_sym.mtype, id_sym.value.value, o.frame)
                return code, id_sym.mtype
            else:
                code = self.emit.emitGETSTATIC(id_sym.value.value + '.' + ctx.name, id_sym.mtype, o.frame)
                return code, id_sym.mtype

    
    def inferId(self, id, expect_type, o):
        for sym in o.symbol:
            if id.name == sym.name:
                if sym.mtype == None:
                    sym.mtype = expect_type
                if isinstance(sym.mtype, ArrayType):
                    if sym.mtype.eleType == None:
                        return None, sym.mtype
                break
    
    def inferArray(self, arr, expect_type, o):
        access = Access(o.frame, o.symbol, isLeft=o.isLeft)
        code, typ = self.visit(arr.arr, access)
        if typ.eleType == None:
            typ.eleType = expect_type
            ele_type = typ.eleType
            code, typ = self.visit(arr.arr, access)
            lit = None
            dimen = typ.dimen[0]
            if isinstance(typ.eleType, IntType):
                lit = ArrayLiteral([IntLiteral(0)]*dimen[-1])
            elif isinstance(typ.eleType, BoolType):
                lit = ArrayLiteral([BooleanLiteral(False)]*dimen[-1])
            elif isinstance(typ.eleType, StringType):
                lit = ArrayLiteral([StringLiteral("")]*dimen[-1])
            elif isinstance(typ.eleType, FloatType):
                lit = ArrayLiteral([FloatType(0.0)]*dimen[-1])
            for d in dimen[::-1][1:]:
                lit = ArrayLiteral([lit]*d)
            lit_code, _ = self.visitArrayLiteral(lit, access)
            code = lit_code + code
        self.emit.printout(code)
    
    def inferCallExpr(self, callee, expect_type, o):
        # args_and_types = [self.visit(p,o) for p in callee.param]
        name = callee.method.name
        method_sym = None
        for method in self.staticFunction:
            if method.name == name:
                method_sym = method
                break
        if method_sym == None:
            partype = [None]*len(callee.param)
            rettype = expect_type
            typ = MType(partype, rettype)
            self.staticFunction.append(Symbol(name, typ, CName(self.className)))
            method_sym = self.staticFunction[-1]
        partype = method_sym.mtype.partype
        """
        TODOs: infer the function  that be invokeed before declared
        e.g.: foo(foo(x))
        """
        args_and_types = []
        access = o
        for (idx, p) in enumerate(callee.param):
            code, typ = self.visit(p, access)
            if code == None:
                if partype[idx] == None:
                    partype[idx] = IntType()
                self.infer(p, partype[idx], access)
                code, typ = self.visit(p, access)
            partype[idx] = typ
        # access = o
        # for p in callee.param:
        #     code, typ = self.visit(p, access)
        #     if code == None:
        #         code, typ = self.infer(p, access)
        # for (expr, expect) in list(map(lambda x,y: (x,y), callee.param, method_sym.mtype.partype)):
        #         expr_code, typ = self.visit(expr, access)
        #         if expr_code == None:
        #             self.infer(expr, expect, access)
        #             expr_code, typ = self.visit(expr, access)
        #         expr_codes.append([expr_code, typ])

    def infer(self, x, expect_type, o):
        if isinstance(x, Id):
            self.inferId(x, expect_type, o)
            return None
        elif isinstance(x, ArrayCell):
            self.inferArray(x, expect_type, o)
            return None
        elif isinstance(x, CallExpr):
            return self.inferCallExpr(x, expect_type, o)