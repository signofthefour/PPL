
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
Type Mismatch In Expression: CallExpr(Id(read),[IntLiteral(4)])
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
Type Mismatch In Expression: CallExpr(Id(read),[IntLiteral(4)])
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
Function Not Return: main
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
Function Not Return: main
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
Type Cannot Be Inferred: Assign(Id(x),BinaryOp(+,IntLiteral(1),CallExpr(Id(foo),[Id(x)])))
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
Function Not Return: main
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
Function Not Return: main
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
Function Not Return: main
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
Type Mismatch In Expression: CallExpr(Id(foo),[Id(x),Id(y),Id(z)])
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
Function Not Return: main
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
Type Mismatch In Statement: Return(FloatLiteral(1.1))
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
Type Mismatch In Statement: Return(IntLiteral(1))
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
Type Cannot Be Inferred: Return(Id(y))
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
Type Mismatch In Statement: Return(FloatLiteral(1.1))
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
Type Mismatch In Statement: Return(Id(y))
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
Type Mismatch In Statement: Return(Id(y))
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

        Function: main
        Body:
        Var: i , x;
            For (i = 1, i <= x*x,i*i+.1.5)
            Do x=x+1;
            EndFor.
        EndBody.
************SOL**********
Type Mismatch In Expression: BinaryOp(+.,BinaryOp(*,Id(i),Id(i)),FloatLiteral(1.5))
===========================

===========================
Testcase#440.txt
***********TEST*******
                
                Function: main
                Body:
                    Var: x;
                    For (x=1, x>1 , x+1) Do
                        Var:y;
                    EndFor.
                EndBody.

            
************SOL**********
Function Not Return: main
===========================

===========================
Testcase#441.txt
***********TEST*******

                Function: main
                Body:
                    Var: x;
                    While (foo(x))
                    Do
                        x=1;
                    EndWhile.
                EndBody.
                
                Function: foo
                Parameter: x
                Body:

                EndBody.
            
************SOL**********
Type Cannot Be Inferred: While(CallExpr(Id(foo),[Id(x)]),[],[Assign(Id(x),IntLiteral(1))])
===========================

===========================
Testcase#442.txt
***********TEST*******

                Function: main
                Body:
                    Var: x,y;
                    While (x)
                    Do
                        Var:z;
                        y=1;
                    EndWhile.
                EndBody.
            
************SOL**********
Function Not Return: main
===========================

===========================
Testcase#443.txt
***********TEST*******
                
                Function: main
                Parameter: x
                Body:
                    x= 1+foo(1);
                    foo(1);
                EndBody.
                Function: foo
                Parameter: x
                Body:
                EndBody.

            
************SOL**********
Type Mismatch In Statement: CallStmt(Id(foo),[IntLiteral(1)])
===========================

===========================
Testcase#444.txt
***********TEST*******

                Function: main
                Parameter: x
                Body:
                    foo(1);
                    x= 1+foo(1);
                EndBody.
                Function: foo
                Parameter: x
                Body:
                EndBody.
            
************SOL**********
Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),CallExpr(Id(foo),[IntLiteral(1)]))
===========================

===========================
Testcase#445.txt
***********TEST*******

                Function: foo
                Parameter: x
                Body:
                EndBody.
                Function: main
                Body:
                    Var:x,y;
                    x= y + foo(1,2);
                EndBody.
            
************SOL**********
Function Not Return: foo
===========================

===========================
Testcase#446.txt
***********TEST*******

                
                Function: main
                Body:
                    Var:x;
                    Do
                        Var:y;
                    While x
                    EndDo.
                EndBody.
            
************SOL**********
Function Not Return: main
===========================

===========================
Testcase#447.txt
***********TEST*******

                
                Function: main
                Body:
                    Var:x=1;
                    If x Then
                    EndIf.
                EndBody.
            
************SOL**********
Type Mismatch In Statement: If(Id(x),[],[])
===========================

===========================
Testcase#448.txt
***********TEST*******

                Function: main
                Body:
                    Var: x=1;
                    For (x = !True, x>1 , 0+1) Do
                    EndFor.
                EndBody.
            
************SOL**********
Type Mismatch In Statement: For(Id(x),UnaryOp(!,BooleanLiteral(true)),BinaryOp(>,Id(x),IntLiteral(1)),BinaryOp(+,IntLiteral(0),IntLiteral(1)),[],[])
===========================

===========================
Testcase#449.txt
***********TEST*******

                Function: main
                Body:
                    Var: x,y=0.5;
                    For (x=1, x>1 , y +. 1) Do
                    EndFor.
                EndBody.
            
************SOL**********
Type Mismatch In Expression: BinaryOp(+.,Id(y),IntLiteral(1))
===========================

===========================
Testcase#450.txt
***********TEST*******

                Function: main
                Body:
                    Var: x;
                    For (x=1, 1+1 , x+1) Do
                    EndFor.
                EndBody.
            
************SOL**********
Type Mismatch In Statement: For(Id(x),IntLiteral(1),BinaryOp(+,IntLiteral(1),IntLiteral(1)),BinaryOp(+,Id(x),IntLiteral(1)),[],[])
===========================

===========================
Testcase#451.txt
***********TEST*******

                Function: main
                Body:
                    Var: x=1,y;
                    While (x)
                    Do
                    EndWhile.
                EndBody.
            
************SOL**********
Type Mismatch In Statement: While(Id(x),[],[])
===========================

===========================
Testcase#452.txt
***********TEST*******

                Function: main
                Body:
                    Var: x=1,y;
                    Do
                    While (x)
                    EndDo.
                EndBody.
            
************SOL**********
Type Mismatch In Statement: Dowhile([],[],Id(x))
===========================

===========================
Testcase#453.txt
***********TEST*******

                Function: foo
                Body:
                EndBody.
                Function: main
                Body:
                    Var:x;
                    foo();
                    foo()[1] = x+1;
                EndBody.
            
************SOL**********
Function Not Return: foo
===========================

===========================
Testcase#454.txt
***********TEST*******

                Function: foo
                Body:
                EndBody.
                Function: main
                Body:
                    Var:x;
                    foo();
                    x = foo();
                EndBody.
            
************SOL**********
Function Not Return: foo
===========================

===========================
Testcase#455.txt
***********TEST*******

                Function: main
                Body:
                    foo();
                EndBody.
                Function: foo
                Body:
                    Return 1;
                EndBody.
            
************SOL**********
Function Not Return: main
===========================

===========================
Testcase#456.txt
***********TEST*******

                Function: main
                Body:
                    Var:x;
                    x = 1+foo();
                EndBody.
                Function: foo
                Body:
                    Return 1.5;
                EndBody.
            
************SOL**********
Function Not Return: main
===========================

===========================
Testcase#457.txt
***********TEST*******
                
                Function: main
                Body:
                    Var: x;
                    If x Then
                        Return 1;
                    Else
                        Return 1.5;
                    EndIf.
                EndBody.
            
************SOL**********
Type Mismatch In Statement: Return(FloatLiteral(1.5))
===========================

===========================
Testcase#458.txt
***********TEST*******

        Function: main
        Body:
            Var: x;
            foo(1,2);
            x = foo(5,99);
            Return 0;
        EndBody.
        Function: foo
        Parameter: x1, x2
        Body:
            Return;
        EndBody.
                   
************SOL**********
Type Mismatch In Expression: Assign(Id(x),CallExpr(Id(foo),[IntLiteral(5),IntLiteral(99)]))
===========================

===========================
Testcase#459.txt
***********TEST*******

                Function: main
                Body:
                    Var: x;
                    Return x;
                EndBody.

            
************SOL**********
Type Cannot Be Inferred: Return(Id(x))
===========================

===========================
Testcase#460.txt
***********TEST*******

                
                Function: main
                Body:
                    Var: a[1][2];
                    a[1+1][0.5+.1.5] = 1;
                EndBody.
            
************SOL**********
Type Mismatch In Expression: ArrayCell(Id(a),[BinaryOp(+,IntLiteral(1),IntLiteral(1)),BinaryOp(+.,FloatLiteral(0.5),FloatLiteral(1.5))])
===========================

===========================
Testcase#461.txt
***********TEST*******

                
                Function: main
                Body:
                    Var: a[1][2];
                    a[1][2][3] = 1;
                EndBody.
            
************SOL**********
Type Mismatch In Expression: ArrayCell(Id(a),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])
===========================

===========================
Testcase#462.txt
***********TEST*******

                Function: foo
                Parameter: n
                Body:
                   Var : x[1][2]={{1,2}} ;
                   Return x;
                EndBody.
                

                Function: main
                Body:
                    Var:x;
                    foo(x)[x+3][0.5]=1;
                EndBody.
            
************SOL**********
Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo),[Id(x)]),[BinaryOp(+,Id(x),IntLiteral(3)),FloatLiteral(0.5)])
===========================

===========================
Testcase#463.txt
***********TEST*******

                
                Var: x;
                Function: fact
                Parameter: n
                Body:
                    If n == 0 Then
                        Return 1;
                    Else
                        Return n * fact (n - 1);
                    EndIf.
                EndBody.
                Function: main
                Body:
                    x = 10;
                    fact(x);
                EndBody.
            
************SOL**********
Type Mismatch In Statement: If(BinaryOp(==,Id(n),IntLiteral(0)),[],[Return(IntLiteral(1))])Else([],[Return(BinaryOp(*,Id(n),CallExpr(Id(fact),[BinaryOp(-,Id(n),IntLiteral(1))])))])
===========================

===========================
Testcase#464.txt
***********TEST*******

                Function: foo
                Parameter: a[5], b
                Body:
                    Var: i;
                    While (i < 5) Do
                        a[i] = b +. 1.0;
                        i = i + 1;
                    EndWhile.
                    i= 0.5;
                EndBody.
                Function: main
                Body:
                EndBody.
            
************SOL**********
Type Mismatch In Statement: Assign(Id(i),FloatLiteral(0.5))
===========================

===========================
Testcase#465.txt
***********TEST*******

                Function: main
                Body:
                    Var:a[5]={1,2,3,4,5};
                    Var: b[2][3]={{1,2,3},{4,5,6}};
                    a[3 + foo(2)] = a[b[2][3]] +. 4.0;
                EndBody.
            
************SOL**********
Invalid Array Literal: ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)),ArrayLiteral(IntLiteral(4),IntLiteral(5),IntLiteral(6)))
===========================

===========================
Testcase#466.txt
***********TEST*******

                Function: foo
                Parameter: x,y
                Body:
                    foo (2 + x, 4. \. y);
                    foo(x,y);
                EndBody. 
                Function: main
                Body:
                    foo(3,6);
                EndBody.           
                
************SOL**********
Type Mismatch In Statement: CallStmt(Id(foo),[IntLiteral(3),IntLiteral(6)])
===========================

===========================
Testcase#467.txt
***********TEST*******

                Function: main
                Body:
                    If True Then
                    ElseIf True Then
                        Var: a;
                    EndIf.
                EndBody.
            
************SOL**********
Function Not Return: main
===========================

===========================
Testcase#468.txt
***********TEST*******

                Function: main
                Body:
                    For (a = 1, a < 10, 1) Do
                        Var:a=1;
                    EndFor.
                EndBody.
            
************SOL**********
Undeclared Identifier: a
===========================

===========================
Testcase#469.txt
***********TEST*******

                Var: a[3]={"Mot","2","Three"};
                Function: main
                Body:
                    a[1] = a[1] + a[2];
                EndBody.
            
************SOL**********
Type Mismatch In Expression: BinaryOp(+,ArrayCell(Id(a),[IntLiteral(1)]),ArrayCell(Id(a),[IntLiteral(2)]))
===========================

===========================
Testcase#470.txt
***********TEST*******

                
                Function: main
                Body:
                    Var:a,b,c,d;
                    a = a + b || c - d;
                EndBody.
            
************SOL**********
Type Mismatch In Expression: BinaryOp(||,BinaryOp(+,Id(a),Id(b)),BinaryOp(-,Id(c),Id(d)))
===========================

===========================
Testcase#471.txt
***********TEST*******

            Function: main
            Body:
                Var: sum = 0, a = 1;
                While a < 10 Do
                    Var: b, cal = 1;
                    While b < 10 Do
                        cal = cal * b;
                        b = b + 1;
                    EndWhile.
                    sum = sum + prod;
                    a = a + 1;
                EndWhile.
            EndBody.
            
************SOL**********
Undeclared Identifier: prod
===========================

===========================
Testcase#472.txt
***********TEST*******

            Function: main 
            Body: 
                Var: a=1,x; 
                a=foo(x); 
            EndBody.             

************SOL**********
Undeclared Function: foo
===========================

===========================
Testcase#473.txt
***********TEST*******

                Function: main
                Body:
                    Var:x;
                    If True Then
                        x = 3;
                    Else 
                        x = 2.0;
                    EndIf.
                EndBody.
            
************SOL**********
Type Mismatch In Statement: Assign(Id(x),FloatLiteral(2.0))
===========================

===========================
Testcase#474.txt
***********TEST*******

                Var:x =1;
                Function: main
                Parameter: y
                Body:
                    x = y + main(0.5) ;
                EndBody.
            
************SOL**********
Type Mismatch In Expression: CallExpr(Id(main),[FloatLiteral(0.5)])
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

                Function: main
                Parameter: x
                Body:
                    Var:y;
                    Do
                        x=1;
                        main(0.5);
                    While y 
                    EndDo.
                EndBody.            
************SOL**********
Type Mismatch In Statement: CallStmt(Id(main),[FloatLiteral(0.5)])
===========================

===========================
Testcase#477.txt
***********TEST*******

                Function: main
                Parameter: x, a, b, c
                Body:
                    If(x == ((False||True) && (a > b + c))) Then
                        a = b - c;
                    Else
                        a = b + c;
                        x = True;
                    EndIf.
                EndBody.
            
************SOL**********
Type Mismatch In Expression: BinaryOp(==,Id(x),BinaryOp(&&,BinaryOp(||,BooleanLiteral(false),BooleanLiteral(true)),BinaryOp(>,Id(a),BinaryOp(+,Id(b),Id(c)))))
===========================

===========================
Testcase#478.txt
***********TEST*******

                Var: abc[2][3][4];
                Function: foo
                Parameter: x[2]
                Body:
                    x[1] = 1;
                    abc[1] = 2.;
                EndBody.
                Function: main
                Body:
                    Var: z[2][3][4] = {1.,2.};
                    Var: w[2] = {3.,4.};
                    Var: x;
                    abc = z;
                    foo(x);
                EndBody.            
************SOL**********
Type Mismatch In Expression: ArrayCell(Id(abc),[IntLiteral(1)])
===========================

===========================
Testcase#479.txt
***********TEST*******

                Var: abc[5];
                Function: foo
                Parameter: x[2]
                Body:
                    x[1] = 1;
                    abc[1] = 2;
                EndBody.
                Function: main
                Body:
                    Var: z[2] = {1,2};
                    Var: w[2] = {3.,4.};
                    Var: x;
                    abc[1] = 1;
                    foo(z);
                    foo(w);
                EndBody.            
************SOL**********
Function Not Return: foo
===========================

===========================
Testcase#480.txt
***********TEST*******

                Var: abc[5];
                Function: foo
                Parameter: x[2]
                Body:
                    x[1] = 1;
                    abc[1] = 2;
                EndBody.
                Function: main
                Body:
                    Var: z[2] = {1,2};
                    Var: w[2] = {3,4};
                    Var: x;
                    abc[1] = 1.5;   
                EndBody.         
************SOL**********
Function Not Return: foo
===========================

===========================
Testcase#481.txt
***********TEST*******

                Function: foo
                Parameter: x[2]
                Body:
                EndBody.
                Function: main
                Body:
                    Var: z[2] = {1,2};
                    Var: w[2] = {3,4};
                    Var: x;
                    foo(z);
                    foo(w[2]);
                EndBody.            
************SOL**********
Function Not Return: foo
===========================

===========================
Testcase#482.txt
***********TEST*******

                    Function: main
                    Parameter: x
                    Body:
                        y= x + main(0.5);

                    EndBody.            
************SOL**********
Type Mismatch In Expression: CallExpr(Id(main),[FloatLiteral(0.5)])
===========================

===========================
Testcase#483.txt
***********TEST*******

                
                Function: main 
        Body:
            If True Then
                Var: a;
                Var: x;
                Var: y;
                x = 1;
                y = 2;
                z = 3;
            EndIf.
        EndBody.
            
************SOL**********
Undeclared Identifier: z
===========================

===========================
Testcase#484.txt
***********TEST*******

        Function: main 
        Parameter: n
        Body: 
            Var:i;
            For (i = 6*9,True, i-1) Do
                Var:x=5;
                a=3;
            EndFor.
        EndBody.
            
************SOL**********
Undeclared Identifier: a
===========================

===========================
Testcase#485.txt
***********TEST*******

        Function: main
        Body:
            Var: x[5];
            If True Then
                While True Do
                    Return x;
                EndWhile.
            EndIf.
        EndBody.
                   
************SOL**********
Type Cannot Be Inferred: If(BooleanLiteral(true),[],[While(BooleanLiteral(true),[],[Return(Id(x))])])
===========================

===========================
Testcase#486.txt
***********TEST*******

        Function: main 
        Parameter: n
        Body: 
            Var:x;
            While x>1 Do
                If x==1 Then Return;
                EndIf.
            EndWhile.
            Return True;
        EndBody.
            
************SOL**********

===========================

===========================
Testcase#487.txt
***********TEST*******

        Function: main 
        Parameter: n
        Body: 
            Var:a;
            Do  
                Var:b;
                Do
                While(b!=4)
                EndDo.
            While(a!=3)                
            EndDo.
            a=1.0;
        EndBody.
            
************SOL**********
Type Mismatch In Statement: Assign(Id(a),FloatLiteral(1.0))
===========================

===========================
Testcase#488.txt
***********TEST*******

        Function: main 
        Parameter: x,y
        Body: 
            Do  
                Return main(x,y);
            While True
            EndDo.
        EndBody.
            
************SOL**********
Type Cannot Be Inferred: Dowhile([],[Return(CallExpr(Id(main),[Id(x),Id(y)]))],BooleanLiteral(true))
===========================

===========================
Testcase#489.txt
***********TEST*******

        Var: x, a[10], b[5];
        Function: main
        Parameter: x
        Body:
            Do
                printStrLn(b[2]);
            While f()[2] EndDo.
        EndBody.
        Function: f
        Body:
            b[1] = "dasd";
            Return a;
        EndBody.
        
************SOL**********
Type Mismatch In Expression: ArrayCell(CallExpr(Id(f),[]),[IntLiteral(2)])
===========================

===========================
Testcase#490.txt
***********TEST*******

        Function: main 
        Parameter: x,y
        Body: 
            Return main(x +3,y +. 10.2);
        EndBody.
            
************SOL**********
Type Cannot Be Inferred: Return(CallExpr(Id(main),[BinaryOp(+,Id(x),IntLiteral(3)),BinaryOp(+.,Id(y),FloatLiteral(10.2))]))
===========================

===========================
Testcase#491.txt
***********TEST*******

        Function: main 
        Parameter:a
        Body: 
            a=1;
            foo(a,3*7, a+ 5,"string",True);
        EndBody.
        Function: foo 
        Parameter: a,b,c,d,e
        Body: 
            Var:z;
            a=4;
            b=21;
            c=6;
            d="Hello";
            z= !e;
            a = (b==c) && !d;
        EndBody.
            
************SOL**********
Function Not Return: main
===========================

===========================
Testcase#492.txt
***********TEST*******

                Function: main 
                Parameter: a,b,c
                Body: 
                    a= (a==b)!= c +3;
                EndBody.
            
************SOL**********
Type Mismatch In Expression: BinaryOp(!=,BinaryOp(==,Id(a),Id(b)),BinaryOp(+,Id(c),IntLiteral(3)))
===========================

===========================
Testcase#493.txt
***********TEST*******

               Function: main 
                Parameter: n
                Body: 
                    If n == 0 Then
                        If n!=0 Then
                            If n!=0 Then
                                a=5;
                            EndIf.
                        EndIf.
                    EndIf.
                EndBody.
            
************SOL**********
Undeclared Identifier: a
===========================

===========================
Testcase#494.txt
***********TEST*******

        Var: x;
        Function: main 
            Parameter: x[5]
            Body:
                x = {1.,2.,3.,4.,5.};
            EndBody.
        Function: foo
            Body:
                x = 2;
            EndBody.
        
************SOL**********
Function Not Return: main
===========================

===========================
Testcase#495.txt
***********TEST*******

        Function : print
            Parameter : x
            Body:
                Return;
            EndBody.

            Function: m
            Body:
                Var : value = 12345;
                Return value;
            EndBody.

            Function: main
            Parameter : x, y
            Body: 
                print(m); 
                Return 0;
            EndBody.
            
************SOL**********
Type Mismatch In Statement: CallStmt(Id(print),[Id(m)])
===========================

===========================
Testcase#496.txt
***********TEST*******

Function: main 
            Parameter: x[5]
            Body:
                Var: y[5]; 
                x = {1,2,3,4,5};
                main(y);
                foo(1.2);
            EndBody.
        Function: foo
            Parameter: x
            Body:
                x = 2;
            EndBody.
            
************SOL**********
Type Mismatch In Statement: Assign(Id(x),IntLiteral(2))
===========================

===========================
Testcase#497.txt
***********TEST*******

Function: main 
            Parameter: x[5]
            Body:
                Var: y[5]; 
                x = {1,2,3,4,5};
                main(y); 
                y = {1.,2.,3.,4.,5.};
            EndBody.
            
************SOL**********
Type Mismatch In Statement: Assign(Id(y),ArrayLiteral(FloatLiteral(1.0),FloatLiteral(2.0),FloatLiteral(3.0),FloatLiteral(4.0),FloatLiteral(5.0)))
===========================

===========================
Testcase#498.txt
***********TEST*******

Function: main 
            Parameter: x[5]
            Body:
                Var: y = 1; 
                x = {1,2,3,4,5};
                main(y); 
            EndBody.
            
************SOL**********
Type Mismatch In Statement: CallStmt(Id(main),[Id(y)])
===========================

===========================
Testcase#499.txt
***********TEST*******

Function: main 
Body:
    Var: a=1,x; 
    a=foo(x); 
EndBody. 
            
************SOL**********
Undeclared Function: foo
===========================

===========================
Testcase#500.txt
***********TEST*******

Function: main
        Parameter: x
        Body:
            If True Then
                Var: x = 1;
                main(1.5);
            EndIf.
            main(2);
        EndBody.
            
************SOL**********
Type Mismatch In Statement: CallStmt(Id(main),[IntLiteral(2)])
===========================
