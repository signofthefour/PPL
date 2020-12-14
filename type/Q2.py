class Program: pass #decl:List[VarDecl],exp:Exp

class VarDecl: pass #name:str,typ:Type

class Type(ABC): pass #abstract class

class IntType(Type): pass

class FloatType(Type): pass

class BoolType(Type): pass

class Exp(ABC): pass #abstract class

class BinOp(Exp): pass #op:str,e1:Exp,e2:Exp #op is +,-,*,/,&&,||, >, <, ==, or  !=

class UnOp(Exp): pass #op:str,e:Exp #op is -, !

class IntLit(Exp): pass #val:int

class FloatLit(Exp): pass #val:float

class BoolLit(Exp): pass #val:bool

class Id(Exp): pass #name:str


from functools import reduce
class StaticCheck(Visitor):
    
    def visitProgram(self,ctx:Program,o):
        env = reduce(lambda lst, x: lst + [self.visitVarDecl(x)], ctx.decl, [])
        self.visit(ctx.exp, env)

    def visitVarDecl(self,ctx:VarDecl,o):
        return {"name" : ctx.name, "type": ctx.typ}

    def visitBinOp(self,ctx:BinOp,o):
        e1 = self.visit(ctx.e1, o)
        e2 = self.visit(ctx.e2, o)
        if ctx.op in ['+', '-', '*']:
            if isinstance(e1, BoolLit) or isinstance(e2, BoolLit):
                raise TypeMismatchInExpression(ctx)
            if isinstance(e1, FloatLit) or isinstance(e2, FloatLit):
                return FloatLit(0)
            else:
                return IntLit(0)
        if ctx.op in ['/']:
            if isinstance(e1, BoolLit) or isinstance(e2, BoolLit):
                raise TypeMismatchInExpression(ctx)
            return FloatLit(0)
                
        if ctx.op in ['&&', '||']:
            if isinstance(e1, BoolLit) and isinstance(e2, BoolLit):
                return BoolLit(True)
            raise TypeMismatchInExpression(ctx)
        else:
            if type(e1) != type(e2):
                raise TypeMismatchInExpression(ctx)
            return BoolLit(True)

    def visitUnOp(self,ctx:UnOp,o):
        e = self.visit(ctx.e, o)
        if ctx.op in ['-']:
            if isinstance(e, BoolLit):
                raise TypeMismatchInExpression(ctx)
            return e
        if ctx.op in ['!']:
            if not isinstance(e, BoolLit):
                raise TypeMismatchInExpression(ctx)
            return e

    def visitIntLit(self,ctx:IntLit,o):
        return IntLit(0)

    def visitFloatLit(self,ctx,o):
        return FloatLit(0)

    def visitBoolLit(self,ctx,o):
        return BoolLit(True)

    def visitId(self,ctx,o):
        a = [idx for (idx, d) in enumerate(o) if d["name"] == ctx.name]
        if len(a) == 0:
            raise UndeclaredIdentifier(ctx.name)
        else:
            typ = o[a[0]]["type"]
            if isinstance(typ, IntType):
                return IntLit(0)
            if isinstance(typ, FloatType):
                return FloatLit(0)
            else:
                return BoolLit(True)
