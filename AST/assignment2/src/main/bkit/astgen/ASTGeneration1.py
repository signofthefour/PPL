# class ASTGeneration(MPVisitor):
    
#     def visitProgram(self,ctx:MPParser.ProgramContext):
#         return self.visitVardecls(ctx.vardecls()) + 1 if ctx.vardecls() else 1

#     def visitVardecls(self,ctx:MPParser.VardeclsContext):
#         return self.visitVardecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail()) + 1

#     def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
#         if ctx.vardecl() and ctx.vardecltail():
#             return self.visitVardecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail()) + 1
#         return 1

#     def visitVardecl(self,ctx:MPParser.VardeclContext): 
#         return self.visitIds(ctx.ids()) + self.visitMptype(ctx.mptype()) + 1

#     def visitMptype(self,ctx:MPParser.MptypeContext):
#         return 1

#     def visitIds(self,ctx:MPParser.IdsContext):
#         return 1 + self.visitIds(ctx.ids()) if ctx.ids() else 1


from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return self.visitVardecls(ctx.vardecls()) + 1 if ctx.vardecls() else 1

    def visitVardecls(self,ctx:BKITParser.VardeclsContext):
        return self.visitVardecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail()) + 1

    def visitVardecltail(self,ctx:BKITParser.VardecltailContext): 
        if ctx.vardecl() and ctx.vardecltail():
            return self.visitVardecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail()) + 1
        return 1

    def visitVardecl(self,ctx:BKITParser.VardeclContext):
        return self.visitIds(ctx.ids()) + self.visitMptype(ctx.mptype()) + 1

    def visitMptype(self,ctx:BKITParser.MptypeContext):
        return 1

    def visitIds(self,ctx:BKITParser.IdsContext):
        return 1 + self.visitIds(ctx.ids()) if ctx.ids() else 1