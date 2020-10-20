import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_var_declare_1(self):
        input = """Var: a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_var_declare_2(self):
        input = """Var: a_c_e,b,c,d;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_var_declare_3(self):
        input = """Var: c, d = 6.12, e=10, f="string";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_var_declare_4(self):
        input = """Var: m[2][7][3], n[10], a, goTHeR;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_var_declare_5(self):
        input = """Var:  m[1][7], n[10], a= 18, gother = "loki????";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_var_declare_6(self):
        input = """Var: a, b, c[10][3][2], aVar, b() ;"""
        expect = "Error on line 1 col 31: ("
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_var_declare_7(self):
        input = """Var: array[2][5][3] = 10, scalar_var = {1,2,3};
                    Var: ace;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_var_declare_8(self):
        input = """Var: a=True, b=0XAB12, c=0o1127;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    
    def test_var_declare_9(self):
        input = """Var: array[1][2][3] = {{1,2,3},{2.5,3e6},{"string","??1810992"},{True, False, True}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_var_declare_10(self):
        input = """Var: scalar = {1,"string",5e6,True}, a[10][22], e=40e5, c, f=20;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    
    def test_var_declare_11(self):
        input = """Var: a, b, k f=20;"""
        expect = "Error on line 1 col 13: f"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_function_declare_1(self):
        input = """ Var: x;
        Function: fact
        Body:

        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))    


    def test_function_declare_2(self):
        input = """ Var: x;
        Function: fact[]
        Body:

        EndBody.
        """
        expect = "Error on line 2 col 22: ["
        self.assertTrue(TestParser.checkParser(input,expect,213))  

    def test_function_declare_3(self):
        input = """ 
        Function: fact
        Parameter: scalar, com[1][23], s_u_Pe
        Body:

        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))  


    def test_function_declare_4(self):
        input = """
        Function: fact
        Parameter: scalar, com[1][23], s_u_Pe
        Body:
            Var: a, arr={1,"abc",{5, 6e3}};
            a = "String";
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))  


    def test_function_declare_5(self):
        input = """ Var: x;
        Function:  
        Body:
            Var s = "Name missing";
        EndBody.
        """
        expect = "Error on line 3 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_function_declare_6(self):
        input = """ Var: x;
        Function:  test
        Parameter: 16;
        Body:
            x = "Wrong parameter"
        EndBody.
        """
        expect = "Error on line 3 col 19: 16"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_function_declare_7(self):
        input = """ Var: x;
        Function:  test
        Var a,b;
        Parameter: scalar
        Body:
            h = "Where is var declare?";
        EndBody.
        """
        expect = "Error on line 3 col 8: Var"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_function_declare_8(self):
        input = """  Var: x;
        Function:  fact
        Parameter: n , c, d
        Body:
            a = "not a var declare";
            Var: c = "a var declare";
        EndBody.
        """
        expect = "Error on line 6 col 12: Var"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    
    def test_function_declare_9(self):
        input = """Var: x;
        Function: foo
        Parameter:
        Body:
            Var: i = "null parameter";
        EndBody.
        """
        expect = "Error on line 4 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    
    def test_function_declare_10(self):
        input = """Var: x;
        Var: y;
        Function: foo
        Body:
        EndBody.

        Var: z = "declare after a funtion";
        """
        expect = "Error on line 7 col 8: Var"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_function_declare_11(self):
        input = """
        Function: func_NAME
        Parameter: x[10], a[2][3][2][9]
        Body:
            a = 10;

            Return a + 10 - 2;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_function_declare_12(self):
        input = """ Var: x = "where is DOT";
        Function: func_NAME
        Parameter: x[10], a[2][3][2][9]
        Body:

        EndBody
        """
        expect = "Error on line 7 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_var_declare_statement_1(self):
        input = """
        Function: test
        Body:
            Var: v_a_r, x[1][2], kOr0="string";
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_var_declare_statement_2(self):
        input = """
        Var: a;
        Function: test
        Body:
            Var: v_a_r={{}, {1,"ac"}};
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    
    def test_var_declare_statement_3(self):
        input = """
        Function: test
        Body:
            Var: x = 4, y = 6;
            Var: c = 2;
            Var: z_1[2][3] = {{6572e21, 2341e+56, 0.5},{"%^DFGZ", "Rvul^%", "sin2xy"}}, a[24], c;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_statements_1(self):
        input = """
        Var: a;
        Function: test
        Body:
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
            r = 5 + 1 +3 * 12e6 % 0X12;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_statement_2(self):
        input = """
        Function: test
        Body:
            b[2][3] = {{2,3,4},{4,5,6}};
            x[1] = 2;
            d = 1e-12;
            m = foo(12);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    
    def test_statement_3(self):
        input = """
        Function: test
        Body:
            a = b = c = d;
        EndBody.
        """
        expect = "Error on line 4 col 18: ="
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_statement_4(self):
        input = """
        Function: test
        Body:
            r = a == b + 2;
            s = r*r + 2;
            t = s || !foo(2+4) && k == 12 + (8*3e-2)\.math(12+change_R);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    
    def test_statement_5(self):
        input = """
        Var: x, y = 5e3, z;
        Function: test
        Body:
            If a == b Then
                a = b;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_statement_6(self):
        input = """
        Function: test
        Body:
            If (True && False) Then a = 5;
            Else a = s || !foo(2+4) && k == 12;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_statement_7(self):
        input = """
        Function: test
        Body:
            If (True && False) Then a = 5;
            ElseIf (as || !foo(2+4) && k == 12) Then dosomething();
            ElseIf (aFunction(!foo(2+4) )) Then dosomething2();
            Else a = s || !foo(2+4) && k == 12;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_statement_8(self):
        input = """
        Function: main
            Body:
                If (True + False) Then a = aFun(-t[2][1]) + 12E-12;
                Else c = s || !foo(2+4) && k == 12 - (8*3e-2)\.math(12+change_R);
            EndBody.
        """
        expect = "Error on line 6 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,234))


    def test_statement_9(self):
        input = """
        Function: test
        Body:
            If (True) Then 
                If (!trueAgain) Then 
                    If (againTrue) Then doSomeThing();
                Else doSongThing();
            EndIf.
            EndIf.
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_statement_10(self):
        input = """
        Function: test
        Body:
            If (True) Then 
                If (!trueAgain) Then 
                    If (againTrue) Then doSomeThing();
                    Else doSongThing();
                    EndIf.
                ElseIf (False) Then doSomeThing();
            EndIf.
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_statement_11(self):
        input = """
        Function: test
        Body:
            If avg < 3 Then raise = "Fail";
            ElseIf avg <=. 4 Then raise = "Y";
            ElseIf avg <=. 6.5 Then raise = "TB";
            ElseIf avg <=. 8. Then raise = "K";
            ElseIf avg <=. 9. Then raise =  "G";
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    


    def test_statement_12(self):
        input = """
        Function: test
        Body:
            If avg < 3 Then raise = "Fail";
            ElseIf avg <=. 4 Then raise = "Y";
            ElseIf avg <=. 6.5 Then raise = "TB";
            ElseIf avg <=. 8. Then raise = "K";
            ElseIf avg <=. 9. Then raise =  "G";
        EndBody.
        EndIf.
        """
        expect = "Error on line 9 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_statement_13(self):
        input = """
        Function: test
        Body:
            If avg < 3 Then raise = "Fail";
            ElseIf avg <=. 4 Then raise = "Y";
            ElseIf avg <=. 6.5 Then raise = "TB";
            ElseIf avg <=. 8. Then raise = "K";
            ElseIf avg <=. 9. Then raise =  "G";
        EndBody.
        EndIf.
        """
        expect = "Error on line 9 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    
    def test_statement_15(self):
        input = """
        Function: test
        Body:
            If foo(2) Then foo(2);
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_statement_16(self):
        input = """
        Function: test
        Body:
            If foo(2) Then foo(2);
            ElseIf foo(2) Then foo(2);
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
  
    def test_statement_17(self):
        input = """
        Function: test
        Body:
            Var: abc = 1, cde = 2, efg = 3;
            If abc + cde == efg Then Else efg = 3;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    
    def test_statement_18(self):
        input = """
        Function: test
        Body:

            If 1 Then 
                Var: x = 4, y = 6;
                Var: c = 2;
                Var: z_1[2][3] = {{6572e21, 2341e+56, 0.5},{"%^DFGZ", "Rvul^%", "sin2xy"}}, a[24], c;
            ElseIf 2 Then
                Var: x = 4, y = 6;
                Var: c = 2;
                Var: z_1[2][3] = {{6572e21, 2341e+56, 0.5},{"%^DFGZ", "Rvul^%", "sin2xy"}}, a[24], c;
            ElseIf 3 Then
                Var: x = 4, y = 6;
                Var: c = 2;
                Var: z_1[2][3] = {{6572e21, 2341e+56, 0.5},{"%^DFGZ", "Rvul^%", "sin2xy"}}, a[24], c;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_statement_19(self):
        input = """
        Function: test
        Body:
            If 1 Then 
                Var: x = 4, y = 6;
                Var: c = 2;
                Var: z_1[2][3] = {{6572e21, 2341e+56, 0.5},{"%^DFGZ", "Rvul^%", "sin2xy"}}, a[24], c;
            ElseIf 2 Then
                Var: x = 4, y = 6;
                Var: c = 2;
                Var: z_1[2][3] = {{6572e21, 2341e+56, 0.5},{"%^DFGZ", "Rvul^%", "sin2xy"}}, a[24], c;
            ElseIf 3 Then
                Var: x = 4, y = 6;
                Var: c = 2;
                Var: z_1[2][3] = {{6572e21, 2341e+56, 0.5},{"%^DFGZ", "Rvul^%", "sin2xy"}}, a[24], c;
            EndIf.
            Var a = 10;
        EndBody.
        """
        expect = "Error on line 17 col 12: Var"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_statement_20(self):
        input = """
        Function: test
        Body:
            If 1 Then 
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_for_statement_1(self):
        input = """
        Function: test
        Body:   
            For (i = 0, i < 10, 1) Do
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_for_statement_2(self):
        input = """
        Function: test
        Parameter: n
        Body:
            Var: x;   
            For (i = 0, i < 10 , 1) Do
                If ( c < a + b) && (a < b + c)   && ( b < a + c) Then
                If (a*a==b*b+c*c) || (b*b==a*a+c*c) || (c*c== a*a+b*b) Then
                    print("tam giac vuong");
                
                ElseIf (a==b) && (b==c) Then print("tam giac deu");
                ElseIf (a==b) || (a==c) || (b==c) Then print("tam giac can");
                Else print("tam giac thuong");
                EndIf.
            Else print("khong phai tam giac");
            EndIf.
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    
    def test_for_statement_3(self):
        input = """
        Function: test
        Body:   
            For (a = (a==b) && (b==c),1 + 1, aFun(-t[2][1]) + 12E-12 ) Do
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_for_statement_4(self):
        input = """
        Function: test
        Parameter: n
        Body:
            Var: i = 0;
            For (i = aFun(-t[2][1]) + 12E-12, i <= aFun(-t[2][1]) + 12E-12, aFun(-t[2][1]) + 12E-12) Do

            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))


    def test_for_statement_5(self):
        input = """
        Function: test
        Parameter: n
        Body:
            Var: i = 0;
            For (i, i <= aFun(-t[2][1]) + 12E-12, aFun(-t[2][1]) + 12E-12) Do

            EndFor.
        EndBody.
        """
        expect = "Error on line 6 col 18: ,"
        self.assertTrue(TestParser.checkParser(input,expect,250))


    def test_for_statement_6(self):
        input = """
        Function: test
        Parameter: n
        Body:
            If 1 Then 
                For (i = 3e12, i <= aFun(-t[2][1]) + 12E-12, aFun(-t[2][1]) + 12E-12) Do
                    doSomeThing();
                EndFor.
            EndIf.

        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
        
    def test_for_statement_7(self):
        input = """
        Function: test
        Body:
            For (i = 0, i < 4, a = a +1) Do
            EndFor.
        EndBody.
        """
        expect = "Error on line 4 col 33: ="
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_for_statement_8(self):
        input = """
        Function: foo
        Body:
            Var: arr[10][10];
            For (i = 0, i < 10, 1) Do  
                For (j = 0, j < 10, 1) Do
                    print(arr[i][j]);
                EndFor.
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_for_statement_9(self):
        input = """
        Function: test
        Body:
            For (i = 0XABC12, afuntion(), "string???????") Do
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_for_statement_10(self):
        input = """
        Function: test
        Body:
            Var: a = 2;
            For (i = 10 - a*a%2, a < 100 * iuuw,  a + 1) Do
                writeln(a*a - i*i);
                i = i + 1;
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_while_statement_1(self):
        input = """
        Function: test
        Body:
            While True Do
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_while_statement_2(self):
        input = """
        Function: test
        Body:
            Var: x = 0;
            While aFun(-t[2][1]) + 12E-12 < 10  Do
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_while_statement_3(self):
        input = """
        Function: test
        Body:
            Var: x = 0;
            While Do
            EndWhile.
        EndBody.
        """
        expect = "Error on line 5 col 12: While"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_while_statement_4(self):
        input = """
        Function: test
        Body:
            Var: x = 0;
            While True Do
                For (i = 0, i < 10 , 1) Do
                If ( c < a + b) && (a < b + c)   && ( b < a + c) Then
                If (a*a==b*b+c*c) || (b*b==a*a+c*c) || (c*c== a*a+b*b) Then
                    print("tam giac vuong");
                
                ElseIf (a==b) && (b==c) Then print("tam giac deu");
                ElseIf (a==b) || (a==c) || (b==c) Then print("tam giac can");
                Else print("tam giac thuong");
                EndIf.
                Else print("khong phai tam giac");
                EndIf.
                EndFor.
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))


    def test_while_statement_5(self):
        input = """
        Function: test
        Body:
            Var: x = 0;
            While True Do
                For (i = 0, i < 10 , 1) Do
                If ( c < a + b) && (a < b + c)   && ( b < a + c) Then
                If (a*a==b*b+c*c) || (b*b==a*a+c*c) || (c*c== a*a+b*b) Then
                    print("tam giac vuong");
                
                ElseIf (a==b) && (b==c) Then print("tam giac deu");
                ElseIf (a==b) || (a==c) || (b==c) Then print("tam giac can");
                Else print("tam giac thuong");
                EndIf.
                Else print("khong phai tam giac");
                EndIf.
                EndFor.
        EndBody.
        """
        expect = "Error on line 18 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_while_statement_6(self):
        input = """
        Function: test
        Parameter: t
        Body:
            While (a*a==b*b+c*c) **|| (b*b==a*a+c*c)** || (c*c== a*a+b*b) Do
                Var: a = 2;
                For (i = 10 - a*a%2, a < 100 * iuuw,  a + 1) Do
                writeln(a*a - i*i);
                i = i + 1;
                EndFor.
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_while_statement_7(self):
        input = """
        Function: test
        Parameter: t
        Body:
            While (a*a==b*b+c*c) **|| (b*b==a*a+c*c)** || (c*c== a*a+b*b) Do
                For (i = 10 - a*a%2, a < 100 * iuuw,  a + 1) Do
                writeln(a*a - i*i);
                i = i + 1;
                EndFor.
                Var: a = 2;
            EndWhile.
        EndBody.
        """
        expect = "Error on line 10 col 16: Var"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_while_statement_8(self):
        input = """
        Function: test
        Body:
            Var: x = 1;
            While (x <= 5) Do
                While (x) Do
                    While x Do
                        While (!(!(x))) Do
                        EndWhile.
                    EndWhile.
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_while_statement_9(self):
        input = """
        Function: test
        Body:
            Var: x = 1;
            If nnnn Then
            While (x <= 5) Do
                While (x) Do
                    While x Do
                        While (!(!(x))) Do
                        EndWhile.
                    EndWhile.
                EndWhile.
            EndWhile.
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_while_statement_10(self):
        input = """
        Function: test
        Body:
            Var: x = 1;
            If nnnn Then
            While (x <= 5) Do
                While (x) Do
                    While x Do
                        While (!(!(x))) Do
                        EndWhile.
                    EndWhile.
                EndWhile.
            EndWhile
            EndIf.
        EndBody.
        """
        expect = "Error on line 14 col 12: EndIf"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_do_while_statement_1(self):
        input = """
        Function: test
        Body:
            Do While True EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_do_while_statement_2(self):
        input = """
        Function: test
        Body:
            Do
                While True Do
                    For (i = 0, i < 10 , 1) Do
                    If ( c < a + b) && (a < b + c)   && ( b < a + c) Then
                    If (a*a==b*b+c*c) || (b*b==a*a+c*c) || (c*c== a*a+b*b) Then
                        print("tam giac vuong");
                    
                    ElseIf (a==b) && (b==c) Then print("tam giac deu");
                    ElseIf (a==b) || (a==c) || (b==c) Then print("tam giac can");
                    Else print("tam giac thuong");
                    EndIf.
                    Else print("khong phai tam giac");
                    EndIf.
                    EndFor.
                EndWhile.
            While (a*a==b*b+c*c) **|| (b*b==a*a+c*c)** || (c*c== a*a+b*b) 
            EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_do_while_statement_3(self):
        input = """
        Function: test
        Body:
            Do a = a + 1; While True Do EndWhile. While True EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_do_while_statement_4(self):
        input = """
        Function: test
        Body:
            Do a = a + 1; While True Do EndWhile.
        EndBody.
        """
        expect = "Error on line 5 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_do_while_statement_5(self):
        input = """
        Function: test
            While True 
                doSomeThing();
            EndWhile.
        EndBody.
        """
        expect = "Error on line 3 col 12: While"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    
    def test_break_statement_1(self):
        input = """
        Function: test
        Body:   
            For (i = 0, i < 10, 2) Do
                Break;
                someStament();
                Break;
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    
    def test_break_statement_2(self):
        input = """
        Function: test
        Parameter: foo
        Body:
            For (i = 0, i < 10, 2) Do
                Break;
                If (True) Then
                Break;
                a[1][2][3][4] = 2.E-59;
                Break;
                EndIf.
                Break;
            EndFor.
            
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_break_statement_3(self):
        input = """
        Function: test
        Body:
            While True Do
            For (i = 0, i < 10, 2) Do
                someStament(); 
                Break;        
            EndFor.
            Break;
            EndWhile.        
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_continue_statement_1(self):
        input = """
        Function: test
        Body:
            For (a = 10, a < 10, 28) Do 
                Continue;
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_continue_statement_2(self):
        input = """
        Function: test
        Body:
            While false Do
                x = True || False;
                Continue;
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_call_statement_1(self):
        input = """
        Function: test
        Body:
            foo (2 + x, 4. \. y);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_call_statement_2(self):
        input = """
        Function: test
        Body:
            foo();
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_call_statement_3(self):
        input = """
        Function: test
        Body:
            foo("12739zd", 0X12F, asd , 6E-232);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_call_statement_4(self):
        input = """
        Function: test
        Body:
            foo(dasd + foo(), "!@$C#hc%", 12. \\. 921.9e5 * 32e1);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_call_statement_5(self):
        input = """
        Function: test
        Body:
            foo(dasd + foo({123,"213"},"aray"), "!@$C#hc%", 12. \\. 921.9e5 * 32e1);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_return_statement_1(self):
        input = """
        Function: test
        Body:
            Return;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_return_statement_2(self):
        input = """
        Function: test
        Body:
            Return asd * 12 + 6e-1;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_return_statement_3(self):
        input = """
        Function: sum
        Parameter: n
        Body:
            If (n == 0) Then Return 0;
            EndIf.
            Return n + sum(n - 1);
            For (i = 0 , i < 10 , i) Do Return i+sum;
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_return_statement_4(self):
        input = """
        Function: sum
        Parameter: n
        Body:
            While True Do
                If a==10 Then 
                    Return a > 12 || b[12][1] + {12};
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_return_statement_5(self):
        input = """
        Function: sum
        Parameter: n
        Body:
            While True Do
                If a==10 Then 
                    Return If a > b Then a;
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = "Error on line 7 col 27: If"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_scope_error_1(self):
        input = """
        Var: x;
        Function: test
        Body:
            Function: b
            Body:  
                Return a;
            EndBody.
        EndBody.
        """
        expect = "Error on line 5 col 12: Function"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_scope_error_2(self):
        input = """
        Var: x;
        Function: test
        Body:
            a = index[a3[function(12233)+3];
        EndBody.
        """
        expect = "Error on line 5 col 43: ;"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_scope_error_3(self):
        input = """
        Var: x;
        Function: test
        Body:
            a = index[a3[function(12233+3])];
        EndBody.
        """
        expect = "Error on line 5 col 41: ]"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_scope_error_4(self):
        input = """
        Var: x;
        Function: test
        Body:
            a = index[a3[function(12233+3) * a(array[13][fun]))];
        EndBody.
        """
        expect = "Error on line 5 col 62: )"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    

    def test_scope_error_5(self):
        input = """
        Var: x;
        Function: test
        Body:
            a = index[a3[]];
        EndBody.
        """
        expect = "Error on line 5 col 25: ]"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    

    def test_program_1(self):
        input = """
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        Function: test
        Body:
            
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))


    def test_program_2(self):
        input = """
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        Function: fact
        Parameter: n
        Body:
        If n == 0 Then
        Return 1;
        Else
        Return n * fact (n - 1);
        EndIf.
        EndBody.
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    
    def test_program_3(self):
        input="""
        Var: a_e1={{1273,1e12},"string"} , n = 0X12CD, iD= 0XAD;
        Function: main **entripoint**
        Parameter: as,sa
        Body:
            cout("HelloWorld") ;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_program_4(self):
        input="""
        Function: test
        Parameter: a, a[1][2]
        Body:
        For(i=expr, a =/= {{{},{}}} + a - b, "bruhhhhhh" + 1) Do
            Return "bruhhhhhh";
        EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_program_5(self):
        input="""
        Function: foo
        Parameter: a[5], b
        Body:
        Var: i = 0;
        While (i < 5) Do
        a[i] = b +. 1.0 + "string" - func("{123}", true[12 + hv(foo(a[0xAD]))]);
        EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_program_6(self):
        input="""
        Function: fibonacci
        Parameter: n
        Body:
            If ((n == 1) || (n == 2)) Then Return 1; EndIf.
            Return fibonacci(n-1) + fibonacci(n - 2);
        EndBody.

        Function: main
        Body:
        Var: n;
        scan(n);

        Return fibonacci(n);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_program_7(self):
        input="""
        Function: fGCD
        Parameter: a,b
        Body:
            If (a == 0) || (b == 0) Then Return a + b;
            While a != b Do 
                If a > b Then a = a - b; 
                Else b = b - a;
                EndIf.
            EndWhile.
            Return a;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))


    def test_program_8(self):
        input = """
        Function: tamgiac
        Body:
            Var: a,b,c;
            input(a,b,c);
            If ( c < a + b) && (a < b + c)   && ( b < a + c) Then
                If (a*a==b*b+c*c) || (b*b==a*a+c*c) || (c*c== a*a+b*b) Then
                    print("tam giac vuong");
                
                ElseIf (a==b) && (b==c) Then print("tam giac deu");
                ElseIf (a==b) || (a==c) || (b==c) Then print("tam giac can");
                Else print("tam giac thuong");
                EndIf.
            Else print("khong phai tam giac");
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_program_9(self):
        input = """
        Var: a = 5, b = 7, lcm;
        Var: max;
        Function: main
        Body:
            Var: maxV;
            maxV = a*b;
            For ( i = max(a,b), i <= maxV, 1) Do
                If (i % a == 0) && (i % b == 0) Then
                    lcm = i;
                    Break;
                EndIf.
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test_program_10(self):
        input = """
        Var: a[2309], m, n, d[2309];
        Function: dijkstra
        Body:
        Var: pq;
        For (i = 1, i <= n, 1) Do
            d[i] = oo;
        EndFor.
        d[1] = 0;
        push(pq, ii(0, 1));
        While size(pq) Do
            Var: u, du;
            u = top(pq, second);
            du = top(pq, first);
            pop(pq);
            If du != d[u] Then Continue; 
            EndIf.
            
            For ( i = 0, i < size(a[u]), 1) Do
                Var: v, uv;
                v = second(a[u][v]);
                uv = first(a[u][v]);
                If d[v] > du + uv Then
                    d[v] = du + uv;
                    push(pq, ii(d[v], v));
                EndIf.
            EndFor.
        EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))
