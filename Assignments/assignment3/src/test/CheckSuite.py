import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_undeclared_function(self):
        """Simple program: main"""
        input = """ Var: x,y=1;
        Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        """Complex program"""
        input = """Function: main  
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """Function: main 
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"),[],([],[
            CallExpr(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_diff_numofparam_stmt_use_ast(self):
        """Complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_init_1(self):
        """Simple program: main"""
        input = """ Var: x,y={};
        Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_init_2(self):
        """Simple program: main"""
        input = """ Var: x="string",y[1][2]={{1,2}};
        Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_init_3(self):
        """Not same dimen"""
        input = """ Var: x="string",y[1][2]={{1,{2}}};
        Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_init_4(self):
        """Not same dimen"""
        input = """ Var: x="string",y[1][2]={{{1},{2}}};
        Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_init_5(self):
        """Not same dimen"""
        input = """ Var: x="string",y[1][2]={1,1.2};
        Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,410))
    
    def test_func_decl(self):
        """Not same dimen"""
        input = """ Var: x="string",y[1][2]={{1,2}};
        Function: foo
        Body:
        Return;
        EndBody.
        Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,411))
    
    def test_no_entry_point(self):
        input = """ Var: x="string",y[1][2]={{1,2}};
        Function: foo
        Body:
        Return;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,412))
    
    def test_func_decl_2(self):
        input = """ Var: x="string",y[1][2]={{1,2}};
        Function: main
        Parameter: x, y,x[1][2]
        Body:
        Return;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,413))
    
    def test_func_decl_3(self):
        """Not same dimen"""
        input = """ Var: x="string",y[1][2]={{1,2}};
        Function: foo
        Body:
        Return 1;
        EndBody.
        Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_func_decl_4(self):
        """Not same dimen"""
        input = """ Var: x="string",y[1][2]={{1,2}};
        Function: foo
        Parameter: x
        Body:
        x = 1 + 2;
        Return 1;
        EndBody.
        Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,415))
    
    def test_func_decl_5(self):
        """
        Var decl in function
        """
        input = """ Var: x="string",y[1][2]={{1,2}};
        Function: foo
        Parameter: x
        Body:
        x = 1 + 2;
        Return 1;
        EndBody.
        Function: main
        Body:
        x = 1. +. 2.;
        foo(x);
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_func_decl_6(self):
        """
        Var decl in function
        """
        input = """ Var: x=1.2,y[1][2]={{1,2}};
        Function: foo
        Parameter: x
        Body:
        x = 1 + 2;
        Return 1;
        EndBody.
        Function: main
        Body:
        x = 1. +. 2.;
        foo(x);
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_func_decl_7(self):
        """
        Var decl in function
        """
        input = """ Var: x=1,y[1][2]={{1,2}};
        Function: foo
        Parameter: x
        Body:
        x = 1 + 2;
        Return;
        EndBody.
        Function: main
        Body:
        foo(x);
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_func_decl_8(self):
        """
        Var decl in function
        """
        input = """ Var: x=1,y[1][2]={{1,2}};
        Function: foo
        Parameter: x
        Body:
        x = 1. + 2.;
        Return;
        EndBody.
        Function: main
        Body:
        foo(x);
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,419))
    
    def test_func_decl_9(self):
        """
        Var decl in function
        """
        input = """ Var: x=1,y[1][2]={{1,2}};
        Function: foo
        Parameter: x
        Body:
        x = 1. +. 2.;
        Return;
        EndBody.
        Function: main
        Body:
        foo(x);
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_func_decl_10(self):
        """
        Var decl in function
        """
        input = """ Var: x=1,y[1][2]={{1,2}};
        Function: main
        Body:
        Var: x;
        x = 1 + foo(x);
        EndBody.
        Function: foo
        Parameter: x
        Body:
        x = 1 + 2;
        Return 1;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,421))
    
    def test_func_decl_11(self):
        """
        Var decl in function
        """
        input = """ Var: x=1,y[1][2]={{1,2}};
        Function: main
        Body:
        Var: x = 1;
        x = 1 + foo(x);
        EndBody.
        Function: foo
        Parameter: x
        Body:
        x = 1 + 2;
        Return 1;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,422))
    
    def test_func_decl_12(self):
        """
        Var decl in function
        """
        input = """ Var: x=1,y[1][2]={{1,2}};
        Function: main
        Body:
        Var: x = 1;
        x = 1 + foo(x,y);
        EndBody.
        Function: foo
        Parameter: x,a[1][2]
        Body:
        x = 1 + 2;
        Return 1;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,423))
    
    def test_func_decl_13(self):
        """
        Var decl in function
        """
        input = """ Var: x=1,y[1][2]={{1,2}};
        Function: main
        Body:
        Var: x = 1;
        x = 1 + foo(x,y);
        EndBody.
        Function: foo
        Parameter: x,a[1][3]
        Body:
        x = 1 + 2;
        Return 1;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,424))
    
    def test_undecl_var(self):
        """
        Var decl in function
        """
        input = """ Var: x=1,y[1][2]={{1,2}};
        Function: main
        Body:
        Var: x = 1;
        x = 1 + foo(x,y,z);
        EndBody.
        Function: foo
        Parameter: x,a[1][3]
        Body:
        x = 1 + 2;
        Return 1;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,425))
    
    def test_call_expr(self):
        """
        Var decl in function
        """
        input = """ Var: x=1,y[1][2]={{1,2}};
        Function: main
        Body:
        Var: x = 1;
        x = 1 + foo(x,foo(x, True));
        EndBody.
        Function: foo
        Parameter: x,y
        Body:
        x = 1 + 2;
        Return 1;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,426))
    
    def test_call_expr_1(self):
        """
        Var decl in function
        """
        input = """ Var: x=1,y[1][2]={{1,2}};
        Function: main
        Body:
        Var: x = 1;
        x = 1 + foo(x,foo(x, 1));
        EndBody.
        Function: foo
        Parameter: x,y
        Body:
        x = 1 + 2;
        Return 1;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,427))
    
    def test_call_expr_2(self):
        """
        Var decl in function
        """
        input = """ Var: x=1,y[1][2]={{1,2}};
        Function: main
        Parameter: main
        Body:
            Var: foo;
            foo = foo + main();
            Return 1;
        EndBody.
        Function: foo
        Parameter: x,y
        Body:
        x = 1 + 2;
        Return 1;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,428))
    
    def test_redecl_global(self):
        """
        Var decl in function
        """
        input = """ Var: x=1,y[1][2]={{1,2}};
        Var: read;
        Function: main
        Parameter: main
        Body:
            Var: foo;
            foo = foo + main();
            Return 1;
        EndBody.
        Function: foo
        Parameter: x,y
        Body:
        x = 1 + 2;
        Return 1;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,429))
    
    def test_return_infunc(self):
        """
        Var decl in function
        """
        input = """ Var: x=1,y[1][2]={{1,2}};
        Function: main
        Body:
            Var: foo;
            foo = foo + main();
            Return 1;
        EndBody.
        Function: foo
        Parameter: x,y
        Body:
        x = 1 + 2;
        Return 1;
        Return 1.1;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,430))
    
    def test_return_in_while(self):
        """
        Var decl in function
        """
        input = """ Var: x=1,y[1][2]={{1,2}};
        Function: main
        Body:
            Var: foo;
            foo = foo + main();
            Return 1;
        EndBody.
        Function: foo
        Parameter: x,y
        Body:
        x = 1 + 2;
        While (y)
        Do
        Return 1.1;
        EndWhile.
        Return 1;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,431))
    
    def test_return_global(self):
        """
        Var decl in function
        """
        input = """ Var: x=1,y[1][2];
        Function: main
        Body:
            Var: foo;
            foo = foo + main();
            Return 1;
        EndBody.
        Function: foo
        Parameter: x
        Body:
        x = 1 + 2;
        Return y;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,432))
    
    def test_return_index_expr(self):
        """
        Var decl in function
        """
        input = """ Var: x=1,y[1][2];
        Function: main
        Body:
            Var: foo;
            foo = foo + main();
            Return 1;
        EndBody.
        Function: foo
        Parameter: x
        Body:
        Return 1;
        EndBody.
        Function: foo1
        Parameter: x, b[1]
        Body:
        b[foo(3) + 2] = b[y[1][1]] + 4;
        Return y;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,433))
    
    def test_return_index_expr_1(self):
        """
        From index op ifer type of function
        """
        input = """ Var: x=1,y[1][2];
        Function: main
        Body:
            Var: foo;
            foo = foo + main();
            Return 1;
        EndBody.
        Function: foo1
        Parameter: x, b[1]
        Body:
        b[foo(3) + 2] = b[y[1][1]] + 4;
        Return y;
        EndBody.
        Function: foo
        Parameter: x
        Body:
        Return 1;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,434))
    
    def test_return_index_expr_2(self):
        """
        From index op ifer type of function
        """
        input = """ Var: x=1,y[1][2];
        Function: main
        Body:
            Var: foo;
            foo = foo + main();
            Return 1;
        EndBody.
        Function: foo1
        Parameter: x, b[1]
        Body:
        b[foo(3) + 2] = b[y[1][1]] + 4;
        Return y;
        EndBody.
        Function: foo
        Parameter: x
        Body:
        Return 1.1;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,435))
    
    def test_return_index_expr_3(self):
        """
        From index op ifer type of function
        """
        input = """ Var: x=1,y[1][2];
        Function: main
        Body:
            Var: foo;
            foo = foo + main();
            Return 1;
        EndBody.
        Function: foo1
        Parameter: x, b[1]
        Body:
        b[foo(3)[1][3] + 2] = b[y[1][1]] + 4;
        Return y;
        EndBody.
        Function: foo
        Parameter: x
        Body:
        Return y;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,436))
    
    def test_return_index_expr_4(self):
        """
        From index op ifer type of function
        """
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Body:
            Var: foo;
            foo = foo + main();
            Return 1;
        EndBody.
        Function: foo1
        Parameter: x, b[1]
        Body:
        b[foo(3)[1][3] + 2] = b[y[1][1]] + 4;
        Return y;
        EndBody.
        Function: foo
        Parameter: x
        Body:
        Return y;
        EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,437))
    
    def test_return_index_expr_5(self):
        """
        From index op ifer type of function
        """
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Body:
            Var: foo;
            foo = foo + main();
            Return 1;
        EndBody.
        Function: foo
        Parameter: x
        Body:
        Return y;
        EndBody.
        Function: foo1
        Parameter: x, b[1]
        Body:
        b[foo(3)[1][3] + 2] = b[y[1][1]] + 4;
        Return y;
        EndBody.
        """
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,438))