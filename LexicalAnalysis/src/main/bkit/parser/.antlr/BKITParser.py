# Generated from /home/nguyendat/Documents/projects/PPL/LexicalAnalysis/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("\35\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\3\6\3\r\n\3")
        buf.write("\r\3\16\3\16\3\4\6\4\22\n\4\r\4\16\4\23\3\4\6\4\27\n\4")
        buf.write("\r\4\16\4\30\3\4\3\4\3\4\2\2\5\2\4\6\2\3\3\2\5\6\2\34")
        buf.write("\2\b\3\2\2\2\4\f\3\2\2\2\6\21\3\2\2\2\b\t\7\4\2\2\t\n")
        buf.write("\7\2\2\3\n\3\3\2\2\2\13\r\t\2\2\2\f\13\3\2\2\2\r\16\3")
        buf.write("\2\2\2\16\f\3\2\2\2\16\17\3\2\2\2\17\5\3\2\2\2\20\22\7")
        buf.write("\3\2\2\21\20\3\2\2\2\22\23\3\2\2\2\23\21\3\2\2\2\23\24")
        buf.write("\3\2\2\2\24\26\3\2\2\2\25\27\7\7\2\2\26\25\3\2\2\2\27")
        buf.write("\30\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\32\3\2\2\2")
        buf.write("\32\33\7\3\2\2\33\7\3\2\2\2\5\16\23\30")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "VAR", "Real_number", "Integer_number", 
                      "String", "HEXADECIMAL", "DECIMAL", "OCTAL", "LETTER", 
                      "ID", "ILLEGAL_ESCAPE", "WS", "UNCLOSE_STRING", "ERROR_CHAR", 
                      "BLOCK_COMMENT", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_number = 1
    RULE_string = 2

    ruleNames =  [ "program", "number", "string" ]

    EOF = Token.EOF
    T__0=1
    VAR=2
    Real_number=3
    Integer_number=4
    String=5
    HEXADECIMAL=6
    DECIMAL=7
    OCTAL=8
    LETTER=9
    ID=10
    ILLEGAL_ESCAPE=11
    WS=12
    UNCLOSE_STRING=13
    ERROR_CHAR=14
    BLOCK_COMMENT=15
    UNTERMINATED_COMMENT=16

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

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(BKITParser.VAR)
            self.state = 7
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Real_number(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Real_number)
            else:
                return self.getToken(BKITParser.Real_number, i)

        def Integer_number(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Integer_number)
            else:
                return self.getToken(BKITParser.Integer_number, i)

        def getRuleIndex(self):
            return BKITParser.RULE_number




    def number(self):

        localctx = BKITParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 9
                _la = self._input.LA(1)
                if not(_la==BKITParser.Real_number or _la==BKITParser.Integer_number):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 12 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.Real_number or _la==BKITParser.Integer_number):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def String(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.String)
            else:
                return self.getToken(BKITParser.String, i)

        def getRuleIndex(self):
            return BKITParser.RULE_string




    def string(self):

        localctx = BKITParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.match(BKITParser.T__0)
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.T__0):
                    break

            self.state = 20 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 19
                self.match(BKITParser.String)
                self.state = 22 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.String):
                    break

            self.state = 24
            self.match(BKITParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





