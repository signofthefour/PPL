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
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_var_decl_3(self):
        input = """Var:x = 1, y = "abc", z = 1e2, l=True, a[1][2]={{1},{2}};"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_var_decl_10(self):  
        input = """Var:x[1] = {1,2,3,4};"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,310)) 
   