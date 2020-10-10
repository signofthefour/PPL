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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3H")
        buf.write("l\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\6\2%\n\2\r\2")
        buf.write("\16\2&\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\5\7?\n\7\3\7")
        buf.write("\3\7\3\7\5\7D\n\7\7\7F\n\7\f\7\16\7I\13\7\3\b\3\b\3\t")
        buf.write("\3\t\5\tO\n\t\3\n\3\n\3\n\3\n\6\nU\n\n\r\n\16\nV\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3")
        buf.write("\17\3\17\3\20\3\20\3\21\3\21\3\21\2\2\22\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \2\6\3\2\16\21\3\2\60\62\b\2")
        buf.write("\'\'))++--//\638\7\2((**,,..9=\2b\2$\3\2\2\2\4*\3\2\2")
        buf.write("\2\6/\3\2\2\2\b8\3\2\2\2\n:\3\2\2\2\f>\3\2\2\2\16J\3\2")
        buf.write("\2\2\20N\3\2\2\2\22P\3\2\2\2\24[\3\2\2\2\26_\3\2\2\2\30")
        buf.write("a\3\2\2\2\32c\3\2\2\2\34e\3\2\2\2\36g\3\2\2\2 i\3\2\2")
        buf.write("\2\"%\5\4\3\2#%\5\6\4\2$\"\3\2\2\2$#\3\2\2\2%&\3\2\2\2")
        buf.write("&$\3\2\2\2&\'\3\2\2\2\'(\3\2\2\2()\7\2\2\3)\3\3\2\2\2")
        buf.write("*+\7\"\2\2+,\7D\2\2,-\5\f\7\2-.\7F\2\2.\5\3\2\2\2/\60")
        buf.write("\7\35\2\2\60\61\7D\2\2\61\62\7\7\2\2\62\63\7\37\2\2\63")
        buf.write("\64\7\22\2\2\64\65\7D\2\2\65\66\7\31\2\2\66\67\7E\2\2")
        buf.write("\67\7\3\2\2\289\t\2\2\29\t\3\2\2\2:;\7\3\2\2;\13\3\2\2")
        buf.write("\2<?\5\16\b\2=?\5\20\t\2><\3\2\2\2>=\3\2\2\2?G\3\2\2\2")
        buf.write("@C\7G\2\2AD\5\16\b\2BD\5\20\t\2CA\3\2\2\2CB\3\2\2\2DF")
        buf.write("\3\2\2\2E@\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2H\r\3")
        buf.write("\2\2\2IG\3\2\2\2JK\7\7\2\2K\17\3\2\2\2LO\5\22\n\2MO\5")
        buf.write("\24\13\2NL\3\2\2\2NM\3\2\2\2O\21\3\2\2\2PT\7\7\2\2QR\7")
        buf.write("@\2\2RS\7\16\2\2SU\7A\2\2TQ\3\2\2\2UV\3\2\2\2VT\3\2\2")
        buf.write("\2VW\3\2\2\2WX\3\2\2\2XY\7H\2\2YZ\7\3\2\2Z\23\3\2\2\2")
        buf.write("[\\\7\7\2\2\\]\7H\2\2]^\5\b\5\2^\25\3\2\2\2_`\t\3\2\2")
        buf.write("`\27\3\2\2\2ab\t\4\2\2b\31\3\2\2\2cd\t\5\2\2d\33\3\2\2")
        buf.write("\2ef\3\2\2\2f\35\3\2\2\2gh\3\2\2\2h\37\3\2\2\2ij\3\2\2")
        buf.write("\2j!\3\2\2\2\t$&>CGNV")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
                     "'ElSelf'", "'ElseIf'", "'EndIf'", "'EndFor'", "'EndWhile'", 
                     "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", 
                     "'Then'", "'Var'", "'While'", "'True'", "'False'", 
                     "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", 
                     "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'=\\='", "'<.'", 
                     "'>.'", "'<=.'", "'>=.'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "':'", "'.'", "';'", "','", "'='" ]

    symbolicNames = [ "<INVALID>", "ARRAY_LIT", "INT_ARRAY", "FLOAT_ARRAY", 
                      "STRING_ARRAY", "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "COMMENT", "UNTERMINATED_COMMENT", "ERROR_CHAR", "WS", 
                      "Integer_literal", "Float_literal", "Boolean_literal", 
                      "String_literal", "BODY", "BREAK", "CONTINUE", "DO", 
                      "ELSE", "ELSELF", "ELSEIF", "ENDBODY", "ENDFOR", "ENDWHILE", 
                      "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                      "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "PLUS_INT", 
                      "PLUS_FLOAT", "MINUS_INT", "MINUS_FLOAT", "STAR_INT", 
                      "STAR_FLOAT", "DIV_INT", "DIV_FLOAT", "MOD", "NOT", 
                      "AND", "OR", "EQUAL", "NOT_EQUAL_INT", "LESS_INT", 
                      "GREATER_INT", "LESS_OR_EQUAL_INT", "GREATER_OR_EQUAL_INT", 
                      "NOT_EQUAL_FLOAT", "LESS_FLOAT", "GREATER_FLOAT", 
                      "LESS_OR_EQUAL_FLOAT", "GREATER_OR_EQUAL_FLOAT", "LEFT_PAREN", 
                      "RIGHT_PARENT", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", 
                      "RIGHT_BRACE", "COLON", "DOT", "SEMI", "COMMA", "ASSIGN" ]

    RULE_program = 0
    RULE_var_declare = 1
    RULE_function_declare = 2
    RULE_primitive_data = 3
    RULE_composite_data = 4
    RULE_var_list = 5
    RULE_var_non_init = 6
    RULE_var_init = 7
    RULE_composite_init = 8
    RULE_primitive_init = 9
    RULE_bool_op = 10
    RULE_int_op = 11
    RULE_float_op = 12
    RULE_if_stmt = 13
    RULE_while_stmt = 14
    RULE_dowhile_stmt = 15

    ruleNames =  [ "program", "var_declare", "function_declare", "primitive_data", 
                   "composite_data", "var_list", "var_non_init", "var_init", 
                   "composite_init", "primitive_init", "bool_op", "int_op", 
                   "float_op", "if_stmt", "while_stmt", "dowhile_stmt" ]

    EOF = Token.EOF
    ARRAY_LIT=1
    INT_ARRAY=2
    FLOAT_ARRAY=3
    STRING_ARRAY=4
    ID=5
    ILLEGAL_ESCAPE=6
    UNCLOSE_STRING=7
    COMMENT=8
    UNTERMINATED_COMMENT=9
    ERROR_CHAR=10
    WS=11
    Integer_literal=12
    Float_literal=13
    Boolean_literal=14
    String_literal=15
    BODY=16
    BREAK=17
    CONTINUE=18
    DO=19
    ELSE=20
    ELSELF=21
    ELSEIF=22
    ENDBODY=23
    ENDFOR=24
    ENDWHILE=25
    FOR=26
    FUNCTION=27
    IF=28
    PARAMETER=29
    RETURN=30
    THEN=31
    VAR=32
    WHILE=33
    TRUE=34
    FALSE=35
    ENDDO=36
    PLUS_INT=37
    PLUS_FLOAT=38
    MINUS_INT=39
    MINUS_FLOAT=40
    STAR_INT=41
    STAR_FLOAT=42
    DIV_INT=43
    DIV_FLOAT=44
    MOD=45
    NOT=46
    AND=47
    OR=48
    EQUAL=49
    NOT_EQUAL_INT=50
    LESS_INT=51
    GREATER_INT=52
    LESS_OR_EQUAL_INT=53
    GREATER_OR_EQUAL_INT=54
    NOT_EQUAL_FLOAT=55
    LESS_FLOAT=56
    GREATER_FLOAT=57
    LESS_OR_EQUAL_FLOAT=58
    GREATER_OR_EQUAL_FLOAT=59
    LEFT_PAREN=60
    RIGHT_PARENT=61
    LEFT_BRACKET=62
    RIGHT_BRACKET=63
    LEFT_BRACE=64
    RIGHT_BRACE=65
    COLON=66
    DOT=67
    SEMI=68
    COMMA=69
    ASSIGN=70

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.VAR]:
                    self.state = 32
                    self.var_declare()
                    pass
                elif token in [BKITParser.FUNCTION]:
                    self.state = 33
                    self.function_declare()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.FUNCTION or _la==BKITParser.VAR):
                    break

            self.state = 38
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

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = BKITParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(BKITParser.VAR)
            self.state = 41
            self.match(BKITParser.COLON)
            self.state = 42
            self.var_list()
            self.state = 43
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declare" ):
                return visitor.visitFunction_declare(self)
            else:
                return visitor.visitChildren(self)




    def function_declare(self):

        localctx = BKITParser.Function_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(BKITParser.FUNCTION)
            self.state = 46
            self.match(BKITParser.COLON)
            self.state = 47
            self.match(BKITParser.ID)
            self.state = 48
            self.match(BKITParser.PARAMETER)
            self.state = 49
            self.match(BKITParser.BODY)
            self.state = 50
            self.match(BKITParser.COLON)
            self.state = 51
            self.match(BKITParser.ENDBODY)
            self.state = 52
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_dataContext(ParserRuleContext):

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
            return BKITParser.RULE_primitive_data

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_data" ):
                return visitor.visitPrimitive_data(self)
            else:
                return visitor.visitChildren(self)




    def primitive_data(self):

        localctx = BKITParser.Primitive_dataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_primitive_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
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


    class Composite_dataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY_LIT(self):
            return self.getToken(BKITParser.ARRAY_LIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_composite_data

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_data" ):
                return visitor.visitComposite_data(self)
            else:
                return visitor.visitChildren(self)




    def composite_data(self):

        localctx = BKITParser.Composite_dataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_composite_data)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(BKITParser.ARRAY_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_non_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_non_initContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_non_initContext,i)


        def var_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_initContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_initContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_var_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_list" ):
                return visitor.visitVar_list(self)
            else:
                return visitor.visitChildren(self)




    def var_list(self):

        localctx = BKITParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 58
                self.var_non_init()
                pass

            elif la_ == 2:
                self.state = 59
                self.var_init()
                pass


            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 62
                self.match(BKITParser.COMMA)
                self.state = 65
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 63
                    self.var_non_init()
                    pass

                elif la_ == 2:
                    self.state = 64
                    self.var_init()
                    pass


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


    class Var_non_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_non_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_non_init" ):
                return visitor.visitVar_non_init(self)
            else:
                return visitor.visitChildren(self)




    def var_non_init(self):

        localctx = BKITParser.Var_non_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_non_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(BKITParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def composite_init(self):
            return self.getTypedRuleContext(BKITParser.Composite_initContext,0)


        def primitive_init(self):
            return self.getTypedRuleContext(BKITParser.Primitive_initContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_init" ):
                return visitor.visitVar_init(self)
            else:
                return visitor.visitChildren(self)




    def var_init(self):

        localctx = BKITParser.Var_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_init)
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.composite_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.primitive_init()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Composite_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def ARRAY_LIT(self):
            return self.getToken(BKITParser.ARRAY_LIT, 0)

        def LEFT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LEFT_BRACKET)
            else:
                return self.getToken(BKITParser.LEFT_BRACKET, i)

        def Integer_literal(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Integer_literal)
            else:
                return self.getToken(BKITParser.Integer_literal, i)

        def RIGHT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RIGHT_BRACKET)
            else:
                return self.getToken(BKITParser.RIGHT_BRACKET, i)

        def getRuleIndex(self):
            return BKITParser.RULE_composite_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_init" ):
                return visitor.visitComposite_init(self)
            else:
                return visitor.visitChildren(self)




    def composite_init(self):

        localctx = BKITParser.Composite_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_composite_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(BKITParser.ID)
            self.state = 82 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 79
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 80
                self.match(BKITParser.Integer_literal)
                self.state = 81
                self.match(BKITParser.RIGHT_BRACKET)
                self.state = 84 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.LEFT_BRACKET):
                    break

            self.state = 86
            self.match(BKITParser.ASSIGN)
            self.state = 87
            self.match(BKITParser.ARRAY_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def primitive_data(self):
            return self.getTypedRuleContext(BKITParser.Primitive_dataContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_primitive_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_init" ):
                return visitor.visitPrimitive_init(self)
            else:
                return visitor.visitChildren(self)




    def primitive_init(self):

        localctx = BKITParser.Primitive_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_primitive_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(BKITParser.ID)
            self.state = 90
            self.match(BKITParser.ASSIGN)
            self.state = 91
            self.primitive_data()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_op" ):
                return visitor.visitBool_op(self)
            else:
                return visitor.visitChildren(self)




    def bool_op(self):

        localctx = BKITParser.Bool_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_bool_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_op" ):
                return visitor.visitInt_op(self)
            else:
                return visitor.visitChildren(self)




    def int_op(self):

        localctx = BKITParser.Int_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_int_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_op" ):
                return visitor.visitFloat_op(self)
            else:
                return visitor.visitChildren(self)




    def float_op(self):

        localctx = BKITParser.Float_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_float_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_if_stmt)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_while_stmt)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhile_stmt" ):
                return visitor.visitDowhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def dowhile_stmt(self):

        localctx = BKITParser.Dowhile_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_dowhile_stmt)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





