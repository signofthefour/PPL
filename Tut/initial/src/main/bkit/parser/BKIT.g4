grammar BKIT;

@lexer::header {
from lexererr import *
}


options{
	language=Python3;
}

program  : IDENTIFIER_Q1 IDENTIFIER_Q2 REAL STRING EOF ;

//question1
IDENTIFIER_Q1: [a-z][a-z0-9]*;


//question2
fragment LETTER: [a-z];
fragment NUMBER: [0-9];

IDENTIFIER_Q2: LETTER(LETTER|NUMBER)*;


//question3
fragment DOT: '.';
fragment EXPO: 'e'SIGN;
fragment SIGN: [-|+]?;
fragment SCIEN: EXPO (NUMBER)+;

fragment SING_QUO: ['];
fragment DOU_QUO: SING_QUO SING_QUO;


REAL: SIGN(NUMBER)+(DOT(NUMBER)+ SCIEN? | SCIEN);

STRING: SING_QUO (~['] ~[\n] | DOU_QUO)+ SING_QUO;

WS: [ \t\r\n]+ -> skip;



