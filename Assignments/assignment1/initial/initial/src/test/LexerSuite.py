import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_identifier_1(self):
        """ Test idedntifier """
        self.assertTrue(TestLexer.checkLexeme("khanh","khanh,<EOF>",101))
    def test_identifier_2(self):
        self.assertTrue(TestLexer.checkLexeme("answ__ersd hsncq12","answ__ersd,hsncq12,<EOF>",102))
    def test_identifier_3(self):
        self.assertTrue(TestLexer.checkLexeme("nguyen_dinh_khanh HCMUT","nguyen_dinh_khanh,Error Token H",103))
    def test_identifier_4(self):
        self.assertTrue(TestLexer.checkLexeme("a__If_Else","a__If_Else,<EOF>",104))
    def test_identifier_5(self):
        self.assertTrue(TestLexer.checkLexeme("_notID","Error Token _",105))
    def test_identifier_6(self):
        self.assertTrue(TestLexer.checkLexeme("av3ng3r g0","av3ng3r,g0,<EOF>",106))
    def test_identifier_7(self):
        self.assertTrue(TestLexer.checkLexeme("trueFalseThenIf","trueFalseThenIf,<EOF>",107))
    def test_identifier_8(self):
        self.assertTrue(TestLexer.checkLexeme("var____If_____Then__","var____If_____Then__,<EOF>",108))
  

    def test_keyword_1(self):
        """ Test keyword """
        self.assertTrue(TestLexer.checkLexeme("Var Function Do","Var,Function,Do,<EOF>",109))
    def test_keyword_2(self):
        self.assertTrue(TestLexer.checkLexeme("VarFunctionDoWhileIfElseElseIf","Var,Function,Do,While,If,Else,ElseIf,<EOF>",110))
    def test_keyword_3(self):
        self.assertTrue(TestLexer.checkLexeme("Var\nVar\ForFor\\EndIfIf","Var,Var,\,For,For,\\,EndIf,If,<EOF>",111))
    def test_keyword_4(self):
        self.assertTrue(TestLexer.checkLexeme("ElseIfIfElseDoEndEndWhileWhile","ElseIf,If,Else,Do,Error Token E",112))

    def test_comment_1(self):
        """ Test comment"""
        self.assertTrue(TestLexer.checkLexeme("""** This is a single-line comment** Var""","Var,<EOF>",113))
    def test_comment_2(self):
        self.assertTrue(TestLexer.checkLexeme("** This @!#%^&^is a \n multi-line~><>: \n comment ><\\{}.**For","For,<EOF>",114))
    def test_comment_3(self):
        self.assertTrue(TestLexer.checkLexeme("*****","*,<EOF>",115))
    def test_comment_4(self):
        self.assertTrue(TestLexer.checkLexeme("** * **","<EOF>",116))
    def test_comment_5(self):
        self.assertTrue(TestLexer.checkLexeme("**** * ***","*,Unterminated Comment",117))
    def test_comment_6(self):
        self.assertTrue(TestLexer.checkLexeme("""** This is a
                                                 * multi-line
                                                 * comment.
                                                 * /-\/-\
                                                  ( > . <)
                                                  (,,)(,,)
                                                 **""","<EOF>",118))
    def test_comment_7(self):
        self.assertTrue(TestLexer.checkLexeme("***** *sample*","*,*,sample,*,<EOF>",119))
    def test_comment_8(self):
        self.assertTrue(TestLexer.checkLexeme("""** Multi_+\*line %^&%!\n Com==ment ****"('"'")"**zzz ""","zzz,<EOF>",120))

    def test_operator_1(self):
        """ Test operators """
        self.assertTrue(TestLexer.checkLexeme("+-Var*%ab\.","+,-,Var,*,%,ab,\.,<EOF>",121))
    def test_operator_2(self):  
        self.assertTrue(TestLexer.checkLexeme("+ - * \\ *. = =/= < = <= <=.","+,-,*,\,*.,=,=/=,<,=,<=,<=.,<EOF>",122))
    def test_operator_3(self):
        self.assertTrue(TestLexer.checkLexeme("!||&&=+==+-*+.","!,||,&&,=,+,==,+,-,*,+.,<EOF>",123))
    def test_operator_4(self):
        self.assertTrue(TestLexer.checkLexeme("23!=21+===+.\\.12..\\=/=123%&&*21==||1%","23,!=,21,+,==,=,+.,\.,12.,.,\,=/=,123,%,&&,*,21,==,||,1,%,<EOF>",124))
    def test_operator_5(self):
        self.assertTrue(TestLexer.checkLexeme("+ - * =/= := <= >= <> = < >( ) [ ] ; , : , ..","+,-,*,=/=,:,=,<=,>=,<,>,=,<,>,(,),[,],;,,,:,,,.,.,<EOF>",125))
    def test_operator_6(self):
        self.assertTrue(TestLexer.checkLexeme("as=/=+==..=/.=","as,=/=,+,==,.,.,=,Error Token /",126))


    def test_separator_1(self):
        """ Test separators"""
        self.assertTrue(TestLexer.checkLexeme("{{{{}.]1:;","{,{,{,{,},.,],1,:,;,<EOF>",127))
    def test_separator_2(self):
        self.assertTrue(TestLexer.checkLexeme("a[a{{13},5}+1]:;","a,[,a,{,{,13,},,,5,},+,1,],:,;,<EOF>",128))
    def test_separator_3(self):
        self.assertTrue(TestLexer.checkLexeme(".[])){'""'1728397.[)}}""\\.",".,[,],),),{,Error Token '",129))


    def test_integer_1(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("012320","0,12320,<EOF>",130))
    def test_integer_2(self):
        self.assertTrue(TestLexer.checkLexeme("0x1132 0XF9A0 ","0x1132,0XF9A0,<EOF>",131))
    def test_integer_3(self):
        self.assertTrue(TestLexer.checkLexeme("0o1391 0O1123","0o13,91,0O1123,<EOF>",132))
    def test_integer_4(self):
        self.assertTrue(TestLexer.checkLexeme("0000X12031ABC","0,0,0,0X12031ABC,<EOF>",133))
    def test_integer_5(self):
        self.assertTrue(TestLexer.checkLexeme("0x0112ABC","0,x0112ABC,<EOF>",134))
    def test_integer_6(self):
        self.assertTrue(TestLexer.checkLexeme("0xabc123 0XABC123","0,xabc123,0XABC123,<EOF>",135))       
    def test_integer_7(self):
        self.assertTrue(TestLexer.checkLexeme("0x00123ABCd 0X00123ABCd","0,x00123ABCd,0,Error Token X",136))
    def test_integer_8(self):
        self.assertTrue(TestLexer.checkLexeme("0o7631 0O012","0o7631,0,Error Token O",137))
    def test_integer_9(self):
        self.assertTrue(TestLexer.checkLexeme("0o123412ack","0o123412,ack,<EOF>",138))
    def test_integer_10(self):
        self.assertTrue(TestLexer.checkLexeme("0o1230o123 0O1230O123","0o1230,o123,0O1230,Error Token O",139))
    def test_integer_11(self):
        self.assertTrue(TestLexer.checkLexeme("-1233 +13289 --0x112FD","-,1233,+,13289,-,-,0x112FD,<EOF>",140))

    def test_float_1(self):
        """ Test floats """
        self.assertTrue(TestLexer.checkLexeme("12.12231 100.","12.12231,100.,<EOF>",141))
    def test_float_2(self):
        self.assertTrue(TestLexer.checkLexeme("112e322 112E332 112e-332 112e+332  112E-332  112e+332","112e322,112E332,112e-332,112e+332,112E-332,112e+332,<EOF>",142))
    def test_float_3(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e3 12.0E3 12.0e-3 12.0e+3 12.0E-3","12.0e3,12.0E3,12.0e-3,12.0e+3,12.0E-3,<EOF>",143))
    def test_float_4(self):
        self.assertTrue(TestLexer.checkLexeme("00.00000000005", "00.00000000005,<EOF>",144))
    def test_float_5(self):
        self.assertTrue(TestLexer.checkLexeme(".1231",".,1231,<EOF>",145))
    def test_float_6(self):
        self.assertTrue(TestLexer.checkLexeme(".22380e3",".,22380e3,<EOF>",146))
    def test_float_7(self):
        self.assertTrue(TestLexer.checkLexeme("60.0.0e6","60.0,.,0e6,<EOF>",147))
    def test_float_8(self):
        self.assertTrue(TestLexer.checkLexeme("0.e4 .5 013e22.32 50.e+9 ","0.e4,.,5,013e22,.,32,50.e+9,<EOF>",148))
    def test_float_9(self):
        self.assertTrue(TestLexer.checkLexeme("-0.E-12 02.e-06  12E+4 0.E322","-,0.E-12,02.e-06,12E+4,0.E322,<EOF>",149))
    def test_float_10(self):
        self.assertTrue(TestLexer.checkLexeme("000. 000.00  0E-00","000.,000.00,0E-00,<EOF>",150))

    def test_boolean_1(self):
        """ Test Bool """
        self.assertTrue(TestLexer.checkLexeme("a<True++False","a,<,True,+,+,False,<EOF>",151))   
    def test_boolean_2(self):
        self.assertTrue(TestLexer.checkLexeme("TrueTrueFalseFalseTRue","True,True,False,False,Error Token T",152))

    def test_string_1(self):
        """ Test String """
        self.assertTrue(TestLexer.checkLexeme(""" "This is a normal string" ""","""This is a normal string,<EOF>""",153))
    def test_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me: '"Where is John?'"" ""","""He asked me: '"Where is John?'",<EOF>""",154))
    def test_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This string contain tab \t"  ""","""This string contain tab \t,<EOF>""",155))
    def test_string_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Some  escape sequences: \\b\\f\\n\\t"     ""","""Some  escape sequences: \\b\\f\\n\\t,<EOF>""",156))
    def test_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "'"'"koro'"y\\'"!=!!"T"  ""","""'"'"koro'"y\\',!=,!,!,T,<EOF>""",157))
    def test_string_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\b \\f 1810992 \\r \\n \\t \\\' \\\\"  ""","""\\b \\f 1810992 \\r \\n \\t \\\' \\\\,<EOF>""",158))  
    def test_string_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "??IO!@#$%^&*()[]{}||//><"  ""","""??IO!@#$%^&*()[]{}||//><,<EOF>""",159))
    def test_string_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "VungTau,VietNam\\t03:**;43 UTC"  ""","""VungTau,VietNam\\t03:**;43 UTC,<EOF>""",160))
    def test_string_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ElseIfIfElseDoEndEndWhileWhile"  ""","""ElseIfIfElseDoEndEndWhileWhile,<EOF>""",161))
    def test_string_10(self):
        self.assertTrue(TestLexer.checkLexeme(""" "+ - * =/= := <= >= <> = < >( ) [ ] ; , : , .."  ""","""+ - * =/= := <= >= <> = < >( ) [ ] ; , : , ..,<EOF>""",162))
    def test_string_11(self):
        self.assertTrue(TestLexer.checkLexeme(""" "**how about a comment in a string**" ""","""**how about a comment in a string**,<EOF>""",163))
    def test_string_12(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" """,""",<EOF>""",164))
    def test_string_13(self):
        self.assertTrue(TestLexer.checkLexeme(""" "c,o,n"f    "u""s"  e ""","""c,o,n,f,u,s,e,<EOF>""",165))
   
    def test_illegal_escape(self):
        """ Test Illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "string contain a simple illegal escape\\d here"  ""","""Illegal Escape In String: string contain a simple illegal escape\\d""",166))
    def test_illegal_escape_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "another\\"  ""","""Illegal Escape In String: another\\\"""",167))
    def test_illegal_escape_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "single quote\'in a String"  ""","""Illegal Escape In String: single quote\'i""",168))
    def test_illegal_escape_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "some special char: !@!#$%%\\^qwqerty"  ""","""Illegal Escape In String: some special char: !@!#$%%\\^""",169))
    def test_illegal_escape_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "normal string" "illegal escape\\# here" ""","""normal string,Illegal Escape In String: illegal escape\\#""",170))
    def test_illegal_escape_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "illegal escape\\@ here" "normal string" ""","""Illegal Escape In String: illegal escape\\@""",171))
 
    
    def test_unterminated_string_1(self):
        """ Test Unterminated String """
        self.assertTrue(TestLexer.checkLexeme(""" "Ooopppss  ""","""Unclosed String: Ooopppss  """,172))
    def test_unterminated_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "n0M@l St1n@"but"uNCl0s3 ""","""n0M@l St1n@,but,Unclosed String: uNCl0s3 """,173))
    def test_unterminated_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "howabout\nendline" ""","""Unclosed String: howabout""",174))
    def test_unterminated_string_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "A quote in string '" ""","""Unclosed String: A quote in string '" """,175))
    def test_unterminated_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Some escape sequences: \\b\\f\\n\\t ""","""Unclosed String: Some escape sequences: \\b\\f\\n\\t """,176))
    def test_unterminated_string_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "                       ""","""Unclosed String:                        """,177))
    def test_unterminated_string_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "nomal string"3mpty" ""","""nomal string,3,mpty,Unclosed String:  """,178))
    def test_unterminated_string_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Unclose first\n "nomal string" ""","""Unclosed String: Unclose first""",179))
    def test_unterminated_string_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "but this is not unclose \" ""","""but this is not unclose ,<EOF>""",180))


    def test_unterminated_comment_1(self):
        """ Test Unterminated Comment """
        self.assertTrue(TestLexer.checkLexeme("""** Oops ""","""Unterminated Comment""",181))
    def test_unterminated_comment_2(self):
        self.assertTrue(TestLexer.checkLexeme("""** 2xOops * ""","""Unterminated Comment""",182))
    def test_unterminated_comment_3(self):
        self.assertTrue(TestLexer.checkLexeme("""******""","""Unterminated Comment""",183))
    def test_unterminated_comment_4(self):
        self.assertTrue(TestLexer.checkLexeme("""** *** **""","""*,Unterminated Comment""",184))
    def test_unterminated_comment_5(self):
        self.assertTrue(TestLexer.checkLexeme("""** ***** **""","""<EOF>""",185))
    def test_unterminated_comment_6(self):
        self.assertTrue(TestLexer.checkLexeme("""** This is a
                                                 * multi-line
                                                 * comment.
                                                 *""","""Unterminated Comment""",186))
    def test_unterminated_comment_7(self):
        self.assertTrue(TestLexer.checkLexeme("""sometoken**comment""","""sometoken,Unterminated Comment""",187))


    def test_error_token_1(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme("some?thing","some,Error Token ?",188))
    def test_error_token_2(self):
        self.assertTrue(TestLexer.checkLexeme("someescape\naa","someescape,aa,<EOF>",189))
    def test_error_token_3(self):
        self.assertTrue(TestLexer.checkLexeme("<>!=!=\==&=","<,>,!=,!=,\,==,Error Token &",190))
    def test_wrong_token_4(self):
        self.assertTrue(TestLexer.checkLexeme("\\\\[]\\///\/\/\ ","\,\,[,],\,Error Token /",191))
    def test_wrong_token_5(self):
        self.assertTrue(TestLexer.checkLexeme("=====/==/=/==/","==,==,=/=,=/=,Error Token /",192))
    def test_wrong_token_6(self):
        self.assertTrue(TestLexer.checkLexeme(" \"sqjwk\'\" \"\"\"\'","sqjwk\'\" ,,Error Token '",193))
    
    def test_general_1(self):
        """ General Test """
        self.assertTrue(TestLexer.checkLexeme("var[1+func(a)]","var,[,1,+,func,(,a,),],<EOF>",194))
    def test_general_2(self):
        self.assertTrue(TestLexer.checkLexeme("For (i = 1, i < n, 1) Do","For,(,i,=,1,,,i,<,n,,,1,),Do,<EOF>",195))
    def test_general_3(self):
        self.assertTrue(TestLexer.checkLexeme("Var: i, arr[100][100];","Var,:,i,,,arr,[,100,],[,100,],;,<EOF>",196))
    def test_general_4(self):
        self.assertTrue(TestLexer.checkLexeme("arr[1][\"ddas\"] + 4 = **ad +cc** 2" ,"arr,[,1,],[,ddas,],+,4,=,2,<EOF>",197))
    def test_general_5(self):
        self.assertTrue(TestLexer.checkLexeme("If (i == 10) Then write(\"OK\");" ,"If,(,i,==,10,),Then,write,(,OK,),;,<EOF>",198))
    def test_general_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" foo(True, "!@$C#hc%", 12. \\. 921.9e5 * 32e1);""" ,"foo,(,True,,,!@$C#hc%,,,12.,\.,921.9e5,*,32e1,),;,<EOF>",199))
    def test_general_7(self):
        self.assertTrue(TestLexer.checkLexeme("s =  !s || !(s ==2) && (t >=. 5432.) && t =/= t*.2;" ,"s,=,!,s,||,!,(,s,==,2,),&&,(,t,>=.,5432.,),&&,t,=/=,t,*.,2,;,<EOF>",200))
    


