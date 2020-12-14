class Exp(ABC): pass #abstract class

class BinOp(Exp): pass #op:str,e1:Exp,e2:Exp #op is +,-,*,/,&&,||, >, <, ==, or  !=

class UnOp(Exp): pass #op:str,e:Exp #op is -, !

class IntLit(Exp): pass #val:int

class FloatLit(Exp): pass #val:float

class BoolLit(Exp): pass #val:bool

class StaticCheck(Visitor):

    def visitBinOp(self,ctx:BinOp,o):
        e1 = self.visit(ctx.e1, o)
        e2 = self.visit(ctx.e2, o)
        if ctx.op in ['+', '-', '*']:
            if e1*e2 == 0:
                raise TypeMismatchInExpression(ctx)
            if e1*e2 < 0:
                return -1
            else:
                return 1
        if ctx.op in ['/']:
            if e1*e2 == 0:
                raise TypeMismatchInExpression(ctx)
            return -1
                
        if ctx.op in ['&&', '||']:
            if (e1 + e2):
                raise TypeMismatchInExpression(ctx)
            return 0
        else:
            if e1 != e2:
                raise TypeMismatchInExpression(ctx)
            return 0

    def visitUnOp(self,ctx:UnOp,o):
        e = self.visit(ctx.e, o)
        if ctx.op in ['-']:
            if e == 0:
                raise TypeMismatchInExpression(ctx)
            return e
        if ctx.op in ['!']:
            if e != 0:
                raise TypeMismatchInExpression(ctx)
            return e

    def visitIntLit(self,ctx:IntLit,o):
        return 1

    def visitFloatLit(self,ctx,o):
        return -1

    def visitBoolLit(self,ctx,o):
        return 0