import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    # def test_lower_identifier(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    # def test_wrong_token(self):
    #     self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    # def test_illegal_escape(self):
    #     """test illegal escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    # def test_unterminated_string(self):
    #     """test unclosed string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    # def test_normal_string_with_escape(self):
    #     """test normal string with escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc\\n def"  ""","""abc\\n def,<EOF>""",107))

    # def test_normal_string(self):
    #     self.assertTrue(TestLexer.checkLexeme("a$b", """khanh,<EOF>""",108))

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

    def test_float1(self):
        """ Test floats """
        self.assertTrue(TestLexer.checkLexeme("12.12231 100.","12.12231,100.,<EOF>",141))
    def test_float2(self):
        self.assertTrue(TestLexer.checkLexeme("112e322 112E332 112e-332 112e+332  112E-332  112e+332","112e322,112E332,112e-332,112e+332,112E-332,112e+332,<EOF>",142))
    def test_float3(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e3 12.0E3 12.0e-3 12.0e+3 12.0E-3","12.0e3,12.0E3,12.0e-3,12.0e+3,12.0E-3,<EOF>",143))
    def test_float4(self):
        self.assertTrue(TestLexer.checkLexeme("00.00000000005", "00.00000000005,<EOF>",144))
    def test_float5(self):
        self.assertTrue(TestLexer.checkLexeme(".1231",".1231,<EOF>",145))
    def test_float6(self):
        self.assertTrue(TestLexer.checkLexeme(".22380e3",".,22380e3,<EOF>",146))
    def test_float7(self):
        self.assertTrue(TestLexer.checkLexeme("0e05 0x00.12e5 100e-10","0e05,0,x00,.,12e5,100e-10,<EOF>",156))
    def test_float8(self):
        self.assertTrue(TestLexer.checkLexeme(".e5 .5 01e2.32 50.e+9 ",".,e5,.,5,01e2,.,32,50.e+9,<EOF>",157))
    def test_float9(self):
        self.assertTrue(TestLexer.checkLexeme("-0.e21 02.e-10  121E+4 0.E09 4060E12","-,0.e21,02.e-10,121E+4,0.E09,4060E12,<EOF>",158))
    def test_float11(self):
        self.assertTrue(TestLexer.checkLexeme("12.E-1 0.E+9 12E2e-2 0e0 0E+0 0E-0","12.E-1,0.E+9,12E2,e,-,2,0e0,0E+0,0E-0,<EOF>",159))
    def test_float12(self):
        self.assertTrue(TestLexer.checkLexeme("0.0E-12 -9.0E12 212E-292+921E2","0.0E-12,-,9.0E12,212E-292,+,921E2,<EOF>",160))
    def test_float13(self):
        self.assertTrue(TestLexer.checkLexeme("144.40055 126.711561 101.395564 25.154157 200.83841 205.313014","144.40055,126.711561,101.395564,25.154157,200.83841,205.313014,<EOF>",161))

    def test_boolean1(self):
        self.assertTrue(TestLexer.checkLexeme("a == True || False","a,==,True,||,False,<EOF>",162))   
    def test_boolean2(self):
        self.assertTrue(TestLexer.checkLexeme("TrueFalseTrueTrueFalseFalseTrueFalse","True,False,True,True,False,False,True,False,<EOF>",163))

    def test_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \\t" ""","""This is a string containing tab \\t,<EOF>""",164))
    def test_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me: '"Where is John?'"" ""","""He asked me: '"Where is John?'",<EOF>""",165))
    def test_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ab\\\\'"c\\n def"  ""","""ab\\\\'"c\\n def,<EOF>""",166))
    def test_string4(self):
        self.assertTrue(TestLexer.checkLexeme("""\"\"\"hello\"\"\"\"""",""",hello,,Unclosed String: """,167))
    def test_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "'"'"ab'"c\\'"!=!!"?"  ""","""'"'"ab'"c\\',!=,!,!,?,<EOF>""",168))
    def test_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\b \\f time \\r \\n \\t \\\' \\\\"  ""","""\\b \\f time \\r \\n \\t \\\' \\\\,<EOF>""",169))  
    def test_string7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "~!@#$%^&*()_+{}?.,.<>|"  ""","""~!@#$%^&*()_+{}?.,.<>|,<EOF>""",170))
    def test_string8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "7I66sTfdiygoAChWx81o\\n04:47:43 UTC"  ""","""7I66sTfdiygoAChWx81o\\n04:47:43 UTC,<EOF>""",171))
    def test_string9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "G17>TY/??PNB/48PBx@fR/e0z Var: x=foo(2)"  ""","""G17>TY/??PNB/48PBx@fR/e0z Var: x=foo(2),<EOF>""",172))
    def test_string10(self):
        self.assertTrue(TestLexer.checkLexeme(""" "https://www.facebook.com/cal=a[2]*3+9/.ar[1][12]"  ""","""https://www.facebook.com/cal=a[2]*3+9/.ar[1][12],<EOF>""",173))
    def test_string11(self):
        self.assertTrue(TestLexer.checkLexeme(""" "**this is a single-line comment**" ""","""**this is a single-line comment**,<EOF>""",174))
    def test_string12(self):
        self.assertTrue(TestLexer.checkLexeme(""" "{string, 12, 12412}, 01292.0e0000}" ""","""{string, 12, 12412}, 01292.0e0000},<EOF>""",175))
    def test_string13(self):
        self.assertTrue(TestLexer.checkLexeme(""" "C6!2xR0X Q/S" "HA%s#sNa^Bj&" "LastName varchar(255)" ""","""C6!2xR0X Q/S,HA%s#sNa^Bj&,LastName varchar(255),<EOF>""",176))
    def test_string14(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Lexical Structure" "copyright\'\"2007-2014'"-'"Dai hoc\'\" \'\"Bach Khoa\'\" Tp.HCM" ""","""Lexical Structure,copyright'"2007-2014'"-'"Dai hoc'" '"Bach Khoa'" Tp.HCM,<EOF>""",177))

    def test_illegal_escape1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",178))
    def test_illegal_escape2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\"  ""","""Illegal Escape In String: abc\\\"""",179))
    def test_illegal_escape3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "thisIs\'aString"  ""","""Illegal Escape In String: thisIs\'a""",180))
    def test_illegal_escape4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "!@!#$%%\\^qwqerty"  ""","""Illegal Escape In String: !@!#$%%\\^""",181))
    def test_illegal_escape5(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"^HX7 v/Eu!dK\" \"!nKgOt4Ilpnm\\$\" "AFC7c&b/0tK#" ""","""^HX7 v/Eu!dK,Illegal Escape In String: !nKgOt4Ilpnm\\$""",182))
    def test_illegal_escape6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "D:\\Works_HK5_PPL_assignment1_src\test\testcases" ""","""Illegal Escape In String: D:\W""",183))
    def test_illegal_escape7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "#justatee\\#tlinh\\#mck\\#lien" "#LOST #Obito #DefJamRecordingsVietNam" ""","""Illegal Escape In String: #justatee\\#""",184))
    
    def test_unterminated_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,185))
    def test_unterminated_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc@?~12"thisIs"x ""","""abc@?~12,thisIs,Unclosed String: x """,186))
    def test_unterminated_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "dna def\nZSEQWQSA" ""","""Unclosed String: dna def\n""",187))
    def test_unterminated_string4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "~!#\\b\\f@#Tstring'\"""","""Unclosed String: ~!#\\b\\f@#Tstring'\"""",188))
    def test_unterminated_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"an.sytung@hcmut.edu.vn\"\\n \"October\" \\f \"2020""","""an.sytung@hcmut.edu.vn,\,n,October,\,f,Unclosed String: 2020""",189))
    def test_unterminated_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Top_trending_gggg124!@\\n" "value '"non-zero'"" "Sunday, 10 October 2048, 7:21:21'PM" "" "" ""","""Top_trending_gggg124!@\\n,value '"non-zero'",Illegal Escape In String: Sunday, 10 October 2048, 7:21:21'P""",190))
    
    def test_unterminated_comment1(self):
        self.assertTrue(TestLexer.checkLexeme("""**{21.e-1, {23e2}, {{12.e+2, 0e8}},2*3-1*""","""Unterminated Comment""",191))
    def test_unterminated_comment2(self):
        self.assertTrue(TestLexer.checkLexeme("""**"skip'"Ne"****@@@@@!@!@@!134112""","""Unterminated Comment""",192))
    def test_unterminated_comment3(self):
        self.assertTrue(TestLexer.checkLexeme("""**x*3+2*.2.Var: ASCII-FF""","""Unterminated Comment""",193))

    def test_array1(self):
        self.assertTrue(TestLexer.checkLexeme("""{1, 5, 7, 12}""","""{,1,,,5,,,7,,,12,},<EOF>""",194))
    # def test_array2(self):
    #     self.assertTrue(TestLexer.checkLexeme("""{{1, 2}, {4, 5}, {3, 5}}""","""{{1, 2}, {4, 5}, {3, 5}},<EOF>""",129))
    # def test_array3(self):
    #     self.assertTrue(TestLexer.checkLexeme("""{{1, 2}, {4, 5}, {3, 5}}""","""{{1, 2}, {4, 5}, {3, 5}},<EOF>""",129))
    # def test_array4(self):
    #     self.assertTrue(TestLexer.checkLexeme("""{"abc","def","ghj"}""","""{"abc","def","ghj"},<EOF>""",129))
    # def test_array5(self):
    #     self.assertTrue(TestLexer.checkLexeme("""{{"kitucc", "dyonla", "hjhj"}, "$~#?hcyaknc!@@!!$", {"tneghj"}}""","""{{"kitucc", "dyonla", "hjhj"}, "$~#?hcyaknc!@@!!$", {"tneghj"}},<EOF>""",129))
    # def test_array6(self):
    #     self.assertTrue(TestLexer.checkLexeme("""{0.2, 12., 5.e2, 9E-2, 100E+1, 25.E-1}""","""{0.2, 12., 5.e2, 9E-2, 100E+1, 25.E-1},<EOF>""",128))
    # def test_array7(self):
    #     self.assertTrue(TestLexer.checkLexeme("""{21.e-1, {23e2}, {{12.e+2, 0e8}}, {8.23, 2.}}""","""{21.e-1, {23e2}, {{12.e+2, 0e8}}, {8.23, 2.}},<EOF>""",128))
    # def test_array8(self):
    #     self.assertTrue(TestLexer.checkLexeme("""{212, {23e2}, {{12.e+2, 0e8}}, {8.23, 2.}}""","""{21.e-1, {23e2}, {{12.e+2, 0e8}}, {8.23, 2.}},<EOF>""",128))
    
    def test_wrong_token1(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",195))
    def test_wrong_token2(self):
        self.assertTrue(TestLexer.checkLexeme("x+2.@@^!@!&*","x,+,2.,Error Token @",196))
    def test_wrong_token3(self):
        self.assertTrue(TestLexer.checkLexeme("abcd\nef\nhihiVx%%^&&","abcd,ef,hihiVx,%,%,Error Token ^",197))
    def test_wrong_token4(self):
        self.assertTrue(TestLexer.checkLexeme("()<=()!!!~?????>?!~","(,),<=,(,),!,!,!,Error Token ~",198))

    def test_full1(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: abc = 12*.2e5 - 0xEF12, st = "@gmail\\ndotcom", bo = (True || x>.5. && y <=.2.); **var here** \\. 91.012e2""","""Var,:,abc,=,12,*.,2e5,-,0xEF12,,,st,=,@gmail\\ndotcom,,,bo,=,(,True,||,x,>.,5.,&&,y,<=.,2.,),;,\.,91.012e2,<EOF>""",199))
    def test_full2(self):
        self.assertTrue(TestLexer.checkLexeme("""For (i = 0, i < n, i=i+1) Do x="'"shi'"show" r=2*.3 == 6 EndFor.""","""For,(,i,=,0,,,i,<,n,,,i,=,i,+,1,),Do,x,=,'"shi'"show,r,=,2,*.,3,==,6,EndFor,.,<EOF>""",200))
    


