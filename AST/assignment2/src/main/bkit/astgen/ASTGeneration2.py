# class ASTGeneration(MPVisitor):
    
#     def visitProgram(self,ctx:MPParser.ProgramContext):
#         return Program(self.visitVardecls(ctx.vardecls())) if ctx.vardecls() else None

#     def visitVardecls(self,ctx:MPParser.VardeclsContext):
#         return self.visitVardecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail())

#     def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
#         if ctx.vardecl() and ctx.vardecltail():
#             return self.visitVardecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail())
#         return []

#     def visitVardecl(self,ctx:MPParser.VardeclContext): 
#         var_type = self.visitMptype(ctx.mptype())
#         return list(map(lambda x: VarDecl(x, var_type), self.visitIds(ctx.ids())))

#     def visitMptype(self,ctx:MPParser.MptypeContext):
#         if ctx.INTTYPE():
#             return IntType()
#         else:
#             return FloatType()

#     def visitIds(self,ctx:MPParser.IdsContext):
#         if ctx.ids():
#                 return self.visitIds(ctx.ids()) + [Id(ctx.ID().getText())]
#         else:
#             if ctx.ID():
#                 return [Id(ctx.ID().getText())]
#             else:
#                 return []


from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return Program(self.visitVardecls(ctx.vardecls())) if ctx.vardecls() else None

    def visitVardecls(self,ctx:BKITParser.VardeclsContext):
        return self.visitVardecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail())

    def visitVardecltail(self,ctx:BKITParser.VardecltailContext): 
        if ctx.vardecl() and ctx.vardecltail():
            return self.visitVardecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail())
        return []

    def visitVardecl(self,ctx:BKITParser.VardeclContext):
        if ctx.ids(): 
            var_type = self.visitMptype(ctx.mptype())
            return list(map(lambda x: VarDecl(x, var_type), self.visitIds(ctx.ids())))[::-1]
        else:
            return []

    def visitMptype(self,ctx:BKITParser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        else:
            return FloatType() 

    def visitIds(self,ctx:BKITParser.IdsContext):
        if ctx.ids():
            return self.visitIds(ctx.ids()) + [Id(ctx.ID().getText())]
        else:
            if ctx.ID():
                return [Id(ctx.ID().getText())]
            else:
                return []