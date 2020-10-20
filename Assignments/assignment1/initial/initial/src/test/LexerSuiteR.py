import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    def test_Illegal_E(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))
    
    def test_simple_array(self):
        self.assertTrue(TestLexer.checkLexeme("""{1, 2, 3, 4}""", """{,1,,,2,,,3,,,4,},<EOF>""", 108))

    def test_int(self):
        self.assertTrue(TestLexer.checkLexeme("""0123""", """0,123,<EOF>""", 109))

    def test_unterminated_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""**abvc""", """Unterminated Comment""", 110))
        
    def test_hexa_var_declare(self):
        input="""Var x=0x12;"""
        expect="""Var,x,=,0x12,;,<EOF>"""
        num=111
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_assign_stmt(self):
        input="""a=12+3;"""
        expect="""a,=,12,+,3,;,<EOF>"""
        num=112
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_function_name_declare(self):
        input="""Function: main"""
        expect="""Function,:,main,<EOF>"""
        num=113
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_dec_hex_same_array(self):
        input="""x={{12,0x12}}"""
        expect="""x,=,{,{,12,,,0x12,},},<EOF>"""
        num=114
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_normal_string(self):
        input="""\"this is a string\""""
        expect="""this is a string,<EOF>"""
        num=115
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))

    def test_Uncl_without_escape(self):
        input="""\"this is an Unclosed String:"""
        expect="""Unclosed String: this is an Unclosed String:"""
        num=116
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_legal_esc(self):
        input="""\" this is a string contain some legal esc: \\',\\b,\\t\""""
        expect=""" this is a string contain some legal esc: \\',\\b,\\t,<EOF>"""
        num=117
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_illegal_esc(self):
        input="""\" this is a string with illegal escape \\h\""""
        expect="""Illegal Escape In String:  this is a string with illegal escape \\h"""
        num=118
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_double_quote_in_string(self):
        input="""\"string with quote '"can be exp'"\""""
        expect="""string with quote '"can be exp'",<EOF>"""
        num=119
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_zero_started_float(self):
        input="""0e0"""
        expect="""0e0,<EOF>"""
        num=120
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_zero_started_2_float(self):
        input="""01e0"""
        expect="""01e0,<EOF>"""
        num=121
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_float_without_right_part(self):
        input="""12000."""
        expect="""12000.,<EOF>"""
        num=122
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_hexa_capital_num(self):
        input="""0xFF"""
        expect="""0xFF,<EOF>"""
        num=123
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_octal_capital(self):
        input="""0O456"""
        expect="""0O456,<EOF>"""
        num=124
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_zero(self):
        input="""0"""
        expect="""0,<EOF>"""
        num=125
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_zero_started_hexa(self):
        input="""0x"""
        expect="""0,x,<EOF>"""
        num=126
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))

    
    def test_comment_in_string_esc(self):
        input="""\"comment in /\\'\\\\string**\""""
        expect="""comment in /\\'\\\\string**,<EOF>"""
        num=127
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_multi_line_comment(self):
        input="""** this
is a
multiline*
comment**"""
        expect="""<EOF>"""
        num=128
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_ambigous_comment(self):
        input="""*****"""
        expect="""*,<EOF>"""
        num=129
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_not_sametype_array(self):
        input="""{"abc",12}"""
        expect="""{,abc,,,12,},<EOF>"""
        num=130
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_empty_string(self):
        input="""\"\""""
        expect=""",<EOF>"""
        num=131
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))
    def test_sing_quote_esc(self):
        input=""""str with sing quote\\'\""""
        expect="""str with sing quote\\',<EOF>"""
        num=132
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_back_slash_legal(self):
        input="""\"str with back slash \\\\ legal\""""
        expect="""str with back slash \\\\ legal,<EOF>"""
        num=133
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_back_slash_illegal(self):
        input="""\"str with back slash illegal \\\""""
        expect="""Illegal Escape In String: str with back slash illegal \\\""""
        num=134
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_multi_type_array(self):
        input="""{"abc",12,12.,True,{12,1e1}}"""
        expect="""{,abc,,,12,,,12.,,,True,,,{,12,,,1e1,},},<EOF>"""
        num=135
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_simple_expr(self):
        input="""a[1]=b+1.0"""
        expect="""a,[,1,],=,b,+,1.0,<EOF>"""
        num=136
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_complicated_composite_var(self):
        input="""a[b[1][3]]"""
        expect="""a,[,b,[,1,],[,3,],],<EOF>"""
        num=137
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_neg_scientific(self):
        input="""1200e-1"""
        expect="""1200e-1,<EOF>"""
        num=138
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_pos_scientific(self):
        input="""122e+1"""
        expect="""122e+1,<EOF>"""
        num=139
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_while_stmt_test(self):
        input="""While (i>1) Do EndWhile."""
        expect="""While,(,i,>,1,),Do,EndWhile,.,<EOF>"""
        num=140
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_logical_exp(self):
        input="""i && a"""
        expect="""i,&&,a,<EOF>"""
        num=141
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_relational_exp(self):
        input="""i =/= a"""
        expect="""i,=/=,a,<EOF>"""
        num=142
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_logical_or_exp(self):
        input="""i||a"""
        expect="""i,||,a,<EOF>"""
        num=143
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_logical_not_exp(self):
        input="""!a"""
        expect="""!,a,<EOF>"""
        num=144
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_relation_equal_exp(self):
        input="""i==a"""
        expect="""i,==,a,<EOF>"""
        num=145
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_not_equal_exp(self):
        input="""i!=a"""
        expect="""i,!=,a,<EOF>"""
        num=146
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_sing_compare_exp(self):
        input="""i>a"""
        expect="""i,>,a,<EOF>"""
        num=147
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_doub_compare_exp(self):
        input="""i>=a"""
        expect="""i,>=,a,<EOF>"""
        num=148
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_expr_in_index_expr(self):
        input="""a[1+foo(a)]"""
        expect="""a,[,1,+,foo,(,a,),],<EOF>"""
        num=149
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_mul_expr_in_func_call(self):
        input="""foo(a < i, a = a+ 1, b[1])"""
        expect="""foo,(,a,<,i,,,a,=,a,+,1,,,b,[,1,],),<EOF>"""
        num=150
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_mul_expr_in_assign(self):
        input="""a = a + foo(10) + b < 2"""
        expect="""a,=,a,+,foo,(,10,),+,b,<,2,<EOF>"""
        num=151
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_int_to_float_func(self):
        input="""int_of_float(1.02)"""
        expect="""int_of_float,(,1.02,),<EOF>"""
        num=152
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_float_to_int_func(self):
        input="""float_to_int(1.092)"""
        expect="""float_to_int,(,1.092,),<EOF>"""
        num=153
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_int_of_string_func(self):
        input="""int_of_string("12")"""
        expect="""int_of_string,(,12,),<EOF>"""
        num=154
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_string_of_int_func(self):
        input="""string_of_int(12)"""
        expect="""string_of_int,(,12,),<EOF>"""
        num=155
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_float_of_string_func(self):
        input="""float_of_string("12.45")"""
        expect="""float_of_string,(,12.45,),<EOF>"""
        num=156
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_func_call_in_func(self):
        input="""int_of_string(read())"""
        expect="""int_of_string,(,read,(,),),<EOF>"""
        num=157
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_multi_type_args(self):
        input="""function(12,"ab",foo(a[1]))"""
        expect="""function,(,12,,,ab,,,foo,(,a,[,1,],),),<EOF>"""
        num=158
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_array_with_blank(self):
        input="""array[1] = {1  , "asd", 22, a }"""
        expect="""array,[,1,],=,{,1,,,asd,,,22,,,a,},<EOF>"""
        num=159
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_unterminated_comment_in_string(self):
        input="""\"string **this is com\ment\""""
        expect="""Illegal Escape In String: string **this is com\\m"""
        num=160
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_Illebefore_comment(self):
        input="""\"string \**comment**\""""
        expect="""Illegal Escape In String: string \*"""
        num=161
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_comment_in_expr(self):
        input="""{**comment**}"""
        expect="""{,},<EOF>"""
        num=162
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_arithmetic_op_expr(self):
        input="""v = (4 \. 3.) *. 3.14 * a;"""
        expect="""v,=,(,4,\.,3.,),*.,3.14,*,a,;,<EOF>"""
        num=163
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_comment_in_string(self):
        input="""\"string **comment**\""""
        expect="""string **comment**,<EOF>"""
        num=164
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_recursive_func_call(self):
        input="""foo(foo(foo(foo(foo("abc")))))"""
        expect="""foo,(,foo,(,foo,(,foo,(,foo,(,abc,),),),),),<EOF>"""
        num=165
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_id_with_under(self):
        input="""a_b"""
        expect="""a_b,<EOF>"""
        num=166
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_wrong_char_in_id(self):
        input="""a$b"""
        expect="""a,Error Token $"""
        num=167
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_all_allow_type_in_id(self):
        input="""aB9_"""
        expect="""aB9_,<EOF>"""
        num=168
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_test_neg_num(self):
        input="""-12"""
        expect="""-,12,<EOF>"""
        num=169
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_khanh_str_test(self):
        input="""\" asdfasd \" adfads\""""
        expect=""" asdfasd ,adfads,Unclosed String: """
        num=170
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_newline_illegal(self):
        input="""\"this is
"""
        expect="""Unclosed String: this is\n"""
        num=171
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_zero_after_octal_prefix(self):
        input="""0o0001"""
        expect="""0,o0001,<EOF>"""
        num=172
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_octal_error_id_error(self):
        input="""0O012"""
        expect="""0,Error Token O"""
        num=173
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_err_hex_err_id(self):
        input="""0X012"""
        expect="""0,Error Token X"""
        num=174
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_comment_with_illegal_newline(self):
        input="""**this
\h
"shit"
**"""
        expect="""<EOF>"""
        num=175
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_neg_int_lit(self):
        input="""-12"""
        expect="""-,12,<EOF>"""
        num=176
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_neg_hex(self):
        input="""-0x12"""
        expect="""-,0x12,<EOF>"""
        num=177
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_comment_between_lit(self):
        input="""-12.**comment**1"""
        expect="""-,12.,1,<EOF>"""
        num=178
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_normal_float_non_scientific_not(self):
        input="""12.1"""
        expect="""12.1,<EOF>"""
        num=179
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test__zero_after_hex_prefix(self):
        input="""0x000"""
        expect="""0,x000,<EOF>"""
        num=180
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_bool_lit(self):
        input="""True False"""
        expect="""True,False,<EOF>"""
        num=181
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_test_all_legal_esc(self):
        input="""\"legal \\b\\t\\r\\n\\f\\\\\\' '\"\""""
        expect="""legal \\b\\t\\r\\n\\f\\\\\\' '",<EOF>"""
        num=182
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_bool_op(self):
        input="""!&&||"""
        expect="""!,&&,||,<EOF>"""
        num=183
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_int_op(self):
        input="""+-*\\\\% ==!=<><=>="""
        expect="""+,-,*,\\,\\%,==,!=,<,>,<=,>=,<EOF>"""
        num=184
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_float_op(self):
        input="""+.-.*.\\=/=<.>.<=.>=."""
        expect="""+.,-.,*.,\\,=/=,<.,>.,<=.,>=.,<EOF>"""
        num=185
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_lit_op_err_char(self):
        input="""[1+1.\\2]@#"""
        expect="""[,1,+,1.,\\,2,],Error Token @"""
        num=186
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_url_str(self):
        input="""\"http://e-learning.hcmut.edu.vn/course/view.php?id=66830\""""
        expect="""http://e-learning.hcmut.edu.vn/course/view.php?id=66830,<EOF>"""
        num=187
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_resolution_test(self):
        input="""this.a.b.c"""
        expect="""this,.,a,.,b,.,c,<EOF>"""
        num=188
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_illegal_id(self):
        input="""IllegalID"""
        expect="""Error Token I"""
        num=189
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_tab_in_str(self):
        input="""\"with tab\t\""""
        expect="""Unclosed String: with tab\t"""
        num=190
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_spec_composite(self):
        input="""{{{}}}"""
        expect="""{,{,{,},},},<EOF>"""
        num=191
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_composite_var_with_simple_expr(self):
        input="""a[-12][0O1]"""
        expect="""a,[,-,12,],[,0O1,],<EOF>"""
        num=192
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_unicode_char(self):
        input="""U+007F"""
        expect="""Error Token U"""
        num=193
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_more_sign_in_scientific(self):
        input="""12e+-1"""
        expect="""12,e,+,-,1,<EOF>"""
        num=194
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_zero_e_zero(self):
        input="""000e000"""
        expect="""000e000,<EOF>"""
        num=195
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_neg_scientific_float(self):
        input="""12.0e-01"""
        expect="""12.0e-01,<EOF>"""
        num=196
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_sequence_e(self):
        input="""12000e-12-ex"""
        expect="""12000e-12,-,ex,<EOF>"""
        num=197
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_ambigous_e(self):
        input="""12e12e12.e1233e.e.e12"""
        expect="""12e12,e12,.,e1233e,.,e,.,e12,<EOF>"""
        num=198
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_ambigous_hex_oct(self):
        input="""-120x10o1o0xox012o0x12o30x1o3x012"""
        expect="""-,120,x10o1o0xox012o0x12o30x1o3x012,<EOF>"""
        num=199
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))


    def test_ambigous_float_int(self):
        input="""12eX0e123e210x120o12E+12e-1231"""
        expect="""12,eX0e123e210x120o12E,+,12e-1231,<EOF>"""
        num=200
        self.assertTrue(TestLexer.checkLexeme(input, expect, num))

