# Generated from LexicalAnalysis.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


	from lexererr import *;



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\4")
        buf.write("\31\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\3")
        buf.write("\3\3\4\6\4\21\n\4\r\4\16\4\22\3\5\6\5\26\n\5\r\5\16\5")
        buf.write("\27\2\2\6\3\2\5\2\7\3\t\4\3\2\5\3\2c|\3\2\62;\5\2\13\f")
        buf.write("\17\17\"\"\2\30\2\7\3\2\2\2\2\t\3\2\2\2\3\13\3\2\2\2\5")
        buf.write("\r\3\2\2\2\7\20\3\2\2\2\t\25\3\2\2\2\13\f\t\2\2\2\f\4")
        buf.write("\3\2\2\2\r\16\t\3\2\2\16\6\3\2\2\2\17\21\5\3\2\2\20\17")
        buf.write("\3\2\2\2\21\22\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23")
        buf.write("\b\3\2\2\2\24\26\t\4\2\2\25\24\3\2\2\2\26\27\3\2\2\2\27")
        buf.write("\25\3\2\2\2\27\30\3\2\2\2\30\n\3\2\2\2\5\2\22\27\2")
        return buf.getvalue()


class LexicalAnalysisLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    WS = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "ID", "WS" ]

    ruleNames = [ "LETTER", "NUMBER", "ID", "WS" ]

    grammarFileName = "LexicalAnalysis.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


