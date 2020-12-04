
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    
	def test_215(self):
		input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (i = 3, i != 5, i*1) Do x=10000*2; EndFor.
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[For(Id('i'),IntLiteral(3),BinaryOp("""!=""",Id('i'),IntLiteral(5)),BinaryOp("""*""",Id('i'),IntLiteral(1)),([],[Assign(Id('x'),BinaryOp("""*""",IntLiteral(10000),IntLiteral(2)))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,215))

	def test_211(self):
		input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            a = (3 + 5) * 10 ; 
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('a'),BinaryOp("""*""",BinaryOp("""+""",IntLiteral(3),IntLiteral(5)),IntLiteral(10)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,211))

	def test_219(self):
		input = """Function: foo 
        Parameter: n, a[10]
        Body: 

        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None),VarDecl(Id('a'),[10],None)],([],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,219))

	def test_264(self):
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
		expect = Program([FuncDecl(Id('foo'),[],([VarDecl(Id('a'),[],IntLiteral(2))],[For(Id('i'),IntLiteral(0),BinaryOp("""<""",Id('a'),IntLiteral(15)),BinaryOp("""+""",Id('a'),IntLiteral(1)),([],[CallStmt(Id('writeln'),[StringLiteral("""15ph GG""")]),Assign(Id('i'),BinaryOp("""+""",Id('i'),IntLiteral(1))),If([(BinaryOp("""<""",Id('i'),IntLiteral(20)),[],[CallStmt(Id('write'),[StringLiteral("""GoPro""")])])],([],[]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,264))

	def test_254(self):
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
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([VarDecl(Id('x'),[],None)],[For(Id('i'),IntLiteral(0),BinaryOp("""<""",Id('i'),BinaryOp("""*""",CallExpr(Id('sqrt'),[Id('n')]),IntLiteral(2))),IntLiteral(1),([],[Assign(Id('x'),BinaryOp("""+""",Id('i'),Id('n'))),CallStmt(Id('writeln'),[BinaryOp("""*""",Id('x'),IntLiteral(3))])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,254))

	def test_213(self):
		input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            If a == 1 Then b = a + 5;
            ElseIf a == 6 Then b= a - 6; 
            EndIf.
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp("""==""",Id('a'),IntLiteral(1)),[],[Assign(Id('b'),BinaryOp("""+""",Id('a'),IntLiteral(5)))]),(BinaryOp("""==""",Id('a'),IntLiteral(6)),[],[Assign(Id('b'),BinaryOp("""-""",Id('a'),IntLiteral(6)))])],([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,213))

	def test_268(self):
		input = """
        Function: foo
        Body:
            For (i = 0, False, 1) Do
            EndFor.
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo'),[],([],[For(Id('i'),IntLiteral(0),BooleanLiteral(False),IntLiteral(1),([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,268))

	def test_271(self):
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
		expect = Program([FuncDecl(Id('test'),[],([VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[5,10],None)],[While(BinaryOp("""<""",Id('i'),IntLiteral(10)),([],[For(Id('j'),IntLiteral(1),BinaryOp("""<""",Id('j'),IntLiteral(10)),IntLiteral(1),([],[Assign(ArrayCell(Id('arr'),[Id('i'),Id('j')]),IntLiteral(1))])),Assign(Id('i'),BinaryOp("""+""",Id('i'),IntLiteral(2)))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,271))

	def test_288(self):
		input = """
        Function: multi
        Parameter: n
        Body:
            If (n == 0) Then Return 0;
            EndIf.
            Return n * sum(n - 1);
        EndBody.
        """
		expect = Program([FuncDecl(Id('multi'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp("""==""",Id('n'),IntLiteral(0)),[],[Return(IntLiteral(0))])],([],[])),Return(BinaryOp("""*""",Id('n'),CallExpr(Id('sum'),[BinaryOp("""-""",Id('n'),IntLiteral(1))])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,288))

	def test_275(self):
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
		expect = Program([FuncDecl(Id('foo'),[],([VarDecl(Id('i'),[],None),VarDecl(Id('j'),[],None),VarDecl(Id('k'),[],None),VarDecl(Id('l'),[],None)],[Dowhile(([],[Assign(Id('i'),BinaryOp("""+""",Id('i'),IntLiteral(1))),While(BinaryOp("""<""",Id('j'),IntLiteral(100)),([],[Dowhile(([],[Assign(Id('k'),BinaryOp("""+""",Id('k'),IntLiteral(1))),While(BinaryOp("""<""",Id('l'),IntLiteral(100)),([],[Assign(Id('l'),BinaryOp("""+""",Id('l'),IntLiteral(2))),While(BinaryOp("""<""",Id('l'),IntLiteral(10)),([],[Assign(Id('l'),BinaryOp("""+""",Id('l'),IntLiteral(3))),While(BinaryOp("""<""",Id('l'),IntLiteral(1)),([],[Assign(Id('l'),BinaryOp("""+""",Id('l'),IntLiteral(4))),While(BinaryOp("""<""",Id('l'),FloatLiteral(0.1)),([],[Assign(Id('l'),BinaryOp("""+""",Id('l'),IntLiteral(5))),While(BinaryOp("""<""",Id('l'),FloatLiteral(0.01)),([],[Assign(Id('l'),BinaryOp("""+""",Id('l'),IntLiteral(6))),While(BinaryOp("""<""",Id('l'),FloatLiteral(0.001)),([],[Assign(Id('l'),BinaryOp("""+""",Id('l'),IntLiteral(7)))]))]))]))]))]))]))]),BinaryOp("""<""",Id('k'),IntLiteral(100))),Assign(Id('j'),BinaryOp("""+""",Id('j'),IntLiteral(3)))]))]),BinaryOp("""<""",BinaryOp("""+""",BinaryOp("""+""",BinaryOp("""+""",Id('i'),Id('j')),Id('k')),Id('l')),CallExpr(Id('foo'),[IntLiteral(2)]))),CallStmt(Id('writeln'),[Id('n')])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,275))

	def test_285(self):
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
		expect = Program([FuncDecl(Id('test'),[],([VarDecl(Id('flag'),[],IntLiteral(0))],[Dowhile(([],[While(UnaryOp("""!""",Id('flag')),([],[]))]),BooleanLiteral(True))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,285))

	def test_209(self):
		input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c = x <= 0; 
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('c'),BinaryOp("""<=""",Id('x'),IntLiteral(0)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,209))

	def test_249(self):
		input = """Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                If x==1 Then Return;
                Else Break;
                EndIf.
            EndWhile.
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[While(BinaryOp(""">""",Id('x'),IntLiteral(1)),([],[If([(BinaryOp("""==""",Id('x'),IntLiteral(1)),[],[Return(None)])],([],[Break()]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,249))

	def test_263(self):
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
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([VarDecl(Id('i'),[],IntLiteral(0))],[For(Id('i'),Id('a'),BinaryOp("""<=""",Id('i'),BinaryOp("""+""",BinaryOp("""-""",BinaryOp("""*""",BinaryOp("""+""",BinaryOp("""-""",BinaryOp("""*""",Id('n'),Id('n')),BinaryOp("""*""",IntLiteral(2),Id('n'))),IntLiteral(1)),IntLiteral(2)),BinaryOp("""+""",BinaryOp("""*""",IntLiteral(2),Id('n')),IntLiteral(1))),BinaryOp("""*""",IntLiteral(4),BinaryOp("""+""",IntLiteral(1),BinaryOp("""*""",IntLiteral(2),Id('n')))))),IntLiteral(1),([],[CallStmt(Id('print'),[BinaryOp("""*""",IntLiteral(3),Id('i'))])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,263))

	def test_239(self):
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
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([VarDecl(Id('i'),[],IntLiteral(0))],[While(BinaryOp("""<""",Id('i'),IntLiteral(5)),([VarDecl(Id('k'),[],IntLiteral(100))],[Assign(ArrayCell(Id('a'),[Id('i')]),BinaryOp("""-""",BinaryOp("""+.""",Id('b'),FloatLiteral(1.0)),BinaryOp("""*""",Id('k'),ArrayCell(Id('a'),[BinaryOp("""+""",Id('i'),IntLiteral(1))])))),Assign(Id('i'),BinaryOp("""+""",Id('i'),IntLiteral(5)))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,239))

	def test_221(self):
		input = """Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                Return 0;
            Else
                Return n * fact (n - 2);
            EndIf.
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp("""==""",Id('n'),IntLiteral(0)),[],[Return(IntLiteral(0))])],([],[Return(BinaryOp("""*""",Id('n'),CallExpr(Id('fact'),[BinaryOp("""-""",Id('n'),IntLiteral(2))])))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,221))

	def test_227(self):
		input = """Function: foo 
        Parameter: n
        Body: 
            If n != 0 Then
                Return 0;
            Else
                Return (n-1) * (n-2) * (n-3) * (n-4);
            EndIf.
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp("""!=""",Id('n'),IntLiteral(0)),[],[Return(IntLiteral(0))])],([],[Return(BinaryOp("""*""",BinaryOp("""*""",BinaryOp("""*""",BinaryOp("""-""",Id('n'),IntLiteral(1)),BinaryOp("""-""",Id('n'),IntLiteral(2))),BinaryOp("""-""",Id('n'),IntLiteral(3))),BinaryOp("""-""",Id('n'),IntLiteral(4))))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,227))

	def test_242(self):
		input = """Function: foo 
        Parameter: n
        Body: 
            Var: i = 100;
            While i < 5000 Do

            EndWhile.
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([VarDecl(Id('i'),[],IntLiteral(100))],[While(BinaryOp("""<""",Id('i'),IntLiteral(5000)),([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,242))

	def test_248(self):
		input = """Function: foo 
        Parameter: n
        Body:
            Var: r = 10., v;
            r = 10.;
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([VarDecl(Id('r'),[],FloatLiteral(10.0)),VarDecl(Id('v'),[],None)],[Assign(Id('r'),FloatLiteral(10.0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,248))

	def test_204(self):
		input = """
        Function: foo
        Parameter: n
        Body:
            c = -.x;
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('c'),UnaryOp("""-.""",Id('x')))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,204))

	def test_267(self):
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
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('t'),[],None)],([],[While(BinaryOp("""<""",Id('t'),IntLiteral(10)),([],[If([(BinaryOp("""%""",Id('t'),IntLiteral(2)),[],[Assign(Id('t'),BinaryOp("""+""",Id('t'),IntLiteral(10)))])],([],[Assign(Id('t'),BinaryOp("""+""",Id('t'),IntLiteral(5)))]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,267))

	def test_203(self):
		input = """ 
        Function: foo 
        Parameter: x
        Body: 
            c = !a; 
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('x'),[],None)],([],[Assign(Id('c'),UnaryOp("""!""",Id('a')))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,203))

	def test_207(self):
		input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c =a + 5; 
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('c'),BinaryOp("""+""",Id('a'),IntLiteral(5)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,207))

	def test_201(self):
		input = """Var: x[1];"""
		expect = Program([VarDecl(Id('x'),[1],None)])
		self.assertTrue(TestAST.checkASTGen(input,expect,201))

	def test_274(self):
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
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([VarDecl(Id('i'),[],IntLiteral(0))],[While(BinaryOp("""<""",Id('i'),IntLiteral(10)),([],[Assign(Id('i'),BinaryOp("""+""",Id('i'),IntLiteral(1))),If([(BinaryOp("""==""",Id('i'),IntLiteral(10)),[],[CallStmt(Id('write'),[StringLiteral("""MVP""")])])],([],[]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,274))

	def test_224(self):
		input = """Function: foo 
        Parameter: n
        Body: 
            While x<10000000000 Do
                If x!=100000 Then Return;
                Else Continue;
                EndIf.
            EndWhile.
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[While(BinaryOp("""<""",Id('x'),IntLiteral(10000000000)),([],[If([(BinaryOp("""!=""",Id('x'),IntLiteral(100000)),[],[Return(None)])],([],[Continue()]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,224))

	def test_214(self):
		input = """ Function: foo 
        Parameter: n 
        Body: 
            If !a Then b = (5 + 10) * 100; 
            Else c= 500000 ; 
            EndIf. 
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[If([(UnaryOp("""!""",Id('a')),[],[Assign(Id('b'),BinaryOp("""*""",BinaryOp("""+""",IntLiteral(5),IntLiteral(10)),IntLiteral(100)))])],([],[Assign(Id('c'),IntLiteral(500000))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,214))

	def test_297(self):
		input = """
        Var: s = 0, arr[2] = {1,2};
        Function: assignmentKTLT
        Parameter: hp1, hp2, d
        Body:
            Var: p1, p2;
            Var: h1;
            Var: armor = False;
            Var: pR;
            p1 = hp1 * (1000 - d) \. int_of_float(1000);
            p2 = (hp2 * d) \. int_of_float(1000);
            h1 = (hp1 + hp2) % 100;
            h2 = (h1*hp2) % 100;

            If (hp2 == 888) Then armor = True;
            EndIf.
            If hp1 == 777 && ((p1 < p2) || (h1 < h2)) && (armor == False) Then
                Var: e = 1;
                d = e;
                p1 = hp1 *. (1000 - d) \. float(1000);
                p2 = (hp2 *. d) \. float(1000);
            EndIf.
            pR = (h1*p1 - h2 * p2) \. (h1*p1 + h2 * p2);
            print(pR);
        EndBody.
        Function: main
        Body:
            assignmentKTLT(544,290,600);
        EndBody.
        """
		expect = Program([VarDecl(Id('s'),[],IntLiteral(0)),VarDecl(Id('arr'),[2],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),FuncDecl(Id('assignmentKTLT'),[VarDecl(Id('hp1'),[],None),VarDecl(Id('hp2'),[],None),VarDecl(Id('d'),[],None)],([VarDecl(Id('p1'),[],None),VarDecl(Id('p2'),[],None),VarDecl(Id('h1'),[],None),VarDecl(Id('armor'),[],BooleanLiteral(False)),VarDecl(Id('pR'),[],None)],[Assign(Id('p1'),BinaryOp("""\.""",BinaryOp("""*""",Id('hp1'),BinaryOp("""-""",IntLiteral(1000),Id('d'))),CallExpr(Id('int_of_float'),[IntLiteral(1000)]))),Assign(Id('p2'),BinaryOp("""\.""",BinaryOp("""*""",Id('hp2'),Id('d')),CallExpr(Id('int_of_float'),[IntLiteral(1000)]))),Assign(Id('h1'),BinaryOp("""%""",BinaryOp("""+""",Id('hp1'),Id('hp2')),IntLiteral(100))),Assign(Id('h2'),BinaryOp("""%""",BinaryOp("""*""",Id('h1'),Id('hp2')),IntLiteral(100))),If([(BinaryOp("""==""",Id('hp2'),IntLiteral(888)),[],[Assign(Id('armor'),BooleanLiteral(True))])],([],[])),If([(BinaryOp("""==""",Id('hp1'),BinaryOp("""&&""",BinaryOp("""&&""",IntLiteral(777),BinaryOp("""||""",BinaryOp("""<""",Id('p1'),Id('p2')),BinaryOp("""<""",Id('h1'),Id('h2')))),BinaryOp("""==""",Id('armor'),BooleanLiteral(False)))),[VarDecl(Id('e'),[],IntLiteral(1))],[Assign(Id('d'),Id('e')),Assign(Id('p1'),BinaryOp("""\.""",BinaryOp("""*.""",Id('hp1'),BinaryOp("""-""",IntLiteral(1000),Id('d'))),CallExpr(Id('float'),[IntLiteral(1000)]))),Assign(Id('p2'),BinaryOp("""\.""",BinaryOp("""*.""",Id('hp2'),Id('d')),CallExpr(Id('float'),[IntLiteral(1000)])))])],([],[])),Assign(Id('pR'),BinaryOp("""\.""",BinaryOp("""-""",BinaryOp("""*""",Id('h1'),Id('p1')),BinaryOp("""*""",Id('h2'),Id('p2'))),BinaryOp("""+""",BinaryOp("""*""",Id('h1'),Id('p1')),BinaryOp("""*""",Id('h2'),Id('p2'))))),CallStmt(Id('print'),[Id('pR')])])),FuncDecl(Id('main'),[],([],[CallStmt(Id('assignmentKTLT'),[IntLiteral(544),IntLiteral(290),IntLiteral(600)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,297))

	def test_281(self):
		input = """
        Var: a;
        Function: foo
        Body:
            Var: zzHQKzz[2][3][4][5] = {{12345, 41e+5, 3.14},{"Yasuo", "Leesin", "Garen"}}, a[234], c;
        EndBody.
        """
		expect = Program([VarDecl(Id('a'),[],None),FuncDecl(Id('foo'),[],([VarDecl(Id('zzHQKzz'),[2,3,4,5],ArrayLiteral([ArrayLiteral([IntLiteral(12345),FloatLiteral(4100000.0),FloatLiteral(3.14)]),ArrayLiteral([StringLiteral("""Yasuo"""),StringLiteral("""Leesin"""),StringLiteral("""Garen""")])])),VarDecl(Id('a'),[234],None),VarDecl(Id('c'),[],None)],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,281))

	def test_208(self):
		input = """ Function: foo 
        Parameter: n 
        Body: 
            If a Then b = 1; EndIf.
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[If([(Id('a'),[],[Assign(Id('b'),IntLiteral(1))])],([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,208))

	def test_298(self):
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
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[5],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('i'),[],IntLiteral(45))],[While(BinaryOp("""<""",Id('i'),IntLiteral(100)),([],[Assign(ArrayCell(Id('a'),[Id('i')]),BinaryOp("""+.""",BinaryOp("""*""",Id('b'),IntLiteral(2)),FloatLiteral(1.0))),Assign(Id('i'),BinaryOp("""+""",BinaryOp("""*""",Id('i'),IntLiteral(2)),IntLiteral(3)))])),Return(ArrayCell(Id('a'),[IntLiteral(35)]))])),FuncDecl(Id('test'),[VarDecl(Id('arr'),[211,930],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp("""<""",Id('i'),ArrayCell(Id('arr'),[IntLiteral(20),IntLiteral(2)])),IntLiteral(1),([],[If([(BinaryOp("""<=""",CallExpr(Id('foo'),[Id('i')]),BinaryOp("""\\""",CallExpr(Id('foo'),[BinaryOp("""+""",Id('i'),IntLiteral(1))]),CallExpr(Id('foo'),[CallExpr(Id('foo'),[Id('i')])]))),[],[Return(None)]),(BinaryOp("""<=""",CallExpr(Id('foo'),[BinaryOp("""\\""",Id('i'),IntLiteral(2))]),BinaryOp("""\\""",CallExpr(Id('foo'),[BinaryOp("""-""",Id('i'),IntLiteral(1))]),CallExpr(Id('foo'),[CallExpr(Id('foo'),[BinaryOp("""\\""",BinaryOp("""*""",IntLiteral(7),Id('i')),IntLiteral(2))])]))),[],[Break()]),(BinaryOp("""<=""",CallExpr(Id('foo'),[IntLiteral(3)]),BinaryOp("""\\""",CallExpr(Id('foo'),[BinaryOp("""+""",Id('i'),IntLiteral(1))]),CallExpr(Id('foo'),[CallExpr(Id('foo'),[BinaryOp("""\\""",BinaryOp("""*""",IntLiteral(7749),Id('i')),IntLiteral(2))])]))),[],[Break()]),(CallExpr(Id('foo'),[IntLiteral(45)]),[],[CallStmt(Id('print'),[StringLiteral("""2 giam khao da cuoi""")])])],([],[While(UnaryOp("""!""",BooleanLiteral(False)),([],[If([(BinaryOp("""==""",UnaryOp("""!""",BooleanLiteral(False)),BooleanLiteral(True)),[],[CallStmt(Id('print'),[BinaryOp("""\\""",CallExpr(Id('foo'),[BinaryOp("""+""",BinaryOp("""*""",Id('i'),Id('i')),IntLiteral(111))]),CallExpr(Id('foo'),[CallExpr(Id('foo'),[BinaryOp("""\\""",BinaryOp("""*""",ArrayCell(Id('arr'),[IntLiteral(2),IntLiteral(1)]),Id('i')),IntLiteral(2))])]))])])],([],[Continue()]))]))]))]))])),FuncDecl(Id('main'),[],([],[CallStmt(Id('test'),[IntLiteral(2293)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,298))

	def test_278(self):
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
		expect = Program([FuncDecl(Id('foo'),[],([VarDecl(Id('i'),[],IntLiteral(0))],[Dowhile(([],[CallStmt(Id('writeln'),[Id('i')]),Assign(Id('i'),BinaryOp("""+""",Id('i'),IntLiteral(1)))]),BinaryOp("""<""",Id('i'),IntLiteral(10)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,278))

	def test_216(self):
		input = """
        Function: foo 
        Parameter: n 
        Body: 
            foo(2 + x, 4. \. y); 
            goo ();
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[CallStmt(Id('foo'),[BinaryOp("""+""",IntLiteral(2),Id('x')),BinaryOp("""\.""",FloatLiteral(4.0),Id('y'))]),CallStmt(Id('goo'),[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,216))

	def test_295(self):
		input = """
        Var: x;
        Function: test
        Body:
            Var: body;
            Var: endBody;
        EndBody.
        """
		expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('test'),[],([VarDecl(Id('body'),[],None),VarDecl(Id('endBody'),[],None)],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,295))

	def test_241(self):
		input = """Function: foo 
        Parameter: n
        Body: 
            While x >1 Do
                If x==1 Then Return;
                EndIf.
            EndWhile.
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[While(BinaryOp(""">""",Id('x'),IntLiteral(1)),([],[If([(BinaryOp("""==""",Id('x'),IntLiteral(1)),[],[Return(None)])],([],[]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,241))

	def test_243(self):
		input = """Function: foo 
        Parameter: n
        Body: 
            While i < 5 Do
                Var: b = 10;
                a[i] = b +. 1.0;
                i = i + 2;
            EndWhile.
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[While(BinaryOp("""<""",Id('i'),IntLiteral(5)),([VarDecl(Id('b'),[],IntLiteral(10))],[Assign(ArrayCell(Id('a'),[Id('i')]),BinaryOp("""+.""",Id('b'),FloatLiteral(1.0))),Assign(Id('i'),BinaryOp("""+""",Id('i'),IntLiteral(2)))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,243))

	def test_256(self):
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
		expect = Program([FuncDecl(Id('test'),[],([VarDecl(Id('i'),[],IntLiteral(21))],[If([(BinaryOp("""==""",Id('i'),IntLiteral(10)),[],[]),(BinaryOp("""==""",Id('i'),IntLiteral(15)),[],[]),(BinaryOp("""==""",Id('i'),IntLiteral(20)),[],[])],([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,256))

	def test_261(self):
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
		expect = Program([FuncDecl(Id('foo'),[],([VarDecl(Id('x'),[],BooleanLiteral(False)),VarDecl(Id('a'),[],None)],[Assign(Id('a'),UnaryOp("""!""",BooleanLiteral(True))),For(Id('i'),IntLiteral(0),BinaryOp("""==""",Id('x'),Id('c')),IntLiteral(1),([],[Assign(Id('x'),BooleanLiteral(False))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,261))

	def test_212(self):
		input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c =x && y; 
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('c'),BinaryOp("""&&""",Id('x'),Id('y')))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,212))

	def test_253(self):
		input = """
        Function: test
        Body:
            Var: arr[1] = {3,4}, x = 4.5, y = 5.;
            If arr[1] >. x Then arr[1] = y;
            EndIf.
        EndBody.
        """
		expect = Program([FuncDecl(Id('test'),[],([VarDecl(Id('arr'),[1],ArrayLiteral([IntLiteral(3),IntLiteral(4)])),VarDecl(Id('x'),[],FloatLiteral(4.5)),VarDecl(Id('y'),[],FloatLiteral(5.0))],[If([(BinaryOp(""">.""",ArrayCell(Id('arr'),[IntLiteral(1)]),Id('x')),[],[Assign(ArrayCell(Id('arr'),[IntLiteral(1)]),Id('y'))])],([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,253))

	def test_205(self):
		input = """
        Function:  a
        Body:
            Var: s = "hi_hi";
            Var: n = "nice";
        EndBody.
        """
		expect = Program([FuncDecl(Id('a'),[],([VarDecl(Id('s'),[],StringLiteral("""hi_hi""")),VarDecl(Id('n'),[],StringLiteral("""nice"""))],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,205))

	def test_226(self):
		input = """Function: foo 
        Parameter: n
        Body: 
            Do
                x = a + b - c * d + e - f * g - 123455;
                y =  a + n + h - y - e - u + e * m;
            While x > 0 + 326264 +  x
            EndDo.
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[Dowhile(([],[Assign(Id('x'),BinaryOp("""-""",BinaryOp("""-""",BinaryOp("""+""",BinaryOp("""-""",BinaryOp("""+""",Id('a'),Id('b')),BinaryOp("""*""",Id('c'),Id('d'))),Id('e')),BinaryOp("""*""",Id('f'),Id('g'))),IntLiteral(123455))),Assign(Id('y'),BinaryOp("""+""",BinaryOp("""-""",BinaryOp("""-""",BinaryOp("""-""",BinaryOp("""+""",BinaryOp("""+""",Id('a'),Id('n')),Id('h')),Id('y')),Id('e')),Id('u')),BinaryOp("""*""",Id('e'),Id('m'))))]),BinaryOp(""">""",Id('x'),BinaryOp("""+""",BinaryOp("""+""",IntLiteral(0),IntLiteral(326264)),Id('x'))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,226))

	def test_265(self):
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
		expect = Program([FuncDecl(Id('foo'),[],([],[While(BooleanLiteral(True),([],[While(BooleanLiteral(False),([],[While(BooleanLiteral(True),([],[]))]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,265))

	def test_282(self):
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
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp("""<""",Id('i'),IntLiteral(10)),IntLiteral(2),([],[Break()])),Assign(Id('a'),BinaryOp("""*""",BinaryOp("""+""",Id('a'),Id('b')),BinaryOp("""-""",Id('a'),Id('b')))),Assign(Id('b'),BinaryOp("""*""",BinaryOp("""+""",Id('a'),Id('b')),BinaryOp("""-""",Id('b'),Id('a')))),If([(BinaryOp("""!=""",BinaryOp("""+""",Id('a'),Id('b')),IntLiteral(0)),[],[CallStmt(Id('writeln'),[BinaryOp("""+""",Id('a'),Id('b'))])])],([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,282))

	def test_225(self):
		input = """Function: foo 
        Parameter: n 
        Body: 
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,225))

	def test_229(self):
		input = """
        Var: a = 5;
        Var: b = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[100];
        """
		expect = Program([VarDecl(Id('a'),[],IntLiteral(5)),VarDecl(Id('b'),[],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],IntLiteral(6)),VarDecl(Id('e'),[],None),VarDecl(Id('f'),[],None),VarDecl(Id('m'),[],None),VarDecl(Id('n'),[100],None)])
		self.assertTrue(TestAST.checkASTGen(input,expect,229))

	def test_251(self):
		input = """Function: foo 
        Parameter: n
        Body: 
        EndBody.
        Function: goo 
        Parameter: n
        Body: 
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[])),FuncDecl(Id('goo'),[VarDecl(Id('n'),[],None)],([],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,251))

	def test_257(self):
		input = """
        Function: test
        Body:   
            For (i = 0, i < 10, 2) Do
                writeln(i);
            EndFor.
        EndBody.
        """
		expect = Program([FuncDecl(Id('test'),[],([],[For(Id('i'),IntLiteral(0),BinaryOp("""<""",Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('writeln'),[Id('i')])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,257))

	def test_273(self):
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
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([VarDecl(Id('i'),[],IntLiteral(0))],[While(BinaryOp("""<=""",Id('i'),Id('n')),([],[If([(BinaryOp("""==""",Id('i'),Id('n')),[],[CallStmt(Id('writeln'),[Id('n')]),Return(None)])],([],[])),Assign(Id('i'),BinaryOp("""+""",Id('i'),IntLiteral(1)))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,273))

	def test_217(self):
		input = """Function: foo 
        Parameter: n 
        Body: 
        x = 10;
        x = (x - 5) * n; 
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('x'),IntLiteral(10)),Assign(Id('x'),BinaryOp("""*""",BinaryOp("""-""",Id('x'),IntLiteral(5)),Id('n')))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,217))

	def test_270(self):
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
		expect = Program([FuncDecl(Id('test'),[VarDecl(Id('m'),[],None),VarDecl(Id('n'),[],None),VarDecl(Id('o'),[],None),VarDecl(Id('p'),[],None)],([VarDecl(Id('x'),[],None)],[While(BinaryOp("""<=""",Id('m'),IntLiteral(2)),([],[While(BinaryOp(""">=""",Id('n'),IntLiteral(1)),([],[While(BinaryOp("""<=""",Id('o'),Id('n')),([],[Assign(Id('o'),BinaryOp("""-""",Id('o'),IntLiteral(1))),While(BinaryOp("""<=""",Id('p'),IntLiteral(2)),([],[Assign(Id('p'),BinaryOp("""+""",Id('p'),IntLiteral(1))),While(BinaryOp("""<=""",Id('p'),IntLiteral(2)),([],[Assign(Id('p'),BinaryOp("""+""",Id('p'),IntLiteral(1))),While(BinaryOp("""<=""",Id('p'),IntLiteral(2)),([],[Assign(Id('p'),BinaryOp("""+""",Id('p'),IntLiteral(1))),While(BinaryOp("""<=""",Id('p'),IntLiteral(2)),([],[Assign(Id('p'),BinaryOp("""+""",Id('p'),IntLiteral(1))),While(BinaryOp("""<=""",Id('p'),IntLiteral(2)),([],[Assign(Id('p'),BinaryOp("""+""",Id('p'),IntLiteral(1))),While(BinaryOp("""<=""",Id('p'),IntLiteral(2)),([],[Assign(Id('p'),BinaryOp("""+""",Id('p'),IntLiteral(1)))]))]))]))]))]))]))])),Assign(Id('x'),BooleanLiteral(True)),Assign(Id('n'),BinaryOp("""-""",Id('n'),IntLiteral(1)))])),Assign(Id('x'),BinaryOp("""*""",BinaryOp("""*""",BinaryOp("""*""",Id('m'),Id('n')),Id('p')),Id('o'))),Assign(Id('m'),BinaryOp("""+""",Id('m'),IntLiteral(1)))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,270))

	def test_279(self):
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
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([VarDecl(Id('a'),[],IntLiteral(0))],[Dowhile(([],[If([(BinaryOp("""&&""",BinaryOp("""!=""",Id('n'),IntLiteral(3)),BinaryOp("""!=""",BinaryOp("""%""",Id('n'),Id('i')),IntLiteral(0))),[],[Assign(Id('a'),IntLiteral(1))])],([],[])),Assign(Id('i'),BinaryOp("""+""",Id('i'),IntLiteral(2)))]),BinaryOp("""<=""",Id('i'),BinaryOp("""*""",Id('n'),Id('n'))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,279))

	def test_294(self):
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
		expect = Program([FuncDecl(Id('foo1'),[],([],[CallStmt(Id('foo'),[])])),FuncDecl(Id('foo2'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None)],([],[CallStmt(Id('writeln'),[BinaryOp("""+.""",BinaryOp("""-.""",BinaryOp("""+.""",Id('a'),Id('b')),Id('c')),Id('d'))])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,294))

	def test_237(self):
		input = """Function: foo 
        Parameter: n
        Body: 
            Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
            x1 = a[3-foo(3)];
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[1,3],ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(12),IntLiteral(1)]),ArrayLiteral([FloatLiteral(12.0),FloatLiteral(12000.0)])]),ArrayLiteral([IntLiteral(23)]),ArrayLiteral([IntLiteral(13),IntLiteral(32)])]))],[Assign(Id('x1'),ArrayCell(Id('a'),[BinaryOp("""-""",IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(3)]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,237))

	def test_299(self):
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
		expect = Program([VarDecl(Id('c'),[1000],None),FuncDecl(Id('test99'),[VarDecl(Id('value'),[],None)],([VarDecl(Id('tmp'),[],IntLiteral(1)),VarDecl(Id('value_'),[],None)],[Assign(Id('value_'),Id('value')),If([(BinaryOp("""==""",Id('value'),IntLiteral(0)),[VarDecl(Id('c'),[2],None)],[Assign(ArrayCell(Id('c'),[IntLiteral(0)]),StringLiteral("""0""")),Assign(ArrayCell(Id('c'),[IntLiteral(1)]),StringLiteral("""\\n"""))]),(BinaryOp("""==""",Id('value'),IntLiteral(1)),[],[For(Id('i'),Id('tmp'),BinaryOp(""">=""",Id('i'),IntLiteral(0)),UnaryOp("""-""",IntLiteral(1)),([],[Assign(ArrayCell(Id('c'),[Id('i')]),BinaryOp("""+""",BinaryOp("""%""",Id('value'),IntLiteral(10)),IntLiteral(48))),Assign(Id('value'),BinaryOp("""\\.""",Id('value'),FloatLiteral(10.0)))])),Assign(ArrayCell(Id('c'),[BinaryOp("""+""",Id('tmp'),IntLiteral(1))]),StringLiteral("""\\b"""))])],([VarDecl(Id('c'),[3],None)],[Assign(ArrayCell(Id('c'),[IntLiteral(0)]),StringLiteral("""0""")),Assign(ArrayCell(Id('c'),[IntLiteral(1)]),StringLiteral("""\\n"""))]))])),FuncDecl(Id('main'),[],([],[CallStmt(Id('test'),[IntLiteral(2293)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,299))

	def test_258(self):
		input = """
        Function: test
        Body:
            Var: abc = 1, cde = 2, efg = 3;
            If abc + cde == efg Then Else efg = 3;
            EndIf.
        EndBody.
        """
		expect = Program([FuncDecl(Id('test'),[],([VarDecl(Id('abc'),[],IntLiteral(1)),VarDecl(Id('cde'),[],IntLiteral(2)),VarDecl(Id('efg'),[],IntLiteral(3))],[If([(BinaryOp("""==""",BinaryOp("""+""",Id('abc'),Id('cde')),Id('efg')),[],[])],([],[Assign(Id('efg'),IntLiteral(3))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,258))

	def test_300(self):
		input = """
        Function: fibonacci1
        Parameter: nEvents
        Body:
            For (i = 0, i < nEvents, 1) Do
                fibonacci(float_to_int(i*.25e5-.2.+(2*fibonacci(2 + 1 + i)\.2e54)*2) + i%2);
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
		expect = Program([FuncDecl(Id('fibonacci1'),[VarDecl(Id('nEvents'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp("""<""",Id('i'),Id('nEvents')),IntLiteral(1),([],[CallStmt(Id('fibonacci'),[BinaryOp("""+""",CallExpr(Id('float_to_int'),[BinaryOp("""+""",BinaryOp("""-.""",BinaryOp("""*.""",Id('i'),FloatLiteral(2500000.0)),FloatLiteral(2.0)),BinaryOp("""*""",BinaryOp("""\.""",BinaryOp("""*""",IntLiteral(2),CallExpr(Id('fibonacci'),[BinaryOp("""+""",BinaryOp("""+""",IntLiteral(2),IntLiteral(1)),Id('i'))])),FloatLiteral(2e+54)),IntLiteral(2)))]),BinaryOp("""%""",Id('i'),IntLiteral(2)))]),If([(BinaryOp("""==""",Id('i'),BinaryOp("""\\""",Id('nEvents'),IntLiteral(5))),[],[Break()])],([],[]))]))])),FuncDecl(Id('fibonacci2'),[],([VarDecl(Id('n'),[],None)],[If([(BinaryOp("""||""",BinaryOp("""==""",Id('n'),IntLiteral(1)),BinaryOp("""==""",Id('n'),IntLiteral(2))),[],[Return(IntLiteral(1))])],([],[])),Return(BinaryOp("""+""",CallExpr(Id('fibonacci'),[BinaryOp("""-""",Id('n'),IntLiteral(1))]),CallExpr(Id('fibonacci'),[BinaryOp("""-""",Id('n'),IntLiteral(2))])))])),FuncDecl(Id('main'),[],([],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,300))

	def test_244(self):
		input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (i = 0, i != 5, i*1) Do x=6; EndFor.
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp("""!=""",Id('i'),IntLiteral(5)),BinaryOp("""*""",Id('i'),IntLiteral(1)),([],[Assign(Id('x'),IntLiteral(6))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,244))

	def test_280(self):
		input = """
        Function: foo
        Body:
            Var: x = 1;
            Do
            While x EndDo.
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo'),[],([VarDecl(Id('x'),[],IntLiteral(1))],[Dowhile(([],[]),Id('x'))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,280))

	def test_202(self):
		input = """Var: y;"""
		expect = Program([VarDecl(Id('y'),[],None)])
		self.assertTrue(TestAST.checkASTGen(input,expect,202))

	def test_232(self):
		input = """
        Var: b[2][3]={{1,2,3},{4,5,6}};
        Var: a[100] = {1,2,3};
        Var: a[100000][1000] = {{2,3},{4,5,6,7,8,9,10}};
        """
		expect = Program([VarDecl(Id('b'),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id('a'),[100],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),VarDecl(Id('a'),[100000,1000],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,232))

	def test_292(self):
		input = """
        Function: foo
        Parameter: n
        Body:
            If (n != 10000) Then Return (n - 9999);
            EndIf.
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp("""!=""",Id('n'),IntLiteral(10000)),[],[Return(BinaryOp("""-""",Id('n'),IntLiteral(9999)))])],([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,292))

	def test_235(self):
		input = """Function: foo 
        Parameter: n
        Body: 
            x1 = a[3-foo(3)];
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('x1'),ArrayCell(Id('a'),[BinaryOp("""-""",IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(3)]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,235))

	def test_262(self):
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
		expect = Program([FuncDecl(Id('foo'),[],([VarDecl(Id('arr'),[100,100,100],None)],[For(Id('i'),IntLiteral(0),BinaryOp("""<""",Id('i'),IntLiteral(100)),IntLiteral(2),([],[For(Id('j'),IntLiteral(0),BinaryOp("""<""",Id('j'),IntLiteral(100)),IntLiteral(2),([],[For(Id('k'),IntLiteral(0),BinaryOp("""<""",Id('k'),IntLiteral(100)),IntLiteral(2),([],[Assign(ArrayCell(Id('arr'),[Id('i'),Id('j'),Id('k')]),IntLiteral(0))]))]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,262))

	def test_238(self):
		input = """Function: foo 
        Parameter: n
        Body: 
            Var: i = 0;
            While i < 5 Do
                b[i] = i +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([VarDecl(Id('i'),[],IntLiteral(0))],[While(BinaryOp("""<""",Id('i'),IntLiteral(5)),([],[Assign(ArrayCell(Id('b'),[Id('i')]),BinaryOp("""+.""",Id('i'),FloatLiteral(1.0))),Assign(Id('i'),BinaryOp("""+""",Id('i'),IntLiteral(1)))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,238))

	def test_289(self):
		input = """
        Function: foo1
        Body:

        EndBody.
        Function: foo2
        Body:
            foo2(2);
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo1'),[],([],[])),FuncDecl(Id('foo2'),[],([],[CallStmt(Id('foo2'),[IntLiteral(2)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,289))

	def test_276(self):
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
		expect = Program([FuncDecl(Id('lcd'),[VarDecl(Id('n'),[],None)],([VarDecl(Id('i'),[],None)],[Assign(Id('i'),BinaryOp("""-""",Id('n'),IntLiteral(1))),While(BinaryOp("""!=""",BinaryOp("""%""",Id('n'),Id('i')),IntLiteral(0)),([],[Assign(Id('i'),BinaryOp("""-""",Id('i'),IntLiteral(1)))])),CallStmt(Id('writeln'),[Id('i')])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,276))

	def test_286(self):
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
		expect = Program([FuncDecl(Id('foo'),[],([],[Assign(Id('a'),BinaryOp("""+""",BinaryOp("""*""",CallExpr(Id('foo'),[IntLiteral(100)]),IntLiteral(28)),IntLiteral(234)))])),FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,286))

	def test_287(self):
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
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[For(Id('i'),IntLiteral(1),BinaryOp("""<""",Id('i'),IntLiteral(2)),IntLiteral(1),([],[If([(BinaryOp("""!=""",BinaryOp("""%""",Id('i'),IntLiteral(2)),IntLiteral(0)),[],[CallStmt(Id('write'),[Id('i')])])],([],[])),Assign(Id('n'),BinaryOp("""-""",Id('n'),Id('i')))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,287))

	def test_247(self):
		input = """Function: test
        Parameter: n
        Body:
            If n > 10 Then
                Return ;
                If n > 11 Then Return n;
                EndIf.
                
            EndIf.
        EndBody."""
		expect = Program([FuncDecl(Id('test'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp(""">""",Id('n'),IntLiteral(10)),[],[Return(None),If([(BinaryOp(""">""",Id('n'),IntLiteral(11)),[],[Return(Id('n'))])],([],[]))])],([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,247))

	def test_231(self):
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
		expect = Program([FuncDecl(Id('test'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp("""!=""",Id('n'),IntLiteral(10)),[],[Return(FloatLiteral(3.1415919191))])],([],[Return(Id('false'))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,231))

	def test_222(self):
		input = """Function: foo 
        Parameter: n
        Body: 
            x = 10;
            y = 15 - x;
            z = x * y;
            fact (z);
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('x'),IntLiteral(10)),Assign(Id('y'),BinaryOp("""-""",IntLiteral(15),Id('x'))),Assign(Id('z'),BinaryOp("""*""",Id('x'),Id('y'))),CallStmt(Id('fact'),[Id('z')])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,222))

	def test_293(self):
		input = """
        Function: foo
        Body:
            Return True;
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo'),[],([],[Return(BooleanLiteral(True))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,293))

	def test_210(self):
		input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            x = y < 100;
            x = !a; 
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('x'),BinaryOp("""<""",Id('y'),IntLiteral(100))),Assign(Id('x'),UnaryOp("""!""",Id('a')))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,210))

	def test_250(self):
		input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (a_a = 0, i != 5, i*1) Do x=6; EndFor.
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[For(Id('a_a'),IntLiteral(0),BinaryOp("""!=""",Id('i'),IntLiteral(5)),BinaryOp("""*""",Id('i'),IntLiteral(1)),([],[Assign(Id('x'),IntLiteral(6))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,250))

	def test_277(self):
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
		expect = Program([FuncDecl(Id('foo'),[],([VarDecl(Id('n'),[],IntLiteral(5)),VarDecl(Id('s'),[],IntLiteral(5))],[Dowhile(([],[Assign(Id('n'),BinaryOp("""+""",Id('n'),IntLiteral(1))),Dowhile(([],[If([(BinaryOp("""==""",BinaryOp("""%""",Id('n'),IntLiteral(2)),IntLiteral(0)),[],[Assign(Id('s'),BinaryOp("""-""",Id('s'),IntLiteral(1)))])],([],[]))]),BinaryOp("""<""",Id('s'),IntLiteral(1000))),Assign(Id('s'),BinaryOp("""*""",Id('s'),Id('n')))]),BinaryOp("""<""",BinaryOp("""+""",BinaryOp("""+""",Id('s'),Id('n')),IntLiteral(1)),Id('max')))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,277))

	def test_218(self):
		input = """Function: foo
        Parameter: n
        Body: 
            Var: a = 10., b, c;
            a = c - (4. \. 3.) *. 3.14 *. a * (c - b *. a);
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([VarDecl(Id('a'),[],FloatLiteral(10.0)),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],[Assign(Id('a'),BinaryOp("""-""",Id('c'),BinaryOp("""*""",BinaryOp("""*.""",BinaryOp("""*.""",BinaryOp("""\.""",FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id('a')),BinaryOp("""-""",Id('c'),BinaryOp("""*.""",Id('b'),Id('a'))))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,218))

	def test_163(self):
		input = """Var: a,b,c;
                Function: main
                Parameter: a
                Body:
                While statement  Do something(); EndWhile.
                EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[While(Id('statement'),([],[CallStmt(Id('something'),[])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,163))

	def test_228(self):
		input = """Function: foo 
        Parameter: n
        Body: 
            a[3+foo(1)] = a[b[1][3]] + 4 * 10 - 7 + b[c[1][3]] + c[b[a][b]];
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[Assign(ArrayCell(Id('a'),[BinaryOp("""+""",IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(1)]))]),BinaryOp("""+""",BinaryOp("""+""",BinaryOp("""-""",BinaryOp("""+""",ArrayCell(Id('a'),[ArrayCell(Id('b'),[IntLiteral(1),IntLiteral(3)])]),BinaryOp("""*""",IntLiteral(4),IntLiteral(10))),IntLiteral(7)),ArrayCell(Id('b'),[ArrayCell(Id('c'),[IntLiteral(1),IntLiteral(3)])])),ArrayCell(Id('c'),[ArrayCell(Id('b'),[Id('a'),Id('b')])])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,228))

	def test_236(self):
		input = """
        Var: x, y[1][3]={{{12345,1}, {12., 12e3}},{23}, {13,32}};
        Function: foo 
        Parameter: n
        Body: 
        EndBody."""
		expect = Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[1,3],ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(12345),IntLiteral(1)]),ArrayLiteral([FloatLiteral(12.0),FloatLiteral(12000.0)])]),ArrayLiteral([IntLiteral(23)]),ArrayLiteral([IntLiteral(13),IntLiteral(32)])])),FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,236))

	def test_260(self):
		input = """
        Var: a;
        Function: foo
        Parameter: a, c
        Body:
        EndBody.
        """
		expect = Program([VarDecl(Id('a'),[],None),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('c'),[],None)],([],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,260))

	def test_259(self):
		input = """
        Function: foo
        Body: 
            For (i = 0, i <= 100\\10, 1) Do
                If i%2 == 1 Then writeln(i\\2);
                EndIf.
            EndFor.
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo'),[],([],[For(Id('i'),IntLiteral(0),BinaryOp("""<=""",Id('i'),BinaryOp("""\\""",IntLiteral(100),IntLiteral(10))),IntLiteral(1),([],[If([(BinaryOp("""==""",BinaryOp("""%""",Id('i'),IntLiteral(2)),IntLiteral(1)),[],[CallStmt(Id('writeln'),[BinaryOp("""\\""",Id('i'),IntLiteral(2))])])],([],[]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,259))

	def test_272(self):
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
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('x'),[],None)],([VarDecl(Id('n'),[],IntLiteral(0)),VarDecl(Id('s'),[],IntLiteral(0))],[Dowhile(([],[Assign(Id('n'),BinaryOp("""-""",Id('n'),IntLiteral(1))),Assign(Id('s'),BinaryOp("""+""",Id('s'),Id('n')))]),BinaryOp("""<""",BinaryOp("""+""",BinaryOp("""*""",Id('s'),Id('n')),IntLiteral(1)),Id('x'))),CallStmt(Id('writeln'),[Id('x')])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,272))

	def test_283(self):
		input = """
        Var: x;
        Function: foo
        Parameter: a, b
        Body:
            print(a);
            print(b);
        EndBody.
        """
		expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([],[CallStmt(Id('print'),[Id('a')]),CallStmt(Id('print'),[Id('b')])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,283))

	def test_240(self):
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
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp("""==""",Id('n'),IntLiteral(0)),[],[If([(BinaryOp("""!=""",Id('n'),IntLiteral(0)),[],[Return(IntLiteral(100))])],([],[Return(IntLiteral(2200))]))])],([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,240))

	def test_291(self):
		input = """Var: successful[10][9];"""
		expect = Program([VarDecl(Id('successful'),[10,9],None)])
		self.assertTrue(TestAST.checkASTGen(input,expect,291))

	def test_206(self):
		input = """ 
        Function: foo 
        Parameter: x
        Body: 
            c =a * 5; 
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('x'),[],None)],([],[Assign(Id('c'),BinaryOp("""*""",Id('a'),IntLiteral(5)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,206))

	def test_290(self):
		input = """
        Function: foo
        Body:
            Var: a = 1;
            While (a != 9) Do
                x = True || False;
            EndWhile.
        EndBody.
        """
		expect = Program([FuncDecl(Id('foo'),[],([VarDecl(Id('a'),[],IntLiteral(1))],[While(BinaryOp("""!=""",Id('a'),IntLiteral(9)),([],[Assign(Id('x'),BinaryOp("""||""",BooleanLiteral(True),BooleanLiteral(False)))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,290))

	def test_284(self):
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
		expect = Program([FuncDecl(Id('foo'),[],([VarDecl(Id('a'),[10],None)],[Dowhile(([],[Assign(ArrayCell(Id('a'),[IntLiteral(1),IntLiteral(2)]),FloatLiteral(3.14)),Break()]),BooleanLiteral(False)),CallStmt(Id('writeln'),[ArrayCell(Id('a'),[IntLiteral(1),IntLiteral(2)])])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,284))

	def test_234(self):
		input = """Function: foo 
        Parameter: n
        Body: 
            If n != n+1 Then
                Return (n-1) * (n-2) * (n-3) * (n-4);
            EndIf.
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp("""!=""",Id('n'),BinaryOp("""+""",Id('n'),IntLiteral(1))),[],[Return(BinaryOp("""*""",BinaryOp("""*""",BinaryOp("""*""",BinaryOp("""-""",Id('n'),IntLiteral(1)),BinaryOp("""-""",Id('n'),IntLiteral(2))),BinaryOp("""-""",Id('n'),IntLiteral(3))),BinaryOp("""-""",Id('n'),IntLiteral(4))))])],([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,234))

	def test_233(self):
		input = """Function: foo 
        Parameter: n
        Body: 
            While x<1000000000000 Do
                If x != 99999 Then Return;
                Else Break;
                EndIf.
            EndWhile.
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[While(BinaryOp("""<""",Id('x'),IntLiteral(1000000000000)),([],[If([(BinaryOp("""!=""",Id('x'),IntLiteral(99999)),[],[Return(None)])],([],[Break()]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,233))

	def test_246(self):
		input = """Function: foo 
        Parameter: n
        Body: 
            n = fact(x) - 3;
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('n'),BinaryOp("""-""",CallExpr(Id('fact'),[Id('x')]),IntLiteral(3)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,246))

	def test_269(self):
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
		expect = Program([FuncDecl(Id('foo'),[],([VarDecl(Id('x'),[],BooleanLiteral(True)),VarDecl(Id('t'),[],IntLiteral(100)),VarDecl(Id('a'),[],None)],[While(BinaryOp("""==""",BinaryOp("""||""",UnaryOp("""!""",Id('x')),Id('t')),IntLiteral(2)),([],[Assign(Id('x'),BooleanLiteral(False)),Assign(Id('a'),BinaryOp("""+""",Id('x'),Id('a'))),Assign(Id('x'),BinaryOp("""-""",Id('a'),Id('x'))),Assign(Id('t'),BinaryOp("""-""",Id('a'),Id('x')))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,269))

	def test_252(self):
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
		expect = Program([FuncDecl(Id('test'),[],([VarDecl(Id('a'),[],IntLiteral(3)),VarDecl(Id('b'),[],IntLiteral(4)),VarDecl(Id('c'),[],IntLiteral(5))],[If([(BinaryOp("""&&""",BinaryOp("""&&""",BinaryOp("""<""",Id('a'),BinaryOp("""+""",Id('b'),Id('c'))),BinaryOp("""<""",Id('b'),BinaryOp("""+""",Id('a'),Id('c')))),BinaryOp("""<""",Id('c'),BinaryOp("""+""",Id('a'),Id('b')))),[],[If([(BinaryOp("""||""",BinaryOp("""||""",BinaryOp("""==""",BinaryOp("""*""",Id('a'),Id('a')),BinaryOp("""+""",BinaryOp("""*""",Id('b'),Id('b')),BinaryOp("""*""",Id('c'),Id('c')))),BinaryOp("""==""",BinaryOp("""*""",Id('b'),Id('b')),BinaryOp("""+""",BinaryOp("""*""",Id('a'),Id('a')),BinaryOp("""*""",Id('c'),Id('c'))))),BinaryOp("""==""",BinaryOp("""*""",Id('c'),Id('c')),BinaryOp("""+""",BinaryOp("""*""",Id('a'),Id('a')),BinaryOp("""*""",Id('b'),Id('b'))))),[],[CallStmt(Id('print'),[StringLiteral("""Day la tam giac vuong""")])])],([],[]))]),(BinaryOp("""&&""",BinaryOp("""==""",Id('a'),Id('b')),BinaryOp("""==""",Id('b'),Id('c'))),[],[CallStmt(Id('print'),[StringLiteral("""Day la tam giac deu""")])]),(BinaryOp("""||""",BinaryOp("""||""",BinaryOp("""==""",Id('a'),Id('b')),BinaryOp("""==""",Id('a'),Id('c'))),BinaryOp("""==""",Id('b'),Id('c'))),[],[CallStmt(Id('print'),[StringLiteral("""Day la tam giac can""")])]),(BinaryOp("""||""",BinaryOp("""||""",BinaryOp(""">""",BinaryOp("""*""",Id('a'),Id('a')),BinaryOp("""+""",BinaryOp("""*""",Id('b'),Id('b')),BinaryOp("""*""",Id('c'),Id('c')))),BinaryOp(""">""",BinaryOp("""*""",Id('b'),Id('b')),BinaryOp("""+""",BinaryOp("""*""",Id('a'),Id('a')),BinaryOp("""*""",Id('c'),Id('c'))))),BinaryOp(""">""",BinaryOp("""*""",Id('c'),Id('c')),BinaryOp("""+""",BinaryOp("""*""",Id('a'),Id('a')),BinaryOp("""*""",Id('b'),Id('b'))))),[],[CallStmt(Id('print'),[StringLiteral("""Day la tam giac tu""")])])],([],[CallStmt(Id('print'),[StringLiteral("""Day la tam giac nhon""")])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,252))

	def test_255(self):
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
		expect = Program([FuncDecl(Id('test'),[],([VarDecl(Id('i'),[],IntLiteral(20)),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],[If([(BinaryOp("""==""",Id('i'),IntLiteral(1)),[],[Assign(Id('a'),IntLiteral(1)),Assign(Id('b'),IntLiteral(2)),Assign(Id('c'),BinaryOp("""*""",BinaryOp("""+""",Id('a'),Id('b')),BinaryOp("""-""",Id('a'),Id('b'))))]),(BinaryOp("""==""",Id('i'),IntLiteral(2)),[],[Assign(Id('a'),IntLiteral(3)),Assign(Id('b'),IntLiteral(4)),Assign(Id('c'),BinaryOp("""*""",BinaryOp("""-""",Id('b'),Id('a')),IntLiteral(2)))]),(BinaryOp("""==""",Id('i'),IntLiteral(3)),[],[Assign(Id('a'),IntLiteral(2)),Assign(Id('b'),IntLiteral(2)),Assign(Id('c'),BinaryOp("""*""",BinaryOp("""*""",BinaryOp("""+""",BinaryOp("""*""",Id('a'),IntLiteral(2)),BinaryOp("""*""",Id('b'),IntLiteral(3))),Id('a')),Id('b')))])],([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,255))

	def test_266(self):
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
		expect = Program([FuncDecl(Id('foo'),[],([VarDecl(Id('n'),[],IntLiteral(0))],[While(BinaryOp("""<""",Id('i'),IntLiteral(10)),([],[CallStmt(Id('writeln'),[StringLiteral("""Hello""")]),Assign(Id('i'),BinaryOp("""+""",Id('i'),IntLiteral(2)))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,266))

	def test_223(self):
		input = """Function: foo 
        Parameter: n
        Body: 
            Var: i = 1;
            While i < 5 Do
                a[i] = b * 2 +. 1.0;
                i = i + 2;
            EndWhile.
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([VarDecl(Id('i'),[],IntLiteral(1))],[While(BinaryOp("""<""",Id('i'),IntLiteral(5)),([],[Assign(ArrayCell(Id('a'),[Id('i')]),BinaryOp("""+.""",BinaryOp("""*""",Id('b'),IntLiteral(2)),FloatLiteral(1.0))),Assign(Id('i'),BinaryOp("""+""",Id('i'),IntLiteral(2)))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,223))

	def test_296(self):
		input = """Function: foo 
        Parameter: n
        Body: 
            a =(foo(3) != foo(4))* 0.e2;
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('a'),BinaryOp("""*""",BinaryOp("""!=""",CallExpr(Id('foo'),[IntLiteral(3)]),CallExpr(Id('foo'),[IntLiteral(4)])),FloatLiteral(0.0)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,296))

	def test_230(self):
		input = """Function: foo 
        Parameter: n
        Body: ** Tran Thanh da cuoi**
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,230))

	def test_245(self):
		input = """Function: foo 
        Parameter: n
        Body: 
        For (i = 0, i < 10, 2) Do
            y = e + u;
            a = n + h - y - e -u + e - m;
        EndFor.
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp("""<""",Id('i'),IntLiteral(10)),IntLiteral(2),([],[Assign(Id('y'),BinaryOp("""+""",Id('e'),Id('u'))),Assign(Id('a'),BinaryOp("""-""",BinaryOp("""+""",BinaryOp("""-""",BinaryOp("""-""",BinaryOp("""-""",BinaryOp("""+""",Id('n'),Id('h')),Id('y')),Id('e')),Id('u')),Id('e')),Id('m')))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,245))

