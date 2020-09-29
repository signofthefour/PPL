# Generated from LexicalAnalysis.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LexicalAnalysisParser import LexicalAnalysisParser
else:
    from LexicalAnalysisParser import LexicalAnalysisParser

# This class defines a complete generic visitor for a parse tree produced by LexicalAnalysisParser.

class LexicalAnalysisVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LexicalAnalysisParser#program.
    def visitProgram(self, ctx:LexicalAnalysisParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LexicalAnalysisParser#letter.
    def visitLetter(self, ctx:LexicalAnalysisParser.LetterContext):
        return self.visitChildren(ctx)



del LexicalAnalysisParser