# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\7\2 \n\2\f\2\16\2#\13\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\5\7\5,\n\5\f\5\16\5/\13\5\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\b\5\b\67\n\b\3\t\3\t\6\t;\n\t\r\t\16\t<\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\f\3\f\6\fF\n\f\r\f\16\fG\3\f\3\f\6\fL")
        buf.write("\n\f\r\f\16\fM\3\f\5\fQ\n\f\3\f\5\fT\n\f\3\r\3\r\3\r\3")
        buf.write("\r\6\rZ\n\r\r\r\16\r[\3\r\3\r\3\16\6\16a\n\16\r\16\16")
        buf.write("\16b\3\16\3\16\2\2\17\3\3\5\2\7\2\t\4\13\2\r\2\17\2\21")
        buf.write("\2\23\2\25\2\27\5\31\6\33\7\3\2\t\3\2c|\4\2\62;c|\3\2")
        buf.write("\62;\5\2--//~~\3\2))\3\2\f\f\5\2\13\f\17\17\"\"\2i\2\3")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write("\2\2\2\3\35\3\2\2\2\5$\3\2\2\2\7&\3\2\2\2\t(\3\2\2\2\13")
        buf.write("\60\3\2\2\2\r\62\3\2\2\2\17\66\3\2\2\2\218\3\2\2\2\23")
        buf.write(">\3\2\2\2\25@\3\2\2\2\27C\3\2\2\2\31U\3\2\2\2\33`\3\2")
        buf.write("\2\2\35!\t\2\2\2\36 \t\3\2\2\37\36\3\2\2\2 #\3\2\2\2!")
        buf.write("\37\3\2\2\2!\"\3\2\2\2\"\4\3\2\2\2#!\3\2\2\2$%\t\2\2\2")
        buf.write("%\6\3\2\2\2&\'\t\4\2\2\'\b\3\2\2\2(-\5\5\3\2),\5\5\3\2")
        buf.write("*,\5\7\4\2+)\3\2\2\2+*\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3")
        buf.write("\2\2\2.\n\3\2\2\2/-\3\2\2\2\60\61\7\60\2\2\61\f\3\2\2")
        buf.write("\2\62\63\7g\2\2\63\64\5\17\b\2\64\16\3\2\2\2\65\67\t\5")
        buf.write("\2\2\66\65\3\2\2\2\66\67\3\2\2\2\67\20\3\2\2\28:\5\r\7")
        buf.write("\29;\5\7\4\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=")
        buf.write("\22\3\2\2\2>?\t\6\2\2?\24\3\2\2\2@A\5\23\n\2AB\5\23\n")
        buf.write("\2B\26\3\2\2\2CE\5\17\b\2DF\5\7\4\2ED\3\2\2\2FG\3\2\2")
        buf.write("\2GE\3\2\2\2GH\3\2\2\2HS\3\2\2\2IK\5\13\6\2JL\5\7\4\2")
        buf.write("KJ\3\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NP\3\2\2\2OQ\5")
        buf.write("\21\t\2PO\3\2\2\2PQ\3\2\2\2QT\3\2\2\2RT\5\21\t\2SI\3\2")
        buf.write("\2\2SR\3\2\2\2T\30\3\2\2\2UY\5\23\n\2VW\n\6\2\2WZ\n\7")
        buf.write("\2\2XZ\5\25\13\2YV\3\2\2\2YX\3\2\2\2Z[\3\2\2\2[Y\3\2\2")
        buf.write("\2[\\\3\2\2\2\\]\3\2\2\2]^\5\23\n\2^\32\3\2\2\2_a\t\b")
        buf.write("\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2cd\3\2\2\2")
        buf.write("de\b\16\2\2e\34\3\2\2\2\17\2!+-\66<GMPSY[b\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IDENTIFIER_Q1 = 1
    IDENTIFIER_Q2 = 2
    REAL = 3
    STRING = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER_Q1", "IDENTIFIER_Q2", "REAL", "STRING", "WS" ]

    ruleNames = [ "IDENTIFIER_Q1", "LETTER", "NUMBER", "IDENTIFIER_Q2", 
                  "DOT", "EXPO", "SIGN", "SCIEN", "SING_QUO", "DOU_QUO", 
                  "REAL", "STRING", "WS" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


