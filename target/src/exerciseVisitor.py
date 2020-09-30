# Generated from src/exercise.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .exerciseParser import exerciseParser
else:
    from exerciseParser import exerciseParser

# This class defines a complete generic visitor for a parse tree produced by exerciseParser.

class exerciseVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by exerciseParser#program.
    def visitProgram(self, ctx:exerciseParser.ProgramContext):
        return self.visitChildren(ctx)



del exerciseParser