# class ASTGeneration(MPVisitor):
    
#     def visitProgram(self,ctx:MPParser.ProgramContext):
#         return self.visitExp(ctx.exp())

#     def visitExp(self,ctx:MPParser.ExpContext):
#         if ctx.ASSIGN():
#             return reduce(lambda rh,lh: Binary(ctx.ASSIGN(0).getText(), lh, rh), list(map(lambda term: self.visitTerm(term), ctx.term()))[::-1])
#         return self.visitTerm(ctx.term(0))

#     def visitTerm(self,ctx:MPParser.TermContext):
#         if ctx.COMPARE():
#             return Binary(ctx.COMPARE().getText(), self.visitFactor(ctx.factor(0)), self.visitFactor(ctx.factor(1)))
#         else:
#             return self.visitFactor(ctx.factor(0))

#     def visitFactor(self,ctx:MPParser.FactorContext):
#         if ANDOR():
#             return reduce(lambda rh,lh: Binary(ctx.ANDOR(0).getText(), rh, lh), list(map(lambda op: self.visitOperand(op), ctx.operand())))
#         return self.visitOperand(ctx.operand(0))

#     def visitOperand(self,ctx:MPParser.OperandContext):
#         if ctx.INTLIT():
#             return IntLiteral(int(ctx.INTLIT().getText()))

#         if ctx.BOOLIT():
#             return BooleanLiteral(bool(ctx.BOOLIT().getText()))
        
#         if ctx.ID():
#             return Id(ctx.ID().getText())
        
#         return self.visitExp(ctx.exp())

from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce
class ASTGeneration(BKITVisitor):
    
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return self.visitExp(ctx.exp())

    def visitExp(self,ctx:BKITParser.ExpContext):
        if ctx.ASSIGN():
            return reduce(lambda rh,lh: Binary(ctx.ASSIGN(0).getText(), lh, rh), list(map(lambda term: self.visitTerm(term), ctx.term()))[::-1])
        return self.visitTerm(ctx.term(0))

    def visitTerm(self,ctx:BKITParser.TermContext): 
        if ctx.COMPARE():
            return Binary(ctx.COMPARE().getText(), self.visitFactor(ctx.factor(0)), self.visitFactor(ctx.factor(1)))
        return self.visitFactor(ctx.factor(0))

    def visitFactor(self,ctx:BKITParser.FactorContext):
        if ANDOR(0):
            return reduce(lambda lh,rh: Binary(ctx.ANDOR(0).getText(), lh, rh), list(map(lambda op: self.visitOperand(op), ctx.operand())))
        return self.visitOperand(ctx.operand(0))

    def visitOperand(self,ctx:BKITParser.OperandContext): 
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))

        if ctx.BOOLIT():
            return BooleanLiteral(bool(ctx.BOOLIT().getText()))
        
        if ctx.ID():
            return Id(ctx.ID().getText())
        
        return self.visitExp(ctx.exp())