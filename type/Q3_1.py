from functools import reduce

class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o:object):
        o = {}
        env = reduce(lambda x, y: dict(y.accept(self, x).items() | x.items()), ctx.decl, o)
        stmts = reduce(lambda x, y: y.accept(self, x), ctx.stmts, env)

    def visitVarDecl(self,ctx:VarDecl,o:object):
        return {ctx.name: None}
        
    def visitAssign(self,ctx:Assign,o):
        rhs_type = ctx.rhs.accept(self, o)
        lhs_type = ctx.lhs.accept(self, o)
        
        if None == rhs_type:
            raise TypeCannotBeInferred(ctx)
            
        if None != rhs_type and None == lhs_type:
            o[ctx.lhs.name] = rhs_type
            lhs_type = rhs_type
            
        if rhs_type != lhs_type:
            raise TypeMismatchInStatement(ctx)
            
        return o
    
    def visitId(self, ctx, o):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
        return o[ctx.name]
            
    def visitBinOp(self,ctx:BinOp,o):
        type1 = ctx.e1.accept(self, o)
        type2 = ctx.e2.accept(self, o)
        join_type = set([type1, type2])
            
        if (ctx.op == '+' or ctx.op == '-' or ctx.op == '*' or ctx.op == '/'):
            if 'float' in join_type or 'bool' in join_type:
                raise TypeMismatchInExpression(ctx)
            if type1 == None:
                o.update({ctx.e1.name: 'int'})
                return ctx.accept(self, o)
            if type2 == None:
                o.update({ctx.e2.name: 'int'})
                return ctx.accept(self, o)
            return 'int'
            
        elif (ctx.op == '+.' or ctx.op == '-.' or ctx.op == '*.' or ctx.op == '/.'):
            if 'int' in join_type or 'bool' in join_type:
                raise TypeMismatchInExpression(ctx)
            if type1 == None:
                o.update({ctx.e1.name: 'float'})
                return ctx.accept(self, o)
            if type2 == None:
                o.update({ctx.e2.name: 'float'})
                return ctx.accept(self, o)
            return 'float'
        
        elif (ctx.op == '>' or ctx.op == '='):
            if 'float' in join_type or 'bool' in join_type:
                raise TypeMismatchInExpression(ctx)
            if type1 == None:
                o.update({ctx.e1.name: 'int'})
                return ctx.accept(self, o)
            if type2 == None:
                o.update({ctx.e2.name: 'int'})
                return ctx.accept(self, o)
            return 'bool'
            
        elif (ctx.op == '>.' or ctx.op == '=.'):
            if 'bool' in join_type or 'int' in join_type:
                raise TypeMismatchInExpression(ctx)
            if type1 == None:
                o.update({ctx.e1.name: 'float'})
                return ctx.accept(self, o)
            if type2 == None:
                o.update({ctx.e2.name: 'float'})
                return ctx.accept(self, o)
            return 'bool'
            
        elif (ctx.op == '&&' or ctx.op == '||' or ctx.op == '>b' or ctx.op == '=b'):
            if 'float' in join_type or 'int' in join_type:
                raise TypeMismatchInExpression(ctx)
            if type1 == None:
                o.update({ctx.e1.name: 'bool'})
                return ctx.accept(self, o)
            if type2 == None:
                o.update({ctx.e2.name: 'bool'})
                return ctx.accept(self, o)
            return 'bool'

    def visitUnOp(self,ctx:UnOp,o):
        join_type = ctx.e.accept(self, o)
    
        if (ctx.op == '!'):
            if 'float' == join_type or 'int' == join_type:
                raise TypeMismatchInExpression(ctx)
            if join_type == None:
                o.update({ctx.e.name: 'bool'})
                return ctx.accept(self, o)
            return 'bool'
            
        elif (ctx.op == '-'):
            if 'float' == join_type or 'bool' == join_type:
                raise TypeMismatchInExpression(ctx)
            if join_type == None:
                o.update({ctx.e.name: 'int'})
                return ctx.accept(self, o)
            return 'int'
            
        elif (ctx.op == '-.'):
            if 'int' == join_type or 'bool' == join_type:
                raise TypeMismatchInExpression(ctx)
            if join_type == None:
                o.update({ctx.e.name: 'float'})
                return ctx.accept(self, o)
            return 'float'
            
        elif (ctx.op == 'i2f'):
            if 'float' == join_type or 'bool' == join_type:
                raise TypeMismatchInExpression(ctx)
            if join_type == None:
                o.update({ctx.e.name: 'int'})
                return ctx.accept(self, o)
            return 'float'
        
        elif (ctx.op == 'floor'):
            if 'int' == join_type or 'bool' == join_type:
                raise TypeMismatchInExpression(ctx)
            if join_type == None:
                o.update({ctx.e.name: 'float'})
                return ctx.accept(self, o)
            return 'int'

    def visitIntLit(self,ctx:IntLit,o):
        return 'int'

    def visitFloatLit(self,ctx,o):
        return 'float'

    def visitBoolLit(self,ctx,o):
        return 'bool'
        