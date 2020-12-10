# class ASTGeneration(MPVisitor):
    
#     def visitProgram(self,ctx:MPParser.ProgramContext):
#         return Program(list(map(lambda var_decl: self.visitVardecl(var_decl), ctx.var_decl())))

#     def visitVardecl(self,ctx:MPParser.VardeclContext): 
#         var_type = self.visitMptype(ctx.mptype())
#         return list(map(lambda x: VarDecl(x, var_type), self.visitIds(ctx.ids())))

#     def visitMptype(self,ctx:MPParser.MptypeContext):
#         if ctx.INTTYPE():
#             return IntType()
#         return FloatType()

#     def visitIds(self,ctx:MPParser.IdsContext):
#         return list(map(lambda x: Id(x.getText()), ctx.ID()))

from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):
    
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        from functools import reduce
        return Program(list(reduce(lambda prog, var_decl: prog + self.visitVardecl(var_decl), ctx.vardecl(), [])))

    def visitVardecl(self,ctx:BKITParser.VardeclContext): 
        var_type = self.visitMptype(ctx.mptype())
        return  list(map(lambda x: VarDecl(x, var_type), self.visitIds(ctx.ids())))

    def visitMptype(self,ctx:BKITParser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        return FloatType()

    def visitIds(self,ctx:BKITParser.IdsContext):
        return list(map(lambda x: Id(x.getText()), ctx.ID()))
    
