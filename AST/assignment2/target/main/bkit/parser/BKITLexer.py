# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("I\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\3\2\3\3\3\3\3\4\6\4\31\n\4\r\4\16")
        buf.write("\4\32\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5&\n\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\5\6-\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\5\79\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\5\bC\n\b\3\t\6\tF\n\t\r\t\16\tG\2\2\n\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\3\2\5\3\2\62;\4\2>>@@\3\2c|\2T\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3\23\3\2\2")
        buf.write("\2\5\25\3\2\2\2\7\30\3\2\2\2\t%\3\2\2\2\13,\3\2\2\2\r")
        buf.write("8\3\2\2\2\17B\3\2\2\2\21E\3\2\2\2\23\24\7*\2\2\24\4\3")
        buf.write("\2\2\2\25\26\7+\2\2\26\6\3\2\2\2\27\31\t\2\2\2\30\27\3")
        buf.write("\2\2\2\31\32\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\b")
        buf.write("\3\2\2\2\34\35\7V\2\2\35\36\7t\2\2\36\37\7w\2\2\37&\7")
        buf.write("g\2\2 !\7H\2\2!\"\7c\2\2\"#\7n\2\2#$\7u\2\2$&\7g\2\2%")
        buf.write("\34\3\2\2\2% \3\2\2\2&\n\3\2\2\2\'(\7c\2\2()\7p\2\2)-")
        buf.write("\7f\2\2*+\7q\2\2+-\7t\2\2,\'\3\2\2\2,*\3\2\2\2-\f\3\2")
        buf.write("\2\2./\7-\2\2/9\7?\2\2\60\61\7/\2\2\619\7?\2\2\62\63\7")
        buf.write("(\2\2\639\7?\2\2\64\65\7~\2\2\659\7?\2\2\66\67\7<\2\2")
        buf.write("\679\7?\2\28.\3\2\2\28\60\3\2\2\28\62\3\2\2\28\64\3\2")
        buf.write("\2\28\66\3\2\2\29\16\3\2\2\2:C\7?\2\2;<\7>\2\2<C\7@\2")
        buf.write("\2=>\7@\2\2>C\7?\2\2?@\7>\2\2@C\7?\2\2AC\t\3\2\2B:\3\2")
        buf.write("\2\2B;\3\2\2\2B=\3\2\2\2B?\3\2\2\2BA\3\2\2\2C\20\3\2\2")
        buf.write("\2DF\t\4\2\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2H")
        buf.write("\22\3\2\2\2\t\2\32%,8BG\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    INTLIT = 3
    BOOLIT = 4
    ANDOR = 5
    ASSIGN = 6
    COMPARE = 7
    ID = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "BOOLIT", "ANDOR", "ASSIGN", "COMPARE", "ID" ]

    ruleNames = [ "T__0", "T__1", "INTLIT", "BOOLIT", "ANDOR", "ASSIGN", 
                  "COMPARE", "ID" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


