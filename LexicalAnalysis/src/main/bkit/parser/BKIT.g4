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

program  : VAR  EOF ;

VAR: 'Var' + ID;

number: (Real_number | Integer_number)+;

string: '"' + (String) + '"';

Real_number: SIGN FLOATING_POINT_NUM;

Integer_number: SIGN (
		DECIMAL
		| HEXADECIMAL
		| OCTAL)
		; 

String:	(LETTER+
	| ESCAPE_SEQUENCE
	| SING_QUOTE DOUBLE_QUOTE
	| DIGIT	
	| PUNCTUATION
	| SING_QUOTE SING_QUOTE
	| SPACE
	)+ 
	;

fragment LOWERCASE_LETTER: [a-z];

fragment UPPERCASE_LETTER: [A-Z];

fragment DIGIT: [0-9];

fragment SIGN: [+-]?;

fragment SPACE: [ ];

fragment ESCAPE_SEQUENCE:
	SING_QUOTE
	| '\\b'
	| '\\f'
	| '\\n'
	| '\\r'
	| '\\t'
	;

fragment SCIENTIFIC: [e](SIGN)(DIGIT)+;

fragment DECIMAL_POINT: [.](DIGIT)*;

fragment FLOATING_POINT_NUM:  (DIGIT+) (DECIMAL_POINT(SCIENTIFIC)? | SCIENTIFIC);

fragment SING_QUOTE: ['];

fragment DOUBLE_QUOTE: ["];

fragment DOUBLE_QUOTE_IN_QUOTE: ['"];

fragment HEXADECIMALDIGIT: [0-9a-fA-F];

fragment OCTALDIGIT: [0-7];

fragment COLON: ':';

fragment SEMI: ';';

fragment DOT: '.';

fragment COMMA: ',';

fragment STR_CHAR: 

//Define sequence
HEXADECIMAL: ('0x' | '0X') HEXADECIMALDIGIT+; 

DECIMAL: DIGIT+;

OCTAL: ('0o' | '0O') OCTALDIGIT+;

LETTER: (LOWERCASE_LETTER | UPPERCASE_LETTER); 

PUNCTUATION: 	COLON
		| SEMI
		| DOT
		| COMMA
		;

ID: LOWERCASE_LETTER (LOWERCASE_LETTER | DIGIT)+;

ILLEGAL_ESCAPE: '"' ('\\' ~[btnfr"'\\] | ~'\\')*;

WS: [ \t\r\n]+ -> skip;

