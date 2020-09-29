grammar LexicalAnalysis;

@lexer::header {
	from lexererr import *;
}

options{
	language=Python3;
}

program :;

letter: ID;

fragment LETTER: [a-z];
fragment NUMBER: [0-9];

ID: LETTER+;
WS: [ \t\r\n]+;
