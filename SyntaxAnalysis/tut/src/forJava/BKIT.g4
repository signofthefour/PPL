//1810700
grammar BKIT;

options{
	language=Java;
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

call_stmt: ID LEFT_PAREN ids_list* RIGHT_PAREN;

ret_stmt: RETURN expr;  // add SEMI to assignment 

// expression
expr: expr1 PLUS_INT expr | expr1;

expr1: expr2 (<assoc=right>MINUS_INT | <assoc=left>STAR_INT) expr1 | expr2;

expr2: expr2 DIV_INT expr2 | operand;

operand: Integer_literal | Float_literal | ID | call_stmt;

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
INT: 'i' 'n' 't';
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
