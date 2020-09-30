grammar question3;

real: REAL;
string: STRING;

fragment NUMBER: [0-9];
fragment DOT: '.';
fragment EXPO: 'e'SIGN;
fragment SIGN: [-|+]?;
fragment SCIEN: EXPO SIGN (NUMBER)+;

fragment SING_QUO: ['];
fragment DOU_QUO: SING_QUO SING_QUO;


REAL: SIGN(NUMBER)+(DOT(NUMBER)+ SCIEN? | SCIEN);

STRING: SING_QUO (~['] | DOU_QUO)+ SING_QUO;

WS: [ \t\r\n]+ -> skip;