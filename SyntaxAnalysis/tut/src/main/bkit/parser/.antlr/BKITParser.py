# Generated from /home/nguyendat/Documents/projects/PPL/SyntaxAnalysis/tut/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36")
        buf.write("\u00a8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\6\2)\n\2\r\2\16\2*\3\2\3\2\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\7\48\n\4\f\4\16\4;\13\4\5\4=\n\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\7\5F\n\5\f\5\16\5I\13\5\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\5\7Q\n\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\7\t\\\n\t\f\t\16\t_\13\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\13\7\13l\n\13\f\13\16")
        buf.write("\13o\13\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\5\rx\n\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\7\16\u0080\n\16\f\16\16\16\u0083")
        buf.write("\13\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\7")
        buf.write("\17\u008e\n\17\f\17\16\17\u0091\13\17\3\20\3\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\5\21\u009c\n\21\3\22\3\22")
        buf.write("\3\22\7\22\u00a1\n\22\f\22\16\22\u00a4\13\22\3\23\3\23")
        buf.write("\3\23\2\5\24\32\34\24\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$\2\3\3\2\7\b\2\u00a8\2(\3\2\2\2\4.\3\2\2\2\6")
        buf.write("\61\3\2\2\2\bG\3\2\2\2\nJ\3\2\2\2\fP\3\2\2\2\16T\3\2\2")
        buf.write("\2\20X\3\2\2\2\22b\3\2\2\2\24e\3\2\2\2\26p\3\2\2\2\30")
        buf.write("w\3\2\2\2\32y\3\2\2\2\34\u0084\3\2\2\2\36\u0092\3\2\2")
        buf.write("\2 \u009b\3\2\2\2\"\u009d\3\2\2\2$\u00a5\3\2\2\2&)\5\4")
        buf.write("\3\2\')\5\6\4\2(&\3\2\2\2(\'\3\2\2\2)*\3\2\2\2*(\3\2\2")
        buf.write("\2*+\3\2\2\2+,\3\2\2\2,-\7\2\2\3-\3\3\2\2\2./\5\n\6\2")
        buf.write("/\60\7\25\2\2\60\5\3\2\2\2\61\62\5$\23\2\62\63\7\30\2")
        buf.write("\2\63<\7\r\2\2\649\5\n\6\2\65\66\7\25\2\2\668\5\n\6\2")
        buf.write("\67\65\3\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:=\3\2\2")
        buf.write("\2;9\3\2\2\2<\64\3\2\2\2<=\3\2\2\2=>\3\2\2\2>?\7\16\2")
        buf.write("\2?@\7\21\2\2@A\5\b\5\2AB\7\22\2\2B\7\3\2\2\2CF\5\4\3")
        buf.write("\2DF\5\f\7\2EC\3\2\2\2ED\3\2\2\2FI\3\2\2\2GE\3\2\2\2G")
        buf.write("H\3\2\2\2H\t\3\2\2\2IG\3\2\2\2JK\5$\23\2KL\5\"\22\2L\13")
        buf.write("\3\2\2\2MQ\5\16\b\2NQ\5\20\t\2OQ\5\22\n\2PM\3\2\2\2PN")
        buf.write("\3\2\2\2PO\3\2\2\2QR\3\2\2\2RS\7\25\2\2S\r\3\2\2\2TU\7")
        buf.write("\30\2\2UV\7\27\2\2VW\5\26\f\2W\17\3\2\2\2XY\7\30\2\2Y")
        buf.write("]\7\r\2\2Z\\\5\24\13\2[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2")
        buf.write("]^\3\2\2\2^`\3\2\2\2_]\3\2\2\2`a\7\16\2\2a\21\3\2\2\2")
        buf.write("bc\7\6\2\2cd\5\26\f\2d\23\3\2\2\2ef\b\13\1\2fg\5\26\f")
        buf.write("\2gm\3\2\2\2hi\f\3\2\2ij\7\26\2\2jl\5\26\f\2kh\3\2\2\2")
        buf.write("lo\3\2\2\2mk\3\2\2\2mn\3\2\2\2n\25\3\2\2\2om\3\2\2\2p")
        buf.write("q\5\30\r\2q\27\3\2\2\2rs\5\32\16\2st\7\t\2\2tu\5\30\r")
        buf.write("\2ux\3\2\2\2vx\5\32\16\2wr\3\2\2\2wv\3\2\2\2x\31\3\2\2")
        buf.write("\2yz\b\16\1\2z{\5\34\17\2{\u0081\3\2\2\2|}\f\4\2\2}~\7")
        buf.write("\n\2\2~\u0080\5\32\16\5\177|\3\2\2\2\u0080\u0083\3\2\2")
        buf.write("\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\33\3\2")
        buf.write("\2\2\u0083\u0081\3\2\2\2\u0084\u0085\b\17\1\2\u0085\u0086")
        buf.write("\5 \21\2\u0086\u008f\3\2\2\2\u0087\u0088\f\5\2\2\u0088")
        buf.write("\u0089\7\f\2\2\u0089\u008e\5 \21\2\u008a\u008b\f\4\2\2")
        buf.write("\u008b\u008c\7\13\2\2\u008c\u008e\5 \21\2\u008d\u0087")
        buf.write("\3\2\2\2\u008d\u008a\3\2\2\2\u008e\u0091\3\2\2\2\u008f")
        buf.write("\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\35\3\2\2\2\u0091")
        buf.write("\u008f\3\2\2\2\u0092\u0093\7\r\2\2\u0093\u0094\5\26\f")
        buf.write("\2\u0094\u0095\7\16\2\2\u0095\37\3\2\2\2\u0096\u009c\7")
        buf.write("\3\2\2\u0097\u009c\7\4\2\2\u0098\u009c\7\30\2\2\u0099")
        buf.write("\u009c\5\20\t\2\u009a\u009c\5\36\20\2\u009b\u0096\3\2")
        buf.write("\2\2\u009b\u0097\3\2\2\2\u009b\u0098\3\2\2\2\u009b\u0099")
        buf.write("\3\2\2\2\u009b\u009a\3\2\2\2\u009c!\3\2\2\2\u009d\u00a2")
        buf.write("\7\30\2\2\u009e\u009f\7\26\2\2\u009f\u00a1\7\30\2\2\u00a0")
        buf.write("\u009e\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2")
        buf.write("\u00a2\u00a3\3\2\2\2\u00a3#\3\2\2\2\u00a4\u00a2\3\2\2")
        buf.write("\2\u00a5\u00a6\t\2\2\2\u00a6%\3\2\2\2\21(*9<EGP]mw\u0081")
        buf.write("\u008d\u008f\u009b\u00a2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "':'", "'.'", "';'", "','", "'='" ]

    symbolicNames = [ "<INVALID>", "Integer_literal", "Float_literal", "String_literal", 
                      "RETURN", "INT", "FLOAT", "PLUS_INT", "MINUS_INT", 
                      "STAR_INT", "DIV_INT", "LEFT_PAREN", "RIGHT_PAREN", 
                      "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", 
                      "COLON", "DOT", "SEMI", "COMMA", "ASSIGN", "ID", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "COMMENT", "UNTERMINATED_COMMENT", 
                      "ERROR_CHAR", "WS" ]

    RULE_program = 0
    RULE_var_declare = 1
    RULE_function_declare = 2
    RULE_function_body = 3
    RULE_ids_list_with_type = 4
    RULE_stmt = 5
    RULE_assign_stmt = 6
    RULE_call_stmt = 7
    RULE_ret_stmt = 8
    RULE_exprs_list = 9
    RULE_expr = 10
    RULE_expr0 = 11
    RULE_expr1 = 12
    RULE_expr2 = 13
    RULE_subexpr = 14
    RULE_operand = 15
    RULE_ids_list = 16
    RULE_primitive_type = 17

    ruleNames =  [ "program", "var_declare", "function_declare", "function_body", 
                   "ids_list_with_type", "stmt", "assign_stmt", "call_stmt", 
                   "ret_stmt", "exprs_list", "expr", "expr0", "expr1", "expr2", 
                   "subexpr", "operand", "ids_list", "primitive_type" ]

    EOF = Token.EOF
    Integer_literal=1
    Float_literal=2
    String_literal=3
    RETURN=4
    INT=5
    FLOAT=6
    PLUS_INT=7
    MINUS_INT=8
    STAR_INT=9
    DIV_INT=10
    LEFT_PAREN=11
    RIGHT_PAREN=12
    LEFT_BRACKET=13
    RIGHT_BRACKET=14
    LEFT_BRACE=15
    RIGHT_BRACE=16
    COLON=17
    DOT=18
    SEMI=19
    COMMA=20
    ASSIGN=21
    ID=22
    ILLEGAL_ESCAPE=23
    UNCLOSE_STRING=24
    COMMENT=25
    UNTERMINATED_COMMENT=26
    ERROR_CHAR=27
    WS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declareContext,i)


        def function_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Function_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Function_declareContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 36
                    self.var_declare()
                    pass

                elif la_ == 2:
                    self.state = 37
                    self.function_declare()
                    pass


                self.state = 40 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.INT or _la==BKITParser.FLOAT):
                    break

            self.state = 42
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ids_list_with_type(self):
            return self.getTypedRuleContext(BKITParser.Ids_list_with_typeContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_declare




    def var_declare(self):

        localctx = BKITParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.ids_list_with_type()
            self.state = 45
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(BKITParser.Primitive_typeContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def LEFT_BRACE(self):
            return self.getToken(BKITParser.LEFT_BRACE, 0)

        def function_body(self):
            return self.getTypedRuleContext(BKITParser.Function_bodyContext,0)


        def RIGHT_BRACE(self):
            return self.getToken(BKITParser.RIGHT_BRACE, 0)

        def ids_list_with_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Ids_list_with_typeContext)
            else:
                return self.getTypedRuleContext(BKITParser.Ids_list_with_typeContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.SEMI)
            else:
                return self.getToken(BKITParser.SEMI, i)

        def getRuleIndex(self):
            return BKITParser.RULE_function_declare




    def function_declare(self):

        localctx = BKITParser.Function_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.primitive_type()
            self.state = 48
            self.match(BKITParser.ID)
            self.state = 49
            self.match(BKITParser.LEFT_PAREN)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.INT or _la==BKITParser.FLOAT:
                self.state = 50
                self.ids_list_with_type()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.SEMI:
                    self.state = 51
                    self.match(BKITParser.SEMI)
                    self.state = 52
                    self.ids_list_with_type()
                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 60
            self.match(BKITParser.RIGHT_PAREN)
            self.state = 61
            self.match(BKITParser.LEFT_BRACE)
            self.state = 62
            self.function_body()
            self.state = 63
            self.match(BKITParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declareContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_function_body




    def function_body(self):

        localctx = BKITParser.Function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.RETURN) | (1 << BKITParser.INT) | (1 << BKITParser.FLOAT) | (1 << BKITParser.ID))) != 0):
                self.state = 67
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.INT, BKITParser.FLOAT]:
                    self.state = 65
                    self.var_declare()
                    pass
                elif token in [BKITParser.RETURN, BKITParser.ID]:
                    self.state = 66
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ids_list_with_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(BKITParser.Primitive_typeContext,0)


        def ids_list(self):
            return self.getTypedRuleContext(BKITParser.Ids_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_ids_list_with_type




    def ids_list_with_type(self):

        localctx = BKITParser.Ids_list_with_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ids_list_with_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.primitive_type()
            self.state = 73
            self.ids_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def ret_stmt(self):
            return self.getTypedRuleContext(BKITParser.Ret_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt




    def stmt(self):

        localctx = BKITParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 75
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.state = 76
                self.call_stmt()
                pass

            elif la_ == 3:
                self.state = 77
                self.ret_stmt()
                pass


            self.state = 80
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(BKITParser.ID)
            self.state = 83
            self.match(BKITParser.ASSIGN)
            self.state = 84
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def exprs_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exprs_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Exprs_listContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(BKITParser.ID)
            self.state = 87
            self.match(BKITParser.LEFT_PAREN)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.Integer_literal) | (1 << BKITParser.Float_literal) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.ID))) != 0):
                self.state = 88
                self.exprs_list(0)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
            self.match(BKITParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ret_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_ret_stmt




    def ret_stmt(self):

        localctx = BKITParser.Ret_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ret_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(BKITParser.RETURN)
            self.state = 97
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exprs_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def exprs_list(self):
            return self.getTypedRuleContext(BKITParser.Exprs_listContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exprs_list



    def exprs_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exprs_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_exprs_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exprs_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprs_list)
                    self.state = 102
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 103
                    self.match(BKITParser.COMMA)
                    self.state = 104
                    self.expr() 
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr0(self):
            return self.getTypedRuleContext(BKITParser.Expr0Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr




    def expr(self):

        localctx = BKITParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.expr0()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr0Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(BKITParser.Expr1Context,0)


        def PLUS_INT(self):
            return self.getToken(BKITParser.PLUS_INT, 0)

        def expr0(self):
            return self.getTypedRuleContext(BKITParser.Expr0Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr0




    def expr0(self):

        localctx = BKITParser.Expr0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr0)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.expr1(0)
                self.state = 113
                self.match(BKITParser.PLUS_INT)
                self.state = 114
                self.expr0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.expr1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(BKITParser.Expr2Context,0)


        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Expr1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Expr1Context,i)


        def MINUS_INT(self):
            return self.getToken(BKITParser.MINUS_INT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr1



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 122
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 123
                    self.match(BKITParser.MINUS_INT)
                    self.state = 124
                    self.expr1(3) 
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(BKITParser.OperandContext,0)


        def expr2(self):
            return self.getTypedRuleContext(BKITParser.Expr2Context,0)


        def DIV_INT(self):
            return self.getToken(BKITParser.DIV_INT, 0)

        def STAR_INT(self):
            return self.getToken(BKITParser.STAR_INT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 139
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Expr2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                        self.state = 133
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 134
                        self.match(BKITParser.DIV_INT)
                        self.state = 135
                        self.operand()
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Expr2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                        self.state = 136
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 137
                        self.match(BKITParser.STAR_INT)
                        self.state = 138
                        self.operand()
                        pass

             
                self.state = 143
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SubexprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_subexpr




    def subexpr(self):

        localctx = BKITParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(BKITParser.LEFT_PAREN)
            self.state = 145
            self.expr()
            self.state = 146
            self.match(BKITParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer_literal(self):
            return self.getToken(BKITParser.Integer_literal, 0)

        def Float_literal(self):
            return self.getToken(BKITParser.Float_literal, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def subexpr(self):
            return self.getTypedRuleContext(BKITParser.SubexprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_operand)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.match(BKITParser.Integer_literal)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(BKITParser.Float_literal)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.match(BKITParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 151
                self.call_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 152
                self.subexpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ids_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ID)
            else:
                return self.getToken(BKITParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_ids_list




    def ids_list(self):

        localctx = BKITParser.Ids_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ids_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(BKITParser.ID)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 156
                self.match(BKITParser.COMMA)
                self.state = 157
                self.match(BKITParser.ID)
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKITParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_primitive_type




    def primitive_type(self):

        localctx = BKITParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            _la = self._input.LA(1)
            if not(_la==BKITParser.INT or _la==BKITParser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.exprs_list_sempred
        self._predicates[12] = self.expr1_sempred
        self._predicates[13] = self.expr2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exprs_list_sempred(self, localctx:Exprs_listContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




