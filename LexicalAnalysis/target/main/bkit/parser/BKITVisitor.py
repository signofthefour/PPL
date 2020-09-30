# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_declaration.
    def visitVar_declaration(self, ctx:BKITParser.Var_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#number.
    def visitNumber(self, ctx:BKITParser.NumberContext):
        return self.visitChildren(ctx)



del BKITParser