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

// 4. Datatypes and values

// 5. Statements

var_declare:  ids_list_with_type SEMI;

function_declare: primitive_type ID LEFT_PAREN (ids_list_with_type (SEMI ids_list_with_type)*)? RIGHT_PAREN
                    LEFT_BRACE
                    function_body
                    RIGHT_BRACE;

function_body: (var_declare | stmt)*; // nullable-list

// statement: assignment, call, return

ids_list_with_type: primitive_type ids_list;

stmt: (assign_stmt | call_stmt | ret_stmt) SEMI; // only SEMI in stmt def

assign_stmt: ID ASSIGN expr;

call_stmt: ID LEFT_PAREN (exprs_list)* RIGHT_PAREN;

ret_stmt: RETURN expr;  // add SEMI to assignment 

exprs_list: expr | exprs_list COMMA expr;

// expression
expr: expr0;

expr0: expr1 PLUS_INT expr0 | expr1;

expr1: expr1 MINUS_INT expr1 | expr2;

expr2: expr2 DIV_INT operand | expr2 STAR_INT operand | operand;

subexpr: LEFT_PAREN expr RIGHT_PAREN;

operand: Integer_literal | Float_literal | ID | call_stmt | subexpr;

ids_list: ID (COMMA ID)*;

primitive_type: INT | FLOAT;

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


String_literal: '"' STRING_CHAR* '"';
// Keywords
RETURN:    'r' 'e' 't' 'u' 'r' 'n';
INT: 'i''n' 't';
FLOAT: 'f' 'l' 'o' 'a' 't';
// Operators
PLUS_INT:       '+';
MINUS_INT:      '-';
STAR_INT:       '*';
DIV_INT:        '/';

// Seperators
LEFT_PAREN:     '(';
RIGHT_PAREN:   ')';
LEFT_BRACKET:   '[';
RIGHT_BRACKET:  ']';
LEFT_BRACE:     '{';
RIGHT_BRACE:    '}';
COLON:          ':';
DOT:            '.';
SEMI:           ';';
COMMA:          ',';
ASSIGN:         '=';

ID: LOWERCASE_LETTER (LOWERCASE_LETTER | DIGIT)*; // must begin with lowercase, case-sensitive

ILLEGAL_ESCAPE: '"' STRING_CHAR* ILL_ESC_SEQUENCE;
UNCLOSE_STRING: '"' STRING_CHAR* EOF;
COMMENT: '**' .*? '**' -> skip;
UNTERMINATED_COMMENT: '**' .*? EOF; 
ERROR_CHAR: [.?];

WS: [ \t\f\r\n]+ -> skip;