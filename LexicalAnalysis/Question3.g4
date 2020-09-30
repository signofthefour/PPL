grammar Question3;

program :;

number: (Real_number | Integer_number)+;

string: '\''  STRING '\'';

Real_number: SIGN FLOATING_POINT_NUM;

Integer_number: SIGN (
		DECIMAL
		| HEXADECIMAL
		| OCTAL)
		; 

fragment LOWERCASE_LETTER: [a-z];

fragment UPPERCASE_LETTER: [A-Z];

fragment DIGIT: [0-9];

fragment SIGN: [+-]?;

fragment SPACE: [ ];

fragment SCIENTIFIC: [e](SIGN)(DIGIT)+;

fragment DECIMAL_POINT: [.](DIGIT)*;

fragment FLOATING_POINT_NUM:  (DIGIT+) (DECIMAL_POINT(SCIENTIFIC)? | SCIENTIFIC);

fragment SING_QUOTE: ['];

fragment DOUBLE_QUOTE: ["];

fragment DOUBLE_QUOTE_IN_QUOTE: ['"];

fragment HEXADECIMALDIGIT: [0-9a-fA-F];

fragment OCTALDIGIT: [0-7];

fragment COLON: ':';

SEMI: ';';

fragment DOT: '.';

COMMA: ',';

//Define sequence
HEXADECIMAL: ('0x' | '0X') HEXADECIMALDIGIT+; 

DECIMAL: DIGIT+;

OCTAL: ('0o' | '0O') OCTALDIGIT+;

fragment LETTER: (LOWERCASE_LETTER | UPPERCASE_LETTER); 

ID: LOWERCASE_LETTER (LOWERCASE_LETTER | DIGIT)*;

fragment SING_QUOTE_IN_STRING: SING_QUOTE SING_QUOTE;

fragment STRING_CHAR: SING_QUOTE_IN_STRING | ~['\b\r\n\f\t];

STRING: STRING_CHAR*; 

WS: [ \t\r\n]+ -> skip;
