# class ASTGeneration(MPVisitor):
    
#     def visitProgram(self,ctx:MPParser.ProgramContext):
#         return self.visitExp(ctx.exp())

#     def visitExp(self,ctx:MPParser.ExpContext):
#         if ctx.ASSIGN():
#             return Binary(ctx.ASSIGN().getText(), self.visitTerm(ctx.term()), self.visitExp(ctx.exp()))
#         else:
#             return self.visitTerm(ctx.term())

#     def visitTerm(self,ctx:MPParser.TermContext):
#         if ctx.COMPARE():
#             return Binary(ctx.COMPARE().getText(), self.visitFactor(ctx.factor(0)), self.visitFactor(ctx.factor(1)))
#         else:
#             return self.visitFactor(ctx.factor(0))

#     def visitFactor(self,ctx:MPParser.FactorContext):
#         if ctx.ANDOR():
#             return Binary(ctx.ANDOR().getText(), self.visitFactor(ctx.factor()), self.visitOperand(ctx.operand()))
#         else:
#             return self.visitOperand(ctx.operand())

#     def visitOperand(self,ctx:MPParser.OperandContext):
#         if ctx.INTLIT():
#             return IntLiteral(int(ctx.INTLIT().getText()))

#         if ctx.BOOLIT():
#             return BoolLiteral(bool(ctx.BOOLIT().getText()))
        
#         if ctx.ID():
#             return Id(ctx.ID().getText())
        
#         return self.visitExp(ctx.exp())

from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return self.visitExp(ctx.exp())

    def visitExp(self,ctx:BKITParser.ExpContext):
        if ctx.ASSIGN():
            return Binary(ctx.ASSIGN().getText(), self.visitTerm(ctx.term()), self.visitExp(ctx.exp()))
        else:
            return self.visitTerm(ctx.term())

    def visitTerm(self,ctx:BKITParser.TermContext): 
        if ctx.COMPARE():
            return Binary(ctx.COMPARE().getText(), self.visitFactor(ctx.factor(0)), self.visitFactor(ctx.factor(1)))
        else:
            return self.visitFactor(ctx.factor(0))

    def visitFactor(self,ctx:BKITParser.FactorContext):
        if ctx.ANDOR():
            return Binary(ctx.ANDOR().getText(), self.visitFactor(ctx.factor()), self.visitOperand(ctx.operand()))
        else:
            return self.visitOperand(ctx.operand())

    def visitOperand(self,ctx:BKITParser.OperandContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))

        if ctx.BOOLIT():
            return BoolLiteral(bool(ctx.BOOLIT().getText()))
        
        if ctx.ID():
            return Id(ctx.ID().getText())
        
        return self.visitExp(ctx.exp())