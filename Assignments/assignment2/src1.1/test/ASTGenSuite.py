
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    
	def test_348(self):
		input = """Var: a,b,c;
Function: main
Parameter: a
Body:
Do something(); While a && bool_of_string("True") EndDo.
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[Dowhile(([],[CallStmt(Id('something'),[])]),BinaryOp("""&&""",Id('a'),CallStmt(Id('bool_of_string'),[StringLiteral("""True""")])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,348))

	def test_304(self):
		input = """Var:x[1] = {1};"""
		expect = Program([VarDecl(Id('x'),[1],ArrayLiteral([IntLiteral(1)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,304))

	def test_311(self):
		input = """Var: a,b,c;
                    Function: main
                    Parameter: a
                    Body:
                    EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,311))

	def test_333(self):
		input = """Var: a,b,c;
Function: main
Parameter: a
Body:
Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
For (i=1, i<3, 2) Do something(); EndFor.
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(12),StringLiteral("""asdf""")])),VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(True),IntLiteral(18)]))],[For(Id('i'),IntLiteral(1),BinaryOp("""<""",Id('i'),IntLiteral(3)),IntLiteral(2),([],[CallStmt(Id('something'),[])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,333))

	def test_372(self):
		input = """Var: a,b,c;
Function: main
Body:
a = b[something()[a[1]] + 1][c + d < 1] + c *. d[1.][21 * 0x21A];
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[Assign(Id('a'),BinaryOp("""+""",ArrayCell(BinaryOp("""+""",ArrayCell(ArrayCell(IntLiteral(1),[]),[]),IntLiteral(1)),[BinaryOp("""<""",BinaryOp("""+""",Id('c'),Id('d')),IntLiteral(1))]),BinaryOp("""*.""",Id('c'),ArrayCell(FloatLiteral(1.0),[BinaryOp("""*""",IntLiteral(21),IntLiteral(538))]))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,372))

	def test_381(self):
		input = """Function: main
Parameter: a, b[1][100]
Body:
While a<b Do
If a > b Then doNothing(); Break;
ElseIf !somecon() Then doSomething();
Else Do something(); While a + foo()[100] EndDo.
EndIf.
EndWhile.
EndBody."""
		expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[1,100],None)],([],[While(BinaryOp("""<""",Id('a'),Id('b')),([],[If([(BinaryOp(""">""",Id('a'),Id('b')),[],[CallStmt(Id('doNothing'),[]),Break()]),(UnaryOp("""!""",CallStmt(Id('somecon'),[])),[],[CallStmt(Id('doSomething'),[])])],([],[Dowhile(([],[CallStmt(Id('something'),[])]),BinaryOp("""+""",Id('a'),ArrayCell(IntLiteral(100),[])))]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,381))

	def test_395(self):
		input = """Var: a,b,c;
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
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('a'),[1,12],None)],([],[If([(Id('expr'),[],[]),(Id('expr'),[],[While(Id('expr'),([],[])),Dowhile(([],[Return(None)]),ArrayLiteral([ArrayLiteral([])]))])],([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,395))

	def test_339(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        For (i = 0x12, a < 2, i + foo() + 1) Do something();
        c = a[23][b[1][2][c]] +. 12; 
        EndFor.
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(12),StringLiteral("""asdf""")])),VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(True),IntLiteral(18)]))],[For(Id('i'),IntLiteral(18),BinaryOp("""<""",Id('a'),IntLiteral(2)),BinaryOp("""+""",BinaryOp("""+""",Id('i'),CallStmt(Id('foo'),[])),IntLiteral(1)),([],[CallStmt(Id('something'),[]),Assign(Id('c'),BinaryOp("""+.""",ArrayCell(IntLiteral(23),[ArrayCell(IntLiteral(1),[IntLiteral(2),Id('c')])]),IntLiteral(12)))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,339))

	def test_317(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        Var: x=1,a[1]=1;
        Var: a,b[1]={"this"};
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[],IntLiteral(1)),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[1],ArrayLiteral([StringLiteral("""this""")]))],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,317))

	def test_390(self):
		input = """Var: a,b,c;
Function: main
Parameter: a
Body:
foo(1+a, b, c)[something][whatever] = 12;
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[Assign(ArrayCell(Id('something'),[Id('whatever')]),IntLiteral(12))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,390))

	def test_330(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        If a == True Then
        EndIf.
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(12),StringLiteral("""asdf""")])),VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(True),IntLiteral(18)]))],[If([(BinaryOp("""==""",Id('a'),BooleanLiteral(True)),[],[])],[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,330))

	def test_318(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]=1;
        Var: a,b[1]={"this"};
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[],IntLiteral(1)),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[1],ArrayLiteral([StringLiteral("""this""")]))],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,318))

	def test_345(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Do something(); While !(abc < 12 || b && True) EndDo.
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[Dowhile(([],[CallStmt(Id('something'),[])]),UnaryOp("""!""",BinaryOp("""<""",Id('abc'),BinaryOp("""&&""",BinaryOp("""||""",IntLiteral(12),Id('b')),BooleanLiteral(True)))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,345))

	def test_358(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        foo(arg1, "???", foo(nothing));
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[Id('arg1'),StringLiteral("""???"""),CallStmt(Id('foo'),[Id('nothing')])])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,358))

	def test_310(self):
		input = """Var:x[1] = {1,2,3,4};"""
		expect = Program([VarDecl(Id('x'),[1],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,310))

	def test_322(self):
		input = """Function: main
                Parameter: a
                Body:
                    If 1 Then
                    EndIf.
                EndBody."""
		expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[If([(IntLiteral(1),[],[])],[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,322))

	def test_369(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        a = b[something()[a[1]] + 1][c + d < 1];
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[Assign(Id('a'),ArrayCell(BinaryOp("""+""",ArrayCell(ArrayCell(IntLiteral(1),[]),[]),IntLiteral(1)),[BinaryOp("""<""",BinaryOp("""+""",Id('c'),Id('d')),IntLiteral(1))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,369))

	def test_325(self):
		input = """Var: a,b,c;
Function: main
Parameter: a
Body:
Var: x=1,a[1]=1;
Var: a,b[1]={"this"};
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[],IntLiteral(1)),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[1],ArrayLiteral([StringLiteral("""this""")]))],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,325))

	def test_378(self):
		input = """Var: a,b,c;
Function: main
Parameter: a, bn
Body:
Return a + bn - a[foo()];
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('bn'),[],None)],([],[Return(BinaryOp("""-""",BinaryOp("""+""",Id('a'),Id('bn')),ArrayCell(CallStmt(Id('foo'),[]),[])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,378))

	def test_315(self):
		input = """Var: a,b,c;
Function: main
Body:
a = a <b - c;
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[Assign(Id('a'),BinaryOp("""<""",Id('a'),BinaryOp("""-""",Id('b'),Id('c'))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,315))

	def test_375(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        b = {{{}}};
        a = (a + b) +. (a-a-.a*a*.a\.b%!c&&a||a==b);
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[Assign(Id('b'),ArrayLiteral([ArrayLiteral([ArrayLiteral([])])])),Assign(Id('a'),BinaryOp("""+.""",BinaryOp("""+""",Id('a'),Id('b')),BinaryOp("""==""",BinaryOp("""||""",BinaryOp("""&&""",BinaryOp("""-.""",BinaryOp("""-""",Id('a'),Id('a')),BinaryOp("""%""",BinaryOp("""\.""",BinaryOp("""*.""",BinaryOp("""*""",Id('a'),Id('a')),Id('a')),Id('b')),UnaryOp("""!""",Id('c')))),Id('a')),Id('a')),Id('b'))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,375))

	def test_400(self):
		input = """Var: a,b,c;
Function: main
Parameter: a, a[1][12]
Body:
For(i=expr, a =/= {{}}, "what is that'"" + 1) Do
Break;Continue;
EndFor.
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('a'),[1,12],None)],([],[For(Id('i'),Id('expr'),BinaryOp("""=/=""",Id('a'),ArrayLiteral([ArrayLiteral([])])),BinaryOp("""+""",StringLiteral("""what is that'\""""),IntLiteral(1)),([],[Break(),Continue()]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,400))

	def test_388(self):
		input = """Var: a,b,c;
Function: main
Parameter: a
Body:
While statement  Do something(); EndWhile.
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[While(Id('statement'),([],[CallStmt(Id('something'),[])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,388))

	def test_379(self):
		input = """Function: main
Parameter: a
Body:
a[1] = b[1] + {1,2,3} + append();
EndBody."""
		expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[Assign(ArrayCell(IntLiteral(1),[]),BinaryOp("""+""",BinaryOp("""+""",ArrayCell(IntLiteral(1),[]),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),CallStmt(Id('append'),[])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,379))

	def test_373(self):
		input = """Var: a,b,c;
Function: main
Body:
a = a + b +. a-a-.a*a*.a\.b%!c&&a||a==b;
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[Assign(Id('a'),BinaryOp("""==""",BinaryOp("""||""",BinaryOp("""&&""",BinaryOp("""-.""",BinaryOp("""-""",BinaryOp("""+.""",BinaryOp("""+""",Id('a'),Id('b')),Id('a')),Id('a')),BinaryOp("""%""",BinaryOp("""\.""",BinaryOp("""*.""",BinaryOp("""*""",Id('a'),Id('a')),Id('a')),Id('b')),UnaryOp("""!""",Id('c')))),Id('a')),Id('a')),Id('b')))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,373))

	def test_327(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        Var: a,b[1]={"this"};
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(12),StringLiteral("""asdf""")])),VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(True),IntLiteral(18)])),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[1],ArrayLiteral([StringLiteral("""this""")]))],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,327))

	def test_398(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a, a[1][12]
        Body:
        For(i=expr, a =/= {{}}, "what is that" + 1) Do
        EndFor.
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('a'),[1,12],None)],([],[For(Id('i'),Id('expr'),BinaryOp("""=/=""",Id('a'),ArrayLiteral([ArrayLiteral([])])),BinaryOp("""+""",StringLiteral("""what is that"""),IntLiteral(1)),([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,398))

	def test_332(self):
		input = """Function: main
                Parameter: a
                Body:
                (1 + c)[foo() + 1][1 + 2][a + v] = a;
                EndBody."""
		expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[Assign(ArrayCell(BinaryOp("""+""",CallStmt(Id('foo'),[]),IntLiteral(1)),[BinaryOp("""+""",IntLiteral(1),IntLiteral(2)),BinaryOp("""+""",Id('a'),Id('v'))]),Id('a'))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,332))

	def test_308(self):
		input = """Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
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
		expect = Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[1,3],ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(12),IntLiteral(1)]),ArrayLiteral([FloatLiteral(12.0),FloatLiteral(12000.0)])]),ArrayLiteral([IntLiteral(23)]),ArrayLiteral([IntLiteral(13),IntLiteral(32)])])),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp("""==""",Id('n'),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp("""*""",Id('n'),CallStmt(Id('fact'),[BinaryOp("""-""",Id('n'),IntLiteral(1))])))]))])),FuncDecl(Id('main'),[],([],[Assign(Id('x'),IntLiteral(10)),CallStmt(Id('fact'),[Id('x')])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,308))

	def test_347(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Do something(); While 1 <. 2.0 EndDo.
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[Dowhile(([],[CallStmt(Id('something'),[])]),BinaryOp("""<.""",IntLiteral(1),FloatLiteral(2.0)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,347))

	def test_377(self):
		input = """Var: a,b,c;
Function: main
Body:

EndBody.
Function: foo
Body:
main();
If a[1] Then foo(); EndIf.
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[])),FuncDecl(Id('foo'),[],([],[CallStmt(Id('main'),[]),If([(ArrayCell(IntLiteral(1),[]),[],[CallStmt(Id('foo'),[])])],[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,377))

	def test_349(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Do something(); While a && b <. 1. +. 3. EndDo.
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[Dowhile(([],[CallStmt(Id('something'),[])]),BinaryOp("""<.""",BinaryOp("""&&""",Id('a'),Id('b')),BinaryOp("""+.""",FloatLiteral(1.0),FloatLiteral(3.0))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,349))

	def test_367(self):
		input = """Var: a,b,c;
Function: main
Body:
foo(a < b + c);
printLn();
a = 1+ 2+2+{1, 2,3};
**print(arg);
printStrLn(arg)**
read();
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[BinaryOp("""<""",Id('a'),BinaryOp("""+""",Id('b'),Id('c')))]),CallStmt(Id('printLn'),[]),Assign(Id('a'),BinaryOp("""+""",BinaryOp("""+""",BinaryOp("""+""",IntLiteral(1),IntLiteral(2)),IntLiteral(2)),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))),CallStmt(Id('read'),[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,367))

	def test_319(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a, b[1]
        Body:
        Var: x=1,a[1]=1;
        Var: a,b[1]={"this"};
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[1],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[],IntLiteral(1)),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[1],ArrayLiteral([StringLiteral("""this""")]))],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,319))

	def test_337(self):
		input = """Var: a,b,c;
Function: main
Parameter: a
Body:
Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
For (i = 2, a < 2, i + 1) Do 
For (i=2, a>1341,a+b) Do EndFor.
something(); EndFor.
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(12),StringLiteral("""asdf""")])),VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(True),IntLiteral(18)]))],[For(Id('i'),IntLiteral(2),BinaryOp("""<""",Id('a'),IntLiteral(2)),BinaryOp("""+""",Id('i'),IntLiteral(1)),([],[For(Id('i'),IntLiteral(2),BinaryOp(""">""",Id('a'),IntLiteral(1341)),BinaryOp("""+""",Id('a'),Id('b')),([],[])),CallStmt(Id('something'),[])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,337))

	def test_324(self):
		input = """Var: a,b,c;
Function: main
Parameter: a, b[1]
Body:
Var: x=1,a[1]=1;
If a Then
EndIf.
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[1],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[],IntLiteral(1))],[If([(Id('a'),[],[])],[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,324))

	def test_356(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Return a < 1 || foo(arg1, "arg2", {1,2});
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[If([(UnaryOp("""!""",BooleanLiteral(True)),[],[Assign(Id('a'),BinaryOp("""<""",Id('a'),Id('c'))),If([(BinaryOp(""">""",BinaryOp("""+""",Id('a'),Id('b')),Id('c')),[],[Assign(Id('a'),BinaryOp("""+""",Id('a'),Id('b')))]),(BinaryOp("""==""",Id('a'),Id('b')),[],[CallStmt(Id('writeln'),[Id('i')])])],([],[Assign(Id('a'),FloatLiteral(120.0))]))])],[]),Return(BinaryOp("""<""",Id('a'),BinaryOp("""||""",IntLiteral(1),CallStmt(Id('foo'),[Id('arg1'),StringLiteral("""arg2"""),ArrayLiteral([IntLiteral(1),IntLiteral(2)])]))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,356))

	def test_306(self):
		input = """Var: b[2][3]={{1,2},{3,4}};
Function: main
Body:
Return;
EndBody."""
		expect = Program([VarDecl(Id('b'),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3),IntLiteral(4)])])),FuncDecl(Id('main'),[],([],[Return(None)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,306))

	def test_362(self):
		input = """Var: a,b,c;
Function: main
Body:
foo(arg1, "???", foo(nothing))[1] = something(foo());
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[Assign(ArrayCell(IntLiteral(1),[]),CallStmt(Id('something'),[CallStmt(Id('foo'),[])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,362))

	def test_380(self):
		input = """
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
		expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[1,100],None)],([],[While(BinaryOp("""<""",Id('a'),Id('b')),([],[If([(BinaryOp(""">""",Id('a'),Id('b')),[],[CallStmt(Id('doNothing'),[]),Break()]),(UnaryOp("""!""",CallStmt(Id('somecon'),[])),[],[CallStmt(Id('doSomething'),[])])],([],[Dowhile(([],[CallStmt(Id('something'),[])]),BinaryOp("""+""",Id('a'),ArrayCell(IntLiteral(100),[])))]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,380))

	def test_370(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        a = b[something()[a[1]] + 1][c + d < 1] + c *. d[1][21];
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[Assign(Id('a'),BinaryOp("""+""",ArrayCell(BinaryOp("""+""",ArrayCell(ArrayCell(IntLiteral(1),[]),[]),IntLiteral(1)),[BinaryOp("""<""",BinaryOp("""+""",Id('c'),Id('d')),IntLiteral(1))]),BinaryOp("""*.""",Id('c'),ArrayCell(IntLiteral(1),[IntLiteral(21)]))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,370))

	def test_392(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        a[3 + foo(2)] = a[b[2][3]] + 4;
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[Assign(ArrayCell(BinaryOp("""+""",IntLiteral(3),CallStmt(Id('foo'),[IntLiteral(2)])),[]),BinaryOp("""+""",ArrayCell(ArrayCell(IntLiteral(2),[IntLiteral(3)]),[]),IntLiteral(4)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,392))

	def test_354(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Return 1 + {{1,2}, "abnd"};
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[If([(UnaryOp("""!""",BooleanLiteral(True)),[],[Assign(Id('a'),BinaryOp("""<""",Id('a'),Id('c'))),If([(BinaryOp(""">""",BinaryOp("""+""",Id('a'),Id('b')),Id('c')),[],[Assign(Id('a'),BinaryOp("""+""",Id('a'),Id('b')))]),(BinaryOp("""==""",Id('a'),Id('b')),[],[CallStmt(Id('writeln'),[Id('i')])])],([],[Assign(Id('a'),FloatLiteral(120.0))]))])],[]),Return(BinaryOp("""+""",IntLiteral(1),ArrayLiteral([StringLiteral("""abnd""")])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,354))

	def test_340(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        While 1 Do something(); EndWhile.
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(12),StringLiteral("""asdf""")])),VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(True),IntLiteral(18)]))],[While(IntLiteral(1),([],[CallStmt(Id('something'),[])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,340))

	def test_350(self):
		input = """Var: a,b,c;
Function: main
Body:
If !(True) Then
a = a <c;
If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12 + e; EndIf.
EndIf.
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[If([(UnaryOp("""!""",BooleanLiteral(True)),[],[Assign(Id('a'),BinaryOp("""<""",Id('a'),Id('c'))),If([(BinaryOp(""">""",BinaryOp("""+""",Id('a'),Id('b')),Id('c')),[],[Assign(Id('a'),BinaryOp("""+""",Id('a'),Id('b')))]),(BinaryOp("""==""",Id('a'),Id('b')),[],[CallStmt(Id('writeln'),[Id('i')])])],([],[Assign(Id('a'),BinaryOp("""+""",IntLiteral(12),Id('e')))]))])],[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,350))

	def test_353(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Return 1 + 1;
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[If([(UnaryOp("""!""",BooleanLiteral(True)),[],[Assign(Id('a'),BinaryOp("""<""",Id('a'),Id('c'))),If([(BinaryOp(""">""",BinaryOp("""+""",Id('a'),Id('b')),Id('c')),[],[Assign(Id('a'),BinaryOp("""+""",Id('a'),Id('b')))]),(BinaryOp("""==""",Id('a'),Id('b')),[],[CallStmt(Id('writeln'),[Id('i')])])],([],[Assign(Id('a'),FloatLiteral(120.0))]))])],[]),Return(BinaryOp("""+""",IntLiteral(1),IntLiteral(1)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,353))

	def test_341(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        While !(x =/= y) Do something(); EndWhile.
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(12),StringLiteral("""asdf""")])),VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(True),IntLiteral(18)]))],[While(UnaryOp("""!""",BinaryOp("""=/=""",Id('x'),Id('y'))),([],[CallStmt(Id('something'),[])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,341))

	def test_320(self):
		input = """Var: a,b,c;
Function: main
Parameter: a, b[1]
Body:
Var: x=1,a[1]={{}};
Var: a,b[1]={"this"};
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[1],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[1],ArrayLiteral([ArrayLiteral([])])),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[1],ArrayLiteral([StringLiteral("""this""")]))],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,320))

	def test_343(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        While !(x &&  y || b) && (a || abc) Do something(); EndWhile.
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(12),StringLiteral("""asdf""")])),VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(True),IntLiteral(18)]))],[While(BinaryOp("""&&""",UnaryOp("""!""",BinaryOp("""||""",BinaryOp("""&&""",Id('x'),Id('y')),Id('b'))),BinaryOp("""||""",Id('a'),Id('abc'))),([],[CallStmt(Id('something'),[])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,343))

	def test_329(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        If 1 + a - b * foo() > 1 Then
        EndIf.
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(12),StringLiteral("""asdf""")])),VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(True),IntLiteral(18)]))],[If([(BinaryOp(""">""",BinaryOp("""-""",BinaryOp("""+""",IntLiteral(1),Id('a')),BinaryOp("""*""",Id('b'),CallStmt(Id('foo'),[]))),IntLiteral(1)),[],[])],[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,329))

	def test_365(self):
		input = """Var: a,b,c;
Function: main
Body:
foo(arg1, "???", foo(nothing), {"asdab", {1,2.e2,123e1,"nothing"}});
printLn();
print(arg);
printStrLn(arg);
read();
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[Id('arg1'),StringLiteral("""???"""),CallStmt(Id('foo'),[Id('nothing')]),ArrayLiteral([StringLiteral("""asdab""")])]),CallStmt(Id('printLn'),[]),CallStmt(Id('print'),[Id('arg')]),CallStmt(Id('printStrLn'),[Id('arg')]),CallStmt(Id('read'),[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,365))

	def test_389(self):
		input = """Var: a,b,c;
Function: main
Parameter: a, b
Body:
While statement Do Break; EndWhile.
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([],[While(Id('statement'),([],[Break()]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,389))

	def test_335(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        For (i = "abc", a < 2, i + 1) Do something(); EndFor.
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(12),StringLiteral("""asdf""")])),VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(True),IntLiteral(18)]))],[For(Id('i'),StringLiteral("""abc"""),BinaryOp("""<""",Id('a'),IntLiteral(2)),BinaryOp("""+""",Id('i'),IntLiteral(1)),([],[CallStmt(Id('something'),[])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,335))

	def test_399(self):
		input = """Var: a,b,c;
Function: main
Parameter: a, a[1][12]
Body:
For(i=expr, a =/= {{}}, "what is that" + 1) Do
EndFor.
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('a'),[1,12],None)],([],[For(Id('i'),Id('expr'),BinaryOp("""=/=""",Id('a'),ArrayLiteral([ArrayLiteral([])])),BinaryOp("""+""",StringLiteral("""what is that"""),IntLiteral(1)),([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,399))

	def test_328(self):
		input = """Var: a,b,c;
Function: main
Parameter: a
Body:
Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
If 1 < a Then
Var: a;
EndIf.
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(12),StringLiteral("""asdf""")])),VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(True),IntLiteral(18)]))],[If([(BinaryOp("""<""",IntLiteral(1),Id('a')),[VarDecl(Id('a'),[],None)],[])],[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,328))

	def test_342(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        While !(x &&  y || b) ** && (a || abc)** Do something(); EndWhile.
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(12),StringLiteral("""asdf""")])),VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(True),IntLiteral(18)]))],[While(UnaryOp("""!""",BinaryOp("""||""",BinaryOp("""&&""",Id('x'),Id('y')),Id('b'))),([],[CallStmt(Id('something'),[])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,342))

	def test_334(self):
		input = """Var: a,b,c;
Function: main
Parameter: a
Body:
Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
For (i = 1, a < 2, i + 1) Do something(); EndFor.
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(12),StringLiteral("""asdf""")])),VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(True),IntLiteral(18)]))],[For(Id('i'),IntLiteral(1),BinaryOp("""<""",Id('a'),IntLiteral(2)),BinaryOp("""+""",Id('i'),IntLiteral(1)),([],[CallStmt(Id('something'),[])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,334))

	def test_336(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        For (i = 0x12, a < 2, i + foo() + 1) Do something(); EndFor.
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(12),StringLiteral("""asdf""")])),VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(True),IntLiteral(18)]))],[For(Id('i'),IntLiteral(18),BinaryOp("""<""",Id('a'),IntLiteral(2)),BinaryOp("""+""",BinaryOp("""+""",Id('i'),CallStmt(Id('foo'),[])),IntLiteral(1)),([],[CallStmt(Id('something'),[])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,336))

	def test_300(self):
		input = """Var:x;"""
		expect = Program([VarDecl(Id('x'),[],None)])
		self.assertTrue(TestAST.checkASTGen(input,expect,300))

	def test_303(self):
		input = """Var:x = 1, y = "abc", z = 1e2, l=True, a[1][2]={{1},{2}};"""
		expect = Program([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('y'),[],StringLiteral("""abc""")),VarDecl(Id('z'),[],FloatLiteral(100.0)),VarDecl(Id('l'),[],BooleanLiteral(True)),VarDecl(Id('a'),[1,2],ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(2)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,303))

	def test_360(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        a = a[c[1][b]][1] + foo(arg1, "???", foo(nothing));
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[Assign(Id('a'),BinaryOp("""+""",ArrayCell(ArrayCell(IntLiteral(1),[Id('b')]),[IntLiteral(1)]),CallStmt(Id('foo'),[Id('arg1'),StringLiteral("""???"""),CallStmt(Id('foo'),[Id('nothing')])])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,360))

	def test_376(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        b = {{{}}};
        a = (a + b) +. (a-a-.a*a*.a\.b%!c&&a||a==b) % a[1][1];
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[Assign(Id('b'),ArrayLiteral([ArrayLiteral([ArrayLiteral([])])])),Assign(Id('a'),BinaryOp("""+.""",BinaryOp("""+""",Id('a'),Id('b')),BinaryOp("""%""",BinaryOp("""==""",BinaryOp("""||""",BinaryOp("""&&""",BinaryOp("""-.""",BinaryOp("""-""",Id('a'),Id('a')),BinaryOp("""%""",BinaryOp("""\.""",BinaryOp("""*.""",BinaryOp("""*""",Id('a'),Id('a')),Id('a')),Id('b')),UnaryOp("""!""",Id('c')))),Id('a')),Id('a')),Id('b')),ArrayCell(IntLiteral(1),[IntLiteral(1)]))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,376))

	def test_314(self):
		input = """Var: x = "yay";"""
		expect = Program([VarDecl(Id('x'),[],StringLiteral("""yay"""))])
		self.assertTrue(TestAST.checkASTGen(input,expect,314))

	def test_331(self):
		input = """Function: main
                Parameter: a
                Body:
                    If 1 + 1 Then
                    For (i=1,i>1,1+2) Do
                        Var: a=10,c[1]={1,2};
                        c[foo() + 1] = a;
                    EndFor.
                    EndIf.
                EndBody."""
		expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[If([(BinaryOp("""+""",IntLiteral(1),IntLiteral(1)),[],[For(Id('i'),IntLiteral(1),BinaryOp(""">""",Id('i'),IntLiteral(1)),BinaryOp("""+""",IntLiteral(1),IntLiteral(2)),([VarDecl(Id('a'),[],IntLiteral(10)),VarDecl(Id('c'),[1],ArrayLiteral([IntLiteral(1),IntLiteral(2)]))],[Assign(ArrayCell(BinaryOp("""+""",CallStmt(Id('foo'),[]),IntLiteral(1)),[]),Id('a'))]))])],[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,331))

	def test_346(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Do something(); While a[1][c[2]] + 123 -1 EndDo.
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[Dowhile(([],[CallStmt(Id('something'),[])]),BinaryOp("""-""",BinaryOp("""+""",ArrayCell(IntLiteral(1),[ArrayCell(IntLiteral(2),[])]),IntLiteral(123)),IntLiteral(1)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,346))

	def test_366(self):
		input = """Var: a,b,c;
Function: main
Body:
foo(arg1, "???", foo(nothing), {"asdab", {1,2.e2,123e1,"nothing"}});
printLn();
**print(arg);
printStrLn(arg)**
read();
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[Id('arg1'),StringLiteral("""???"""),CallStmt(Id('foo'),[Id('nothing')]),ArrayLiteral([StringLiteral("""asdab""")])]),CallStmt(Id('printLn'),[]),CallStmt(Id('read'),[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,366))

	def test_396(self):
		input = """Var: a,b,c;
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
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('a'),[1,12],None)],([],[If([(Id('expr'),[],[]),(Id('expr'),[],[While(Id('expr'),([],[])),Dowhile(([],[Return(None)]),ArrayLiteral([ArrayLiteral([])]))])],([],[CallStmt(Id('nothing'),[]),Assign(Id('a'),BinaryOp("""==""",IntLiteral(1),BinaryOp("""+""",Id('b'),Id('a'))))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,396))

	def test_364(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        foo(arg1, "???", foo(nothing), {"asdab", {1,2.e2,123e1,"nothing"}});
        printLn();
        print(arg);
        printStrLn(arg);
        read();
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[Id('arg1'),StringLiteral("""???"""),CallStmt(Id('foo'),[Id('nothing')]),ArrayLiteral([StringLiteral("""asdab""")])]),CallStmt(Id('printLn'),[]),CallStmt(Id('print'),[Id('arg')]),CallStmt(Id('printStrLn'),[Id('arg')]),CallStmt(Id('read'),[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,364))

	def test_338(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        For (i = 0x12, a < 2, i + foo() + 1) Do something();
        c = a[23][b[1][2][c]] +. 12.; 
        EndFor.
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(12),StringLiteral("""asdf""")])),VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(True),IntLiteral(18)]))],[For(Id('i'),IntLiteral(18),BinaryOp("""<""",Id('a'),IntLiteral(2)),BinaryOp("""+""",BinaryOp("""+""",Id('i'),CallStmt(Id('foo'),[])),IntLiteral(1)),([],[CallStmt(Id('something'),[]),Assign(Id('c'),BinaryOp("""+.""",ArrayCell(IntLiteral(23),[ArrayCell(IntLiteral(1),[IntLiteral(2),Id('c')])]),FloatLiteral(12.0)))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,338))

	def test_394(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a, a[1][12]
        Body:
        If expr Then 
        ElseIf expr Then
        Else
        EndIf.
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('a'),[1,12],None)],([],[If([(Id('expr'),[],[]),(Id('expr'),[],[])],([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,394))

	def test_307(self):
		input = """Var: x;
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
		expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp("""==""",Id('n'),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp("""*""",Id('n'),CallStmt(Id('fact'),[BinaryOp("""-""",Id('n'),IntLiteral(1))])))]))])),FuncDecl(Id('main'),[],([],[Assign(Id('x'),IntLiteral(10)),CallStmt(Id('fact'),[Id('x')])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,307))

	def test_386(self):
		input = """
        Function: nothing
        Body:
        Var: a = {1238,32412, 120};
        EndBody.
        Function: foo
        Parameter: a,b,c
        Body:
        nothing(a[1][1][b[k]]);
        EndBody."""
		expect = Program([FuncDecl(Id('nothing'),[],([VarDecl(Id('a'),[],ArrayLiteral([IntLiteral(1238),IntLiteral(32412),IntLiteral(120)]))],[])),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[CallStmt(Id('nothing'),[ArrayCell(IntLiteral(1),[IntLiteral(1),ArrayCell(Id('k'),[])])])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,386))

	def test_382(self):
		input = """
        Function: main
        Parameter: a, b[1][100]
        Body:
        While a<b Do
            If a > b Then doNothing(); Break;
            ElseIf !somecon() Then doSomething();
            ElseIf a \ 100 -20 Then Continue;
            stop();
            what();
            Else Do something(); While a + foo()[100] EndDo.
            EndIf.
        EndWhile.
        EndBody."""
		expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[1,100],None)],([],[While(BinaryOp("""<""",Id('a'),Id('b')),([],[If([(BinaryOp(""">""",Id('a'),Id('b')),[],[CallStmt(Id('doNothing'),[]),Break()]),(UnaryOp("""!""",CallStmt(Id('somecon'),[])),[],[CallStmt(Id('doSomething'),[])]),(BinaryOp("""-""",BinaryOp("""\\""",Id('a'),IntLiteral(100)),IntLiteral(20)),[],[Continue(),CallStmt(Id('stop'),[]),CallStmt(Id('what'),[])])],([],[Dowhile(([],[CallStmt(Id('something'),[])]),BinaryOp("""+""",Id('a'),ArrayCell(IntLiteral(100),[])))]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,382))

	def test_383(self):
		input = """Function: foo
Body:

If a > b Then doNothing(); Break;

ElseIf !somecon() Then doSomething();

ElseIf a \ 100 -20 Then Continue;
stop();

ElseIf whatever() Then 

ElseIf anything() Then Do something(); While a + foo()[100] EndDo.
EndIf.
EndBody.
Function: main
Parameter: a, b[1][100]
Body:
While a<b Do
EndWhile.
EndBody."""
		expect = Program([FuncDecl(Id('foo'),[],([],[If([(BinaryOp(""">""",Id('a'),Id('b')),[],[CallStmt(Id('doNothing'),[]),Break()]),(UnaryOp("""!""",CallStmt(Id('somecon'),[])),[],[CallStmt(Id('doSomething'),[])]),(BinaryOp("""-""",BinaryOp("""\\""",Id('a'),IntLiteral(100)),IntLiteral(20)),[],[Continue(),CallStmt(Id('stop'),[])]),(CallStmt(Id('whatever'),[]),[],[]),(CallStmt(Id('anything'),[]),[],[Dowhile(([],[CallStmt(Id('something'),[])]),BinaryOp("""+""",Id('a'),ArrayCell(IntLiteral(100),[])))])],[])])),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[1,100],None)],([],[While(BinaryOp("""<""",Id('a'),Id('b')),([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,383))

	def test_352(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Return ;
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[If([(UnaryOp("""!""",BooleanLiteral(True)),[],[Assign(Id('a'),BinaryOp("""<""",Id('a'),Id('c'))),If([(BinaryOp(""">""",BinaryOp("""+""",Id('a'),Id('b')),Id('c')),[],[Assign(Id('a'),BinaryOp("""+""",Id('a'),Id('b')))]),(BinaryOp("""==""",Id('a'),Id('b')),[],[CallStmt(Id('writeln'),[Id('i')])])],([],[Assign(Id('a'),FloatLiteral(120.0))]))])],[]),Return(None)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,352))

	def test_326(self):
		input = """Var: a,b,c;
Function: main
Parameter: a
Body:
Var: x=1,a[1]={12, "asdf"},b=1.21;
Var: a,b[1]={"this"};
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral(12),StringLiteral("""asdf""")])),VarDecl(Id('b'),[],FloatLiteral(1.21)),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[1],ArrayLiteral([StringLiteral("""this""")]))],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,326))

	def test_357(self):
		input = """Var: a,b,c;
Function: main
Body:
If !(True) Then

a = a <c;
If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
EndIf.
Return  main();
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[If([(UnaryOp("""!""",BooleanLiteral(True)),[],[Assign(Id('a'),BinaryOp("""<""",Id('a'),Id('c'))),If([(BinaryOp(""">""",BinaryOp("""+""",Id('a'),Id('b')),Id('c')),[],[Assign(Id('a'),BinaryOp("""+""",Id('a'),Id('b')))]),(BinaryOp("""==""",Id('a'),Id('b')),[],[CallStmt(Id('writeln'),[Id('i')])])],([],[Assign(Id('a'),FloatLiteral(120.0))]))])],[]),Return(CallStmt(Id('main'),[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,357))

	def test_351(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        Break;
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Continue;
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[If([(UnaryOp("""!""",BooleanLiteral(True)),[],[Break(),Assign(Id('a'),BinaryOp("""<""",Id('a'),Id('c'))),If([(BinaryOp(""">""",BinaryOp("""+""",Id('a'),Id('b')),Id('c')),[],[Assign(Id('a'),BinaryOp("""+""",Id('a'),Id('b')))]),(BinaryOp("""==""",Id('a'),Id('b')),[],[CallStmt(Id('writeln'),[Id('i')])])],([],[Assign(Id('a'),FloatLiteral(120.0))]))])],[]),Continue()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,351))

	def test_312(self):
		input = """Var: a,b,c;
                Function: main
                Parameter: a
                Body:
                EndBody.
                Function: foo
                Parameter: a,b,c[1]
                Body:
                EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[])),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[1],None)],([],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,312))

	def test_316(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[If([(UnaryOp("""!""",BooleanLiteral(True)),[],[Assign(Id('a'),BinaryOp("""<""",Id('a'),Id('c'))),If([(BinaryOp(""">""",BinaryOp("""+""",Id('a'),Id('b')),Id('c')),[],[Assign(Id('a'),BinaryOp("""+""",Id('a'),Id('b')))]),(BinaryOp("""==""",Id('a'),Id('b')),[],[CallStmt(Id('writeln'),[Id('i')])])],([],[Assign(Id('a'),FloatLiteral(120.0))]))])],[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,316))

	def test_387(self):
		input = """
        Function: foo
        Parameter: a,b,c
        Body:
        nothing(a[1][1][b[k]]);
        EndBody."""
		expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[CallStmt(Id('nothing'),[ArrayCell(IntLiteral(1),[IntLiteral(1),ArrayCell(Id('k'),[])])])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,387))

	def test_391(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: a[5] = {1,4,3,2,0};
        Var: b[2][3]={{1,2,3},{4,5,6}};
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('a'),[5],ArrayLiteral([IntLiteral(1),IntLiteral(4),IntLiteral(3),IntLiteral(2),IntLiteral(0)])),VarDecl(Id('b'),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])]))],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,391))

	def test_309(self):
		input = """Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
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
x = 10;
fact (x);
EndBody."""
		expect = Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[1,3],ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(12),IntLiteral(1)]),ArrayLiteral([FloatLiteral(12.0),FloatLiteral(12000.0)])]),ArrayLiteral([IntLiteral(23)]),ArrayLiteral([IntLiteral(13),IntLiteral(32)])])),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[Assign(Id('a'),BinaryOp("""<""",Id('a'),Id('b'))),If([(BinaryOp("""==""",Id('n'),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp("""*""",Id('n'),CallStmt(Id('fact'),[BinaryOp("""-""",Id('n'),IntLiteral(1))])))]))])),FuncDecl(Id('main'),[],([],[Assign(Id('x'),IntLiteral(10)),CallStmt(Id('fact'),[Id('x')])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,309))

	def test_384(self):
		input = """
        Function: main_123_main
        Parameter: a, b[1][100]
        Body:
        While a<b Do
        EndWhile.
        EndBody."""
		expect = Program([FuncDecl(Id('main_123_main'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[1,100],None)],([],[While(BinaryOp("""<""",Id('a'),Id('b')),([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,384))

	def test_374(self):
		input = """Var: a,b,c;
Function: main
Body:
a = (a + b) +. (a-a-.a*a*.a\.b%!c&&a||a==b);
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[Assign(Id('a'),BinaryOp("""+.""",BinaryOp("""+""",Id('a'),Id('b')),BinaryOp("""==""",BinaryOp("""||""",BinaryOp("""&&""",BinaryOp("""-.""",BinaryOp("""-""",Id('a'),Id('a')),BinaryOp("""%""",BinaryOp("""\.""",BinaryOp("""*.""",BinaryOp("""*""",Id('a'),Id('a')),Id('a')),Id('b')),UnaryOp("""!""",Id('c')))),Id('a')),Id('a')),Id('b'))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,374))

	def test_359(self):
		input = """Var: a,b,c;
Function: main
Body:
foo(arg1, "???", foo(nothing));
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[Id('arg1'),StringLiteral("""???"""),CallStmt(Id('foo'),[Id('nothing')])])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,359))

	def test_368(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        a = b[something()[a[1]] + 1 ];
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[Assign(Id('a'),ArrayCell(BinaryOp("""+""",ArrayCell(ArrayCell(IntLiteral(1),[]),[]),IntLiteral(1)),[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,368))

	def test_313(self):
		input = """Var: a,b,c;
            Function: main
            Parameter: a
            Body:
            Var:x = 1, y;
            EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('y'),[],None),VarDecl(Id('x'),[],IntLiteral(1))],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,313))

	def test_344(self):
		input = """Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        a = !(x &&  y || b) && (a || abc);
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[Assign(Id('a'),BinaryOp("""&&""",UnaryOp("""!""",BinaryOp("""||""",BinaryOp("""&&""",Id('x'),Id('y')),Id('b'))),BinaryOp("""||""",Id('a'),Id('abc'))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,344))

	def test_305(self):
		input = """Var: a,b=1,c[3]={1,2,3};
Function: main
Body:
Return;
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],IntLiteral(1)),VarDecl(Id('c'),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id('main'),[],([],[Return(None)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,305))

	def test_321(self):
		input = """Function: main
                Parameter: a
                Body:
                    If 1 + a - b * foo() > 1 Then
                    EndIf.
                EndBody."""
		expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[If([(BinaryOp(""">""",BinaryOp("""-""",BinaryOp("""+""",IntLiteral(1),Id('a')),BinaryOp("""*""",Id('b'),CallStmt(Id('foo'),[]))),IntLiteral(1)),[],[])],[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,321))

	def test_385(self):
		input = """Function: somwname
Body:

EndBody."""
		expect = Program([FuncDecl(Id('somwname'),[],([],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,385))

	def test_301(self):
		input = """Var:x = 1;"""
		expect = Program([VarDecl(Id('x'),[],IntLiteral(1))])
		self.assertTrue(TestAST.checkASTGen(input,expect,301))

	def test_323(self):
		input = """Function: main
                Parameter: a
                Body:
                EndBody."""
		expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,323))

	def test_371(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        a = b[something()[a[1]] + 1][c + d < 1] + c *. d[1][21 * 0x21AF];
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[Assign(Id('a'),BinaryOp("""+""",ArrayCell(BinaryOp("""+""",ArrayCell(ArrayCell(IntLiteral(1),[]),[]),IntLiteral(1)),[BinaryOp("""<""",BinaryOp("""+""",Id('c'),Id('d')),IntLiteral(1))]),BinaryOp("""*.""",Id('c'),ArrayCell(IntLiteral(1),[BinaryOp("""*""",IntLiteral(21),IntLiteral(8623))]))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,371))

	def test_363(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        foo(arg1, "???", foo(nothing), {"asdab", {1,2.e2,123e1,"nothing"}});
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[Id('arg1'),StringLiteral("""???"""),CallStmt(Id('foo'),[Id('nothing')]),ArrayLiteral([StringLiteral("""asdab""")])])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,363))

	def test_302(self):
		input = """Var:x = 1, y;"""
		expect = Program([VarDecl(Id('y'),[],None),VarDecl(Id('x'),[],IntLiteral(1))])
		self.assertTrue(TestAST.checkASTGen(input,expect,302))

	def test_393(self):
		input = """Var: a,b,c;
Function: main
Parameter: a, a[1][12]
Body:
Var: x[1][2] = {"ab","da"};
a[3 + foo(2)] = a[b[2][3]] + 4;
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('a'),[1,12],None)],([VarDecl(Id('x'),[1,2],ArrayLiteral([StringLiteral("""ab"""),StringLiteral("""da""")]))],[Assign(ArrayCell(BinaryOp("""+""",IntLiteral(3),CallStmt(Id('foo'),[IntLiteral(2)])),[]),BinaryOp("""+""",ArrayCell(ArrayCell(IntLiteral(2),[IntLiteral(3)]),[]),IntLiteral(4)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,393))

	def test_397(self):
		input = """Var: a,b,c;
Function: main
Parameter: a, a[1][12]
Body:
If expr Then 
ElseIf expr Then
While expr Do EndWhile.
Do Return; While {{}} EndDo.
Else nothing(); a=b+a; Continue;
EndIf.
EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('a'),[1,12],None)],([],[If([(Id('expr'),[],[]),(Id('expr'),[],[While(Id('expr'),([],[])),Dowhile(([],[Return(None)]),ArrayLiteral([ArrayLiteral([])]))])],([],[CallStmt(Id('nothing'),[]),Assign(Id('a'),BinaryOp("""+""",Id('b'),Id('a'))),Continue()]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,397))

	def test_355(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Return (a < 1) || (b >. !c);
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[If([(UnaryOp("""!""",BooleanLiteral(True)),[],[Assign(Id('a'),BinaryOp("""<""",Id('a'),Id('c'))),If([(BinaryOp(""">""",BinaryOp("""+""",Id('a'),Id('b')),Id('c')),[],[Assign(Id('a'),BinaryOp("""+""",Id('a'),Id('b')))]),(BinaryOp("""==""",Id('a'),Id('b')),[],[CallStmt(Id('writeln'),[Id('i')])])],([],[Assign(Id('a'),FloatLiteral(120.0))]))])],[]),Return(BinaryOp("""||""",BinaryOp("""<""",Id('a'),IntLiteral(1)),BinaryOp(""">.""",Id('b'),UnaryOp("""!""",Id('c')))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,355))

	def test_361(self):
		input = """Var: a,b,c;
        Function: main
        Body:
        a = a[c[1][b]][1] < foo(arg1, "???", foo(nothing));
        EndBody."""
		expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('main'),[],([],[Assign(Id('a'),BinaryOp("""<""",ArrayCell(ArrayCell(IntLiteral(1),[Id('b')]),[IntLiteral(1)]),CallStmt(Id('foo'),[Id('arg1'),StringLiteral("""???"""),CallStmt(Id('foo'),[Id('nothing')])])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,361))

