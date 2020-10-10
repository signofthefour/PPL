//1810700
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program: (var_declare | function_declare)+ EOF;

// 1. program structure

var_declare: VAR 
            // id_list = id | id with initial
                SEMI;

function_declare: FUNCTION COLON ID
                    PARAMETER //param_list
                    BODY COLON
                    // statements_list
                    ENDBODY DOT;

// 4. Datatypes and values
primitive_type: Integer_literal | Float_literal | String_literal | Boolean_literal;
composite_type: array;

array: ;
INT_ARRAY: LEFT_BRACE ()RIGHT_BRACE;
// 4.1 boolean op
bool_op: NOT | AND | OR;

// 4.2 integer op
int_op: PLUS_INT
        | MINUS_INT
        | STAR_INT
        | DIV_INT
        | MOD
        | EQUAL
        | NOT_EQUAL_INT
        | LESS_INT
        | GREATER_INT
        | LESS_OR_EQUAL_INT
        | GREATER_OR_EQUAL_INT;

// 4.3 float op
float_op: PLUS_FLOAT
            | MINUS_FLOAT
            | STAR_FLOAT
            | DIV_FLOAT
//            | EQUAL
            | NOT_EQUAL_FLOAT
            | LESS_FLOAT
            | GREATER_FLOAT
            | LESS_OR_EQUAL_FLOAT
            | GREATER_OR_EQUAL_FLOAT
            ;

// 4.4 string op: No string op


// 5. Statements
if_stmt: ;
while_stmt: ;
dowhile_stmt: ;

ID: LOWERCASE_LETTER (LOWERCASE_LETTER | DIGIT)*; // must begin with lowercase, case-sensitive

ILLEGAL_ESCAPE: '"' STRING_CHAR* ILL_ESC_SEQUENCE;
UNCLOSE_STRING: '"' STRING_CHAR* ([\b\t\r\n\f] | EOF) 
    {
        y = str(self.text);
        self.text = y[1:]
    };
COMMENT: '**' .*? '**' -> skip;
UNTERMINATED_COMMENT: '**' .*? EOF; 
ERROR_CHAR: [.?];

WS: [ \t\f\r\n]+ -> skip;

// letter
fragment LOWERCASE_LETTER: [a-z];
fragment UPPERCASE_LETTER: [A-Z];
fragment DIGIT: [0-9];
fragment LETTER: (LOWERCASE_LETTER | UPPERCASE_LETTER); 

//float
fragment SCIENTIFIC: [Ee](MINUS_INT)?(DIGIT)+;

fragment DECIMAL_POINT: [.](DIGIT)*;
fragment FLOATING_POINT_NUM:  (DIGIT+) (DECIMAL_POINT(SCIENTIFIC)? | SCIENTIFIC);

// string
fragment ILL_ESC_SEQUENCE: '\\' ~[btrnf'\\];
fragment SUP_ESC_SEQUENCE: '\\' [bfrnt'\\];
fragment DOUBLE_QUOTE_IN_STRING: '\'' '"';
fragment STRING_CHAR: ~[\b\t\r\n\f'\\"] | SUP_ESC_SEQUENCE | DOUBLE_QUOTE_IN_STRING;

// integer
fragment HEXADECIMALDIGIT: [0-9a-fA-F];
fragment OCTALDIGIT: [0-7];
fragment HEXADECIMAL: ('0x' | '0X') HEXADECIMALDIGIT+; 
fragment DECIMAL: DIGIT+;
fragment OCTAL: ('0o' | '0O') OCTALDIGIT+;

Integer_literal: DECIMAL 
                | HEXADECIMAL 
                | OCTAL;

Float_literal: FLOATING_POINT_NUM;

Boolean_literal: TRUE | FALSE;

String_literal: '"' STRING_CHAR* '"'
    {
        y = str(self.text)
        self.text = y[1:-1]
    };

// Keywords
BODY :     'Body';
BREAK:     'Break';
CONTINUE:  'Continue';
DO:        'Do';
ELSE:      'Else';
ELSELF:    'ElSelf';
ELSEIF:    'ElseIf';
ENDBODY:   'EndIf';
ENDFOR:    'EndFor';
ENDWHILE:  'EndWhile';
FOR:       'For';
FUNCTION:  'Function';
IF:        'If';
PARAMETER: 'Parameter';
RETURN:    'Return';
THEN:      'Then';
VAR:       'Var';
WHILE:     'While';
TRUE:      'True';
FALSE:     'False';
ENDDO:     'EndDo';

// Operators
PLUS_INT:       '+';
PLUS_FLOAT:     '+.';
MINUS_INT:      '-';
MINUS_FLOAT:    '-.';
STAR_INT:       '*';
STAR_FLOAT:     '*.';
DIV_INT:        '\\';
DIV_FLOAT:      '\\.';
MOD:            '%';
NOT:            '!';
AND:            '&&';
OR:             '||';
EQUAL:          '==';
NOT_EQUAL_INT:  '!=';
LESS_INT:           '<';
GREATER_INT:        '>';
LESS_OR_EQUAL_INT:  '<=';
GREATER_OR_EQUAL_INT:'>=';
NOT_EQUAL_FLOAT:'=\\=';
LESS_FLOAT:     '<.';
GREATER_FLOAT:  '>.';
LESS_OR_EQUAL_FLOAT: '<=.';
GREATER_OR_EQUAL_FLOAT: '>=.';

// Seperators
LEFT_PAREN:     '(';
RIGHT_PARENT:   ')';
LEFT_BRACKET:   '[';
RIGHT_BRACKET:  ']';
LEFT_BRACE:     '{';
RIGHT_BRACE:    '}';
COLON:          ':';
DOT:            '.';
SEMI:           ';';
COMMA:          ',';
ASSIGN:         '=';