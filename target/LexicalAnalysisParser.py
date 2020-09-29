# Generated from LexicalAnalysis.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\4")
        buf.write("\13\4\2\t\2\4\3\t\3\3\2\3\2\3\3\3\3\3\3\2\2\4\2\4\2\2")
        buf.write("\2\b\2\6\3\2\2\2\4\b\3\2\2\2\6\7\3\2\2\2\7\3\3\2\2\2\b")
        buf.write("\t\7\3\2\2\t\5\3\2\2\2\2")
        return buf.getvalue()


class LexicalAnalysisParser ( Parser ):

    grammarFileName = "LexicalAnalysis.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "ID", "WS" ]

    RULE_program = 0
    RULE_letter = 1

    ruleNames =  [ "program", "letter" ]

    EOF = Token.EOF
    ID=1
    WS=2

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LexicalAnalysisParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = LexicalAnalysisParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LexicalAnalysisParser.ID, 0)

        def getRuleIndex(self):
            return LexicalAnalysisParser.RULE_letter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetter" ):
                return visitor.visitLetter(self)
            else:
                return visitor.visitChildren(self)




    def letter(self):

        localctx = LexicalAnalysisParser.LetterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_letter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(LexicalAnalysisParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





