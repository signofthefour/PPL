 
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
Type Mismatch In Statement: VarDecl(Id(y),[1,2],ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2))))
===========================

===========================
Testcase#408.txt
***********TEST*******
 Var: x="string",y[1][2]={{{1},{2}}};
        Function: main
                   Body: 
                        foo();
                   EndBody.
************SOL**********
Type Mismatch In Statement: VarDecl(Id(y),[1,2],ArrayLiteral(ArrayLiteral(ArrayLiteral(IntLiteral(1)),ArrayLiteral(IntLiteral(2)))))
===========================

===========================
Testcase#409.txt
***********TEST*******
 Var: x="string",y[1][2]={1,1.2};
        Function: main
                   Body: 
                        foo();
                   EndBody.
************SOL**********
Type Mismatch In Statement: VarDecl(Id(y),[1,2],ArrayLiteral(IntLiteral(1),FloatLiteral(1.2)))
===========================
