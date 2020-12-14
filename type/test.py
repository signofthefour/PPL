from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        env = dict({'ctx': None})
        reduce(lambda env, x: self.visitVarDecl(x, env), ctx.decl, env)
        for stmt in ctx.stmts:
            self.visit(stmt, [env])
            
    def visitBlock(self,ctx:Block,o):
        env = dict({'ctx': None})
        reduce(lambda env, x: self.visitVarDecl(x, env), ctx.decl, env)
        for stmt in ctx.stmts:
            self.visitAssign(stmt, [env]+o)

    def visitVarDecl(self,ctx:VarDecl,o):
        if ctx.name in o:
            raise Redeclared(ctx)
        o.update(dict({ctx.name: None}))

    def visitAssign(self,ctx:Assign,o):
        o[0]['ctx'] = None
        rhs = self.visit(ctx.rhs, o)
        o[0]['ctx'] = None
        lhs = self.visit(ctx.lhs, o)
        if type(lhs) == type(rhs):
            if lhs == None:
                raise TypeCannotBeInferred(ctx)
            else:
                return
        if lhs == None:
            o[0][ctx.lhs.name] = rhs
            return
        if isinstance(ctx.rhs, Id) and rhs == None:
            o[0][ctx.rhs.name] = lhs
            return
        raise TypeMismatchInStatement(ctx)

    def visitBinOp(self,ctx:BinOp,o):
        if ctx.op in ['+', '-', '*', '/']:
            o[0]['ctx'] = IntLit(0)
            a = self.visit(ctx.e1, o)

            o[0]['ctx'] = IntLit(0)
            b = self.visit(ctx.e2, o)

            if isinstance(a, IntLit) and isinstance(b, IntLit):
                return IntLit(0)

        if ctx.op in ['+.', '-.', '*.', '/.']:
            o[0]['ctx'] = FloatLit(0)
            a = self.visit(ctx.e1, o)

            o[0]['ctx'] = FloatLit(0)
            b = self.visit(ctx.e2, o)

            if isinstance(a, FloatLit) and isinstance(b, FloatLit):
                return FloatLit(0)

        if ctx.op in ['>', '=']:
            o[0]['ctx'] = IntLit(0)
            a = self.visit(ctx.e1, o)

            o[0]['ctx'] = IntLit(0)
            b = self.visit(ctx.e2, o)

            if isinstance(a, IntLit) and isinstance(b, IntLit):
                return BoolLit(0)

        if ctx.op in ['>.', '=.']:
            o[0]['ctx'] = FloatLit(0)
            a = self.visit(ctx.e1, o)

            o[0]['ctx'] = FloatLit(0)
            b = self.visit(ctx.e2, o)

            if isinstance(a, FloatLit) and isinstance(b, FloatLit):
                return BoolLit(0)

        if ctx.op in ['!','&&', '||', '>b', '=b']:
            o[0]['ctx'] = BoolLit(0)
            a = self.visit(ctx.e1, o)

            o[0]['ctx'] = BoolLit(0)
            b = self.visit(ctx.e2, o)

            if isinstance(a, BoolLit) and isinstance(b, BoolLit):
                return BoolLit(0)

        raise TypeMismatchInExpression(ctx)

    def visitUnOp(self,ctx:UnOp,o):
        if ctx.op in ['-']:
            o[0]['ctx'] = IntLit(0)
            a = self.visit(ctx.e, o)

            if isinstance(a, IntLit):
                return IntLit(0)

        if ctx.op in ['-.']:
            o[0]['ctx'] = FloatLit(0)
            a = self.visit(ctx.e, o)

            if isinstance(a, FloatLit):
                return FloatLit(0)

        if ctx.op in ['!']:
            o[0]['ctx'] = BoolLit(0)
            a = self.visit(ctx.e, o)

            if isinstance(a, BoolLit):
                return BoolLit(0)

        if ctx.op in ['i2f']:
            o[0]['ctx'] = IntLit(0)
            a = self.visit(ctx.e, o)

            if isinstance(a, IntLit):
                return FloatLit(0)

        if ctx.op in ['floor']:
            o[0]['ctx'] = FloatLit(0)
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
        for scope in o:
            if ctx.name in scope:
                if scope[ctx.name] == None:
                    scope[ctx.name] = scope['ctx']
                return scope[ctx.name]
        raise UndeclaredIdentifier(ctx.name)