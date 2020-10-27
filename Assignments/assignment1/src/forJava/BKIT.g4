//1810700
grammar BKIT;

options{
	// language=Python3;
    language=Java;
}

program: (var_declare SEMI)* function_declare* EOF;

// 1. program structure

var_declare: VAR COLON
            var_list;

// main_function_declare: FUNCTION COLON 'main'
//                     (PARAMETER COLON params_list)?
//                     BODY COLON
//                     stmt_list
//                     ENDBODY DOT;

function_declare: FUNCTION COLON ID
                    (PARAMETER COLON params_list)?
                    BODY COLON
                    (var_declare_stmt SEMI)* stmt*
                    ENDBODY DOT;

array: ID ASSIGN array_lit;

// 4. Datatypes and 
primitive_data: INT_LIT | FLOAT_LIT | STRING_LIT | BOOL_LIT;
composite_data: array_lit;

// array_lit: LEFT_BRACE (
//                 array_lit (COMMA array_lit)*
//                 | int_array
//                 | float_array
//                 | string_array
//                 ) 
//             RIGHT_BRACE;
array_lit: LEFT_BRACE (primitive_data | composite_data) (COMMA (primitive_data | composite_data))* RIGHT_BRACE;
// int_array: (INT_LIT | ID) (COMMA (INT_LIT | ID))*;
// float_array: (FLOAT_LIT | ID) (COMMA (FLOAT_LIT | ID))*;
// string_array: (STRING_LIT | ID) (COMMA (STRING_LIT | ID))*;
// var declare

// var declare
var_list: (var_non_init | var_init) (COMMA (var_non_init | var_init))*; //non empty
scalar_var: ID;
var_non_init: ID (LEFT_BRACKET INT_LIT RIGHT_BRACKET)+ | ID;
composite_var: ID (LEFT_BRACKET (composite_var | INT_LIT) RIGHT_BRACKET)+;
// var_init: composite_init | primitive_init;
var_init: (composite_var | scalar_var) ASSIGN (composite_data | primitive_data);
composite_init: composite_var ASSIGN array_lit;
primitive_init: scalar_var ASSIGN primitive_data;

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
assign_stmt: var_non_init ASSIGN (expr);
break_stmt: BREAK;
continue_stmt: CONTINUE;
call_stmt: function_call ;
return_stmt: RETURN expr?;

// 5.1 stmt utils
init_for: scalar_var ASSIGN expr;
con_for: expr;
update_for: expr;
// 6. expr_utils
expr: expr1 (EQUAL
            | NOT_EQUAL_INT
            | LESS_INT
            | GREATER_INT
            | LESS_OR_EQUAL_INT
            | GREATER_OR_EQUAL_INT 
            | NOT_EQUAL_FLOAT
            | LESS_FLOAT
            | GREATER_FLOAT
            | LESS_OR_EQUAL_FLOAT
            | GREATER_OR_EQUAL_FLOAT) expr1 | expr1;
        
expr1: expr1 (AND | OR) expr2 | expr2;
expr2: expr2 (PLUS_FLOAT | PLUS_INT | MINUS_FLOAT | MINUS_INT) expr3 | expr3;
expr3: expr3 (STAR_INT | STAR_INT | DIV_FLOAT |  DIV_INT | MOD) expr4 | expr4;
expr4: NOT expr4 | expr5;
expr5: (MINUS_FLOAT | MINUS_INT) expr5 | expr6;
expr6: expr7 index_op | expr7;
expr7: function_call | expr8;
expr8: operand | LEFT_PAREN expr RIGHT_PAREN;
operand: var_non_init | primitive_data | composite_data;
// expr: int_expr1 | float_expr1 | string_expr | boolean_expr;

// boolean_type_expr: (int_expr1 (EQUAL
//                                 | NOT_EQUAL_INT
//                                 | LESS_INT
//                                 | GREATER_INT
//                                 | LESS_OR_EQUAL_INT
//                                 | GREATER_OR_EQUAL_INT ) int_expr1)
//             | (float_expr1 (
//                                 | NOT_EQUAL_FLOAT
//                                 | LESS_FLOAT
//                                 | GREATER_FLOAT
//                                 | LESS_OR_EQUAL_FLOAT
//                                 | GREATER_OR_EQUAL_FLOAT ) float_expr1
//             )
//             ;
// int_expr1: int_expr1 (PLUS_INT | MINUS_INT) int_expr2 | int_expr2;
// int_expr2: int_expr2 (STAR_INT | DIV_INT | MOD) int_expr3 | int_expr3;
// int_expr3: (MINUS_INT) int_expr3 | int_expr4;
// int_expr4: int_expr5 index_op | int_expr5;
// int_expr5: int_func_call | int_expr6;
// int_expr6: int_operand | LEFT_PAREN int_expr1 RIGHT_PAREN;
// int_operand: INT_LIT | scalar_var
//             | INT_OF_FLOAT LEFT_PAREN float_expr1 RIGHT_PAREN
//             | INT_OF_STRING LEFT_PAREN STRING_LIT RIGHT_PAREN;


// float_expr1: float_expr1 (PLUS_FLOAT | MINUS_FLOAT) float_expr2 | float_expr2;
// float_expr2: float_expr2 (STAR_FLOAT | DIV_FLOAT) float_expr3 | float_expr3;
// float_expr3: (MINUS_FLOAT) float_expr3 | float_expr4;
// float_expr4: float_expr5 index_op | float_expr5;
// float_expr5: float_func_call | float_expr6;
// float_expr6: float_operand | LEFT_PAREN float_expr1 RIGHT_PAREN;
// float_operand: FLOAT_LIT | scalar_var
//             | FLOAT_TO_INT LEFT_PAREN int_expr1 RIGHT_PAREN
//             | FLOAT_OF_STRING LEFT_PAREN string_expr RIGHT_PAREN;

// constant: INT_LIT | FLOAT_LIT;

// boolean_expr: boolean_expr (AND | OR) boolean_expr1 | boolean_expr1 | boolean_type_expr;
// boolean_expr1: NOT boolean_expr1 | boolean_expr2;
// boolean_expr2: boolean_expr3 index_op | boolean_expr3;
// boolean_expr3: boolean_func_call | boolean_expr4;
// boolean_expr4: boolean_operand | LEFT_PAREN boolean_expr RIGHT_PAREN;
// boolean_operand: BOOL_LIT |scalar_var
//                 | BOOL_OF_STRING LEFT_PAREN string_expr RIGHT_PAREN
//                 ;

// string_expr: ID | STRING_LIT | string_func_call;

function_call: ID LEFT_PAREN (expr (COMMA expr)*)* RIGHT_PAREN;
// int_func_call: ID LEFT_PAREN (expr (COMMA expr)*)* RIGHT_PAREN;
// float_func_call: ID LEFT_PAREN (expr (COMMA expr)*)* RIGHT_PAREN;
// boolean_func_call: ID LEFT_PAREN (expr (COMMA expr)*)* RIGHT_PAREN;
// string_func_call: ID LEFT_PAREN (expr (COMMA expr)*)* RIGHT_PAREN;

index_op: LEFT_BRACKET expr RIGHT_BRACKET | LEFT_BRACKET expr RIGHT_BRACKET index_op;

ID: LOWERCASE_LETTER (LOWERCASE_LETTER | DIGIT | UPPERCASE_LETTER | '_')*; // must begin with lowercase, case-sensitive



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
fragment HEXADECIMALDIGIT: [0-9a-fA-F];
fragment OCTALDIGIT: [0-7];
fragment HEXADECIMAL: ('0x' | '0X') [1-9a-fA-F]HEXADECIMALDIGIT*;
fragment DECIMAL: [0] | [1-9][0-9]*;

fragment OCTAL: ('0o' | '0O') [1-7] OCTALDIGIT*;

INT_LIT: DECIMAL 
                | HEXADECIMAL 
                | OCTAL;

FLOAT_LIT: FLOATING_POINT_NUM;

BOOL_LIT: TRUE | FALSE;

STRING_LIT: DOUBLE_QUOTE STRING_CHAR* DOUBLE_QUOTE
    {

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
MOD:            '\\%';
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

    };
UNCLOSE_STRING: '"' STRING_CHAR* ([\b\t\r\n\f] | EOF) 
    {
    };
UNTERMINATED_COMMENT: '**' ('*'~'*' | ~'*')*? EOF;
ERROR_CHAR: .;
