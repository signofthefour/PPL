grammar BKIT;
//MSSV: 1810992

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

//programstructure
program  : (var_declare*)  (func_declare)* EOF;

//var declare
var_declare: VAR COLON var_list (AS )? SEMI;
var_list: (initted_var | non_initted_var) (',' (initted_var |non_initted_var))*;

//func_declare ()
main_func: ;
func_declare: FUNCTION COLON IDENTIFIER (PARAMETER COLON para_list)? BODY COLON func_body  ENDBODY DOT;
func_body: stm_list;
stm_list: var_declare* stm*;
stm:  assign_stmt
    | if_stmt
    | for_stmt
    | while_stmt
    | do_while_stmt
    | break_stmt
    | continue_stmt
    | call_stmt
    | return_stmt ;



// List of Tokens


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
COMMENT: ('**' .*? '**') -> skip;

//init type
non_initted_var: scalar_var | composite_var;
initted_var: scalar_init | composite_init;

//init rules:
scalar_init: scalar_var AS literals;
composite_init: composite_var AS literals;

//var type:
scalar_var: IDENTIFIER;
composite_var:  IDENTIFIER (LK INTEGER RK)+ ;

//para_list:
para_list: (scalar_var | composite_var)  (',' (scalar_var | composite_var))*;



// ===================================== STATMENT ====================================
//if stament:
if_stmt: IF expression THEN stm_list (ELSEIF expression THEN stm_list)* (ELSE stm_list)? ENDIF DOT ;

//assignment stament:
assign_stmt: (scalar_var | composite_ass) AS expression SEMI ;
composite_ass: IDENTIFIER index_op;  

//for statement:
for_stmt: FOR LP scalar_var AS expression CM expression CM exp1 RP DO stm_list ENDFOR DOT ;

//while stament 
while_stmt: WHILE expression DO stm_list ENDWHILE DOT;

//do-while statement:
do_while_stmt: DO stm_list WHILE expression ENDDO DOT ;

//break stament:
break_stmt: BREAK SEMI;

//continue statement:
continue_stmt: CONTINUE SEMI;

//return statement:
return_stmt: RETURN  (expression (',' expression)*)? SEMI;

//func_call statement
func_call: IDENTIFIER LP (expression (',' expression)*)?  RP ;
call_stmt: func_call SEMI;

// ===================================== STATMENT ====================================




// ===================================== EXPRESSON ===================================
//relation operator
RELATION_OP: EQUAL | FNEQUAL | FLESSOE | FGROE | FLESS | FGR | INEQUAL | ILESSOE | IGROE | ILESS | IGR ;
ADDSUB: FADDOP | FSUBOP | IADDOP | ISUBOP;
MULDIV: FMULOP | FDIVOP | IMULOP | IDIVOP | IREMAIN;
NEGSIGN: ISUBOP | FSUBOP;
index_op: (LK expression RK)+;

//expression
expression: exp0;
exp0: exp1 RELATION_OP exp1 | exp1;
exp1: exp1 (BAND | BOR) exp2 | exp2;
exp2: exp2 (ADDSUB) exp3 | exp3;
exp3: exp3 (MULDIV) exp4 | exp4;
exp4: BNEG exp4 | exp5;
exp5: ADDSUB exp5 | exp6;
exp6: exp6 index_op | exp7;
exp7: func_call |exp8;
exp8: LP (expression) RP | operand;
operand: IDENTIFIER | literals | BOLEAN;


// ===================================== EXPRESSON ===================================s


//Identifiers
IDENTIFIER: LETTER(LETTER|UPCASE_LETTER|NUMBER|'_')*;

//seprators
LB:     '{';
RB:     '}';
LK:     '[';
RK:     ']';
LP:     '(';
RP:     ')';
SEMI:   ';';
COLON:  ':';
CM:     ',';
DOT:    '.';




//Literals
literals: array_list | INTEGER | FLOAT | BOLEAN | LSTRING ;

//Integer
INTEGER: [1-9]NUMBER* | HEX[1-9A-F][0-9A-F]* | OCTA[1-7][0-7]* | '0'; // 
//Float
FLOAT: NUMBER+ (DOT(NUMBER)* SCIEN? | SCIEN); // Error, contain 0;
//Bolean
BOLEAN: TRUE | FALSE;

//Array:
bool_array: BOLEAN (',' BOLEAN)*;
int_array: INTEGER (',' INTEGER)* ;
float_array: FLOAT (',' FLOAT)*;
string_array: LSTRING (',' LSTRING)*;
array_index: int_array | float_array | string_array | bool_array;
array_list: LB ((array_list | array_index)( ',' (array_list | array_index))*)? RB;

//operators
// Arithmetic operators
FADDOP:     '+.';
IADDOP:     '+';
FSUBOP:     '-.';
ISUBOP:     '-';
FMULOP:     '*.';
IMULOP:     '*';
FDIVOP:     '\\.';
IDIVOP:     '\\';
IREMAIN:    '%';


//Relational operators
EQUAL:      '==';
//for float
FNEQUAL:    '=/=';
FLESSOE:    '<=.';
FGROE:      '>=.';
FLESS:      '<.';
FGR:        '>.';
//for integer:
INEQUAL:    '!=';
ILESSOE:    '<=';
IGROE:      '>=';
ILESS:      '<';
IGR:        '>';

// Boolean operators
BNEG:       '!';
BAND:       '&&';
BOR:        '||';

//assign op
AS:     '=';

//List of keywowrds (Note: endbody have a dot)
VAR:        'Var';
FUNCTION:   'Function';
BODY:       'Body';
ELSE:       'Else';
ENDFOR:     'EndFor';
IF:         'If';
ENDDO:      'EndDo';
BREAK:      'Break';
ELSEIF:     'ElseIf';
ENDWHILE:   'EndWhile';
PARAMETER:  'Parameter';
WHILE:      'While';
CONTINUE:   'Continue';
ENDBODY:    'EndBody';
FOR:        'For';
RETURN:     'Return';
TRUE:       'True';
DO:         'Do';
ENDIF:      'EndIf';
THEN:       'Then';
FALSE:      'False';

ERROR_CHAR: .;
UNCLOSE_STRING: DOUQUO CHAR_STRING* ('\n' | EOF) 
{
    self.text = (self.text)[1:]
};
ILLEGAL_ESCAPE: '"' CHAR_STRING* ILLEGAL_CHAR {
    self.text = (self.text)[1:]
};
UNTERMINATED_COMMENT: '**' .*?;


//fragments
fragment DOUQUO: '"';
fragment LETTER:        [a-z];
fragment UPCASE_LETTER: [A-Z];
fragment NUMBER:        [0-9];
fragment EXPO:          ('e'|'E')SIGN;
fragment SIGN:          ('-' | '+')?;
fragment SCIEN:         EXPO (NUMBER)+;
fragment HEX:           '0x' | '0X';
fragment OCTA:          '0o' | '0O';
fragment SDOUQUO:       SINGQUO DOUQUO;
fragment SINGQUO:       '\'';
fragment ESCAPE_CHAR : '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\\'' | '\\\\' ;
fragment ILLEGAL_CHAR: ('\\' ~[bfrnt'\\]) | '\'' ~'"' ;

fragment CHAR_STRING:   ESCAPE_CHAR | '\'' '"' |~[\n'"\\] ;

//String
LSTRING: DOUQUO CHAR_STRING* DOUQUO { self.text = self.text[1:-1] };


