
===========================
Testcase#400.txt
***********TEST*******
 Var: x,y=1;
        Function: main
                   Body: 
                        foo();
                   EndBody.
************SOL**********
Undeclared Function: foo
===========================

===========================
Testcase#401.txt
***********TEST*******
Function: main  
                   Body:
                        printStrLn();
                    EndBody.
************SOL**********
Type Mismatch In Statement: CallStmt(Id(printStrLn),[])
===========================

===========================
Testcase#402.txt
***********TEST*******
Function: main 
                    Body:
                        printStrLn(read(4));
                    EndBody.
************SOL**********
Type Mismatch In Statement: CallExpr(Id(read),[IntLiteral(4)])
===========================

===========================
Testcase#403.txt
***********TEST*******
Program([FuncDecl(Id(main)[],([][CallExpr(Id(foo),[])]))])
************SOL**********
Undeclared Function: foo
===========================

===========================
Testcase#404.txt
***********TEST*******
Program([FuncDecl(Id(main)[],([][CallStmt(Id(printStrLn),[CallExpr(Id(read),[IntLiteral(4)])])]))])
************SOL**********
Type Mismatch In Statement: CallExpr(Id(read),[IntLiteral(4)])
===========================

===========================
Testcase#405.txt
***********TEST*******
Program([FuncDecl(Id(main)[],([][CallStmt(Id(printStrLn),[])]))])
************SOL**********
Type Mismatch In Statement: CallStmt(Id(printStrLn),[])
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
Type Mismatch In Statement: VarDecl(Id(y),ArrayLiteral())
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
Undeclared Function: foo
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
Invalid Array Literal: ArrayLiteral(IntLiteral(1),ArrayLiteral(IntLiteral(2)))
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
Invalid Array Literal: ArrayLiteral(ArrayLiteral(IntLiteral(1)),ArrayLiteral(IntLiteral(2)))
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
Invalid Array Literal: ArrayLiteral(IntLiteral(1),FloatLiteral(1.2))
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
No Entry Point
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
Redeclared Parameter: x
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
Type Mismatch In Statement: CallStmt(Id(foo),[])
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
Type Mismatch In Statement: CallStmt(Id(foo),[])
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
Type Mismatch In Statement: Assign(Id(x),BinaryOp(+.,FloatLiteral(1.0),FloatLiteral(2.0)))
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
Type Mismatch In Statement: CallStmt(Id(foo),[Id(x)])
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
Type Mismatch In Expression: BinaryOp(+,FloatLiteral(1.0),FloatLiteral(2.0))
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
Type Mismatch In Statement: CallStmt(Id(foo),[Id(x)])
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
Type Cannot Be Inferred: CallExpr(Id(foo),[Id(x)])
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
Type Mismatch In Statement: CallExpr(Id(foo),[Id(x),Id(y),Id(z)])
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
Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),CallExpr(Id(foo),[Id(x),CallExpr(Id(foo),[Id(x),BooleanLiteral(true)])]))
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
Undeclared Function: main
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
Redeclared Variable: read
===========================
