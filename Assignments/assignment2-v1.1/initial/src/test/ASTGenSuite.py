import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x = {1 , 2};
        """
        expect = Program([VarDecl(Id("x"),[],ArrayLiteral([IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    # def test_simple_program2(self):
    #     """Simple program: int main() {} """
    #     input = """Var:x[12];"""
    #     expect = Program([VarDecl(Id("x"),[12],None)])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,301))

    # def test_simple_program3(self):
    #     """
    #         Function: test
    #             Body:
    #                 a = 1 -. -9;
    #             EndBody.
    #     """
    #     expect = a
    #     self.assertTrue(TestAST.checkASTGen(input,expect,303))