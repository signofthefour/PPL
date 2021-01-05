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

    # def test_ret(self):
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     EndBody.
    #     Function: foo
    #     Body: 
    #     Var: x = 1, y = 3;
    #     y = x;
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 506))

    # def test_ret(self):
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     EndBody.
    #     Function: foo
    #     Parameter: y, z
    #     Body: 
    #     Var: x = 1;
    #     y = x;
    #     z = 1.2;
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 507))
    
    # def test_arr(self):
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     EndBody.
    #     Function: foo
    #     Parameter: y, z
    #     Body: 
    #     Var: x = 1;
    #     y = x;
    #     z = {1,2};
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 508))

    # def test_arr(self):
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     EndBody.
    #     Function: foo
    #     Parameter: y, z[2][1]
    #     Body: 
    #     Var: x = 1;
    #     y = x;
    #     z = {{1},{2}};
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 509))
    
    # def test_arr_flit(self):
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     EndBody.
    #     Function: foo
    #     Parameter: y, z[2][1]
    #     Body: 
    #     Var: x = 1;
    #     y = x;
    #     z = {{1.2},{2.3}};
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 510))

    # def test_str_flit(self):
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     EndBody.
    #     Function: foo
    #     Parameter: y, z[2][1]
    #     Body: 
    #     Var: x = 1;
    #     y = x;
    #     z = {{"ab"},{"cd"}};
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 511))
    
    # def test_arr_blit(self):
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     EndBody.
    #     Function: foo
    #     Parameter: y, z[2][1]
    #     Body: 
    #     Var: x = 1;
    #     y = x;
    #     z = {{"ab"},{"cd"}};
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 511))

    # def test_infer(self):
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     EndBody.
    #     Function: foo
    #     Parameter: y, z[2][1][3]
    #     Body: 
    #     Var: x = 1;
    #     y = x;
    #     z[1][1][1] = 1;
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 512))

    # def test_if_without_infer(self):
    #     """Do not have else"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     EndBody.
    #     Function: foo
    #     Body:
    #     Var: y = True, x = 1;
    #     If y Then x = 2;
    #     EndIf.
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 513))

    # def test_if_with_else(self):
    #     """Do have else"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Body:
    #     Var: y = True, x = 1;
    #     If y Then x = 2;
    #     Return 1;
    #     Else x = 3;
    #     EndIf.
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 514))

    # def test_if_with_return(self):
    #     """Do have return"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Body:
    #     Var: y = True, x = 1;
    #     If y Then x = 2;
    #     Return 1;
    #     Else x = 3;
    #     EndIf.
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 515))

    # def test_if_with_inif(self):
    #     """Do have elseif"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Body:
    #     Var: y = True, x = 1;
    #     If y Then x = 2;
    #     ElseIf !y Then x =10;
    #     Return 1;
    #     Else x = 3;
    #     EndIf.
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 516))

    # def test_if_with_complex_expr(self):
    #     """Do have complex expr"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Body:
    #     Var: y = True, x = 1;
    #     If y && False Then x = 2;
    #     ElseIf 1 < 2 Then x =10;
    #     Return 1;
    #     Else x = 3;
    #     EndIf.
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 517))
    
    # def test_if_with_complex_expr(self):
    #     """Do have complex expr and infer"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Parameter: z
    #     Body:
    #     Var: y = True, x = 1;
    #     If y && z Then x = 2;
    #     ElseIf 1 < 2 Then x =10;
    #     Return 1;
    #     Else x = 3;
    #     EndIf.
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 518))

    # def test_simple_while(self):
    #     """Do have simple while"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Body:
    #     Var: y = True, x = 1;
    #     While y Do y = False;
    #     EndWhile.
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 518))

    # def test_simple_while_with_infer(self):
    #     """Do have simple while with infer type"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Parameter: z
    #     Body:
    #     Var: y = True, x = 1;
    #     While z Do y = False;
    #     EndWhile.
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 519))

    # def test_simple_while_with_infer(self):
    #     """Do have simple while which have decl"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Parameter: z
    #     Body:
    #     Var: y = True, x = 1;
    #     While z Do 
    #     Var: x = 1.2;
    #     y = False;
    #     Break;
    #     EndWhile.
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 519))

    # def test_simple_while_with_infer(self):
    #     """Do have simple while which have break"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Parameter: z
    #     Body:
    #     Var: y = True, x = 1;
    #     While z Do 
    #     Var: x = 1.2;
    #     y = False;
    #     Break;
    #     EndWhile.
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 520))

    # def test_simple_while_with_infer(self):
    #     """Do have simple while which have continue"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Parameter: z
    #     Body:
    #     Var: y = True, x = 1;
    #     While z Do 
    #     Var: x = 1.2;
    #     y = False;
    #     Continue;
    #     EndWhile.
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 521))

    # def test_simple_for(self):
    #     """Do have simple while which have break"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Body:
    #     Var: y = True, x = 1;
    #     For (x = 0, y, 1) Do
    #     x = 2;
    #     EndFor.
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 521))

    # def test_simple_dowhile(self):
    #     """Do have simple while which have break"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Body:
    #     Var: y = True, x = 1;
    #     Do x = 2 While y EndDo.
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 522))

    # def test_simple_dowhile(self):
    #     """Do have simple while which have break"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     foo(x);
    #     printStrLn("abs");
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Parameter: z
    #     Body:
    #     Var: y = True, x = 1;
    #     z = 1;
    #     Return ;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 523))

    # def test_callee(self):
    #     """Do param do not infer in function after"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     foo(x);
    #     printStrLn("abs");
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Parameter: z
    #     Body:
    #     Var: y = True, x = 1;
    #     printStrLn("abs");
    #     Return ;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 524))


    # def test_callee_expr(self):
    #     """Do param do not infer in function after"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1, y[1][2];
    #     x = foo();
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Body:
    #     Var: y = True, x = 1;
    #     printStrLn("abs");
    #     Return 1;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 525))

    # def test_arr_1(self):
    #     """Do param do not infer in function after"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1, y[1][2] = {{1,2}};
    #     Return;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 526))

    # def test_arr_2(self):
    #     """Do param do not infer in function after"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1, y[1][2] = {{1,2}};
    #     printStrLn(string_of_int(y[0][1]));
    #     Return;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 527))

    # def test_callee_ret(self):
    #     """Do param do not infer in function after"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x = 1;
    #     foo(x);
    #     printStrLn(string_of_int(x));
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Parameter: z
    #     Body: 
    #     Var: x = 1;
    #     z = 999;
    #     Return;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 528))

    # def test_callee_ret(self):
    #     """Do param do not infer in function after"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x[3] = {1,2,3};
    #     foo(x);
    #     printStrLn(string_of_int(x[1]));
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Parameter: z[3]
    #     Body: 
    #     Var: x = 1;
    #     z[1] = 999;
    #     Return;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 529))

    # def test_callee_ret(self):
    #     """Do param do not infer in function after"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x[3] = {1,2,3};
    #     foo(x);
    #     printStrLn(string_of_int(x[1]));
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Parameter: z[3]
    #     Body: 
    #     Var: x = 1;
    #     z[1] = 999;
    #     x= 10;
    #     printStrLn(string_of_int(x));
    #     Return;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 530))

    # def test_callee_ret(self):
    #     """Do param do not infer in function after"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x[3] = {1,2,3};
    #     foo(x);
    #     printStrLn(string_of_int(x[1]));
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Parameter: z[3]
    #     Body: 
    #     Var: x = 1;
    #     z[1] = 999;
    #     x= 10 + fooo(1);
    #     printStrLn(string_of_int(x));
    #     Return;
    #     EndBody.
    #     Function: fooo
    #     Parameter: z
    #     Body: 
    #     Return z;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 531))
    # def test_if(self):
    #     """Do param do not infer in function after"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x[3] = {1,2,3};
    #     If x[0] < 2 Then x[1] = 5;
    #     ElseIf x[1] > 4 Then x[1] =10;
    #     Return;
    #     Else x[1] = 3;
    #     EndIf.
    #     printStrLn(string_of_int(x[1]));
    #     Return;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 532))

    # def test_callee(self):
    #     """Do param do not infer in function after"""
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x[3] = {1,2,3};
    #     x[1] = foo(x[2], foo(1,2));
    #     Return;
    #     EndBody.
    #     Function: foo
    #     Parameter: x, y
    #     Body:
    #     Return x + y;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 533))

    # def test_if_var(self):
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: x[3] = {1,2,3};
    #     If x[1] > 1 Then
    #     Var: x = 1;
    #     printStrLn(string_of_int(x));
    #     EndIf.
    #     Return;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 534))

    # def test_while_var(self):
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: y[3] = {1,2,3}, x = 10;
    #     While y[1] < 10 Do
    #     Var: x = 1;
    #     printStrLn(string_of_int(x));
    #     y[1] = y[1] + 1;
    #     EndWhile.
    #     Return;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 535))

    # def test_dowhile_var(self):
    #     input = """
    #     Function: main
    #     Body: 
    #     Var: y[3] = {1,2,3}, x = 10;
    #     Do
    #     Var: x = 1;
    #     printStrLn(string_of_int(x));
    #     y[1] = y[1] + 1;
    #     While y[1] < 10
    #     EndDo.
    #     Return;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 536))

    # def test_dowhile_var(self):
    #     input = """
    #     Var: l = 999;
    #     Function: main
    #     Body: 
    #     Var: y[3] = {1,2,3}, z = 10, x = 1;
    #     For (x = 1, x < 10, 1) Do
    #     Var: z = 1;
    #     printStrLn(string_of_int(x));
    #     EndFor.
    #     printStrLn(string_of_int(l));
    #     Return;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_static(self):
        input = """
        Function: main
        Body:
        Var: x = 1;
        printStrLn(string_of_int(foo(1, foo(x, 1))));
        Return;
        EndBody.
        Function: foo
        Parameter: x, y
        Body:
        Return x + y;
        EndBody.
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 538))


    # def test_static(self):
    #     input = """
    #     Var: k = 999;
    #     Function: main
    #     Body: 
    #     Var: y[3] = {1,2,3}, z = 10, x = 1;
    #     For (x = 1, x < 10, 1) Do
    #     Var: z = 1;
    #     printStrLn(string_of_int(k));
    #     EndFor.
    #     Return;
    #     EndBody.
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 538))
