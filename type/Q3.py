from abc import ABC
class Program: pass #decl:List[VarDecl],stmts:List[Assign]

class VarDecl: pass #name:str

class Assign: pass#lhs:Id,rhs:Exp

class Exp(ABC): pass#abstract class

class BinOp(Exp): pass#op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b

class UnOp(Exp): pass#op:str,e:Exp #op is -,-., !,i2f, floor

class IntLit(Exp): pass#val:int

class FloatLit(Exp): pass#val:float

class BoolLit(Exp): pass#val:bool

class Id(Exp): pass#name:str

class TypeMismatchInExpression(Exception): pass

class TypeCannotBeInferred(Exception): pass

class TypeMismatchInStatement(Exception): pass

class UndeclaredIdentifier(Exception): pass

class Visitor():
    pass

from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        list_decl = list(map(lambda x: self.visitVarDecl(x, o), ctx.decl))
        env = {'ctx': None}
        for d in list_decl:
            env.update(d)
        for stmt in ctx.stmts:
            self.visitAssign(stmt, env)

    def visitVarDecl(self,ctx:VarDecl,o):
        return {ctx.name: None}

    def visitAssign(self,ctx:Assign,o):
        o['ctx'] = None
        rhs = self.visit(ctx.rhs, o)
        o['ctx'] = None
        try:
            lhs = self.visit(ctx.lhs, o)
        except TypeCannotBeInferred as e:
            lhs = o[ctx.lhs.name]
        if type(lhs) == type(rhs):
            if lhs == None:
                raise TypeCannotBeInferred(ctx)
            else: return
        if lhs == None:
            o[ctx.lhs.name] = rhs
            return
        if isinstance(rhs, Id):
            rhs = lhs
        raise TypeMismatchInStatement(ctx)

    def visitBinOp(self,ctx:BinOp,o):
        if ctx.op in ['+', '-', '*', '/']:
            o['ctx'] = IntLit(0)
            a = self.visit(ctx.e1, o)

            o['ctx'] = IntLit(0)
            b = self.visit(ctx.e2, o)

            if isinstance(a, IntLit) and isinstance(b, IntLit):
                return IntLit(0)

        if ctx.op in ['+.', '-.', '*.', '/.']:
            o['ctx'] = FloatLit(0)
            a = self.visit(ctx.e1, o)

            o['ctx'] = FloatLit(0)
            b = self.visit(ctx.e2, o)

            if isinstance(a, FloatLit) and isinstance(b, FloatLit):
                return FloatLit(0)

        if ctx.op in ['>', '=']:
            o['ctx'] = IntLit(0)
            a = self.visit(ctx.e1, o)

            o['ctx'] = IntLit(0)
            b = self.visit(ctx.e2, o)

            if isinstance(a, IntLit) and isinstance(b, IntLit):
                return BoolLit(0)

        if ctx.op in ['>.', '=.']:
            o['ctx'] = FloatLit(0)
            a = self.visit(ctx.e1, o)

            o['ctx'] = FloatLit(0)
            b = self.visit(ctx.e2, o)

            if isinstance(a, FloatLit) and isinstance(b, FloatLit):
                return BoolLit(0)

        if ctx.op in ['!','&&', '||', '>b', '=b']:
            o['ctx'] = BoolLit(0)
            a = self.visit(ctx.e1, o)

            o['ctx'] = BoolLit(0)
            b = self.visit(ctx.e2, o)

            if isinstance(a, BoolLit) and isinstance(b, BoolLit):
                return BoolLit(0)

        raise TypeMismatchInExpression(ctx)

    def visitUnOp(self,ctx:UnOp,o):
        if ctx.op in ['-']:
            o['ctx'] = IntLit(0)
            a = self.visit(ctx.e, o)

            if isinstance(a, IntLit):
                return IntLit(0)

        if ctx.op in ['-.']:
            o['ctx'] = FloatLit(0)
            a = self.visit(ctx.e, o)

            if isinstance(a, FloatLit):
                return FloatLit(0)

        if ctx.op in ['!']:
            o['ctx'] = BoolLit(0)
            a = self.visit(ctx.e, o)

            if isinstance(a, BoolLit):
                return BoolLit(0)

        if ctx.op in ['i2f']:
            o['ctx'] = IntLit(0)
            a = self.visit(ctx.e, o)

            if isinstance(a, IntLit):
                return FloatLit(0)

        if ctx.op in ['floor']:
            o['ctx'] = FloatLit(0)
            a = self.visit(ctx.e, o)

            if isinstance(a, FloatLit):
                return IntLit(0)

        raise TypeMismatchInExpression(ctx)

    def visitIntLit(self,ctx:IntLit,o):
        return IntLit(0)

    def visitFloatLit(self,ctx:FloatLit,o):
        return FloatLit(1.1)

    def visitBoolLit(self,ctx:BoolLit,o):
        return BoolLit(True)

    def visitId(self,ctx:Id,o):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
        
        if o[ctx.name] == None:
            o[ctx.name] = o['ctx']
        return o[ctx.name]

