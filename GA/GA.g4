grammar GA;

//program structure: 
program: (var_declare | func_declare)+ EOF;

//primetive_type:
type: INT | FLOAT;    

//var declear:
ids_list: ID(',' ID)*  ;
var_declare: type ids_list SM;

//function declear:
func_declare: type ID LP (type ids_list ( SM type ids_list))? RP LB func_body RB;
func_body: (var_declare | statement)*;

//main statements: 
statement: (assign_stmt | call_stmt | rt_stmt)  SM;
assign_stmt: ID EQ expression ;
call_stmt: ID LP expression_list RP ;
rt_stmt: RETURN expression ;

//keywords
INT:'int';
FLOAT:'float';
RETURN:'return';

//fragments
fragment NUMBER: [0-9];
fragment DOT: '.';
fragment EXPO: 'e'SIGN;
fragment SIGN: [-|+]?;
fragment SCIEN: EXPO (NUMBER)+;


ID: [a-z][a-z0-9]*;
INTLIT: SIGN [1-9][0-9]*;
FLOATLIT: SIGN(NUMBER)+(DOT(NUMBER)+ SCIEN? | SCIEN);

//seprators
LB: '{';
RB: '}';
SM: ';';
CM: ',';
EQ: '=';
LP: '(';
RP: ')';


//operators
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';

//expressions
expression: exp0;
exp0: exp1 ADDOP exp0 | exp1;
exp1: exp2 SUBOP exp2 | exp2;
exp2: exp2 MULOP operand | exp2 DIVOP operand | operand;
operand: INTLIT | FLOATLIT | ID | call_stmt | sub_exp;
sub_exp: LP expression RP;

expression_list: expression (',' expression)*;


WS: [ \t\f\r\n]+ -> skip;