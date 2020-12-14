from functools import reduce
class StaticCheck(Visitor):
    
    def visitProgram(self,ctx:Program,o:object):
        env = reduce(lambda lst,x: lst + [self.visit(x,lst)], ctx.decl, [])

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        else:
            return ctx.name

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        else:
            return ctx.name

    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name)
        else:
            param = reduce(lambda lst, x: lst + [self.visit(x, lst)], ctx.param, [])
            decl = reduce(lambda lst, x: lst + [self.visit(x, lst)], ctx.body[0], [])
            env = o + [ctx.name] + param + decl
            exe=list(map(lambda x: self.visit(x,env), ctx.body[1]))
            return ctx.name


    def visitIntType(self,ctx:IntType,o:object): pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass
        def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass

    def visitId(self,ctx:Id,o:object):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)