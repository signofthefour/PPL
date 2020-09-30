grammar question2;

id: IDENTIFIER;

fragment LETTER: [a-z];
fragment NUMBER: [0-9];

IDENTIFIER: LETTER(LETTER|NUMBER)*;
WS: [ \t\r\n]+->skip;