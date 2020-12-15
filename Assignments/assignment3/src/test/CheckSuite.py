import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *
# from AST_GEN_TEST import *

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
        expect = str(TypeMismatchInStatement(VarDecl(Id("y"),[],ArrayLiteral([]))))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_init_2(self):
        """Simple program: main"""
        input = """ Var: x="string",y[1][2]={{1,2}};
        Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_init_3(self):
        """Not same dimen"""
        input = """ Var: x="string",y[1][2]={{1,{2}}};
        Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(InvalidArrayLiteral(ArrayLiteral([IntLiteral(1),ArrayLiteral([IntLiteral(2)])])))
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_init_4(self):
        """Not same dimen"""
        input = """ Var: x="string",y[1][2]={{{1},{2}}};
        Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(InvalidArrayLiteral(ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(2)])])))
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_init_5(self):
        """Not same dimen"""
        input = """ Var: x="string",y[1][2]={1,1.2};
        Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(InvalidArrayLiteral(ArrayLiteral([IntLiteral(1),FloatLiteral(1.2)])))
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
        expect = str(FunctionNotReturn("main"))
        self.assertTrue(TestChecker.test(input,expect,411))
    
    def test_no_entry_point(self):
        input = """ Var: x="string",y[1][2]={{1,2}};
        Function: foo
        Body:
        Return;
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,412))
    
    def test_func_decl_2(self):
        input = """ Var: x="string",y[1][2]={{1,2}};
        Function: main
        Parameter: x, y,x[1][2]
        Body:
        Return;
        EndBody."""
        expect = str(Redeclared(Parameter(), "x"))
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
                
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[])))
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
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[])))
        
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
        expect = str(TypeMismatchInStatement(Assign(Id("x"),BinaryOp("""+.""",FloatLiteral(1.0),FloatLiteral(2.0)))))
        
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
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("x")])))
        
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
        expect = str(FunctionNotReturn("main"))
        
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
        expect = str(TypeMismatchInExpression(BinaryOp("""+""",FloatLiteral(1.0),FloatLiteral(2.0))))
        
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
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("x")])))
        
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
        expect = str(TypeCannotBeInferred(Assign(Id("x"),BinaryOp("""+""",IntLiteral(1),CallExpr(Id("foo"),[Id("x")])))))
        
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
        expect = str(FunctionNotReturn("main"))
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
        expect = str(FunctionNotReturn("main"))
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
        expect = str(FunctionNotReturn("main"))
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
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[Id("x"),Id("y"),Id("z")])))
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

        expect = str(TypeMismatchInExpression(BinaryOp("""+""",IntLiteral(1),CallExpr(Id("foo"),[Id("x"),CallExpr(Id("foo"),[Id("x"),BooleanLiteral(True)])]))))

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
        expect = str(FunctionNotReturn("main"))

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
        expect = str(Undeclared(Function(), "main"))

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
        expect = str(Redeclared(Variable(), "read"))
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
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.1))))
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
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))

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
        expect = str(TypeCannotBeInferred(Return(Id("y"))))
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
        expect = str()
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
        expect = str()
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
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.1))))

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
        expect = str(TypeMismatchInStatement(Return(Id("y"))))
        
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
        expect = str(TypeMismatchInStatement(Return(Id("y"))))
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
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,438))
    
    def test_for_loop(self):
        """
        From index op ifer type of function
        """
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Body:
            Var: foo;
            Var: i , x;
            For (i = 1, i <= x*x,i*i+.1.5)
            Do x=x+1;
            EndFor.
            Return 1;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("""+.""",BinaryOp("""*""",Id("i"),Id("i")),FloatLiteral(1.5))))

        self.assertTrue(TestChecker.test(input,expect,439))
    
    def test_for_loop_1(self):
        """
        From index op ifer type of function
        """
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Body:
            Var: foo;
            Var: i , x;
            For (i = 1, i <= x*x,i*i+1)
            Do x=x+1;
            Return 1.1;
            EndFor.
            Return 1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,440))
    
    def test_for_loop_2(self):
        """
        From index op ifer type of function
        """
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Body:
            Var: foo;
            Var: i , x;
            For (i = 1, i <= x*x,i*i+1)
            Do x=x+1;
            For (i = 1, i <= x*x,i*i+1)
            Do x=x+1;
            Return True;
            EndFor.
            Return 1.1;
            EndFor.
            Return 1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.1))))

        self.assertTrue(TestChecker.test(input,expect,441))
    
    def test_return_type(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x
        Body:
            x= 1+foo(1);
            foo(1);
        Return;
        EndBody.
        Function: foo
        Parameter: x
        Body:
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[IntLiteral(1)])))

        self.assertTrue(TestChecker.test(input,expect,442))
    
    def test_return_type_1(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x, y[1][3]
        Body:
            x= 1+foo(1);
            Return y;
        EndBody.
        Function: foo
        Parameter: x
        Body:
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id("y"))))

        self.assertTrue(TestChecker.test(input,expect,443))
    
    def test_return_type_2(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x, y[1][3]
        Body:
            x= 1+foo(1);
            Return y;
        EndBody.
        Function: foo
        Parameter: x
        Body:
        Return 1.1;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id("y"))))

        self.assertTrue(TestChecker.test(input,expect,444))
    
    def test_return_type_3(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x, y[1][3]
        Body:
        Var: i;
            For (i = 1, i <= x*x,i*i+1)
            Do x=x+1;
            If True Then
            Return True;
            EndIf.
            EndFor.
        EndBody.
        Function: foo
        Parameter: x
        Body:
        x = 1 + main(x, y);
        Return 1.1;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("""+""",IntLiteral(1),CallExpr(Id("main"),[Id("x"),Id("y")]))))

        self.assertTrue(TestChecker.test(input,expect,445))
    
    def test_return_type_4(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x, y[1][3]
        Body:
        Var: i;
        x = 1;
        If x Then
        EndIf.
        Return;
        EndBody.
        Function: foo
        Parameter: x
        Body:
        Return 1.1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(If([(Id("x"),[],[])],[])))

        self.assertTrue(TestChecker.test(input,expect,446))
    
    def test_return_type_5(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x, y[1][3]
        Body:
        For (x = 1, x>1 , 0.+.1.) Do
        EndFor.
        Return;
        EndBody.
        Function: foo
        Parameter: x
        Body:
        Return 1.1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(For(Id("x"),IntLiteral(1),BinaryOp(""">""",Id("x"),IntLiteral(1)),BinaryOp("""+.""",FloatLiteral(0.0),FloatLiteral(1.0)),([],[]))))

        self.assertTrue(TestChecker.test(input,expect,447))
    
    def test_return_type_6(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x, y[1][3]
        Body:
        For (x = True, x>1 , 0 + 1) Do
        EndFor.
        Return;
        EndBody.
        Function: foo
        Parameter: x
        Body:
        Return 1.1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(For(Id("x"),BooleanLiteral(True),BinaryOp(""">""",Id("x"),IntLiteral(1)),BinaryOp("""+""",IntLiteral(0),IntLiteral(1)),([],[]))))

        self.assertTrue(TestChecker.test(input,expect,448))
    
    def test_return_type_7(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x, y[1][3]
        Body:
        For (x = 1, x + 1 , 0 + 1) Do
        EndFor.
        Return;
        EndBody.
        Function: foo
        Parameter: x
        Body:
        Return 1.1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(For(Id("x"),IntLiteral(1),BinaryOp("""+""",Id("x"),IntLiteral(1)),BinaryOp("""+""",IntLiteral(0),IntLiteral(1)),([],[]))))

        self.assertTrue(TestChecker.test(input,expect,449))
    
    def test_return_type_8(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x, y[1][3]
        Body:
        For (x = 1, False , y) Do
        EndFor.
        Return;
        EndBody.
        Function: foo
        Parameter: x
        Body:
        Return 1.1;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,450))
    
    def test_assign_stmt(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x, y
        Body:
        Var: a = 1;
        y = a + foo(x);
        EndBody.
        Function: foo
        Parameter: x
        Body:
        Return 1;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id("y"),BinaryOp("""+""",Id("a"),CallExpr(Id("foo"),[Id("x")])))))

        self.assertTrue(TestChecker.test(input,expect,451))
    
    def test_assign_stmt_2(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x, y
        Body:
        Var: a = 1;
        x = 1;
        y = a + foo(x);
        Return;
        EndBody.
        Function: foo
        Parameter: x
        Body:
        Return 1.1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.1))))

        self.assertTrue(TestChecker.test(input,expect,452))
    
    def test_assign_stmt_3(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x, y
        Body:
        Var: a = 1;
        x = 1;
        y = a + foo(x);
        Return;
        EndBody.
        Function: foo
        Parameter: x
        Body:
        Return 1.1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.1))))

        self.assertTrue(TestChecker.test(input,expect,453))
    
    def test_assign_stmt_4(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x, y
        Body:
        Var: a = 1;
        x = 1;
        y = a + foo(x, foo(x, 1));
        Return;
        EndBody.
        Function: foo
        Parameter: x, y
        Body:
        Return 1.1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.1))))

        self.assertTrue(TestChecker.test(input,expect,454))
    
    def test_assign_stmt_5(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x
        Body:
        Var: a = 1;
        x = 1;
        y[1] = a;
        Return;
        EndBody.
        Function: foo
        Parameter: x, y
        Body:
        Return 1.1;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id("y"),[IntLiteral(1)])))

        self.assertTrue(TestChecker.test(input,expect,455))
    
    def test_assign_stmt_6(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x
        Body:
        Var: a = 1;
        x = 1;
        y[1][2] = a;
        Return;
        EndBody.
        Function: foo
        Parameter: x, y
        Body:
        Return 1.1;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,456))
    
    def test_assign_stmt_7(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x
        Body:
        Var: a = 1;
        x = 1;
        y = a;
        Return;
        EndBody.
        Function: foo
        Parameter: x, y
        Body:
        Return 1.1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("y"),Id("a"))))
        
        self.assertTrue(TestChecker.test(input,expect,457))
    
    def test_58(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x
        Body:
        Return x;
        EndBody.
        Function: foo
        Parameter: x, y
        Body:
        Return 1.1;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id("x"))))

        self.assertTrue(TestChecker.test(input,expect,458))
    
    def test_59(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        a[1+1][0.5+.1.5] = 1;
        Return a;
        EndBody.
        Function: foo
        Parameter: x, y
        Body:
        Return 1.1;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id("a"),[BinaryOp("""+""",IntLiteral(1),IntLiteral(1)),BinaryOp("""+.""",FloatLiteral(0.5),FloatLiteral(1.5))])))

        self.assertTrue(TestChecker.test(input,expect,459))
    
    def test_60(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        a[1+1][x] = y;
        Return a;
        EndBody.
        Function: foo
        Parameter: x, y
        Body:
        Return 1.1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("a"),[BinaryOp("""+""",IntLiteral(1),IntLiteral(1)),Id("x")]),Id("y"))))

        self.assertTrue(TestChecker.test(input,expect,460))
    
    def test_61(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][0.5]=1;
        Return a;
        EndBody.
        Function: foo
        Parameter: x, y
        Body:
        Return 1.1;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[Id("x")])))

        self.assertTrue(TestChecker.test(input,expect,461))
    
    def test_501(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][0.5]=1;
        Return a;
        EndBody.
        Function: foo
        Parameter: x
        Body:
        Return 1.1;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id("foo"),[Id("x")]),[BinaryOp("""+""",Id("x"),IntLiteral(3)),FloatLiteral(0.5)]),IntLiteral(1))))
        

        self.assertTrue(TestChecker.test(input,expect,501))
    
    def test_62(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y
        Body:
        Return 1.1;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][0.5]=1;
        Return a;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[Id("x")])))

        self.assertTrue(TestChecker.test(input,expect,462))
    
    def test_63(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y
        Body:
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][0.5]=1;
        Return a;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,463))
    
    def test_64(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x
        Body:
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][0.5]=1;
        Return a;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(CallExpr(Id("foo"),[Id("x")]),[BinaryOp("""+""",Id("x"),IntLiteral(3)),FloatLiteral(0.5)])))

        self.assertTrue(TestChecker.test(input,expect,464))
    
    # def test_65(self):
    #     input = """ Var: x=1,y[1][2] = {{1,2}};
    #     Function: foo
    #     Parameter: x
    #     Body:
    #     Return y;
    #     EndBody.
    #     Function: main
    #     Parameter: x
    #     Body:
    #     Var: a[1][2];
    #     foo(x)[x+3][2]=1;
    #     Return a;
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(input,expect,502))
    
    def test_65(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x
        Body:
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][2]=1;
        a[1][1] = 2;
        Return a;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,465))
    
    def test_66(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x
        Body:
        If True Then
                ElseIf True Then
                    Return a;
                EndIf.
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][2]=1;
        a[1][1] = 2;
        Return a;
        EndBody.
        """
        expect = str(Undeclared(Variable(), "a"))

        self.assertTrue(TestChecker.test(input,expect,466))
    
    def test_67(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x
        Body:
        Var: a = 1;
        If a Then
                ElseIf True Then
                    a = 12;
                EndIf.
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][2]=1;
        a[1][1] = 2;
        Return a;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(If([(Id("a"),[],[]),(BooleanLiteral(True),[],[Assign(Id("a"),IntLiteral(12))])],[])))
        
        self.assertTrue(TestChecker.test(input,expect,467))
    
    def test_68(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x
        Body:
        Var: a = True;
        If a Then
        ElseIf True Then
        a = 12;
        EndIf.
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][2]=1;
        a[1][1] = 2;
        Return a;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),IntLiteral(12))))

        self.assertTrue(TestChecker.test(input,expect,468))
    
    def test_69(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x
        Body:
        Var: a = True;
        If a Then
        ElseIf True Then
        a = False;
        EndIf.
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][2]=1;
        a[1][1] = 2;
        Return a;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,469))
    
    def test_70(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x
        Body:
        Var:a,b,c,d;
                    a = a + b || c - d;
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][2]=1;
        a[1][1] = 2;
        Return a;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("""||""",BinaryOp("""+""",Id("a"),Id("b")),BinaryOp("""-""",Id("c"),Id("d")))))

        self.assertTrue(TestChecker.test(input,expect,470))

    def test_71(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x
        Body:
        Var:a,b,c,d;
        a = b || c >. d;
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][2]=1;
        a[1][1] = 2;
        Return a;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp(""">.""",BinaryOp("""||""",Id("b"),Id("c")),Id("d"))))

        self.assertTrue(TestChecker.test(input,expect,471))
    
    def test_72(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x
        Body:
        Var:a,b,c,d;
        a = b || (c >. d);
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][2]=1;
        a[1][1] = 2;
        Return a;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,472))
    
    def test_73(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x
        Body:
        Var:a,b,c,d;
        a = b || (c >. d);
        a = 1;
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][2]=1;
        a[1][1] = 2;
        Return a;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),IntLiteral(1))))
        
        self.assertTrue(TestChecker.test(input,expect,473))
    
    def test_74(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x
        Body:
        Var:a,b,c,d;
        a = b || (c >. d);
        a = c;
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][2]=1;
        a[1][1] = 2;
        Return a;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),Id("c"))))
        
        self.assertTrue(TestChecker.test(input,expect,474))
    
    def test_75(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x
        Body:
        Var:a,b,c,d;
        a = b || (c >. d);
        c = c - b;
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][2]=1;
        a[1][1] = 2;
        Return a;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("""-""",Id("c"),Id("b"))))

        
        self.assertTrue(TestChecker.test(input,expect,476))
    
    def test_77(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x
        Body:
        Var:a,b,c,d;
        a = b || (c >. d);
        c = c - d;
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][2]=1;
        a[1][1] = 2;
        Return a;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("""-""",Id("c"),Id("d"))))
        
        self.assertTrue(TestChecker.test(input,expect,477))
    
    def test_78(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:a,b,c,d;
        a = b || (c >. d);
        c = c -. d;
        y = c;
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][2]=1;
        a[1][1] = 2;
        Return a;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("y"),Id("c"))))
        
        self.assertTrue(TestChecker.test(input,expect,478))
    
    def test_79(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:a,b,c,d;
        a = b || (c >. d);
        c = c -. d;
        y[1][1] = c;
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][2]=1;
        a[1][1] = 2;
        Return a;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[Id("x")])))

        self.assertTrue(TestChecker.test(input,expect,479))
    
    def test_102(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:a,b,c,d;
        a = b || (c >. d);
        c = c -. d;
        y[1][1] = c && d;
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][2]=1;
        a[1][1] = 2;
        Return a;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("""&&""",Id("c"),Id("d"))))

        self.assertTrue(TestChecker.test(input,expect,502))
    
    def test_80(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x
        Body:
        Var:a,b,c,d;
        a = b || (c >. d);
        c = c -. d;
        y[1][1] = c && d;
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Var: a[1][2];
        foo(x)[x+3][2]=1;
        a[1][1] = 2;
        Return a;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("""&&""",Id("c"),Id("d"))))

        self.assertTrue(TestChecker.test(input,expect,480))
    
    def test_81(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:a[2] = {1,2}, b[2] = {2,3};
        main(a);
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Return x;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id("y"))))

        self.assertTrue(TestChecker.test(input,expect,481))
    
    def test_82(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:a[2] = {1,2}, b[2] = {2,3};
        main(a[1]);
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Return x;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id("y"))))

        self.assertTrue(TestChecker.test(input,expect,482))
    
    def test_83(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:a[2] = {1,2}, b[2] = {2.,3.};
        main(a[2]);
        main(b);
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Return x;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[Id("b")])))

        self.assertTrue(TestChecker.test(input,expect,483))
    
    def test_84(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:a[2] = {1,2}, b[2] = {2,2};
        main(a[2]);
        main(b[2]);
        Return y;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Return x;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id("y"))))

        self.assertTrue(TestChecker.test(input,expect,484))
    
    def test_85(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:a[2] = {1,2}, b[2] = {2,2};
        main(a);
        main(b[2]);
        Return a;
        EndBody.
        Function: main
        Parameter: x
        Body:
        Return x;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(Id("x"))))

        self.assertTrue(TestChecker.test(input,expect,485))
    
    def test_86(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:a[2] = {1,2}, b[2] = {2,2};
        main(a);
        main(b[2]);
        Return a;
        EndBody.
        Function: main
        Parameter: x
        Body:
        x = 1;
        Return x;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),IntLiteral(1))))

        self.assertTrue(TestChecker.test(input,expect,486))
    
    def test_87(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:a[2] = {1,2}, b[2] = {2,2};
        main(a);
        main(b[2]);
        Return a;
        EndBody.
        Function: main
        Parameter: x
        Body:
        x[1] = True;
        Return x;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("x"),[IntLiteral(1)]),BooleanLiteral(True))))

        self.assertTrue(TestChecker.test(input,expect,487))
    
    def test_88(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:a[2] = {1,2}, b[2] = {2,2};
        main(a);
        main(b[2]);
        Return a;
        EndBody.
        Function: main
        Parameter: x
        Body:
        x[1] = 1;
        Return x;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(Id("x"))))

        self.assertTrue(TestChecker.test(input,expect,488))
    
    def test_89(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:a[2] = {1,2}, b[2] = {2,2};
        main(a);
        main(b[2]);
        Return a;
        EndBody.
        Function: main
        Parameter: x
        Body:
        x[1] = 1;
        Return;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,489))
    
    def test_90(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:a[2] = {1,2}, b[2] = {2,2};
        main(a);
        main(b[2]);
        Return a;
        EndBody.
        Function: main
        Parameter: x
        Body:
        x[1] = x[1] + 1;
        Return;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,490))
    
    def test_91(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:z;
        Var: a=4;
        Var: b=21;
        Var: c=6;
        Var: d="Hello";
            z= !e;
            a = (b==c) && !d;
        Return a;
        EndBody.
        Function: main
        Parameter: x
        Body:
        x[1] = x[1] + 1;
        Return;
        EndBody.
        """
        expect = str(Undeclared(Identifier(), "e"))

        self.assertTrue(TestChecker.test(input,expect,491))
    
    def test_92(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:z;
        Var: a=4;
        Var: b=21;
        Var: c=6;
        Var: d="Hello";
            z= !True;
            a = (b==c) && !d;
        Return a;
        EndBody.
        Function: main
        Parameter: x
        Body:
        x[1] = x[1] + 1;
        Return;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(UnaryOp("""!""",Id("d"))))

        self.assertTrue(TestChecker.test(input,expect,492))
    
    def test_93(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:z;
        Var: a=4;
        Var: b=21;
        Var: c=6;
        Var: d="True";
            z= !True;
            a = (b==c) && !bool_of_string(d);
        Return a;
        EndBody.
        Function: main
        Parameter: x
        Body:
        x[1] = x[1] + 1;
        Return;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),BinaryOp("""&&""",BinaryOp("""==""",Id("b"),Id("c")),UnaryOp("""!""",CallExpr(Id("bool_of_string"),[Id("d")]))))))

        self.assertTrue(TestChecker.test(input,expect,493))
    
    def test_94(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:z;
        Var: a=4;
        Var: b=21;
        Var: c=6;
        Var: d="True";
            z= !True;
            a = (b==c) && !bool_of_string(c);
        Return a;
        EndBody.
        Function: main
        Parameter: x
        Body:
        x[1] = x[1] + 1;
        Return;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id("bool_of_string"),[Id("c")])))

        self.assertTrue(TestChecker.test(input,expect,494))
    
    def test_95(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:z;
        Var: a=4;
        Var: b=21;
        Var: c=6;
        Var: d="True";
            z= !True;
            a = (b>.c) && !bool_of_string(d);
        Return a;
        EndBody.
        Function: main
        Parameter: x
        Body:
        x[1] = x[1] + 1;
        Return;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp(""">.""",Id("b"),Id("c"))))

        self.assertTrue(TestChecker.test(input,expect,495))
    
    def test_96(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:z;
        Var: a;
        Var: b=21;
        Var: c=6;
        Var: d="True";
            z= !True;
            a = (b>c) && !bool_of_string(d);
        Return -.a;
        EndBody.
        Function: main
        Parameter: x
        Body:
        x[1] = x[1] + 1;
        Return;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(UnaryOp("""-.""",Id("a"))))

        self.assertTrue(TestChecker.test(input,expect,496))
    
    def test_97(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:z;
        Var: a;
        Var: b=21;
        Var: c=6;
        Var: d="True";
            z= !True;
            a = (b>c) && !bool_of_string(d);
        Return !!a && b;
        EndBody.
        Function: main
        Parameter: x
        Body:
        x[1] = x[1] + 1;
        Return;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("""&&""",UnaryOp("""!""",UnaryOp("""!""",Id("a"))),Id("b"))))

        self.assertTrue(TestChecker.test(input,expect,497))
    
    def test_98(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:z;
        Var: a;
        Var: b=21;
        Var: c=6;
        Var: d="True";
            z= !True;
            a = (b>c) && !bool_of_string(d);
        Return bool_of_string(d);
        EndBody.
        Function: main
        Parameter: x
        Body:
        x[1] = x[1] + 1;
        Return;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id("x"),[IntLiteral(1)])))

        self.assertTrue(TestChecker.test(input,expect,498))
    
    def test_99(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:z;
        Var: a;
        Var: b=21;
        Var: c=6;
        Var: d="True";
            z= !True;
            a = (b>c) && !bool_of_string(d);
        Return bool_of_string(d);
        EndBody.
        Function: main
        Parameter: x
        Body:
        x = x && 1;
        Return;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("""&&""",Id("x"),IntLiteral(1))))

        self.assertTrue(TestChecker.test(input,expect,499))
    
    def test_100(self):
        input = """ Var: x=1,y[1][2] = {{1,2}};
        Function: foo
        Parameter: x, y[1][2]
        Body:
        Var:z;
        Var: a;
        Var: b=21;
        Var: c=6;
        Var: d="True";
            z= !True;
            a = (b>c) && !bool_of_string(d);
        Return "nothing" && True;
        EndBody.
        Function: main
        Parameter: x
        Body:
        x = x && 1;
        Return;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("""&&""",StringLiteral("""nothing"""),BooleanLiteral(True))))

        self.assertTrue(TestChecker.test(input,expect,500))