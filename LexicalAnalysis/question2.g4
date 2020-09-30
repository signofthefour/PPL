lexer grammar question2;

fragment LETTER: [a-z];
fragment NUMBER: [0-9];

IDENTIFIER: LETTER(LETTER|NUMBER)+;
WS: [ \t\r\n]->skip;