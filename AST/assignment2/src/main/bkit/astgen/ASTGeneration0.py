# class ASTGeneration(MPVisitor):
    
#     def visitProgram(self,ctx:MPParser.ProgramContext):
#         if ctx.vardecls():
#             return self.visitVardecls(ctx.vardecls()) + 1 if ctx.vardecls() else 1

#     def visitVardecls(self,ctx:MPParser.VardeclsContext):
#         if ctx.vardecl():
#             return self.visitVardecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail())
#         else:
#             return 0

#     def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
#         if ctx.vardecl():
#             return self.visitVarDecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail()) 
#         else:
#             return 0

#     def visitVardecl(self,ctx:MPParser.VardeclContext): 
#         res = self.visitMptype(ctx.mptype()) + self.visitIds(ctx.ids())
#         if res:
#             return res + 1
#         else:
#             return res

#     def visitMptype(self,ctx:MPParser.MptypeContext):
#         if ctx.INTTYPE() or ctx.FLOATTYPE():
#             return 1
#         else:
#             return 0

#     def visitIds(self,ctx:MPParser.IdsContext):
#         if ctx.ids():
#             return 1 + 1 + self.visitIds(ctx.ids())
#         else:
#             if ctx.ID():
#                 return 1
#             else:
#                 return 0


from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        if ctx.vardecls():
            return self.visitVardecls(ctx.vardecls()) + 1 if ctx.vardecls() else 1
        else:
            return 1

    def visitVardecls(self,ctx:BKITParser.VardeclsContext):
        if ctx.vardecl():
            return self.visitVardecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail())
        else:
            return 0

    def visitVardecltail(self,ctx:BKITParser.VardecltailContext): 
        return self.

    def visitVardecl(self,ctx:BKITParser.VardeclContext):
        return self.visitIds() + self.visitMptype()

    def visitMptype(self,ctx:BKITParser.MptypeContext):
        return 1

    def visitIds(self,ctx:BKITParser.IdsContext):
        if ctx.ids():
            return 1 + self.visitIds(ctx.Ids())
        else:
            return 0