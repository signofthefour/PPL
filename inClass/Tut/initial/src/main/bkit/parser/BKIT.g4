grammar BKIT;

@lexer::header {
from lexererr import *
}

options {language = Python3;}

//program structure: 
program: (var_declare | func_declare)+ EOF;

//primetive_type:
var_type: INT | FLOAT;   

//main statements: 
statement: (assign_stmt | call_stmt | rt_stmt)  SM;
call_stmt: ID LP (expression_list)? RP ;
assign_stmt: ID EQ expression ;
rt_stmt: RETURN expression ; 

//var declear:
ids_list: ID(',' ID)*  ;
var_declare: var_type ids_list SM;

//function declear:
func_declare: var_type ID LP (var_type ids_list ( SM var_type ids_list)*)* RP LB func_body RB;
func_body: (var_declare | statement)*;



//keywords
INT:'int';
FLOAT:'float';
RETURN:'return';

//fragments
fragment NUMBER: [0-9];
fragment DOT: '.';
fragment EXPO: 'e'SIGN;
fragment SIGN: '-'?;
fragment SCIEN: EXPO (NUMBER)+;


ID: [a-z][a-z0-9]*;
INTLIT: SIGN [0-9]+;
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
expression:  exp0  ;
exp0: exp1 ADDOP exp0 | exp1;
exp1: exp1 SUBOP exp2 | exp2;
exp2: exp2 MULOP operand | exp2 DIVOP operand | operand;

operand: INTLIT | FLOATLIT | ID | call_stmt | sub_exp ;
sub_exp: LP expression RP;

expression_list: expression (',' expression)*;


WS: [ \t\f\r\n]+ -> skip;