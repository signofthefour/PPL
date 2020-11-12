import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_var_decl_1(self):
        input = """Var:x = 1;"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(1))])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_var_decl_2(self):
        input = """Var:x = 1, y;"""
        expect = Program([VarDecl(Id('y'), [], None),VarDecl(Id('x'),[],IntLiteral(1))])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_var_decl_3(self):
        input = """Var:x = 1, y = "abc", z = 1e2, l=True, a[1][2]={{1},{2}};"""
        expect = Program([VarDecl(Id('x'),[],IntLiteral(1)),VarDecl(Id('y'),[],StringLiteral('abc')),VarDecl(Id('z'),[],FloatLiteral(100.0)),VarDecl(Id('l'),[],BooleanLiteral('True')),VarDecl(Id('a'),[1,2],ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(2)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_var_decl_4(self):
        input = """Var:x[1] = {1};"""
        expect = Program([VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(1)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_var_decl_10(self):  
        input = """Var:x[1] = {1,2,3,4};"""
        expect = Program([VarDecl(Id("x"),[1],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    
    def test_func_decl_1(self):
        input = """Var: a,b,c;
                    Function: main
                    Parameter: a
                    Body:
                    EndBody."""

        expect = None
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    
    def test_func_decl_2(self):
        input = """Var: a,b,c;
                Function: main
                Parameter: a
                Body:
                EndBody.
                Function: foo
                Parameter: a,b,c[1]
                Body:
                EndBody."""
        expect = None
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_func_decl_3(self):
        input = """Var: a,b,c;
            Function: main
            Parameter: a
            Body:
            Var:x = 1, y;
            EndBody."""
        expect = None
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_if_stmt_1(self):
        input = """Function: main
                Parameter: a
                Body:
                    If 1 + a - b * foo() > 1 Then
                    EndIf.
                EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[If([(BinaryOp('>',BinaryOp('-',BinaryOp('+',IntLiteral('1'),Id('a')),BinaryOp('*',Id('b'),CallStmt(Id('foo'),[]))),IntLiteral('1')),[],[])],[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))


    def test_if_stmt_2(self):
        input = """Function: main
                Parameter: a
                Body:
                    If 1 Then
                    EndIf.
                EndBody."""
        expect = None
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_if_stmt_3(self):
        input = """Function: main
                Parameter: a
                Body:
                EndBody."""
        expect = None
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_for_stmt_1(self):
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
        expect = None
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_assign_1(self):
        input = """Function: main
                Parameter: a
                Body:
                (1 + c)[foo() + 1][1 + 2][a + v] = a;
                EndBody."""
        expect = None
        self.assertTrue(TestAST.checkASTGen(input,expect,332))