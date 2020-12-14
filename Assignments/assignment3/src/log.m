
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

            
            
************SOL**********
No Entry Point
===========================

===========================
Testcase#402.txt
***********TEST*******


                Function: main
                Body:
                    x=1;
                EndBody.    
            
************SOL**********
Undeclared Identifier: x
===========================

===========================
Testcase#403.txt
***********TEST*******


                Function: main
                Parameter:x
                Body:
                    x=1;
                    x=1.6;
                EndBody.
            
************SOL**********
Type Mismatch In Statement: Assign(Id(x),FloatLiteral(1.6))
===========================

===========================
Testcase#404.txt
***********TEST*******

                Function: foo
                Parameter: x
                Body:
                EndBody.
                Function: main
                Body:
                    Var: x, y = 0.5;
                    x = 1. +. foo(1);
                    y = foo(2.5) -. 1.;
                EndBody.
            
************SOL**********
Type Mismatch In Expression: CallExpr(Id(foo),[FloatLiteral(2.5)])
===========================

===========================
Testcase#405.txt
***********TEST*******

                Function: foo
                Parameter: x
                Body:
                Return;
                EndBody.
                Function: main
                Body:
                    Var: x, y = 0.5;
                    foo(x);
                EndBody.
            
************SOL**********
Type Cannot Be Inferred: CallStmt(Id(foo),[Id(x)])
===========================

===========================
Testcase#406.txt
***********TEST*******

        Function: main
        Parameter: main
        Body:
            Var: foo;
            foo = foo + main();
            Return 1;
        EndBody.
        Function: foo
        Body:
        EndBody.
                   
************SOL**********
Undeclared Function: main
===========================

===========================
Testcase#407.txt
***********TEST*******

            Function: main 
            Parameter: x,y
            Body:
                x = 1; 
                main( 1.1, 0); 
            EndBody.
            
************SOL**********
Type Mismatch In Statement: CallStmt(Id(main),[FloatLiteral(1.1),IntLiteral(0)])
===========================

===========================
Testcase#408.txt
***********TEST*******

            Function: foo 
            Parameter: x,y
            Body:
            EndBody.
            Function: main
            Parameter: x,y
            Body:
                foo(1,2);  
                foo(1. , 2.); 
            EndBody.
            
************SOL**********
Type Mismatch In Statement: CallStmt(Id(foo),[FloatLiteral(1.0),FloatLiteral(2.0)])
===========================

===========================
Testcase#409.txt
***********TEST*******

            Function: main
            Parameter: x,y
            Body:
                y=0.5;
                For(x=1,x==1,x+1) Do
                EndFor.
                For(y=1,1==1,y +. 1.2) Do
                EndFor.
            EndBody.    
            
************SOL**********
Type Mismatch In Statement: For(Id(y),IntLiteral(1),BinaryOp(==,IntLiteral(1),IntLiteral(1)),BinaryOp(+.,Id(y),FloatLiteral(1.2)),[],[])
===========================

===========================
Testcase#410.txt
***********TEST*******

            Function: main 
            Parameter: x
            Body:
                Var: y = 1; 
                x = 1.0; 
                main(y); 
            EndBody.
            
************SOL**********
Type Mismatch In Statement: CallStmt(Id(main),[Id(y)])
===========================

===========================
Testcase#411.txt
***********TEST*******

            Function: main 
            Parameter: x
            Body:
                Var: y = 1; 
                main(y); 
                x = 1.0; 
            EndBody.
            
************SOL**********
Type Mismatch In Statement: Assign(Id(x),FloatLiteral(1.0))
===========================

===========================
Testcase#412.txt
***********TEST*******
Function: main 
                    Body:
                        printStrLn(read(4));
                    EndBody.
************SOL**********
Type Mismatch In Expression: CallExpr(Id(read),[IntLiteral(4)])
===========================

===========================
Testcase#413.txt
***********TEST*******
Program([FuncDecl(Id(main)[],([][CallStmt(Id(printStrLn),[CallExpr(Id(read),[IntLiteral(4)])])]))])
************SOL**********
Type Mismatch In Expression: CallExpr(Id(read),[IntLiteral(4)])
===========================

===========================
Testcase#414.txt
***********TEST*******
Function: main  
                   Body:
                        printStrLn();
                    EndBody.
************SOL**********
Type Mismatch In Statement: CallStmt(Id(printStrLn),[])
===========================

===========================
Testcase#415.txt
***********TEST*******
Program([FuncDecl(Id(main)[],([][CallStmt(Id(printStrLn),[])]))])
************SOL**********
Type Mismatch In Statement: CallStmt(Id(printStrLn),[])
===========================

===========================
Testcase#416.txt
***********TEST*******
Program([FuncDecl(Id(main)[],([][CallExpr(Id(foo),[])]))])
************SOL**********
Undeclared Function: foo
===========================

===========================
Testcase#417.txt
***********TEST*******

                
                Function: main
                Parameter: x,y,z,t,k
                Body:
                    y= x + y \ z * t;
                    x= k % t;
                    y= x == z;
                EndBody.
            
************SOL**********
Type Mismatch In Statement: Assign(Id(y),BinaryOp(==,Id(x),Id(z)))
===========================

===========================
Testcase#418.txt
***********TEST*******
 
        Function: main 
        Parameter: global_var
        Body:
            global_var = 25+6-.2.5%3\100 ; 
        EndBody.
        
************SOL**********
Type Mismatch In Expression: BinaryOp(%,FloatLiteral(2.5),IntLiteral(3))
===========================

===========================
Testcase#419.txt
***********TEST*******

                Var: a[1][2]= {{1,2}};
                Function: main
                Parameter: x
                Body:
                    a[1][2] = x;
                    x[1] = 1;
                EndBody.
            
************SOL**********
Type Mismatch In Expression: ArrayCell(Id(x),[IntLiteral(1)])
===========================

===========================
Testcase#420.txt
***********TEST*******
                
                Function: main
                Body:
                    Var:a[5]= {1,2,3,4,5};
                    Var:b[5];
                    a=b;
                    a[5]=b;
                EndBody.
            
************SOL**********

===========================

===========================
Testcase#421.txt
***********TEST*******

                
                Function: main
                Body:
                    Var:a[5]= {1,2,3,4,5};
                    Var:b[5];
                    b={1.,2.,3.,4.,5.};
                    a=b;
                EndBody.
            
************SOL**********
Type Mismatch In Statement: Assign(Id(a),Id(b))
===========================

===========================
Testcase#422.txt
***********TEST*******
               
                Function: main
                Body:
                    Var:a[5]= {1,2,3,4,5};
                    Var:b[4]= {1,2,3,4};
                    a=b;
                EndBody.
            
************SOL**********

===========================

===========================
Testcase#423.txt
***********TEST*******
             
                Function: main
                Body:
                    Var:a[5]= {1,2,3,4,5};
                    Var:b[5];
                    Var:c;
                    c = b[5] +. 1;
                    a=b; 
                EndBody.
            
************SOL**********
Type Mismatch In Expression: BinaryOp(+.,ArrayCell(Id(b),[IntLiteral(5)]),IntLiteral(1))
===========================

===========================
Testcase#424.txt
***********TEST*******
                
                Function: main
                Body:
                    Var:a[5],b[5];
                    a=b;
                EndBody.
            
************SOL**********
Type Cannot Be Inferred: Assign(Id(a),Id(b))
===========================

===========================
Testcase#425.txt
***********TEST*******
                
                Var: x[5]={1,2};
                Var: x=1;
                Function: main
                Body:
                EndBody.            
        
************SOL**********
Redeclared Variable: x
===========================

===========================
Testcase#426.txt
***********TEST*******

                Var:x;
                Function: main
                Body:
                    Var:x;
                    Var:main;
                    Var:x[5]={1,2,3,4,5};
                EndBody.
            
************SOL**********
Redeclared Variable: x
===========================

===========================
Testcase#427.txt
***********TEST*******

                Function: main
                Body:
                EndBody.
                Function: main
                Parameter: x
                Body:

                EndBody.
            
************SOL**********
Redeclared Function: main
===========================

===========================
Testcase#428.txt
***********TEST*******

                
                Function: main
                Parameter: x
                Body:
                    Var:x;
                EndBody.
            
************SOL**********
Redeclared Variable: x
===========================

===========================
Testcase#429.txt
***********TEST*******

                
                Function: main
                Parameter: x,x
                Body:

                EndBody.
            
************SOL**********
Redeclared Parameter: x
===========================

===========================
Testcase#430.txt
***********TEST*******

                Var:x;
                Function: main
                Parameter: x
                Body:
                    x=foo;
                EndBody.
            
************SOL**********
Undeclared Identifier: foo
===========================

===========================
Testcase#431.txt
***********TEST*******
               
                Function: main
                Body:
                    foo();
                EndBody.
            
************SOL**********
Undeclared Function: foo
===========================

===========================
Testcase#432.txt
***********TEST*******

                Function: main
                Parameter: x,y,a
                Body:
                    y = a +foo(x);
                EndBody.

                Function: foo
                Parameter: x
                Body:

                EndBody.
            
************SOL**********
Type Cannot Be Inferred: Assign(Id(y),BinaryOp(+,Id(a),CallExpr(Id(foo),[Id(x)])))
===========================

===========================
Testcase#433.txt
***********TEST*******

                
                Function: main
                Body:
                    Var: x,y;
                    x=y;
                EndBody.
            
************SOL**********
Type Cannot Be Inferred: Assign(Id(x),Id(y))
===========================

===========================
Testcase#434.txt
***********TEST*******

                
                Function: main
                Body:
                    Var:x;
                    If (foo(x)) Then
                        x=1;
                    EndIf.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                EndBody.

            
************SOL**********
Type Cannot Be Inferred: If(CallExpr(Id(foo),[Id(x)]),[],[Assign(Id(x),IntLiteral(1))])
===========================

===========================
Testcase#435.txt
***********TEST*******

                Function: foo
                Parameter: x,y
                Body:
                EndBody.

                Function: main
                Body:
                    Var:x=1,y;
                    foo(x,y);
                EndBody.
            
************SOL**********
Type Cannot Be Inferred: CallStmt(Id(foo),[Id(x),Id(y)])
===========================

===========================
Testcase#436.txt
***********TEST*******

                
                Function: main
                Body:
                    Var:x;
                    x = 1 + foo(x);
                EndBody.               
                Function: foo
                Parameter: x
                Body:

                EndBody.

            
************SOL**********
Type Cannot Be Inferred: Assign(Id(x),BinaryOp(+,IntLiteral(1),CallExpr(Id(foo),[Id(x)])))
===========================

===========================
Testcase#437.txt
***********TEST*******

                
Function: main
Body:
    Var:x;
    If x Then
        Var:y;
    EndIf.
EndBody.
            
************SOL**********

===========================

===========================
Testcase#438.txt
***********TEST*******

                
                Function: main
                Body:
                    Var:x;
                    If x Then
                        x=1;
                    Else
                        Var:y,z;
                        y=x;
                    EndIf.
                EndBody.
            
************SOL**********
Type Mismatch In Statement: Assign(Id(x),IntLiteral(1))
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
Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2)])
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
                    foo() = x+1;
                EndBody.
            
************SOL**********

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
Type Mismatch In Expression: Assign(Id(x),CallExpr(Id(foo),[]))
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
Type Mismatch In Statement: [Return(expr=IntLiteral(value=1))]
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
Type Mismatch In Statement: [Return(expr=FloatLiteral(value=1.5))]
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
Type Mismatch In Statement: CallStmt(Id(fact),[Id(x)])
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
Type Mismatch In Statement: CallStmt(Id(foo),[Id(z)])
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
Type Mismatch In Statement: Assign(ArrayCell(Id(abc),[IntLiteral(1)]),FloatLiteral(1.5))
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
Type Mismatch In Statement: CallStmt(Id(foo),[Id(z)])
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
Type Mismatch In Statement: [While(exp=BinaryOp(op='>', left=Id(name='x'), right=IntLiteral(value=1)), sl=([], [If(ifthenStmt=[(BinaryOp(op='==', left=Id(name='x'), right=IntLiteral(value=1)), [], [Return(expr=None)])], elseStmt=())])), Return(expr=BooleanLiteral(value=True))]
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
Type Mismatch In Statement: [Dowhile(sl=([], [Return(expr=CallExpr(method=Id(name='main'), param=[Id(name='x'), Id(name='y')]))]), exp=BooleanLiteral(value=True))]
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
Type Mismatch In Statement: [Return(expr=CallExpr(method=Id(name='main'), param=[BinaryOp(op='+', left=Id(name='x'), right=IntLiteral(value=3)), BinaryOp(op='+.', left=Id(name='y'), right=FloatLiteral(value=10.2))]))]
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
Type Mismatch In Expression: UnaryOp(!,Id(d))
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
