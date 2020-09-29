grammar Question2;

letter: ID;

fragment LOWERCASE_LETTER: [a-z];
fragment NUMBER: [0-9];


ID: LOWERCASE_LETTER (LOWERCASE_LETTER | NUMBER)+;
WS: [ \t\r\n]+ -> skip;
