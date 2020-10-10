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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
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
                     "<INVALID>", "'Body'", "'Break'", "'Continue'", "'Do'", 
                     "'Else'", "'ElSelf'", "'ElseIf'", "'EndIf'", "'EndFor'", 
                     "'EndWhile'", "'For'", "'Function'", "'If'", "'Parameter'", 
                     "'Return'", "'Then'", "'Var'", "'While'", "'True'", 
                     "'False'", "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", 
                     "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", 
                     "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'=\\='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "':'", "'.'", "';'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "REAL_NUMBER", "ID", "ILLEGAL_ESCAPE", 
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
                      "RIGHT_BRACE", "COLON", "DOT", "SEMI", "COMMA" ]

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

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





