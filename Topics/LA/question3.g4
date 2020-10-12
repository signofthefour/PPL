grammar question3;

real: REAL;
string: QUOTE  (STRING)  QUOTE;

fragment NUMBER: [0-9];
fragment DOT: '.';
fragment EXPO: 'e'SIGN;
fragment SIGN: [-|+]?;
fragment SCIEN: EXPO (NUMBER)+;

fragment SING_QUO: ['];
fragment DOU_QUO: SING_QUO SING_QUO;


REAL: SIGN(NUMBER)+(DOT(NUMBER)+ SCIEN? | SCIEN);

STRING: (~['] ~[\n] | DOU_QUO)+ ;
QUOTE: ['];


WS: [ \t\r\n]+ -> skip;