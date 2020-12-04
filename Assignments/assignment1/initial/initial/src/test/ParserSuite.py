import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test1(self):
        input = """Var: x[1];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test2(self):
        input = """Var: y;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test3(self):
        input = """ 
        Function: foo 
        Parameter: x
        Body: 
            c = !a; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test4(self):
        input = """
        Function: foo
        Parameter: n
        Body:
            c = -.x;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test5(self):
        input = """
        Function:  a
        Body:
            Var: s = "hi_hi";
            Var: n = "nice";
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test6(self):
        input = """ 
        Function: foo 
        Parameter: x
        Body: 
            c =a * 5; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test7(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c =a + 5; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test8(self):
        input = """ Function: foo 
        Parameter: n 
        Body: 
            If a Then b = 1; EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test9(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c = x <= 0; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    
    def test10(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            x = y < 100;
            x = !a; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test11(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            a = (3 + 5) * 10 ; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    
    def test12(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c =x && y; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test13(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            If a == 1 Then b = a + 5;
            ElseIf a == 6 Then b= a - 6; 
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    
    def test14(self):
        input = """ Function: foo 
        Parameter: n 
        Body: 
            If !a Then b = (5 + 10) * 100; 
            Else c= 500000 ; 
            EndIf. 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test15(self):
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (i = 3, i != 5, i*1) Do x=10000*2; EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test16(self):
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            foo(2 + x, 4. \. y); 
            goo ();
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    
    def test17(self):
        input = """Function: foo 
        Parameter: n 
        Body: 
        x = 10;
        x = (x - 5) * n; 
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test18(self):
        input = """Function: foo
        Parameter: n
        Body: 
            Var: a = 10., b, c;
            a = c - (4. \. 3.) *. 3.14 *. a * (c - b *. a);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test19(self):
        input = """Function: foo 
        Parameter: n, a[10]
        Body: 

        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test20(self):
        input = """Var: x, y =1, y = "abc'" hello \\t ", m[1], n[10] = {1,2,{"an",5.4},5.e-12};
            Var: a_jacj933 = 00012.21; 
        Function: fact
        Parameter: n, aca_312aAX[3][44][0x31FF], cxa[0x12][0o1][8][0]
        Body:
        Var: t, r= 10.;
        Var: thread = 00212.3123E+3120, r= 10.;
        v = (4. \\. 3.) *.   3.14 *. r * r * a;

        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test21(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                Return 0;
            Else
                Return n * fact (n - 2);
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    
    def test22(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            x = 10;
            y = 15 - x;
            z = x * y;
            fact (z);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test23(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: i = 1;
            While i < 5 Do
                a[i] = b * 2 +. 1.0;
                i = i + 2;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test24(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            While x<10000000000 Do
                If x!=100000 Then Return;
                Else Continue;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    
    def test25(self):
        input = """Function: foo 
        Parameter: n 
        Body: 
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test26(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            Do
                x = a + b - c * d + e - f * g - 123455;
                y =  a + n + h - y - e - u + e * m;
            While x > 0 + 326264 +  x
            EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test27(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            If n != 0 Then
                Return 0;
            Else
                Return (n-1) * (n-2) * (n-3) * (n-4);
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test28(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            a[3+foo(1)] = a[b[1][3]] + 4 * 10 - 7 + b[c[1][3]] + c[b[a][b]];
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    
    def test29(self):
        input = """
        Var: a = 5;
        Var: b = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[100];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    
    def test30(self):
        """ test comment in function """
        input = """Function: foo 
        Parameter: n
        Body: ** Tran Thanh da cuoi**
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test31(self):
        input = """
        Function: test
        Parameter: n
        Body:
            If n != 10 Then
                Return 3.1415919191;
            Else
                Return false;
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    
    def test32(self):
        input = """
        Var: b[2][3]={{1,2,3},{4,5,6}};
        Var: a[100] = {1,2,3};
        Var: a[100000][1000] = {{2,3},{4,5,6,7,8,9,10}};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test33(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            While x<1000000000000 Do
                If x != 99999 Then Return;
                Else Break;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    
    def test34(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            If n != n+1 Then
                Return (n-1) * (n-2) * (n-3) * (n-4);
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test35(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            x1 = a[3-foo(3)];
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test36(self):
        input = """
        Var: x, y[1][3]={{{12345,1}, {12., 12e3}},{23}, {13,32}};
        Function: foo 
        Parameter: n
        Body: 
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test37(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
            x1 = a[3-foo(3)];
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test38(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: i = 0;
            While i < 5 Do
                b[i] = i +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test39(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: i = 0;
            While i < 5 Do
                Var: k = 100;
                a[i] = b +. 1.0 - k * a[i+1];
                i = i + 5;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test40(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                If n!=0 Then
                    Return 100;
                Else 
                    Return 2200;
                EndIf.
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test41(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            While x >1 Do
                If x==1 Then Return;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test42(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: i = 100;
            While i < 5000 Do

            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test43(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            While i < 5 Do
                Var: b = 10;
                a[i] = b +. 1.0;
                i = i + 2;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test44(self):
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (i = 0, i != 5, i*1) Do x=6; EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test45(self):
        input = """Function: foo 
        Parameter: n
        Body: 
        For (i = 0, i < 10, 2) Do
            y = e + u;
            a = n + h - y - e -u + e - m;
        EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test46(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            n = fact(x) - 3;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test47(self):
        input = """Function: test
        Parameter: n
        Body:
            If n > 10 Then
                Return ;
                If n > 11 Then Return n;
                EndIf.
                
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test48(self):
        input = """Function: foo 
        Parameter: n
        Body:
            Var: r = 10., v;
            r = 10.;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test49(self):
        """ test error break """
        input = """Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                If x==1 Then Return;
                Else Break;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test50(self):
        """ test error scala-type in for_stmt """
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (a_a = 0, i != 5, i*1) Do x=6; EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test51(self):
        """ test multi function """
        input = """Function: foo 
        Parameter: n
        Body: 
        EndBody.
        Function: goo 
        Parameter: n
        Body: 
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test52(self):
        input = """
        Function: test
        Body:
            Var: a = 3, b = 4, c = 5;
            If (a < b + c) && ( b < a + c) && ( c < a + b) Then
                If (a*a==b*b+c*c) || (b*b==a*a+c*c) || (c*c== a*a+b*b) Then
                    print("Day la tam giac vuong");
                EndIf.
            ElseIf (a==b) && (b==c) Then print("Day la tam giac deu");
            ElseIf (a==b) || (a==c) || (b==c) Then print("Day la tam giac can");
            ElseIf (a*a > b*b+c*c) || (b*b > a*a+c*c) || (c*c > a*a+b*b) Then print("Day la tam giac tu");
            Else print("Day la tam giac nhon");
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test53(self):
        input = """
        Function: test
        Body:
            Var: arr[1] = {3,4}, x = 4.5, y = 5.;
            If arr[1] >. x Then arr[1] = y;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    
    def test54(self):
        input = """
        Function: foo
        Parameter: n
        Body:
            Var: x;   
            For (i = 0, i < sqrt(n)*2, 1) Do
                x = i + n;
                writeln(x*3);
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test55(self):
        input = """
        Function: test
        Body:
            Var: i = 20, a, b, c;
            If i == 1 Then 
                a = 1;
                b = 2;
                c = (a + b) * (a - b);
            ElseIf i == 2 Then
                a = 3;
                b = 4;
                c = (b - a) * 2;
            ElseIf i == 3 Then
                a = 2;
                b = 2;
                c = (a*2 + b*3) * a * b;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test56(self):
        input = """
        Function: test
        Body:
            Var: i = 21;
            If i == 10 Then 
            ElseIf i == 15 Then
            ElseIf i == 20 Then
            Else
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test57(self):
        input = """
        Function: test
        Body:   
            For (i = 0, i < 10, 2) Do
                writeln(i);
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test58(self):
        input = """
        Function: test
        Body:
            Var: abc = 1, cde = 2, efg = 3;
            If abc + cde == efg Then Else efg = 3;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    
    def test59(self):
        input = """
        Function: foo
        Body: 
            For (i = 0, i <= 100\\10, 1) Do
                If i%2 == 1 Then writeln(i\\2);
                EndIf.
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test60(self):
        input = """
        Var: a;
        Function: foo
        Parameter: a, c
        Body:
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test61(self):
        input = """
        Function: foo
        Body:
            Var: x = False, a;
            a = !True;
            For (i = 0, x == c, 1) Do
                x = False;
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test62(self):
        input = """
        Function: foo
        Body:
            Var: arr[100][100][100];
            For (i = 0, i < 100, 2) Do  
                For (j = 0, j < 100, 2) Do
                    For (k = 0, k < 100, 2) Do
                        arr[i][j][k] = 0;
                    EndFor.
                EndFor.
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test63(self):
        input = """
        Function: foo
        Parameter: n
        Body:
            Var: i = 0;
            For (i = a, i <= (n*n - 2*n + 1) * 2 - (2*n + 1) + 4 * (1 +2*n) , 1) Do
                print(3*i);
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test64(self):
        input = """
        Function: foo
        Body:
            Var: a = 2;
            For (i = 0 , a < 15, a + 1) Do
                writeln("15ph GG");
                i = i + 1;
                    If i < 20 Then write("GoPro");
                    EndIf.
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test65(self):
        input = """
        Function: foo
        Body:
            While True Do
                While False Do
                    While True Do
                    EndWhile.
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test66(self):
        input = """
        Function: foo
        Body:
            Var: n = 0;
            While i < 10 Do
                writeln("Hello");
                i = i + 2;
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test67(self):
        input = """
        Function: foo
        Parameter: t
        Body:
            While t < 10 Do
                If t%2 Then t = t + 10;
                Else t = t + 5;
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test68(self):
        input = """
        Function: foo
        Body:
            For (i = 0, False, 1) Do
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test69(self):
        input = """
        Function: foo
        Body:
            Var: x = True, t = 100, a;
            While (!x || t == 2) Do
                x = False;
                a = x + a;
                x = a - x;
                t = a -x;
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test70(self):
        input = """
        Function: test
        Parameter: m, n, o, p
        Body:
            Var: x;
            While (m <= 2) Do
                While (n >= 1) Do
                    While (o <= n) Do
                        o = o - 1;
                        While (p <= 2) Do
                            p = p + 1;
                            While (p <= 2) Do
                                p = p + 1;
                                While (p <= 2) Do
                                    p = p + 1;
                                    While (p <= 2) Do
                                        p = p + 1;
                                        While (p <= 2) Do
                                            p = p + 1;
                                            While (p <= 2) Do
                                                p = p + 1;
                                            EndWhile.
                                        EndWhile.
                                    EndWhile.
                                EndWhile.
                            EndWhile.
                        EndWhile.
                    EndWhile.
                    x = True;
                    n = n - 1;
                EndWhile.
                x = m * n * p * o;
                m = m + 1;
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test71(self):
        input = """
        Function: test
        Body:
            Var: i, arr[5][10];
            While (i < 10) Do
                For (j = 1, j < 10, 1) Do
                    arr[i][j] = 1;
                EndFor.
                i = i + 2;
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test72(self):
        input = """
        Function: foo
        Parameter: x
        Body:
            Var: n = 0, s = 0;
            Do 
                n = n - 1;
                s = s + n;
            While s * n + 1 < x EndDo.
            writeln(x);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test73(self):
        input = """
        Function: foo
        Parameter: n
        Body:
            Var: i = 0;
            While (i <= n) Do
                If (i == n) Then
                    writeln(n);
                    Return;
                EndIf.
                i = i + 1;
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test74(self):
        input = """
        Function: foo
        Parameter: n
        Body:
            Var: i = 0;
            While i < 10 Do
                i = i + 1;
                If (i == 10) Then write("MVP");
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test75(self):
        input = """
        Function: foo
        Body:
            Var: i, j, k, l;
            Do 
                i = i + 1;
                While (j < 100) Do
                    Do
                        k = k + 1;
                        While (l < 100) Do
                            l = l + 2;
                            While (l < 10) Do
                                l = l + 3;
                                While (l < 1) Do
                                    l = l + 4;
                                    While (l < 0.1) Do
                                        l = l + 5;
                                        While (l < 0.01) Do
                                            l = l + 6;
                                            While (l < 0.001) Do
                                                l = l + 7;
                                            EndWhile.
                                        EndWhile.
                                    EndWhile.
                                EndWhile.
                            EndWhile.
                        EndWhile.
                    While (k < 100) EndDo.
                    j = j + 3;
                EndWhile.
            While (i + j + k + l < foo(2)) EndDo.
            writeln(n);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test76(self):
        input = """
        Function: lcd
        Parameter: n
        Body:
            Var: i;
            i = n - 1;
            While (n % i != 0) Do
                i = i - 1;
            EndWhile.
            writeln(i);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test77(self):
        input = """
        Function: foo
        Body:
            Var: n = 5, s = 5;
            Do
                n = n + 1;
                Do 
                    If n%2 == 0 Then s = s - 1;
                    EndIf.
                While (s < 1000) 
                EndDo.
                s = s * n;
            While (s + n + 1 < max) EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test78(self):
        input = """
        Function: foo
        Body:
            Var: i = 0;
            Do 
                writeln(i);
                i = i + 1;
            While (i < 10) EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test79(self):
        input = """
        Function: foo
        Parameter: n
        Body:
            Var: a = 0;
            Do
                If (n!=3) && (n%i!=0) Then
                    a=1;
                EndIf.
                i = i + 2;
            While i<=n*n EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test80(self):
        input = """
        Function: foo
        Body:
            Var: x = 1;
            Do
            While x EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test81(self):
        input = """
        Var: a;
        Function: foo
        Body:
            Var: zzHQKzz[2][3][4][5] = {{12345, 41e+5, 3.14},{"Yasuo", "Leesin", "Garen"}}, a[234], c;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    
    def test82(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            For (i = 0, i < 10, 2) Do
                Break;
            EndFor.
        a = (a + b) * (a - b);
        b = (a + b) * (b - a);
        If a + b != 0  Then writeln(a+b);
        EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    
    def test83(self):
        input = """
        Var: x;
        Function: foo
        Parameter: a, b
        Body:
            print(a);
            print(b);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test84(self):
        input = """
        Function: foo
        Body:
            Var: a[10];
            Do 
                a[1][2] = 3.14;
                Break;
            While False EndDo.
            writeln(a[1][2]);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test85(self):
        input = """
        Function: test
        Body:
            Var: flag = 0;
            Do
                While !flag Do
                EndWhile.
            While True
            EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test86(self):
        input = """
        Function: foo
        Body:
            a = foo(100) * 28 + 234;
        EndBody.
        Function: foo
        Parameter: n
        Body:
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test87(self):
        input = """
        Function: foo
        Parameter: n
        Body:
            For (i = 1, i < 2, 1) Do
                If (i%2 !=0) Then write(i);
                EndIf.
                n = n - i;
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test88(self):
        input = """
        Function: multi
        Parameter: n
        Body:
            If (n == 0) Then Return 0;
            EndIf.
            Return n * sum(n - 1);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test89(self):
        input = """
        Function: foo1
        Body:

        EndBody.
        Function: foo2
        Body:
            foo2(2);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test90(self):
        input = """
        Function: foo
        Body:
            Var: a = 1;
            While (a != 9) Do
                x = True || False;
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test91(self):
        input = """Var: successful[10][9];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))


    def test92(self):
        input = """
        Function: foo
        Parameter: n
        Body:
            If (n != 10000) Then Return (n - 9999);
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test93(self):
        input = """
        Function: foo
        Body:
            Return True;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test94(self):
        input = """
        Function: foo1
        Body:
            foo ();
        EndBody.
        Function: foo2
        Parameter: a, b, c, d
        Body:
            writeln(a+.b-.c+.d);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test95(self):
        input = """
        Var: x;
        Function: test
        Body:
            Var: body;
            Var: endBody;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test96(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            a =(foo(3) != foo(4))* 0.e2;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test97(self):
        input = """
        Var: s = 0, arr[2] = {1,2};
        Function: assignmentKTLT
        Parameter: hp1, hp2, d
        Body:
            Var: p1, p2;
            Var: h1;
            Var: armor = False;
            Var: pR;
            p1 = hp1 * (1000 - d) \\. int_of_float(1000);
            p2 = (hp2 * d) \\. int_of_float(1000);
            h1 = (hp1 + hp2) % 100;
            h2 = (h1*hp2) % 100;

            If (hp2 == 888) Then armor = True;
            EndIf.
            If hp1 == 777 && ((p1 < p2) || (h1 < h2)) && (armor == False) Then
                Var: e = 1;
                d = e;
                p1 = hp1 *. (1000 - d) \\. float(1000);
                p2 = (hp2 *. d) \\. float(1000);
            EndIf.
            pR = (h1*p1 - h2 * p2) \\. (h1*p1 + h2 * p2);
            print(pR);
        EndBody.
        Function: main
        Body:
            assignmentKTLT(544,290,600);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))


    def test98(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
        Var: i = 45;
        While (i < 100) Do
            a[i] = b * 2 +. 1.0;
            i = i * 2 + 3;
        EndWhile.
        Return a[35];
        EndBody.
        Function: test
        Parameter: arr[211][930], b, c
        Body:
            For (i = 0 , i < arr[20][2] , 1) Do
                If foo(i) <= (foo(i+1)\\foo(foo(i))) Then
                    Return;
                ElseIf foo(i\\2) <= (foo(i-1)\\foo(foo(7*i\\2))) Then
                    Break;
                ElseIf foo(3) <= (foo(i+1)\\foo(foo(7749*i\\2))) Then
                    Break;
                ElseIf foo(45) Then print("2 giam khao da cuoi");
                Else 
                    While !False Do
                        If (!False == True) Then print((foo(i*i+111)\\foo(foo(arr[2][1]*i\\2))));
                        Else Continue;
                        EndIf.    
                    EndWhile.
                EndIf.
            EndFor.
        EndBody.
        Function: main
        Body:
            test(2293);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test99(self):
        input = """
        Var: c[1000];
        Function: test99
        Parameter: value
        Body:
            Var: tmp = 1;
            Var: value_;
            value_ = value;
            If (value == 0) Then
                Var: c[2];
                c[0] = "0";
                c[1] = "\\n";
            ElseIf (value == 1) Then
                For (i = tmp, i >= 0, -1) Do
                    c[i] = (value % 10) + 48;
                    value = value \\. 10.;
                EndFor.
                c[tmp+1] = "\\b";
            Else
                Var: c[3];
                c[0] = "0";
                c[1] = "\\n";
            EndIf.
        EndBody.
        Function: main
        Body:
            test(2293);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test300(self):
        input = """
        Function: fibonacci1
        Parameter: nEvents
        Body:
            For (i = 0, i < nEvents, 1) Do
                fibonacci(float_to_int(i*.25e5-.2.+(2*fibonacci(2 + 1 + i)\\.2e54)*2) + i%2);
                If i == nEvents\\5 Then Break;
                EndIf.
            EndFor.
        EndBody.
        Function: fibonacci2
        Body:
            Var: n;
            If (n == 1) || (n == 2) Then
                Return 1;
            EndIf.
            Return fibonacci(n - 1) + fibonacci(n - 2);
        EndBody.
        Function: main
        Body:
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))