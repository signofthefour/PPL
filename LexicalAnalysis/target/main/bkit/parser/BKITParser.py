# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("\25\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\4\6\4\21\n\4\r\4\16\4\22\3\4\2\2\5\2\4\6\2\3\3\2")
        buf.write("\4\5\2\22\2\b\3\2\2\2\4\13\3\2\2\2\6\20\3\2\2\2\b\t\7")
        buf.write("\13\2\2\t\n\7\2\2\3\n\3\3\2\2\2\13\f\7\13\2\2\f\r\7\6")
        buf.write("\2\2\r\16\7\b\2\2\16\5\3\2\2\2\17\21\t\2\2\2\20\17\3\2")
        buf.write("\2\2\21\22\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23\7\3")
        buf.write("\2\2\2\3\22")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "':'", "';'", "'.'", "','", "'Var'" ]

    symbolicNames = [ "<INVALID>", "STRING", "Real_number", "Integer_number", 
                      "Ids_list", "COLON", "SEMI", "DOT", "COMMA", "VAR", 
                      "ILLEGAL_ESCAPE", "WS", "UNCLOSE_STRING", "ERROR_CHAR", 
                      "BLOCK_COMMENT", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_var_declaration = 1
    RULE_number = 2

    ruleNames =  [ "program", "var_declaration", "number" ]

    EOF = Token.EOF
    STRING=1
    Real_number=2
    Integer_number=3
    Ids_list=4
    COLON=5
    SEMI=6
    DOT=7
    COMMA=8
    VAR=9
    ILLEGAL_ESCAPE=10
    WS=11
    UNCLOSE_STRING=12
    ERROR_CHAR=13
    BLOCK_COMMENT=14
    UNTERMINATED_COMMENT=15

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




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


    class Var_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def Ids_list(self):
            return self.getToken(BKITParser.Ids_list, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declaration" ):
                return visitor.visitVar_declaration(self)
            else:
                return visitor.visitChildren(self)




    def var_declaration(self):

        localctx = BKITParser.Var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.match(BKITParser.VAR)
            self.state = 10
            self.match(BKITParser.Ids_list)
            self.state = 11
            self.match(BKITParser.SEMI)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = BKITParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 13
                _la = self._input.LA(1)
                if not(_la==BKITParser.Real_number or _la==BKITParser.Integer_number):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 16 
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





