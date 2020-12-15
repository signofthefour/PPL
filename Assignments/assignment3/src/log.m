
===========================
Testcase#400.txt
***********TEST*******
 Var: x,y=1;
        Function: main
                   Body: 
                        foo();
                   EndBody.
************SOL**********
Undeclared(Function(), "foo")
===========================

===========================
Testcase#401.txt
***********TEST*******
Function: main  
                   Body:
                        printStrLn();
                    EndBody.
************SOL**********
TypeMismatchInStatement(CallStmt(Id("printStrLn"),[]))
===========================

===========================
Testcase#402.txt
***********TEST*******
Function: main 
                    Body:
                        printStrLn(read(4));
                    EndBody.
************SOL**********
TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)]))
===========================

===========================
Testcase#403.txt
***********TEST*******
Program([FuncDecl(Id("main"),[],([],[CallExpr(Id("foo"),[])]))])
************SOL**********
Undeclared(Function(), "foo")
===========================

===========================
Testcase#404.txt
***********TEST*******
Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("printStrLn"),[CallExpr(Id("read"),[IntLiteral(4)])])]))])
************SOL**********
TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)]))
===========================

===========================
Testcase#405.txt
***********TEST*******
Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("printStrLn"),[])]))])
************SOL**********
TypeMismatchInStatement(CallStmt(Id("printStrLn"),[]))
===========================

===========================
Testcase#406.txt
***********TEST*******
 Var: x,y={};
        Function: main
                   Body: 
                        foo();
                   EndBody.
************SOL**********
TypeMismatchInStatement(VarDecl(Id("y"),[],ArrayLiteral([])))
===========================

===========================
Testcase#407.txt
***********TEST*******
 Var: x="string",y[1][2]={{1,2}};
        Function: main
                   Body: 
                        foo();
                   EndBody.
************SOL**********
Undeclared(Function(), "foo")
===========================

===========================
Testcase#408.txt
***********TEST*******
 Var: x="string",y[1][2]={{1,{2}}};
        Function: main
                   Body: 
                        foo();
                   EndBody.
************SOL**********
InvalidArrayLiteral(ArrayLiteral([IntLiteral(1),ArrayLiteral([IntLiteral(2)])]))
===========================

===========================
Testcase#409.txt
***********TEST*******
 Var: x="string",y[1][2]={{{1},{2}}};
        Function: main
                   Body: 
                        foo();
                   EndBody.
************SOL**********
InvalidArrayLiteral(ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(2)])]))
===========================

===========================
Testcase#410.txt
***********TEST*******
 Var: x="string",y[1][2]={1,1.2};
        Function: main
                   Body: 
                        foo();
                   EndBody.
************SOL**********
InvalidArrayLiteral(ArrayLiteral([IntLiteral(1),FloatLiteral(1.2)]))
===========================

===========================
Testcase#411.txt
***********TEST*******
 Var: x="string",y[1][2]={{1,2}};
        Function: foo
        Body:
        Return;
        EndBody.
        Function: main
                   Body: 
                        foo();
                   EndBody.
************SOL**********
FunctionNotReturn("main")
===========================

===========================
Testcase#412.txt
***********TEST*******
 Var: x="string",y[1][2]={{1,2}};
        Function: foo
        Body:
        Return;
        EndBody.
************SOL**********
NoEntryPoint()
===========================

===========================
Testcase#413.txt
***********TEST*******
 Var: x="string",y[1][2]={{1,2}};
        Function: main
        Parameter: x, y,x[1][2]
        Body:
        Return;
        EndBody.
************SOL**********
Redeclared(Parameter(), "x")
===========================

===========================
Testcase#414.txt
***********TEST*******
 Var: x="string",y[1][2]={{1,2}};
        Function: foo
        Body:
        Return 1;
        EndBody.
        Function: main
                   Body: 
                        foo();
                   EndBody.
************SOL**********
TypeMismatchInStatement(CallStmt(Id("foo"),[]))
===========================

===========================
Testcase#415.txt
***********TEST*******
 Var: x="string",y[1][2]={{1,2}};
        Function: foo
        Parameter: x
        Body:
        x = 1 + 2;
        Return 1;
        EndBody.
        Function: main
                   Body: 
                        foo();
                   EndBody.
************SOL**********
TypeMismatchInStatement(CallStmt(Id("foo"),[]))
===========================

===========================
Testcase#416.txt
***********TEST*******
 Var: x="string",y[1][2]={{1,2}};
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
        EndBody.
************SOL**********
TypeMismatchInStatement(Assign(Id("x"),BinaryOp("""+.""",FloatLiteral(1.0),FloatLiteral(2.0))))
===========================

===========================
Testcase#417.txt
***********TEST*******
 Var: x=1.2,y[1][2]={{1,2}};
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
        EndBody.
************SOL**********
TypeMismatchInStatement(CallStmt(Id("foo"),[Id("x")]))
===========================

===========================
Testcase#418.txt
***********TEST*******
 Var: x=1,y[1][2]={{1,2}};
        Function: foo
        Parameter: x
        Body:
        x = 1 + 2;
        Return;
        EndBody.
        Function: main
        Body:
        foo(x);
        EndBody.
************SOL**********
FunctionNotReturn("main")
===========================

===========================
Testcase#419.txt
***********TEST*******
 Var: x=1,y[1][2]={{1,2}};
        Function: foo
        Parameter: x
        Body:
        x = 1. + 2.;
        Return;
        EndBody.
        Function: main
        Body:
        foo(x);
        EndBody.
************SOL**********
TypeMismatchInExpression(BinaryOp("""+""",FloatLiteral(1.0),FloatLiteral(2.0)))
===========================

===========================
Testcase#420.txt
***********TEST*******
 Var: x=1,y[1][2]={{1,2}};
        Function: foo
        Parameter: x
        Body:
        x = 1. +. 2.;
        Return;
        EndBody.
        Function: main
        Body:
        foo(x);
        EndBody.
************SOL**********
TypeMismatchInStatement(CallStmt(Id("foo"),[Id("x")]))
===========================

===========================
Testcase#421.txt
***********TEST*******
 Var: x=1,y[1][2]={{1,2}};
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
        EndBody.
************SOL**********
TypeCannotBeInferred(Assign(Id("x"),BinaryOp("""+""",IntLiteral(1),CallExpr(Id("foo"),[Id("x")]))))
===========================

===========================
Testcase#422.txt
***********TEST*******
 Var: x=1,y[1][2]={{1,2}};
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
        EndBody.
************SOL**********
FunctionNotReturn("main")
===========================

===========================
Testcase#423.txt
***********TEST*******
 Var: x=1,y[1][2]={{1,2}};
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
        EndBody.
************SOL**********
FunctionNotReturn("main")
===========================

===========================
Testcase#424.txt
***********TEST*******
 Var: x=1,y[1][2]={{1,2}};
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
        EndBody.
************SOL**********
FunctionNotReturn("main")
===========================

===========================
Testcase#425.txt
***********TEST*******
 Var: x=1,y[1][2]={{1,2}};
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
        EndBody.
************SOL**********
TypeMismatchInExpression(CallExpr(Id("foo"),[Id("x"),Id("y"),Id("z")]))
===========================

===========================
Testcase#426.txt
***********TEST*******
 Var: x=1,y[1][2]={{1,2}};
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
        EndBody.
************SOL**********
TypeMismatchInExpression(BinaryOp("""+""",IntLiteral(1),CallExpr(Id("foo"),[Id("x"),CallExpr(Id("foo"),[Id("x"),BooleanLiteral(True)])])))
===========================

===========================
Testcase#427.txt
***********TEST*******
 Var: x=1,y[1][2]={{1,2}};
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
        EndBody.
************SOL**********
FunctionNotReturn("main")
===========================

===========================
Testcase#428.txt
***********TEST*******
 Var: x=1,y[1][2]={{1,2}};
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
        EndBody.
************SOL**********
Undeclared(Function(), "main")
===========================

===========================
Testcase#429.txt
***********TEST*******
 Var: x=1,y[1][2]={{1,2}};
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
        EndBody.
************SOL**********
Redeclared(Variable(), "read")
===========================

===========================
Testcase#430.txt
***********TEST*******
 Var: x=1,y[1][2]={{1,2}};
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
        EndBody.
************SOL**********
TypeMismatchInStatement(Return(FloatLiteral(1.1)))
===========================

===========================
Testcase#431.txt
***********TEST*******
 Var: x=1,y[1][2]={{1,2}};
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
        EndBody.
************SOL**********
TypeMismatchInStatement(Return(IntLiteral(1)))
===========================

===========================
Testcase#432.txt
***********TEST*******
 Var: x=1,y[1][2];
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
        EndBody.
************SOL**********
TypeCannotBeInferred(Return(Id("y")))
===========================

===========================
Testcase#433.txt
***********TEST*******
 Var: x=1,y[1][2];
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
        EndBody.
************SOL**********

===========================

===========================
Testcase#434.txt
***********TEST*******
 Var: x=1,y[1][2];
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
        EndBody.
************SOL**********

===========================

===========================
Testcase#435.txt
***********TEST*******
 Var: x=1,y[1][2];
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
        EndBody.
************SOL**********
TypeMismatchInStatement(Return(FloatLiteral(1.1)))
===========================

===========================
Testcase#436.txt
***********TEST*******
 Var: x=1,y[1][2];
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
        EndBody.
************SOL**********
TypeMismatchInStatement(Return(Id("y")))
===========================

===========================
Testcase#437.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        EndBody.
************SOL**********
TypeMismatchInStatement(Return(Id("y")))
===========================

===========================
Testcase#438.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********

===========================

===========================
Testcase#439.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
        Function: main
        Body:
            Var: foo;
            Var: i , x;
            For (i = 1, i <= x*x,i*i+.1.5)
            Do x=x+1;
            EndFor.
            Return 1;
        EndBody.
        
************SOL**********
TypeMismatchInExpression(BinaryOp("""+.""",BinaryOp("""*""",Id("i"),Id("i")),FloatLiteral(1.5)))
===========================

===========================
Testcase#440.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(Return(IntLiteral(1)))
===========================

===========================
Testcase#441.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(Return(FloatLiteral(1.1)))
===========================

===========================
Testcase#442.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(CallStmt(Id("foo"),[IntLiteral(1)]))
===========================

===========================
Testcase#443.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeCannotBeInferred(Return(Id("y")))
===========================

===========================
Testcase#444.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeCannotBeInferred(Return(Id("y")))
===========================

===========================
Testcase#445.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(BinaryOp("""+""",IntLiteral(1),CallExpr(Id("main"),[Id("x"),Id("y")])))
===========================

===========================
Testcase#446.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(If([(Id("x"),[],[])],[]))
===========================

===========================
Testcase#447.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(For(Id("x"),IntLiteral(1),BinaryOp(""">""",Id("x"),IntLiteral(1)),BinaryOp("""+.""",FloatLiteral(0.0),FloatLiteral(1.0)),([],[])))
===========================

===========================
Testcase#448.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(For(Id("x"),BooleanLiteral(True),BinaryOp(""">""",Id("x"),IntLiteral(1)),BinaryOp("""+""",IntLiteral(0),IntLiteral(1)),([],[])))
===========================

===========================
Testcase#449.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(For(Id("x"),IntLiteral(1),BinaryOp("""+""",Id("x"),IntLiteral(1)),BinaryOp("""+""",IntLiteral(0),IntLiteral(1)),([],[])))
===========================

===========================
Testcase#450.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********

===========================

===========================
Testcase#451.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeCannotBeInferred(Assign(Id("y"),BinaryOp("""+""",Id("a"),CallExpr(Id("foo"),[Id("x")]))))
===========================

===========================
Testcase#452.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(Return(FloatLiteral(1.1)))
===========================

===========================
Testcase#453.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(Return(FloatLiteral(1.1)))
===========================

===========================
Testcase#454.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(Return(FloatLiteral(1.1)))
===========================

===========================
Testcase#455.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(ArrayCell(Id("y"),[IntLiteral(1)]))
===========================

===========================
Testcase#456.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********

===========================

===========================
Testcase#457.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(Assign(Id("y"),Id("a")))
===========================

===========================
Testcase#458.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeCannotBeInferred(Return(Id("x")))
===========================

===========================
Testcase#459.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(ArrayCell(Id("a"),[BinaryOp("""+""",IntLiteral(1),IntLiteral(1)),BinaryOp("""+.""",FloatLiteral(0.5),FloatLiteral(1.5))]))
===========================

===========================
Testcase#460.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(Assign(ArrayCell(Id("a"),[BinaryOp("""+""",IntLiteral(1),IntLiteral(1)),Id("x")]),Id("y")))
===========================

===========================
Testcase#461.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(CallExpr(Id("foo"),[Id("x")]))
===========================

===========================
Testcase#462.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(CallExpr(Id("foo"),[Id("x")]))
===========================

===========================
Testcase#463.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeCannotBeInferred(Return(Id("y")))
===========================

===========================
Testcase#464.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(ArrayCell(CallExpr(Id("foo"),[Id("x")]),[BinaryOp("""+""",Id("x"),IntLiteral(3)),FloatLiteral(0.5)]))
===========================

===========================
Testcase#465.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********

===========================

===========================
Testcase#466.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
Undeclared(Variable(), "a")
===========================

===========================
Testcase#467.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(If([(Id("a"),[],[]),(BooleanLiteral(True),[],[Assign(Id("a"),IntLiteral(12))])],[]))
===========================

===========================
Testcase#468.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(Assign(Id("a"),IntLiteral(12)))
===========================

===========================
Testcase#469.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********

===========================

===========================
Testcase#470.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(BinaryOp("""||""",BinaryOp("""+""",Id("a"),Id("b")),BinaryOp("""-""",Id("c"),Id("d"))))
===========================

===========================
Testcase#471.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(BinaryOp(""">.""",BinaryOp("""||""",Id("b"),Id("c")),Id("d")))
===========================

===========================
Testcase#472.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********

===========================

===========================
Testcase#473.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(Assign(Id("a"),IntLiteral(1)))
===========================

===========================
Testcase#474.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(Assign(Id("a"),Id("c")))
===========================

===========================
Testcase#475.txt
***********TEST*******

        Var:x =1;
        Function: main
        Parameter: y
        Body:
            x = main(0.5) + y;
        EndBody.            
************SOL**********
Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(main),[FloatLiteral(0.5)]),Id(y))
===========================

===========================
Testcase#476.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(BinaryOp("""-""",Id("c"),Id("b")))
===========================

===========================
Testcase#477.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(BinaryOp("""-""",Id("c"),Id("d")))
===========================

===========================
Testcase#478.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(Assign(Id("y"),Id("c")))
===========================

===========================
Testcase#479.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(CallExpr(Id("foo"),[Id("x")]))
===========================

===========================
Testcase#480.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(BinaryOp("""&&""",Id("c"),Id("d")))
===========================

===========================
Testcase#481.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeCannotBeInferred(Return(Id("y")))
===========================

===========================
Testcase#482.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeCannotBeInferred(Return(Id("y")))
===========================

===========================
Testcase#483.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(CallStmt(Id("main"),[Id("b")]))
===========================

===========================
Testcase#484.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeCannotBeInferred(Return(Id("y")))
===========================

===========================
Testcase#485.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(Return(Id("x")))
===========================

===========================
Testcase#486.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(Assign(Id("x"),IntLiteral(1)))
===========================

===========================
Testcase#487.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(Assign(ArrayCell(Id("x"),[IntLiteral(1)]),BooleanLiteral(True)))
===========================

===========================
Testcase#488.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(Return(Id("x")))
===========================

===========================
Testcase#489.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********

===========================

===========================
Testcase#490.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********

===========================

===========================
Testcase#491.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
Undeclared(Identifier(), "e")
===========================

===========================
Testcase#492.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(UnaryOp("""!""",Id("d")))
===========================

===========================
Testcase#493.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInStatement(Assign(Id("a"),BinaryOp("""&&""",BinaryOp("""==""",Id("b"),Id("c")),UnaryOp("""!""",CallExpr(Id("bool_of_string"),[Id("d")])))))
===========================

===========================
Testcase#494.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(CallExpr(Id("bool_of_string"),[Id("c")]))
===========================

===========================
Testcase#495.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(BinaryOp(""">.""",Id("b"),Id("c")))
===========================

===========================
Testcase#496.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(UnaryOp("""-.""",Id("a")))
===========================

===========================
Testcase#497.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(BinaryOp("""&&""",UnaryOp("""!""",UnaryOp("""!""",Id("a"))),Id("b")))
===========================

===========================
Testcase#498.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(ArrayCell(Id("x"),[IntLiteral(1)]))
===========================

===========================
Testcase#499.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(BinaryOp("""&&""",Id("x"),IntLiteral(1)))
===========================

===========================
Testcase#500.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(BinaryOp("""&&""",StringLiteral("""nothing"""),BooleanLiteral(True)))
===========================

===========================
Testcase#501.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id("foo"),[Id("x")]),[BinaryOp("""+""",Id("x"),IntLiteral(3)),FloatLiteral(0.5)]),IntLiteral(1)))
===========================

===========================
Testcase#502.txt
***********TEST*******
 Var: x=1,y[1][2] = {{1,2}};
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
        
************SOL**********
TypeMismatchInExpression(BinaryOp("""&&""",Id("c"),Id("d")))
===========================
