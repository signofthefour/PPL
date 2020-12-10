class StaticCheck(Visitor):
    
    def visitProgram(self,ctx:Program,o:object):
        from functools import reduce
        reduce(lambda lst, x: self.visitVarDecl(x, lst) if isinstance(x, VarDecl) else self.visitConstDecl(x, lst), ctx.decl ,[])

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name not in o:
            raise RedeclaredDeclaration(ctx.name)
        return ctx.name
        

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name not in o:
            raise RedeclaredDeclaration(ctx.name)
        return ctx.name


    def visitIntType(self,ctx:IntType,o:object): pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass