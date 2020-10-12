# Generated from /home/khanh/Documents/schoolLife/201/PPL/testAss/BKIT.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("\23\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\2\2\4\2\4\2\2\2\20\2\6\3\2\2\2\4\f")
        buf.write("\3\2\2\2\6\7\7\6\2\2\7\b\7\20\2\2\b\t\7\3\2\2\t\n\7\17")
        buf.write("\2\2\n\13\7\2\2\3\13\3\3\2\2\2\f\r\7\6\2\2\r\16\7\20\2")
        buf.write("\2\16\17\7\5\2\2\17\20\7\17\2\2\20\21\7\2\2\3\21\5\3\2")
        buf.write("\2\2\2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Var'", "'Function:'", "<INVALID>", "'{'", "'}'", 
                     "'['", "']'", "'('", "')'", "';'", "':'", "','", "'='", 
                     "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "ID", "VAR_ID", "VAR_LIST", "VAR", "FUNCTION", 
                      "WS", "LB", "RB", "LK", "RK", "LP", "RP", "SEMI", 
                      "COLON", "CM", "EQ", "ADDOP", "SUBOP", "MULOP", "DIVOP", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_var_delare = 1

    ruleNames =  [ "program", "var_delare" ]

    EOF = Token.EOF
    ID=1
    VAR_ID=2
    VAR_LIST=3
    VAR=4
    FUNCTION=5
    WS=6
    LB=7
    RB=8
    LK=9
    RK=10
    LP=11
    RP=12
    SEMI=13
    COLON=14
    CM=15
    EQ=16
    ADDOP=17
    SUBOP=18
    MULOP=19
    DIVOP=20
    ERROR_CHAR=21
    UNCLOSE_STRING=22
    ILLEGAL_ESCAPE=23
    UNTERMINATED_COMMENT=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(BKITParser.VAR)
            self.state = 5
            self.match(BKITParser.COLON)
            self.state = 6
            self.match(BKITParser.ID)
            self.state = 7
            self.match(BKITParser.SEMI)
            self.state = 8
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_delareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def VAR_LIST(self):
            return self.getToken(BKITParser.VAR_LIST, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_delare




    def var_delare(self):

        localctx = BKITParser.Var_delareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_delare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(BKITParser.VAR)
            self.state = 11
            self.match(BKITParser.COLON)

            self.state = 12
            self.match(BKITParser.VAR_LIST)
            self.state = 13
            self.match(BKITParser.SEMI)
            self.state = 14
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





