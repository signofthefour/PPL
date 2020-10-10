# Generated from BKIT.g4 by ANTLR 4.8
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
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\3\2\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Body'", "'Break'", "'Continue'", 
                     "'Do'", "'Else'", "'ElSelf'", "'ElseIf'", "'EndIf'", 
                     "'EndFor'", "'EndWhile'", "'For'", "'Function'", "'If'", 
                     "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
                     "'True'", "'False'", "'EndDo'", "'+'", "'+.'", "'-'", 
                     "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", 
                     "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'=\\='", "'<.'", "'>.'", "'<=.'", "'>=.'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "':'", "'.'", 
                     "';'", "','" ]

    symbolicNames = [ "<INVALID>", "REAL_NUMBER", "ID", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "COMMENT", "UNTERMINATED_COMMENT", 
                      "ERROR_CHAR", "WS", "Literal", "Integer_literal", 
                      "Float_literal", "Boolean_literal", "String_literal", 
                      "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSELF", 
                      "ELSEIF", "ENDBODY", "ENDFOR", "ENDWHILE", "FOR", 
                      "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "VAR", 
                      "WHILE", "TRUE", "FALSE", "ENDDO", "PLUS_INT", "PLUS_FLOAT", 
                      "MINUS_INT", "MINUS_FLOAT", "STAR_INT", "STAR_FLOAT", 
                      "DIV_INT", "DIV_FLOAT", "MOD", "NOT", "AND", "OR", 
                      "EQUAL", "NOT_EQUAL_INT", "LESS_INT", "GREATER_INT", 
                      "LESS_OR_EQUAL_INT", "GREATER_OR_EQUAL_INT", "NOT_EQUAL_FLOAT", 
                      "LESS_FLOAT", "GREATER_FLOAT", "LESS_OR_EQUAL_FLOAT", 
                      "GREATER_OR_EQUAL_FLOAT", "LEFT_PAREN", "RIGHT_PARENT", 
                      "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", 
                      "COLON", "DOT", "SEMI", "COMMA" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    REAL_NUMBER=1
    ID=2
    ILLEGAL_ESCAPE=3
    UNCLOSE_STRING=4
    COMMENT=5
    UNTERMINATED_COMMENT=6
    ERROR_CHAR=7
    WS=8
    Literal=9
    Integer_literal=10
    Float_literal=11
    Boolean_literal=12
    String_literal=13
    BODY=14
    BREAK=15
    CONTINUE=16
    DO=17
    ELSE=18
    ELSELF=19
    ELSEIF=20
    ENDBODY=21
    ENDFOR=22
    ENDWHILE=23
    FOR=24
    FUNCTION=25
    IF=26
    PARAMETER=27
    RETURN=28
    THEN=29
    VAR=30
    WHILE=31
    TRUE=32
    FALSE=33
    ENDDO=34
    PLUS_INT=35
    PLUS_FLOAT=36
    MINUS_INT=37
    MINUS_FLOAT=38
    STAR_INT=39
    STAR_FLOAT=40
    DIV_INT=41
    DIV_FLOAT=42
    MOD=43
    NOT=44
    AND=45
    OR=46
    EQUAL=47
    NOT_EQUAL_INT=48
    LESS_INT=49
    GREATER_INT=50
    LESS_OR_EQUAL_INT=51
    GREATER_OR_EQUAL_INT=52
    NOT_EQUAL_FLOAT=53
    LESS_FLOAT=54
    GREATER_FLOAT=55
    LESS_OR_EQUAL_FLOAT=56
    GREATER_OR_EQUAL_FLOAT=57
    LEFT_PAREN=58
    RIGHT_PARENT=59
    LEFT_BRACKET=60
    RIGHT_BRACKET=61
    LEFT_BRACE=62
    RIGHT_BRACE=63
    COLON=64
    DOT=65
    SEMI=66
    COMMA=67

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
            return BKITParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
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





