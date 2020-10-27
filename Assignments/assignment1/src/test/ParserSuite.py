import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;
                    Function: main
                    Body:
                    Return;
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;
                    Function: main
                    Body:
                    Return;
                    EndBody."""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_primitive_init_declare(self):
        input="""Var: a,b=1;
                Function: main
                    Body:
                    Return;
                    EndBody."""
        expect= "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_composite_init_declare(self):
        input="""Var: a,b[3]={1,2,3};
                Function: main
                    Body:
                    Return;
                    EndBody."""
        expect= "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_both_init_declare(self):
        input="""Var: a,b=1,c[3]={1,2,3};
                    Function: main
                    Body:
                    Return;
                    EndBody."""
        expect= "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_complicated_composite_declare(self):
        input="""Var: b[2][3]={{1,2},{3,4}};
                    Function: main
                    Body:
                    Return;
                    EndBody."""
        expect= "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_simple_prog(self):
        input="""Var: x;
                Function: fact
                Parameter: n
                Body:
                If n == 0 Then
                Return 1;
                Else
                Return n * fact(n-1);
                EndIf.
                EndBody.
                Function: main
                ** this is a comment **
                Body:
                x = 10;
                fact (x);
                EndBody."""
        expect= "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))  
    
    def test_composite_declare(self):
        input="""Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
                Function: fact
                Parameter: n
                Body:
                If n == 0 Then
                Return 1;
                Else
                Return n * fact(n-1);
                EndIf.
                EndBody.
                Function: main
                ** this is a comment **
                Body:
                x = 10;
                fact (x);
                EndBody."""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_unterminated_comment(self):
        input="""Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
            Function: fact
            Parameter: n
            Body:
            a = a < b;
            If n == 0 Then
            Return 1;
            Else
            Return n * fact(n-1);
            EndIf.
            EndBody.
            Function: main
            Body:
            x = ""10;
            fact (x);
            EndBody."""
        expect="Error on line 14 col 18: 10"
        self.assertTrue(TestParser.checkParser(input, expect, 209))
    def test_non_body_func(self):
        input="""Function: main"""
        expect="""Error on line 1 col 14: <EOF>"""
        num=210
        self.assertTrue(TestParser.checkParser(input, expect, num))
    def test_test_nonsemi_stmt(self):
        input="""Function: main
Var: a
Body:Var
a=1
EndBody."""
        expect="""Error on line 2 col 0: Var"""
        num=211
        self.assertTrue(TestParser.checkParser(input, expect, num))


    def test_non_func_prog(self):
        input="""Var: a,b,c;"""
        expect="""successful"""
        num=212
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_invalid_expr(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        a = a <b;
        EndBody."""
        expect="""successful"""
        num=213
        self.assertTrue(TestParser.checkParser(input, expect, num))


    def test_khang_testcase(self):
        input="""Var: x = "yay";"""
        expect="""successful"""
        num=214
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_invalid_bool_expr(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        a = a <b < c;
        EndBody."""
        expect="""Error on line 4 col 17: <"""
        num=215
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_if_expr(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        EndBody."""
        expect="""successful"""
        num=216
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_var_decl_stmt(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        Var: x=1,a[1]=1;
        Var: a,b[1]={"this"};
        EndBody."""
        expect="""successful"""
        num=217
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_params_1(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]=1;
        Var: a,b[1]={"this"};
        EndBody."""
        expect="""successful"""
        num=218
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_params_2(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a, b[1]
        Body:
        Var: x=1,a[1]=1;
        Var: a,b[1]={"this"};
        EndBody."""
        expect="""successful"""
        num=219
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_params_3(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a, b[1];
        Body:
        Var: x=1,a[1]=1;
        Var: a,b[1]={"this"};
        EndBody."""
        expect="""Error on line 3 col 26: ;"""
        num=220
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_params_4(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a = 1, b[1]
        Body:
        Var: x=1,a[1]=1;
        Var: a,b[1]={"this"};
        EndBody."""
        expect="""Error on line 3 col 21: ="""
        num=221
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_params_5(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a, b[1], {12,3}
        Body:
        Var: x=1,a[1]=1;
        Var: a,b[1]={"this"};
        EndBody."""
        expect="""Error on line 3 col 28: {"""
        num=222
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_params_6(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a + b
        Body:
        Var: x=1,a[1]=1;
        Var: a,b[1]={"this"};
        EndBody."""
        expect="""Error on line 3 col 21: +"""
        num=223
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_var_decl_not_in_head(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a, b[1]
        Body:
        Var: x=1,a[1]=1;
        If a Then
        EndIf.
        Var: a,b[1]={"this"};
        EndBody."""
        expect="""Error on line 8 col 8: Var"""
        num=224
        self.assertTrue(TestParser.checkParser(input, expect, num))
    
    def test_params_7(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a;
        Body:
        Var: x=1,a[1]=1;
        Var: a,b[1]={"this"};
        EndBody."""
        expect="""Error on line 3 col 20: ;"""
        num=225
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_var_decl_2(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},b=a<c;
        Var: a,b[1]={"this"};
        EndBody."""
        expect="""Error on line 5 col 37: a"""
        num=226
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_var_decl_3(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        Var: a,b[1]={"this"};
        EndBody."""
        expect="""successful"""
        num=227
        self.assertTrue(TestParser.checkParser(input, expect, num))
    
    def test_var_decl_4(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        If 1 < a Then
        Var: a;
        EndIf.
        Var: a,b[1]={"this"};
        EndBody."""
        expect="""Error on line 9 col 8: Var"""
        num=228
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_if_stmt_1(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        If 1 + a - b * foo() > 1 Then
        EndIf.
        EndBody."""
        expect="""successful"""
        num=229
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_if_stmt_2(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        If a == True Then
        EndIf.
        EndBody."""
        expect="""successful"""
        num=230
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_if_stmt_3(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        If a && True || !b Then
        EndIf.
        EndBody."""
        expect="""successful"""
        num=231
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_if_stmt_4(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        If a && True || !b Then
        ElseIf something Then
        If something123El_se Then
        EndIf.
        EndIf.
        EndBody."""
        expect="""successful"""
        num=232
        self.assertTrue(TestParser.checkParser(input, expect, num))
    
    def test_for_stmt_1(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        For something Do something() EndFor.
        EndBody."""
        expect="""Error on line 6 col 12: something"""
        num=233
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_for_stmt_2(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        For (i = 1, a < 2, i = i + 1) Do something(); EndFor.
        EndBody."""
        expect="""Error on line 6 col 29: ="""
        num=234
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_for_stmt_3(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        For (i = "abc", a < 2, i + 1) Do something(); EndFor.
        EndBody."""
        expect="""successful"""
        num=235
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_for_stmt_4(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        For (i = 0x12, a < 2, i + foo() + 1) Do something(); EndFor.
        EndBody."""
        expect="""successful"""
        num=236
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_for_stmt_5(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        For (i = 2, a < 2, i + 1) Do 
        For (i=2) Do EndFor.
        something(); EndFor.
        EndBody."""
        expect="""Error on line 7 col 16: )"""
        num=237
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_for_stmt_6(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        For (i = 0x12, a < 2, i + foo() + 1) Do something();
        c = a[23][b[1][2][c]] +. 12.; 
        EndFor.
        EndBody."""
        expect="""successful"""
        num=238
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_for_stmt_7(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        For (i = 0x12, a < 2, i + foo() + 1) Do something();
        c = a[23][b[1][2][c]] +. 12; 
        EndFor.
        EndBody."""
        expect="""successful"""
        num=239
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_while_stmt_1(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        While statement Do something(); EndWhile.
        EndBody."""
        expect="""successful"""
        num=240
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_while_stmt_1(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        While 1 Do something(); EndWhile.
        EndBody."""
        expect="""successful"""
        num=240
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_while_stmt_2(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        While !(x =/= y) Do something(); EndWhile.
        EndBody."""
        expect="""successful"""
        num=241
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_while_stmt_3(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        While !(x &&  y || b) ** && (a || abc)** Do something(); EndWhile.
        EndBody."""
        expect="""successful"""
        num=242
        self.assertTrue(TestParser.checkParser(input, expect, num))
    
    def test_while_stmt_4(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        While !(x &&  y || b) && (a || abc) Do something(); EndWhile.
        EndBody."""
        expect="""successful"""
        num=243
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_complicate_bool_expr(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        a = !(x &&  y || b) && (a || abc);
        EndBody."""
        expect="""successful"""
        num=244
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_dowhile_stmt_1(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Do something(); While !(abc < 12 || b && True) EndDo.
        EndBody."""
        expect="""successful"""
        num=245
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_dowhile_stmt_2(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Do something(); While a[1][c[2]] + 123 -1 EndDo.
        EndBody."""
        expect="""successful"""
        num=246
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_dowhile_stmt_3(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Do something(); While 1 <. 2.0 EndDo.
        EndBody."""
        expect="""successful"""
        num=247
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_dowhile_stmt_4(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Do something(); While a && bool_of_string("True") EndDo.
        EndBody."""
        expect="""successful"""
        num=248
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_dowhile_stmt_5(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Do something(); While a && b <. 1. +. 3. EndDo.
        EndBody."""
        expect="""successful"""
        num=249
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_wrong_exp(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e; EndIf.
        EndIf.
        EndBody."""
        expect="""Error on line 6 col 80: e"""
        num=250
        self.assertTrue(TestParser.checkParser(input, expect, num))
    
    def test_break_continue(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        Break;
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Continue;
        EndBody."""
        expect="""successful"""
        num=251
        self.assertTrue(TestParser.checkParser(input, expect, num))
    
    def test_return_stmt_1(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Return ;
        EndBody."""
        expect="""successful"""
        num=252
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_return_stmt_2(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Return 1 + 1;
        EndBody."""
        expect="""successful"""
        num=253
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_return_stmt_3(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Return 1 + {{1,2}, "abnd"};
        EndBody."""
        expect="""successful"""
        num=254
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_return_stmt_4(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Return (a < 1) || (b >. !c);
        EndBody."""
        expect="""successful"""
        num=255
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_return_stmt_5(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Return a < 1 || foo(arg1, "arg2", {1,2});
        EndBody."""
        expect="""successful"""
        num=256
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_return_stmt_6(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Return If a > b Then a + 1 EndIf.;
        EndBody."""
        expect="""Error on line 9 col 15: If"""
        num=257
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_call_stmt_1(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        foo(arg1, "???", foo(nothing));
        EndBody."""
        expect="""successful"""
        num=258
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_call_stmt_2(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        foo(arg1, "???", foo(nothing))
        EndBody."""
        expect="""Error on line 5 col 8: EndBody"""
        num=259
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_call_stmt_3(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        a = a[c[1][b]][1] + foo(arg1, "???", foo(nothing));
        EndBody."""
        expect="""successful"""
        num=260
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_call_stmt_4(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        a = a[c[1][b]][1] < foo(arg1, "???", foo(nothing));
        EndBody."""
        expect="""successful"""
        num=261
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_call_stmt_5(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        foo(arg1, "???", foo(nothing)) = something(foo());
        EndBody."""
        expect="""Error on line 4 col 39: ="""
        num=262
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_call_stmt_6(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        foo(arg1, "???", foo(nothing), {"asdab", {1,2.e2,123e1,"nothing"}});
        EndBody."""
        expect="""successful"""
        num=263
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_call_stmt_7(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        foo(arg1, "???", foo(nothing), {"asdab", {1,2.e2,123e1,"nothing"}});
        printLn();
        print(arg);
        printStrLn(arg);
        read();
        EndBody."""
        expect="""successful"""
        num=264
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_call_stmt_8(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        foo(arg1, "???", foo(nothing), {"asda\\bb", {1,2.e2,123e1,"nothing"}});
        printLn();
        print(arg);
        printStrLn(arg);
        read();
        EndBody."""
        expect="""successful"""
        num=265
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_call_stmt_9(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        foo(arg1, "???", foo(nothing), {"asda\\bb", {1,2.e2,123e1,"nothing"}});
        printLn();
        **print(arg);
        printStrLn(arg)**;
        read();
        EndBody."""
        expect="""Error on line 7 col 25: ;"""
        num=266
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_call_stmt_10(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        foo(a < b + c);
        printLn();
        **print(arg);
        printStrLn(arg)**;
        read();
        EndBody."""
        expect="""Error on line 7 col 25: ;"""
        num=267
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_idx_operator_1(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        a = b[something()[a[1]] + 1 ];
        EndBody."""
        expect="""successful"""
        num=268
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_idx_operator_2(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        a = b[something()[a[1]] + 1][c + d < 1];
        EndBody."""
        expect="""successful"""
        num=269
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_idx_operator_3(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        a = b[something()[a[1]] + 1][c + d < 1] + c *. d[1][21];
        EndBody."""
        expect="""successful"""
        num=270
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_idx_operator_4(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        a = b[something()[a[1]] + 1][c + d < 1] + c *. d[1][21 * 0x21AF];
        EndBody."""
        expect="""successful"""
        num=271
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_idx_operator_5(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        a = b[something()[a[1]] + 1][c + d < 1] + c *. d[1.][21 * 0x21Af];
        EndBody."""
        expect="""Error on line 4 col 71: f"""
        num=272
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_op_expr_1(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        a = a + b +. a-a-.a*a*.a\\b\\.b%!c&&a||a==b;
        EndBody."""
        expect="""successful"""
        num=273
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_op_expr_2(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        a = (a + b) +. (a-a-.a*a*.a\\b\\.b%!c&&a||a==b;
        EndBody."""
        expect="""Error on line 4 col 52: ;"""
        num=274
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_op_expr_3(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        b = {{{}}};
        a = (a + b) +. (a-a-.a*a*.a\\b\\.b%!c&&a||a==b);
        EndBody."""
        expect="""successful"""
        num=275
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_op_expr_4(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        b = {{{}}};
        a = (a + b) +. (a-a-.a*a*.a\\b\\.b%!c&&a||a==b) % a[1][1];
        EndBody."""
        expect="""successful"""
        num=276
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_function_structure_1(self):
        input="""Var: a,b,c;
        Function: main
        Body:
        Body:
        EndBody."""
        expect="""Error on line 4 col 8: Body"""
        num=277
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_function_structure_2(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a < b
        Body:
        Body:
        EndBody."""
        expect="""Error on line 3 col 21: <"""
        num=278
        self.assertTrue(TestParser.checkParser(input, expect, num))

    
    def test_function_structure_3(self):
        input="""
        Function: main,fact
        Parameter: a < b
        Body:
        Body:
        EndBody."""
        expect="""Error on line 2 col 22: ,"""
        num=279
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_function_structure_4(self):
        input="""
        Function: main
        Parameter: a, b[1][100]
        Body:
        While a<b Do
            If a > b Then doNothing(); Break;
            ElseIf !somecon() Then doSomething();
            Else Do something(); While a + foo()[100] EndDo.
            EndIf.
        EndWhile.
        EndBody."""
        expect="""successful"""
        num=280
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_function_structure_5(self):
        input="""
        Function: main
        Parameter: a, b[1][100]
        Body:
        While a<b Do
            If a > b Then doNothing(); Break;
            ElseIf !somecon() Then doSomething();
            Else Do something(); While a + foo()[100] EndDo.
            EndIf.
        EndDo.
        EndBody."""
        expect="""Error on line 10 col 8: EndDo"""
        num=281
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_function_structure_6(self):
        input="""
        Function: main
        Parameter: a, b[1][100]
        Body:
        While a<b Do
            If a > b Then doNothing(); Break;
            ElseIf !somecon() Then doSomething();
            ElseIf a \\ 100 -20 Then Continue;
            stop();
            Else what();
            Else Do something(); While a + foo()[100] EndDo.
            EndIf.
        EndWhile.
        EndBody."""
        expect="""Error on line 11 col 12: Else"""
        num=282
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_function_structure_7(self):
        input="""
        If a > b Then doNothing(); Break;
            ElseIf !somecon() Then doSomething();
            ElseIf a \\ 100 -20 Then Continue;
            stop();
            Else what();
            Else Do something(); While a + foo()[100] EndDo.
            EndIf.
        Function: main
        Parameter: a, b[1][100]
        Body:
        While a<b Do
        EndWhile.
        EndBody."""
        expect="""Error on line 2 col 8: If"""
        num=283
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_function_structure_8(self):
        input="""
        Function: main_123_main
        Parameter: a, b[1][100]
        Body:
        While a<b Do
        EndWhile.
        EndBody."""
        expect="""successful"""
        num=284
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_function_structure_9(self):
        input="""
        Function: 
        Body:
        
        EndBody."""
        expect="""Error on line 3 col 8: Body"""
        num=285
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_function_structure_10(self):
        input="""
        Function: nothing
        Body:
        Var: a = {1238,32412, 120};
        EndBody.
        Function: foo
        Parameter: a,b,c
        Body:
        nothing(a[1][1][b[k]]);
        EndBody."""
        expect="""successful"""
        num=286
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_array_lit_with_expr(self):
        input="""
        Function: foo
        Parameter: a,b,c
        Body:
        nothing(a[1][1][b[k]]);
        EndBody."""
        expect="""successful"""
        num=287
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_while_stmt_extra(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        While statement  something(); EndWhile.
        EndBody."""
        expect="""successful"""
        num=288
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_while_stmt_extra(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        While statement  something(); EndWhile.
        EndBody."""
        expect="""Error on line 5 col 25: something"""
        num=288
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_extra_1(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: 12e1,0.001
        Body:
        While statement  something(); EndWhile.
        EndBody."""
        expect="""Error on line 3 col 19: 12e1"""
        num=289
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_extra_2(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        1 == 12
        EndBody."""
        expect="""Error on line 5 col 8: 1"""
        num=290
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_extra_3(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: a[5] = {1,4,3,2,0};
        Var: b[2][3]={{1,2,3},{4,5,6}};
        EndBody."""
        expect="""successful"""
        num=291
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_extra_4(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        a[3 + foo(2)] = a[b[2][3]] + 4;
        EndBody."""
        expect="""successful"""
        num=292
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_extra_5(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a, a[1][12]
        Body:
        Var: x[1][2] = {ab,da};
        a[3 + foo(2)] = a[b[2][3]] + 4;
        EndBody."""
        expect="""Error on line 5 col 24: ab"""
        num=293
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_extra_6(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a, a[1][12]
        Body:
        If expr Then 
        ElseIf expr Then
        Else
        EndIf.
        EndBody."""
        expect="""successful"""
        num=294
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_extra_7(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a, a[1][12]
        Body:
        If expr Then 
        ElseIf expr Then
        While expr Do EndWhile.
        Do Return; While {{}} EndDo.
        Else
        EndIf.
        EndBody."""
        expect="""successful"""
        num=295
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_extra_8(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a, a[1][12]
        Body:
        If expr Then 
        ElseIf expr Then
        While expr Do EndWhile.
        Do Return; While {{}} EndDo.
        Else nothing(); a=(1==b+a);
        EndIf.
        EndBody."""
        expect="""successful"""
        num=296
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_extra_9(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a, a[1][12]
        Body:
        If expr Then 
        ElseIf expr Then
        While expr Do EndWhile.
        Do Return; While {{}} EndDo.
        Else nothing(); a=1=b+a;
        EndIf.
        EndBody."""
        expect="""Error on line 9 col 27: ="""
        num=297
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_extra_10(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a, a[1][12]
        Body:
        For(i=expr, a =/= {{}}, "what is that" + 1) Do
        EndFor.
        EndBody."""
        expect="""successful"""
        num=298
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_extra_11(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a, a[1][12]
        Body:
        For(i=expr, a =/= {{}, "what is that" + 1) Do
        EndFor.
        EndBody."""
        expect="""Error on line 5 col 46: +"""
        num=299
        self.assertTrue(TestParser.checkParser(input, expect, num))

    def test_extra_12(self):
        input="""Var: a,b,c;
        Function: main
        Parameter: a, a[1][12]
        Body:
        For(i=expr, a =/= {{}}, "what is that'"\\b" + 1) Do
        Break Continue;
        EndFor.
        EndBody."""
        expect="""Error on line 6 col 14: Continue"""
        num=300
        self.assertTrue(TestParser.checkParser(input, expect, num))