# Generated from /home/nguyendat/Documents/projects/PPL/SyntaxAnalysis/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("A\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\6\2\35\n\2\r\2\16\2\36\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b")
        buf.write("\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\2\2")
        buf.write("\16\2\4\6\b\n\f\16\20\22\24\26\30\2\6\3\2\13\16\3\2-/")
        buf.write("\b\2$$&&((**,,\60\65\7\2%%\'\'))++\66:\2\66\2\34\3\2\2")
        buf.write("\2\4\"\3\2\2\2\6%\3\2\2\2\b.\3\2\2\2\n\60\3\2\2\2\f\62")
        buf.write("\3\2\2\2\16\64\3\2\2\2\20\66\3\2\2\2\228\3\2\2\2\24:\3")
        buf.write("\2\2\2\26<\3\2\2\2\30>\3\2\2\2\32\35\5\4\3\2\33\35\5\6")
        buf.write("\4\2\34\32\3\2\2\2\34\33\3\2\2\2\35\36\3\2\2\2\36\34\3")
        buf.write("\2\2\2\36\37\3\2\2\2\37 \3\2\2\2 !\7\2\2\3!\3\3\2\2\2")
        buf.write("\"#\7\37\2\2#$\7C\2\2$\5\3\2\2\2%&\7\32\2\2&\'\7A\2\2")
        buf.write("\'(\7\4\2\2()\7\34\2\2)*\7\17\2\2*+\7A\2\2+,\7\26\2\2")
        buf.write(",-\7B\2\2-\7\3\2\2\2./\t\2\2\2/\t\3\2\2\2\60\61\5\f\7")
        buf.write("\2\61\13\3\2\2\2\62\63\3\2\2\2\63\r\3\2\2\2\64\65\t\3")
        buf.write("\2\2\65\17\3\2\2\2\66\67\t\4\2\2\67\21\3\2\2\289\t\5\2")
        buf.write("\29\23\3\2\2\2:;\3\2\2\2;\25\3\2\2\2<=\3\2\2\2=\27\3\2")
        buf.write("\2\2>?\3\2\2\2?\31\3\2\2\2\4\34\36")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'Body'", "'Break'", "'Continue'", "'Do'", 
                     "'Else'", "'ElSelf'", "'ElseIf'", "'EndIf'", "'EndFor'", 
                     "'EndWhile'", "'For'", "'Function'", "'If'", "'Parameter'", 
                     "'Return'", "'Then'", "'Var'", "'While'", "'True'", 
                     "'False'", "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", 
                     "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", 
                     "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'=\\='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "':'", "'.'", "';'", 
                     "','", "'='" ]

    symbolicNames = [ "<INVALID>", "INT_ARRAY", "ID", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "COMMENT", "UNTERMINATED_COMMENT", 
                      "ERROR_CHAR", "WS", "Integer_literal", "Float_literal", 
                      "Boolean_literal", "String_literal", "BODY", "BREAK", 
                      "CONTINUE", "DO", "ELSE", "ELSELF", "ELSEIF", "ENDBODY", 
                      "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                      "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", 
                      "ENDDO", "PLUS_INT", "PLUS_FLOAT", "MINUS_INT", "MINUS_FLOAT", 
                      "STAR_INT", "STAR_FLOAT", "DIV_INT", "DIV_FLOAT", 
                      "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL_INT", 
                      "LESS_INT", "GREATER_INT", "LESS_OR_EQUAL_INT", "GREATER_OR_EQUAL_INT", 
                      "NOT_EQUAL_FLOAT", "LESS_FLOAT", "GREATER_FLOAT", 
                      "LESS_OR_EQUAL_FLOAT", "GREATER_OR_EQUAL_FLOAT", "LEFT_PAREN", 
                      "RIGHT_PARENT", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", 
                      "RIGHT_BRACE", "COLON", "DOT", "SEMI", "COMMA", "ASSIGN" ]

    RULE_program = 0
    RULE_var_declare = 1
    RULE_function_declare = 2
    RULE_primitive_type = 3
    RULE_composite_type = 4
    RULE_array = 5
    RULE_bool_op = 6
    RULE_int_op = 7
    RULE_float_op = 8
    RULE_if_stmt = 9
    RULE_while_stmt = 10
    RULE_dowhile_stmt = 11

    ruleNames =  [ "program", "var_declare", "function_declare", "primitive_type", 
                   "composite_type", "array", "bool_op", "int_op", "float_op", 
                   "if_stmt", "while_stmt", "dowhile_stmt" ]

    EOF = Token.EOF
    INT_ARRAY=1
    ID=2
    ILLEGAL_ESCAPE=3
    UNCLOSE_STRING=4
    COMMENT=5
    UNTERMINATED_COMMENT=6
    ERROR_CHAR=7
    WS=8
    Integer_literal=9
    Float_literal=10
    Boolean_literal=11
    String_literal=12
    BODY=13
    BREAK=14
    CONTINUE=15
    DO=16
    ELSE=17
    ELSELF=18
    ELSEIF=19
    ENDBODY=20
    ENDFOR=21
    ENDWHILE=22
    FOR=23
    FUNCTION=24
    IF=25
    PARAMETER=26
    RETURN=27
    THEN=28
    VAR=29
    WHILE=30
    TRUE=31
    FALSE=32
    ENDDO=33
    PLUS_INT=34
    PLUS_FLOAT=35
    MINUS_INT=36
    MINUS_FLOAT=37
    STAR_INT=38
    STAR_FLOAT=39
    DIV_INT=40
    DIV_FLOAT=41
    MOD=42
    NOT=43
    AND=44
    OR=45
    EQUAL=46
    NOT_EQUAL_INT=47
    LESS_INT=48
    GREATER_INT=49
    LESS_OR_EQUAL_INT=50
    GREATER_OR_EQUAL_INT=51
    NOT_EQUAL_FLOAT=52
    LESS_FLOAT=53
    GREATER_FLOAT=54
    LESS_OR_EQUAL_FLOAT=55
    GREATER_OR_EQUAL_FLOAT=56
    LEFT_PAREN=57
    RIGHT_PARENT=58
    LEFT_BRACKET=59
    RIGHT_BRACKET=60
    LEFT_BRACE=61
    RIGHT_BRACE=62
    COLON=63
    DOT=64
    SEMI=65
    COMMA=66
    ASSIGN=67

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
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.VAR]:
                    self.state = 24
                    self.var_declare()
                    pass
                elif token in [BKITParser.FUNCTION]:
                    self.state = 25
                    self.function_declare()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.FUNCTION or _la==BKITParser.VAR):
                    break

            self.state = 30
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

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_declare




    def var_declare(self):

        localctx = BKITParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(BKITParser.VAR)
            self.state = 33
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

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COLON)
            else:
                return self.getToken(BKITParser.COLON, i)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_function_declare




    def function_declare(self):

        localctx = BKITParser.Function_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(BKITParser.FUNCTION)
            self.state = 36
            self.match(BKITParser.COLON)
            self.state = 37
            self.match(BKITParser.ID)
            self.state = 38
            self.match(BKITParser.PARAMETER)
            self.state = 39
            self.match(BKITParser.BODY)
            self.state = 40
            self.match(BKITParser.COLON)
            self.state = 41
            self.match(BKITParser.ENDBODY)
            self.state = 42
            self.match(BKITParser.DOT)
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

        def Integer_literal(self):
            return self.getToken(BKITParser.Integer_literal, 0)

        def Float_literal(self):
            return self.getToken(BKITParser.Float_literal, 0)

        def String_literal(self):
            return self.getToken(BKITParser.String_literal, 0)

        def Boolean_literal(self):
            return self.getToken(BKITParser.Boolean_literal, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_primitive_type




    def primitive_type(self):

        localctx = BKITParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.Integer_literal) | (1 << BKITParser.Float_literal) | (1 << BKITParser.Boolean_literal) | (1 << BKITParser.String_literal))) != 0)):
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


    class Composite_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self):
            return self.getTypedRuleContext(BKITParser.ArrayContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_composite_type




    def composite_type(self):

        localctx = BKITParser.Composite_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_composite_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.array()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_array




    def array(self):

        localctx = BKITParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_bool_op




    def bool_op(self):

        localctx = BKITParser.Bool_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bool_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.NOT) | (1 << BKITParser.AND) | (1 << BKITParser.OR))) != 0)):
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


    class Int_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS_INT(self):
            return self.getToken(BKITParser.PLUS_INT, 0)

        def MINUS_INT(self):
            return self.getToken(BKITParser.MINUS_INT, 0)

        def STAR_INT(self):
            return self.getToken(BKITParser.STAR_INT, 0)

        def DIV_INT(self):
            return self.getToken(BKITParser.DIV_INT, 0)

        def MOD(self):
            return self.getToken(BKITParser.MOD, 0)

        def EQUAL(self):
            return self.getToken(BKITParser.EQUAL, 0)

        def NOT_EQUAL_INT(self):
            return self.getToken(BKITParser.NOT_EQUAL_INT, 0)

        def LESS_INT(self):
            return self.getToken(BKITParser.LESS_INT, 0)

        def GREATER_INT(self):
            return self.getToken(BKITParser.GREATER_INT, 0)

        def LESS_OR_EQUAL_INT(self):
            return self.getToken(BKITParser.LESS_OR_EQUAL_INT, 0)

        def GREATER_OR_EQUAL_INT(self):
            return self.getToken(BKITParser.GREATER_OR_EQUAL_INT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_int_op




    def int_op(self):

        localctx = BKITParser.Int_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_int_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.PLUS_INT) | (1 << BKITParser.MINUS_INT) | (1 << BKITParser.STAR_INT) | (1 << BKITParser.DIV_INT) | (1 << BKITParser.MOD) | (1 << BKITParser.EQUAL) | (1 << BKITParser.NOT_EQUAL_INT) | (1 << BKITParser.LESS_INT) | (1 << BKITParser.GREATER_INT) | (1 << BKITParser.LESS_OR_EQUAL_INT) | (1 << BKITParser.GREATER_OR_EQUAL_INT))) != 0)):
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


    class Float_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS_FLOAT(self):
            return self.getToken(BKITParser.PLUS_FLOAT, 0)

        def MINUS_FLOAT(self):
            return self.getToken(BKITParser.MINUS_FLOAT, 0)

        def STAR_FLOAT(self):
            return self.getToken(BKITParser.STAR_FLOAT, 0)

        def DIV_FLOAT(self):
            return self.getToken(BKITParser.DIV_FLOAT, 0)

        def NOT_EQUAL_FLOAT(self):
            return self.getToken(BKITParser.NOT_EQUAL_FLOAT, 0)

        def LESS_FLOAT(self):
            return self.getToken(BKITParser.LESS_FLOAT, 0)

        def GREATER_FLOAT(self):
            return self.getToken(BKITParser.GREATER_FLOAT, 0)

        def LESS_OR_EQUAL_FLOAT(self):
            return self.getToken(BKITParser.LESS_OR_EQUAL_FLOAT, 0)

        def GREATER_OR_EQUAL_FLOAT(self):
            return self.getToken(BKITParser.GREATER_OR_EQUAL_FLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_float_op




    def float_op(self):

        localctx = BKITParser.Float_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_float_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.PLUS_FLOAT) | (1 << BKITParser.MINUS_FLOAT) | (1 << BKITParser.STAR_FLOAT) | (1 << BKITParser.DIV_FLOAT) | (1 << BKITParser.NOT_EQUAL_FLOAT) | (1 << BKITParser.LESS_FLOAT) | (1 << BKITParser.GREATER_FLOAT) | (1 << BKITParser.LESS_OR_EQUAL_FLOAT) | (1 << BKITParser.GREATER_OR_EQUAL_FLOAT))) != 0)):
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


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_if_stmt




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dowhile_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_dowhile_stmt




    def dowhile_stmt(self):

        localctx = BKITParser.Dowhile_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dowhile_stmt)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





