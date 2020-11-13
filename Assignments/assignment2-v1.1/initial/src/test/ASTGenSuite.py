import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x;
        """
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = """Var:x[12];"""
        expect = Program([VarDecl(Id("x"),[12],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))