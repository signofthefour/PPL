import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_int(self):
    #     """Simple program: int main() {} """
    #     input = """Function: main
    #                Body: 
    #                     print(string_of_int(120));
    #                EndBody."""
    #     expect = "120"
    #     self.assertTrue(TestCodeGen.test(input,expect,500))
    # def test_int_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],([],[
    # 			CallStmt(Id("print"),[
    #                 CallExpr(Id("string_of_int"),[IntLiteral(120)])])]))])
    # 	expect = "120"
    # 	self.assertTrue(TestCodeGen.test(input,expect,501))

    # def test_decl(self):
    #     input = """
    #     Var: x = 1;
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    # def test_main(self):
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     EndBody.
    #     Function: foo
    #     Body: 
    #     Var: x = 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 503))
    
    # def test_ret(self):
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     EndBody.
    #     Function: foo
    #     Body: 
    #     Var: x = 1;
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 504))
    # def test_ret(self):
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     EndBody.
    #     Function: foo
    #     Parameter: z
    #     Body: 
    #     Var: x = 1, y = 3;
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_ret(self):
        input = """
        Function: main
        Body: 
        Var: x = 1;
        EndBody.
        Function: foo
        Body: 
        Var: x = 1, y = 3;
        y = x;
        Return 1;
        EndBody.
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 506))