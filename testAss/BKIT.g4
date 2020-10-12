grammar BKIT;

// @lexer::header {
// from lexererr import *
// }

// @lexer::members {
// def emit(self):
//     tk = self.type
//     result = super().emit()
//     if tk == self.UNCLOSE_STRING:       
//         raise UncloseString(result.text)
//     elif tk == self.ILLEGAL_ESCAPE:
//         raise IllegalEscape(result.text)
//     elif tk == self.ERROR_CHAR:
//         raise ErrorToken(result.text)
//     elif tk == self.UNTERMINATED_COMMENT:
//         raise UnterminatedComment()
//     else:
//         return result;
// }

// options{
// 	language=Python3;
// }

//programstructure
program  : var_declare ;

//parser rules:

//var declare
var_declare: VAR COLON var_list (AS )? SEMI;
var_list: (initted_var | non_initted_var) (',' (initted_var |non_initted_var))*;


// List of Tokens
//List of keywowrds
VAR:        'Var';
FUNCTION:   'Function:';
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

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

//some others rules
non_initted_var: IDENTIFIER (LK NUM RK)* ;
initted_var: IDENTIFIER (LK NUM RK)* AS literals;

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
literals: INTERGER | FLOAT | BOLEAN | array_list;
//Integer
INTERGER: NUMBER+ | HEX[0-9A-F]+ | OCTA[0-7]+;
//Float
FLOAT: NUMBER+ (DOT(NUMBER)* SCIEN? | SCIEN)?;
//Bolean
BOLEAN: TRUE | FALSE;
//String


//Array:


array_list: LB array_list | int_array | float_array ( ',' array_list)* RB;
int_array: LB INTERGER (',' INTERGER)* RB;
float_array: LB FLOAT (',' FLOAT)* RB;






//operators

ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
AS:     '=';


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;


//fragments
fragment LETTER:        [a-z];
fragment UPCASE_LETTER: [A-Z];
fragment NUMBER:        [0-9];
fragment EXPO:          ('e'|'E')SIGN;
fragment SIGN:          ('-' | '+')?;
fragment SCIEN:         EXPO (NUMBER)+;
fragment HEX:           '0x' | '0X';
fragment OCTA:          '0o' | '0O';

NUM: NUMBER+;

