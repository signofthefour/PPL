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

num_tokens = 0
}

options{
	language=Python3;
}

program  : VAR  EOF ;

var_declaration: 'Var' Ids_list SEMI; 

number: (Real_number | Integer_number)+;

STRING: '"' + (STRING_CHAR*) + '"';

Real_number: SIGN FLOATING_POINT_NUM;

Integer_number: SIGN (
		DECIMAL
		| HEXADECIMAL
		| OCTAL)
		; 

Ids_list: ID (COMMA ID)*;

fragment LOWERCASE_LETTER: [a-z];

fragment UPPERCASE_LETTER: [A-Z];

fragment DIGIT: [0-9];

fragment SIGN: [+-]?;

fragment SPACE: [ ];

fragment ESCAPE_SEQUENCE: '\\' [btrnf'\\];

fragment ESCAPE_ILLEGAL: '\\' ~[btrnf'\\] | ~'\\';

fragment SCIENTIFIC: [e](SIGN)(DIGIT)+;

fragment DECIMAL_POINT: [.](DIGIT)*;

fragment FLOATING_POINT_NUM:  (DIGIT+) (DECIMAL_POINT(SCIENTIFIC)? | SCIENTIFIC);

fragment SING_QUOTE: ['];

fragment DOUBLE_QUOTE: ["];

fragment DOUBLE_QUOTE_IN_QUOTE: ['"];

fragment HEXADECIMALDIGIT: [0-9a-fA-F];

fragment OCTALDIGIT: [0-7];

COLON: ':';


SEMI: ';';

DOT: '.';

COMMA: ',';

VAR: 'Var';

//Define sequence
fragment HEXADECIMAL: ('0x' | '0X') HEXADECIMALDIGIT+; 

fragment DECIMAL: DIGIT+;

fragment OCTAL: ('0o' | '0O') OCTALDIGIT+;

fragment LETTER: (LOWERCASE_LETTER | UPPERCASE_LETTER); 

fragment STRING_CHAR: ~ [\b\t\n\f\r\\"] | ESCAPE_SEQUENCE | SING_QUOTE DOUBLE_QUOTE | EOF;

fragment PUNCTUATION: 	COLON
		| SEMI
		| DOT
		| COMMA
		;

fragment ID: LOWERCASE_LETTER (LOWERCASE_LETTER | DIGIT)*;

ILLEGAL_ESCAPE: '"' STRING_CHAR* ESCAPE_ILLEGAL;

WS: [ \t\r\n]+ -> skip;

UNCLOSE_STRING: '"' STRING_CHAR* ([\b\t\r\f\n] | EOF);

ERROR_CHAR: .;

BLOCK_COMMENT: '**' .*? '**' -> channel(HIDDEN);

UNTERMINATED_COMMENT: '**' .*? EOF;  	
