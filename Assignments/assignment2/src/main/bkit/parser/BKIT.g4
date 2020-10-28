//1810700
grammar BKIT;

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
    // language=Java;
}

program: (var_declare SEMI)* function_declare* EOF;

// 1. program structure

var_declare: VAR COLON
            var_list;

function_declare: FUNCTION COLON ID
                    (PARAMETER COLON params_list)?
                    BODY COLON
                    (var_declare_stmt SEMI)* stmt*
                    ENDBODY DOT;

array: ID ASSIGN array_lit;

// 4. Datatypes and 
primitive_data: INT_LIT | FLOAT_LIT | STRING_LIT | BOOL_LIT;

array_lit: LEFT_BRACE ((primitive_data | array_lit) (COMMA (primitive_data | array_lit))*)? RIGHT_BRACE;

// var declare
var_list: (var_non_init | var_init) (COMMA (var_non_init | var_init))*; //non empty
var_non_init: ID (LEFT_BRACKET INT_LIT RIGHT_BRACKET)+ | ID;
composite_var: ID (LEFT_BRACKET (composite_var | expr) RIGHT_BRACKET)+;
// var_init: composite_init | primitive_init;
var_init: ( ID (LEFT_BRACKET INT_LIT RIGHT_BRACKET)+ | ID) ASSIGN (array_lit | primitive_data);
composite_init: composite_var ASSIGN array_lit;
primitive_init: ID ASSIGN primitive_data;

// func_utils
params_list: var_non_init (COMMA var_non_init)*;
// 4.0 op

// 5. Statements
stmt_list: (var_declare_stmt SEMI)* stmt*;
stmt: if_stmt
        | for_stmt
        | while_stmt
        | dowhile_stmt
        | assign_stmt SEMI
        | break_stmt SEMI
        | continue_stmt SEMI
        | call_stmt SEMI
        | return_stmt SEMI;

if_stmt: IF expr
            THEN stmt_list 
         (ELSEIF expr
            THEN stmt_list)*
         (ELSE stmt_list)?
         ENDIF DOT;

var_declare_stmt: var_declare;
for_stmt: FOR LEFT_PAREN init_for COMMA con_for COMMA update_for RIGHT_PAREN DO
            stmt_list
            ENDFOR DOT;
while_stmt: WHILE expr DO stmt_list ENDWHILE DOT;
dowhile_stmt: DO stmt_list WHILE expr ENDDO DOT;
assign_stmt: (composite_var | ID) ASSIGN (expr);
break_stmt: BREAK;
continue_stmt: CONTINUE;
call_stmt: function_call ;
return_stmt: RETURN expr?;

// 5.1 stmt utils
init_for: ID ASSIGN expr;
con_for: expr;
update_for: expr;
// 6. expr_utils
expr: expr1 REL_OP expr1 | expr1;
        
expr1: expr1 BIN_LOGICAL_OP expr2 | expr2;
expr2: expr2 ADD_OP expr3 | expr3;
expr3: expr3 MUL_OP expr4 | expr4;
expr4: UN_LOGICAL_OP expr4 | expr5;
expr5: UN_OP expr5 | expr6;
expr6: expr7 index_op | expr7;
expr7: function_call | expr8;
expr8: operand | LEFT_PAREN expr RIGHT_PAREN;
operand: var_non_init | primitive_data | array_lit;


function_call: ID LEFT_PAREN (expr (COMMA expr)*)* RIGHT_PAREN;


index_op: LEFT_BRACKET expr RIGHT_BRACKET | LEFT_BRACKET expr RIGHT_BRACKET index_op;

ID: LOWERCASE_LETTER (LOWERCASE_LETTER | DIGIT | UPPERCASE_LETTER | '_')*; // must begin with lowercase, case-sensitive

REL_OP: EQUAL
            | NOT_EQUAL_INT
            | LESS_INT
            | GREATER_INT
            | LESS_OR_EQUAL_INT
            | GREATER_OR_EQUAL_INT 
            | NOT_EQUAL_FLOAT
            | LESS_FLOAT
            | GREATER_FLOAT
            | LESS_OR_EQUAL_FLOAT
            | GREATER_OR_EQUAL_FLOAT;
        
BIN_LOGICAL_OP: (AND | OR);
ADD_OP: (PLUS_FLOAT | PLUS_INT | MINUS_FLOAT | MINUS_INT);
MUL_OP: (STAR_INT | STAR_FLOAT | DIV_FLOAT |  DIV_INT | MOD);
UN_LOGICAL_OP: NOT;
UN_OP: (MINUS_FLOAT | MINUS_INT);

// letter
fragment LOWERCASE_LETTER: [a-z];
fragment UPPERCASE_LETTER: [A-Z];
fragment DIGIT: [0-9];
fragment LETTER: (LOWERCASE_LETTER | UPPERCASE_LETTER); 

//float
fragment SCIENTIFIC: [Ee](MINUS_INT | PLUS_INT)?(DIGIT)+;
fragment DECIMAL_POINT: [.](DIGIT)*;
fragment FLOATING_POINT_NUM:  (DIGIT+) (DECIMAL_POINT(SCIENTIFIC)? | SCIENTIFIC);

// string
fragment ILL_ESC_SEQUENCE: '\\' ~[btrnf'\\];
fragment SUP_ESC_SEQUENCE: '\\' [bfrnt'\\];
fragment DOUBLE_QUOTE_IN_STRING: '\'' '"';
fragment STRING_CHAR: ~[\b\t\r\n\f'\\"] | SUP_ESC_SEQUENCE | DOUBLE_QUOTE_IN_STRING;

// integer
fragment HEXADECIMALDIGIT: [0-9A-F];
fragment OCTALDIGIT: [0-7];
fragment HEXADECIMAL: ('0x' | '0X') [1-9A-F]HEXADECIMALDIGIT*;
fragment DECIMAL: [0] | [1-9][0-9]*;

fragment OCTAL: ('0o' | '0O') [1-7] OCTALDIGIT*;

INT_LIT: DECIMAL 
                | HEXADECIMAL 
                | OCTAL;

FLOAT_LIT: FLOATING_POINT_NUM;

BOOL_LIT: TRUE | FALSE;

STRING_LIT: DOUBLE_QUOTE STRING_CHAR* DOUBLE_QUOTE
    {
        y = str(self.text)
        self.text = y[1:-1]
    };

// Keywords
BODY :     'Body';
BREAK:     'Break';
CONTINUE:  'Continue';
DO:        'Do';
ELSE:      'Else';
ELSEIF:    'ElseIf';
ENDIF:     'EndIf';
ENDBODY:   'EndBody';
ENDFOR:    'EndFor';
ENDWHILE:  'EndWhile';
FOR:       'For';
FUNCTION:  'Function';
IF:        'If';
PARAMETER: 'Parameter';
RETURN:    'Return';
THEN:      'Then';
VAR:       'Var';
WHILE:     'While';
TRUE:      'True';
FALSE:     'False';
ENDDO:     'EndDo';

// Operators
PLUS_INT:       '+';
PLUS_FLOAT:     '+.';
MINUS_INT:      '-';
MINUS_FLOAT:    '-.';
STAR_INT:       '*';
STAR_FLOAT:     '*.';
DIV_INT:        '\\';
DIV_FLOAT:      '\\.';
MOD:            '%';
NOT:            '!';
AND:            '&&';
OR:             '||';
EQUAL:          '==';
NOT_EQUAL_INT:  '!=';
LESS_INT:           '<';
GREATER_INT:        '>';
LESS_OR_EQUAL_INT:  '<=';
GREATER_OR_EQUAL_INT:'>=';
NOT_EQUAL_FLOAT:'=/=';
LESS_FLOAT:     '<.';
GREATER_FLOAT:  '>.';
LESS_OR_EQUAL_FLOAT: '<=.';
GREATER_OR_EQUAL_FLOAT: '>=.';

// Seperators
LEFT_PAREN:     '(';
RIGHT_PAREN:   ')';
LEFT_BRACKET:   '[';
RIGHT_BRACKET:  ']';
LEFT_BRACE:     '{';
RIGHT_BRACE:    '}';
COLON:          ':';
DOT:            '.';
SEMI:           ';';
COMMA:          ',';
ASSIGN:         '=';
DOUBLE_QUOTE:   '"';


// type corection function
// TYPE_CORR_FUNC: INT_OF_FLOAT
//                 | INT_OF_STRING
//                 | FLOAT_TO_INT
//                 | FLOAT_OF_STRING
//                 | BOOL_OF_STRING
//                 | STRING_OF_BOOL
//                 | STRING_OF_INT
//                 | STRING_OF_FLOAT
//                 ;
INT_OF_FLOAT: 'int_of_float';
INT_OF_STRING: 'int_of_string';
FLOAT_TO_INT: 'float_to_int';
FLOAT_OF_STRING: 'float_of_string';
BOOL_OF_STRING: 'bool_of_string';
STRING_OF_BOOL: 'string_of_bool';
STRING_OF_INT: 'string_of_int';
STRING_OF_FLOAT: 'string_of_float';

COMMENT: '**' .*? '**' -> skip;
WS: [ \t\f\r\n]+ -> skip;
ILLEGAL_ESCAPE: '"' STRING_CHAR* ILL_ESC_SEQUENCE
    {
        y = str(self.text)
        self.text = y[1:]
    };
UNCLOSE_STRING: '"' STRING_CHAR* ([\b\t\r\n\f] | EOF) 
    {
        y = str(self.text)
        self.text = y[1:]
    };
UNTERMINATED_COMMENT: '**' ('*'~'*' | ~'*')*? EOF;
ERROR_CHAR: .;
