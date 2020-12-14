
===========================
Testcase#300.txt
***********TEST*******
Var:x;
************SOL**********
Program([VarDecl(Id(x))])
===========================

===========================
Testcase#301.txt
***********TEST*******
Var:x = 1;
************SOL**********
Program([VarDecl(Id(x),IntLiteral(1))])
===========================

===========================
Testcase#302.txt
***********TEST*******
Var:x = 1, y;
************SOL**********
Program([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(y))])
===========================

===========================
Testcase#303.txt
***********TEST*******
Var:x = 1, y = "abc", z = 1e2, l=True, a[1][2]={{1},{2}};
************SOL**********
Program([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(y),StringLiteral(abc)),VarDecl(Id(z),FloatLiteral(100.0)),VarDecl(Id(l),BooleanLiteral(true)),VarDecl(Id(a),[1,2],ArrayLiteral(ArrayLiteral(IntLiteral(1)),ArrayLiteral(IntLiteral(2))))])
===========================

===========================
Testcase#304.txt
***********TEST*******
Var:x[1] = {1};
************SOL**********
Program([VarDecl(Id(x),[1],ArrayLiteral(IntLiteral(1)))])
===========================

===========================
Testcase#305.txt
***********TEST*******
Var: a,b=1,c[3]={1,2,3};
Function: main
Body:
Return;
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b),IntLiteral(1)),VarDecl(Id(c),[3],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3))),FuncDecl(Id(main)[],([][Return()]))])
===========================

===========================
Testcase#306.txt
***********TEST*******
Var: b[2][3]={{1,2},{3,4}};
Function: main
Body:
Return;
EndBody.
************SOL**********
Program([VarDecl(Id(b),[2,3],ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2)),ArrayLiteral(IntLiteral(3),IntLiteral(4)))),FuncDecl(Id(main)[],([][Return()]))])
===========================

===========================
Testcase#307.txt
***********TEST*******
Var: x;
Function: fact
Parameter: n
Body:
If n == 0 Then
Return 1;
Else
Return n * fact(n-1);
EndIf.
EndBody.
Function: main
** this is a comment **
Body:
x = 10;
fact (x);
EndBody.
************SOL**********
Program([VarDecl(Id(x)),FuncDecl(Id(fact)[VarDecl(Id(n))],([][If(BinaryOp(==,Id(n),IntLiteral(0)),[],[Return(IntLiteral(1))])Else([],[Return(BinaryOp(*,Id(n),CallExpr(Id(fact),[BinaryOp(-,Id(n),IntLiteral(1))])))])])),FuncDecl(Id(main)[],([][Assign(Id(x),IntLiteral(10)),CallStmt(Id(fact),[Id(x)])]))])
===========================

===========================
Testcase#308.txt
***********TEST*******
Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
Function: fact
Parameter: n
Body:
If n == 0 Then
Return 1;
Else
Return n * fact(n-1);
EndIf.
EndBody.
Function: main
** this is a comment **
Body:
x = 10;
fact (x);
EndBody.
************SOL**********
Program([VarDecl(Id(x)),VarDecl(Id(y),[1,3],ArrayLiteral(ArrayLiteral(ArrayLiteral(IntLiteral(12),IntLiteral(1)),ArrayLiteral(FloatLiteral(12.0),FloatLiteral(12000.0))),ArrayLiteral(IntLiteral(23)),ArrayLiteral(IntLiteral(13),IntLiteral(32)))),FuncDecl(Id(fact)[VarDecl(Id(n))],([][If(BinaryOp(==,Id(n),IntLiteral(0)),[],[Return(IntLiteral(1))])Else([],[Return(BinaryOp(*,Id(n),CallExpr(Id(fact),[BinaryOp(-,Id(n),IntLiteral(1))])))])])),FuncDecl(Id(main)[],([][Assign(Id(x),IntLiteral(10)),CallStmt(Id(fact),[Id(x)])]))])
===========================

===========================
Testcase#309.txt
***********TEST*******
Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
Function: fact
Parameter: n
Body:
a = a < b;
If n == 0 Then
Return 1;
Else
Return n * fact(n-1);
EndIf.
EndBody.
Function: main
Body:
x = 10;
fact (x);
EndBody.
************SOL**********
Program([VarDecl(Id(x)),VarDecl(Id(y),[1,3],ArrayLiteral(ArrayLiteral(ArrayLiteral(IntLiteral(12),IntLiteral(1)),ArrayLiteral(FloatLiteral(12.0),FloatLiteral(12000.0))),ArrayLiteral(IntLiteral(23)),ArrayLiteral(IntLiteral(13),IntLiteral(32)))),FuncDecl(Id(fact)[VarDecl(Id(n))],([][Assign(Id(a),BinaryOp(<,Id(a),Id(b))),If(BinaryOp(==,Id(n),IntLiteral(0)),[],[Return(IntLiteral(1))])Else([],[Return(BinaryOp(*,Id(n),CallExpr(Id(fact),[BinaryOp(-,Id(n),IntLiteral(1))])))])])),FuncDecl(Id(main)[],([][Assign(Id(x),IntLiteral(10)),CallStmt(Id(fact),[Id(x)])]))])
===========================

===========================
Testcase#310.txt
***********TEST*******
Var:x[1] = {1,2,3,4};
************SOL**********
Program([VarDecl(Id(x),[1],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)))])
===========================

===========================
Testcase#311.txt
***********TEST*******
Var: a,b,c;
                    Function: main
                    Parameter: a
                    Body:
                    EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([][]))])
===========================

===========================
Testcase#312.txt
***********TEST*******
Var: a,b,c;
                Function: main
                Parameter: a
                Body:
                EndBody.
                Function: foo
                Parameter: a,b,c[1]
                Body:
                EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([][])),FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c),[1])],([][]))])
===========================

===========================
Testcase#313.txt
***********TEST*******
Var: a,b,c;
            Function: main
            Parameter: a
            Body:
            Var:x = 1, y;
            EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(y))][]))])
===========================

===========================
Testcase#314.txt
***********TEST*******
Var: x = "yay";
************SOL**********
Program([VarDecl(Id(x),StringLiteral(yay))])
===========================

===========================
Testcase#315.txt
***********TEST*******
Var: a,b,c;
Function: main
Body:
a = a <b - c;
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][Assign(Id(a),BinaryOp(<,Id(a),BinaryOp(-,Id(b),Id(c))))]))])
===========================

===========================
Testcase#316.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][If(UnaryOp(!,BooleanLiteral(true)),[],[Assign(Id(a),BinaryOp(<,Id(a),Id(c))),If(BinaryOp(>,BinaryOp(+,Id(a),Id(b)),Id(c)),[],[Assign(Id(a),BinaryOp(+,Id(a),Id(b)))])ElseIf(BinaryOp(==,Id(a),Id(b)),[],[CallStmt(Id(writeln),[Id(i)])])Else([],[Assign(Id(a),FloatLiteral(120.0))])])]))])
===========================

===========================
Testcase#317.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        Var: x=1,a[1]=1;
        Var: a,b[1]={"this"};
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],IntLiteral(1)),VarDecl(Id(a)),VarDecl(Id(b),[1],ArrayLiteral(StringLiteral(this)))][]))])
===========================

===========================
Testcase#318.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]=1;
        Var: a,b[1]={"this"};
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],IntLiteral(1)),VarDecl(Id(a)),VarDecl(Id(b),[1],ArrayLiteral(StringLiteral(this)))][]))])
===========================

===========================
Testcase#319.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a, b[1]
        Body:
        Var: x=1,a[1]=1;
        Var: a,b[1]={"this"};
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b),[1])],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],IntLiteral(1)),VarDecl(Id(a)),VarDecl(Id(b),[1],ArrayLiteral(StringLiteral(this)))][]))])
===========================

===========================
Testcase#320.txt
***********TEST*******
Var: a,b,c;
Function: main
Parameter: a, b[1]
Body:
Var: x=1,a[1]={{}};
Var: a,b[1]={"this"};
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b),[1])],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],ArrayLiteral(ArrayLiteral())),VarDecl(Id(a)),VarDecl(Id(b),[1],ArrayLiteral(StringLiteral(this)))][]))])
===========================

===========================
Testcase#321.txt
***********TEST*******
Function: main
                Parameter: a
                Body:
                    If 1 + a - b * foo() > 1 Then
                    EndIf.
                EndBody.
************SOL**********
Program([FuncDecl(Id(main)[VarDecl(Id(a))],([][If(BinaryOp(>,BinaryOp(-,BinaryOp(+,IntLiteral(1),Id(a)),BinaryOp(*,Id(b),CallExpr(Id(foo),[]))),IntLiteral(1)),[],[])]))])
===========================

===========================
Testcase#322.txt
***********TEST*******
Function: main
                Parameter: a
                Body:
                    If 1 Then
                    EndIf.
                EndBody.
************SOL**********
Program([FuncDecl(Id(main)[VarDecl(Id(a))],([][If(IntLiteral(1),[],[])]))])
===========================

===========================
Testcase#323.txt
***********TEST*******
Function: main
                Parameter: a
                Body:
                EndBody.
************SOL**********
Program([FuncDecl(Id(main)[VarDecl(Id(a))],([][]))])
===========================

===========================
Testcase#324.txt
***********TEST*******
Var: a,b,c;
Function: main
Parameter: a, b[1]
Body:
Var: x=1,a[1]=1;
If a Then
EndIf.
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b),[1])],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],IntLiteral(1))][If(Id(a),[],[])]))])
===========================

===========================
Testcase#325.txt
***********TEST*******
Var: a,b,c;
Function: main
Parameter: a
Body:
Var: x=1,a[1]=1;
Var: a,b[1]={"this"};
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],IntLiteral(1)),VarDecl(Id(a)),VarDecl(Id(b),[1],ArrayLiteral(StringLiteral(this)))][]))])
===========================

===========================
Testcase#326.txt
***********TEST*******
Var: a,b,c;
Function: main
Parameter: a
Body:
Var: x=1,a[1]={12, "asdf"},b=1.21;
Var: a,b[1]={"this"};
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],ArrayLiteral(IntLiteral(12),StringLiteral(asdf))),VarDecl(Id(b),FloatLiteral(1.21)),VarDecl(Id(a)),VarDecl(Id(b),[1],ArrayLiteral(StringLiteral(this)))][]))])
===========================

===========================
Testcase#327.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        Var: a,b[1]={"this"};
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],ArrayLiteral(IntLiteral(12),StringLiteral(asdf))),VarDecl(Id(a),ArrayLiteral(IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(true),IntLiteral(18))),VarDecl(Id(a)),VarDecl(Id(b),[1],ArrayLiteral(StringLiteral(this)))][]))])
===========================

===========================
Testcase#328.txt
***********TEST*******
Var: a,b,c;
Function: main
Parameter: a
Body:
Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
If 1 < a Then
Var: a;
EndIf.
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],ArrayLiteral(IntLiteral(12),StringLiteral(asdf))),VarDecl(Id(a),ArrayLiteral(IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(true),IntLiteral(18)))][If(BinaryOp(<,IntLiteral(1),Id(a)),[VarDecl(Id(a))],[])]))])
===========================

===========================
Testcase#329.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        If 1 + a - b * foo() > 1 Then
        EndIf.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],ArrayLiteral(IntLiteral(12),StringLiteral(asdf))),VarDecl(Id(a),ArrayLiteral(IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(true),IntLiteral(18)))][If(BinaryOp(>,BinaryOp(-,BinaryOp(+,IntLiteral(1),Id(a)),BinaryOp(*,Id(b),CallExpr(Id(foo),[]))),IntLiteral(1)),[],[])]))])
===========================

===========================
Testcase#330.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        If a == True Then
        EndIf.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],ArrayLiteral(IntLiteral(12),StringLiteral(asdf))),VarDecl(Id(a),ArrayLiteral(IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(true),IntLiteral(18)))][If(BinaryOp(==,Id(a),BooleanLiteral(true)),[],[])]))])
===========================

===========================
Testcase#331.txt
***********TEST*******
Function: main
                Parameter: a
                Body:
                    If 1 + 1 Then
                    For (i=1,i>1,1+2) Do
                        Var: a=10,c[1]={1,2};
                        c[foo() + 1] = a;
                    EndFor.
                    EndIf.
                EndBody.
************SOL**********
Program([FuncDecl(Id(main)[VarDecl(Id(a))],([][If(BinaryOp(+,IntLiteral(1),IntLiteral(1)),[],[For(Id(i),IntLiteral(1),BinaryOp(>,Id(i),IntLiteral(1)),BinaryOp(+,IntLiteral(1),IntLiteral(2)),[VarDecl(Id(a),IntLiteral(10)),VarDecl(Id(c),[1],ArrayLiteral(IntLiteral(1),IntLiteral(2)))],[Assign(ArrayCell(Id(c),[BinaryOp(+,CallExpr(Id(foo),[]),IntLiteral(1))]),Id(a))])])]))])
===========================

===========================
Testcase#332.txt
***********TEST*******
Function: main
                Parameter: a
                Body:
                (1 + c)[foo() + 1][1 + 2][a + v] = a;
                EndBody.
************SOL**********
Program([FuncDecl(Id(main)[VarDecl(Id(a))],([][Assign(ArrayCell(BinaryOp(+,IntLiteral(1),Id(c)),[BinaryOp(+,CallExpr(Id(foo),[]),IntLiteral(1)),BinaryOp(+,IntLiteral(1),IntLiteral(2)),BinaryOp(+,Id(a),Id(v))]),Id(a))]))])
===========================

===========================
Testcase#333.txt
***********TEST*******
Var: a,b,c;
Function: main
Parameter: a
Body:
Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
For (i=1, i<3, 2) Do something(); EndFor.
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],ArrayLiteral(IntLiteral(12),StringLiteral(asdf))),VarDecl(Id(a),ArrayLiteral(IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(true),IntLiteral(18)))][For(Id(i),IntLiteral(1),BinaryOp(<,Id(i),IntLiteral(3)),IntLiteral(2),[],[CallStmt(Id(something),[])])]))])
===========================

===========================
Testcase#334.txt
***********TEST*******
Var: a,b,c;
Function: main
Parameter: a
Body:
Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
For (i = 1, a < 2, i + 1) Do something(); EndFor.
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],ArrayLiteral(IntLiteral(12),StringLiteral(asdf))),VarDecl(Id(a),ArrayLiteral(IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(true),IntLiteral(18)))][For(Id(i),IntLiteral(1),BinaryOp(<,Id(a),IntLiteral(2)),BinaryOp(+,Id(i),IntLiteral(1)),[],[CallStmt(Id(something),[])])]))])
===========================

===========================
Testcase#335.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        For (i = "abc", a < 2, i + 1) Do something(); EndFor.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],ArrayLiteral(IntLiteral(12),StringLiteral(asdf))),VarDecl(Id(a),ArrayLiteral(IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(true),IntLiteral(18)))][For(Id(i),StringLiteral(abc),BinaryOp(<,Id(a),IntLiteral(2)),BinaryOp(+,Id(i),IntLiteral(1)),[],[CallStmt(Id(something),[])])]))])
===========================

===========================
Testcase#336.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        For (i = 0x12, a < 2, i + foo() + 1) Do something(); EndFor.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],ArrayLiteral(IntLiteral(12),StringLiteral(asdf))),VarDecl(Id(a),ArrayLiteral(IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(true),IntLiteral(18)))][For(Id(i),IntLiteral(18),BinaryOp(<,Id(a),IntLiteral(2)),BinaryOp(+,BinaryOp(+,Id(i),CallExpr(Id(foo),[])),IntLiteral(1)),[],[CallStmt(Id(something),[])])]))])
===========================

===========================
Testcase#337.txt
***********TEST*******
Var: a,b,c;
Function: main
Parameter: a
Body:
Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
For (i = 2, a < 2, i + 1) Do 
For (i=2, a>1341,a+b) Do EndFor.
something(); EndFor.
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],ArrayLiteral(IntLiteral(12),StringLiteral(asdf))),VarDecl(Id(a),ArrayLiteral(IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(true),IntLiteral(18)))][For(Id(i),IntLiteral(2),BinaryOp(<,Id(a),IntLiteral(2)),BinaryOp(+,Id(i),IntLiteral(1)),[],[For(Id(i),IntLiteral(2),BinaryOp(>,Id(a),IntLiteral(1341)),BinaryOp(+,Id(a),Id(b)),[],[]),CallStmt(Id(something),[])])]))])
===========================

===========================
Testcase#338.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        For (i = 0x12, a < 2, i + foo() + 1) Do something();
        c = a[23][b[1][2][c]] +. 12.; 
        EndFor.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],ArrayLiteral(IntLiteral(12),StringLiteral(asdf))),VarDecl(Id(a),ArrayLiteral(IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(true),IntLiteral(18)))][For(Id(i),IntLiteral(18),BinaryOp(<,Id(a),IntLiteral(2)),BinaryOp(+,BinaryOp(+,Id(i),CallExpr(Id(foo),[])),IntLiteral(1)),[],[CallStmt(Id(something),[]),Assign(Id(c),BinaryOp(+.,ArrayCell(Id(a),[IntLiteral(23),ArrayCell(Id(b),[IntLiteral(1),IntLiteral(2),Id(c)])]),FloatLiteral(12.0)))])]))])
===========================

===========================
Testcase#339.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        For (i = 0x12, a < 2, i + foo() + 1) Do something();
        c = a[23][b[1][2][c]] +. 12; 
        EndFor.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],ArrayLiteral(IntLiteral(12),StringLiteral(asdf))),VarDecl(Id(a),ArrayLiteral(IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(true),IntLiteral(18)))][For(Id(i),IntLiteral(18),BinaryOp(<,Id(a),IntLiteral(2)),BinaryOp(+,BinaryOp(+,Id(i),CallExpr(Id(foo),[])),IntLiteral(1)),[],[CallStmt(Id(something),[]),Assign(Id(c),BinaryOp(+.,ArrayCell(Id(a),[IntLiteral(23),ArrayCell(Id(b),[IntLiteral(1),IntLiteral(2),Id(c)])]),IntLiteral(12)))])]))])
===========================

===========================
Testcase#340.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        While 1 Do something(); EndWhile.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],ArrayLiteral(IntLiteral(12),StringLiteral(asdf))),VarDecl(Id(a),ArrayLiteral(IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(true),IntLiteral(18)))][While(IntLiteral(1),[],[CallStmt(Id(something),[])])]))])
===========================

===========================
Testcase#341.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        While !(x =/= y) Do something(); EndWhile.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],ArrayLiteral(IntLiteral(12),StringLiteral(asdf))),VarDecl(Id(a),ArrayLiteral(IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(true),IntLiteral(18)))][While(UnaryOp(!,BinaryOp(=/=,Id(x),Id(y))),[],[CallStmt(Id(something),[])])]))])
===========================

===========================
Testcase#342.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        While !(x &&  y || b) ** && (a || abc)** Do something(); EndWhile.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],ArrayLiteral(IntLiteral(12),StringLiteral(asdf))),VarDecl(Id(a),ArrayLiteral(IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(true),IntLiteral(18)))][While(UnaryOp(!,BinaryOp(||,BinaryOp(&&,Id(x),Id(y)),Id(b))),[],[CallStmt(Id(something),[])])]))])
===========================

===========================
Testcase#343.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: x=1,a[1]={12, "asdf"},a={12,12.e5,True,0x12};
        While !(x &&  y || b) && (a || abc) Do something(); EndWhile.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(a),[1],ArrayLiteral(IntLiteral(12),StringLiteral(asdf))),VarDecl(Id(a),ArrayLiteral(IntLiteral(12),FloatLiteral(1200000.0),BooleanLiteral(true),IntLiteral(18)))][While(BinaryOp(&&,UnaryOp(!,BinaryOp(||,BinaryOp(&&,Id(x),Id(y)),Id(b))),BinaryOp(||,Id(a),Id(abc))),[],[CallStmt(Id(something),[])])]))])
===========================

===========================
Testcase#344.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        a = !(x &&  y || b) && (a || abc);
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([][Assign(Id(a),BinaryOp(&&,UnaryOp(!,BinaryOp(||,BinaryOp(&&,Id(x),Id(y)),Id(b))),BinaryOp(||,Id(a),Id(abc))))]))])
===========================

===========================
Testcase#345.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Do something(); While !(abc < 12 || b && True) EndDo.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([][Dowhile([],[CallStmt(Id(something),[])],UnaryOp(!,BinaryOp(<,Id(abc),BinaryOp(&&,BinaryOp(||,IntLiteral(12),Id(b)),BooleanLiteral(true)))))]))])
===========================

===========================
Testcase#346.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Do something(); While a[1][c[2]] + 123 -1 EndDo.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([][Dowhile([],[CallStmt(Id(something),[])],BinaryOp(-,BinaryOp(+,ArrayCell(Id(a),[IntLiteral(1),ArrayCell(Id(c),[IntLiteral(2)])]),IntLiteral(123)),IntLiteral(1)))]))])
===========================

===========================
Testcase#347.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Do something(); While 1 <. 2.0 EndDo.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([][Dowhile([],[CallStmt(Id(something),[])],BinaryOp(<.,IntLiteral(1),FloatLiteral(2.0)))]))])
===========================

===========================
Testcase#348.txt
***********TEST*******
Var: a,b,c;
Function: main
Parameter: a
Body:
Do something(); While a && bool_of_string("True") EndDo.
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([][Dowhile([],[CallStmt(Id(something),[])],BinaryOp(&&,Id(a),CallExpr(Id(bool_of_string),[StringLiteral(True)])))]))])
===========================

===========================
Testcase#349.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Do something(); While a && b <. 1. +. 3. EndDo.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([][Dowhile([],[CallStmt(Id(something),[])],BinaryOp(<.,BinaryOp(&&,Id(a),Id(b)),BinaryOp(+.,FloatLiteral(1.0),FloatLiteral(3.0))))]))])
===========================

===========================
Testcase#350.txt
***********TEST*******
Var: a,b,c;
Function: main
Body:
If !(True) Then
a = a <c;
If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12 + e; EndIf.
EndIf.
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][If(UnaryOp(!,BooleanLiteral(true)),[],[Assign(Id(a),BinaryOp(<,Id(a),Id(c))),If(BinaryOp(>,BinaryOp(+,Id(a),Id(b)),Id(c)),[],[Assign(Id(a),BinaryOp(+,Id(a),Id(b)))])ElseIf(BinaryOp(==,Id(a),Id(b)),[],[CallStmt(Id(writeln),[Id(i)])])Else([],[Assign(Id(a),BinaryOp(+,IntLiteral(12),Id(e)))])])]))])
===========================

===========================
Testcase#351.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        Break;
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Continue;
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][If(UnaryOp(!,BooleanLiteral(true)),[],[Break(),Assign(Id(a),BinaryOp(<,Id(a),Id(c))),If(BinaryOp(>,BinaryOp(+,Id(a),Id(b)),Id(c)),[],[Assign(Id(a),BinaryOp(+,Id(a),Id(b)))])ElseIf(BinaryOp(==,Id(a),Id(b)),[],[CallStmt(Id(writeln),[Id(i)])])Else([],[Assign(Id(a),FloatLiteral(120.0))])]),Continue()]))])
===========================

===========================
Testcase#352.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Return ;
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][If(UnaryOp(!,BooleanLiteral(true)),[],[Assign(Id(a),BinaryOp(<,Id(a),Id(c))),If(BinaryOp(>,BinaryOp(+,Id(a),Id(b)),Id(c)),[],[Assign(Id(a),BinaryOp(+,Id(a),Id(b)))])ElseIf(BinaryOp(==,Id(a),Id(b)),[],[CallStmt(Id(writeln),[Id(i)])])Else([],[Assign(Id(a),FloatLiteral(120.0))])]),Return()]))])
===========================

===========================
Testcase#353.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Return 1 + 1;
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][If(UnaryOp(!,BooleanLiteral(true)),[],[Assign(Id(a),BinaryOp(<,Id(a),Id(c))),If(BinaryOp(>,BinaryOp(+,Id(a),Id(b)),Id(c)),[],[Assign(Id(a),BinaryOp(+,Id(a),Id(b)))])ElseIf(BinaryOp(==,Id(a),Id(b)),[],[CallStmt(Id(writeln),[Id(i)])])Else([],[Assign(Id(a),FloatLiteral(120.0))])]),Return(BinaryOp(+,IntLiteral(1),IntLiteral(1)))]))])
===========================

===========================
Testcase#354.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Return 1 + {{1,2}, "abnd"};
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][If(UnaryOp(!,BooleanLiteral(true)),[],[Assign(Id(a),BinaryOp(<,Id(a),Id(c))),If(BinaryOp(>,BinaryOp(+,Id(a),Id(b)),Id(c)),[],[Assign(Id(a),BinaryOp(+,Id(a),Id(b)))])ElseIf(BinaryOp(==,Id(a),Id(b)),[],[CallStmt(Id(writeln),[Id(i)])])Else([],[Assign(Id(a),FloatLiteral(120.0))])]),Return(BinaryOp(+,IntLiteral(1),ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2)),StringLiteral(abnd))))]))])
===========================

===========================
Testcase#355.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Return (a < 1) || (b >. !c);
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][If(UnaryOp(!,BooleanLiteral(true)),[],[Assign(Id(a),BinaryOp(<,Id(a),Id(c))),If(BinaryOp(>,BinaryOp(+,Id(a),Id(b)),Id(c)),[],[Assign(Id(a),BinaryOp(+,Id(a),Id(b)))])ElseIf(BinaryOp(==,Id(a),Id(b)),[],[CallStmt(Id(writeln),[Id(i)])])Else([],[Assign(Id(a),FloatLiteral(120.0))])]),Return(BinaryOp(||,BinaryOp(<,Id(a),IntLiteral(1)),BinaryOp(>.,Id(b),UnaryOp(!,Id(c)))))]))])
===========================

===========================
Testcase#356.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        If !(True) Then
        
        a = a <c;
        If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
        EndIf.
        Return a < 1 || foo(arg1, "arg2", {1,2});
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][If(UnaryOp(!,BooleanLiteral(true)),[],[Assign(Id(a),BinaryOp(<,Id(a),Id(c))),If(BinaryOp(>,BinaryOp(+,Id(a),Id(b)),Id(c)),[],[Assign(Id(a),BinaryOp(+,Id(a),Id(b)))])ElseIf(BinaryOp(==,Id(a),Id(b)),[],[CallStmt(Id(writeln),[Id(i)])])Else([],[Assign(Id(a),FloatLiteral(120.0))])]),Return(BinaryOp(<,Id(a),BinaryOp(||,IntLiteral(1),CallExpr(Id(foo),[Id(arg1),StringLiteral(arg2),ArrayLiteral(IntLiteral(1),IntLiteral(2))]))))]))])
===========================

===========================
Testcase#357.txt
***********TEST*******
Var: a,b,c;
Function: main
Body:
If !(True) Then

a = a <c;
If (a + b > c) Then a = a+b; ElseIf a == b Then writeln(i); Else a = 12.e1; EndIf.
EndIf.
Return  main();
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][If(UnaryOp(!,BooleanLiteral(true)),[],[Assign(Id(a),BinaryOp(<,Id(a),Id(c))),If(BinaryOp(>,BinaryOp(+,Id(a),Id(b)),Id(c)),[],[Assign(Id(a),BinaryOp(+,Id(a),Id(b)))])ElseIf(BinaryOp(==,Id(a),Id(b)),[],[CallStmt(Id(writeln),[Id(i)])])Else([],[Assign(Id(a),FloatLiteral(120.0))])]),Return(CallExpr(Id(main),[]))]))])
===========================

===========================
Testcase#358.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        foo(arg1, "???", foo(nothing));
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][CallStmt(Id(foo),[Id(arg1),StringLiteral(???),CallExpr(Id(foo),[Id(nothing)])])]))])
===========================

===========================
Testcase#359.txt
***********TEST*******
Var: a,b,c;
Function: main
Body:
foo(arg1, "???", foo(nothing));
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][CallStmt(Id(foo),[Id(arg1),StringLiteral(???),CallExpr(Id(foo),[Id(nothing)])])]))])
===========================

===========================
Testcase#360.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        a = a[c[1][b]][1] + foo(arg1, "???", foo(nothing));
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][Assign(Id(a),BinaryOp(+,ArrayCell(Id(a),[ArrayCell(Id(c),[IntLiteral(1),Id(b)]),IntLiteral(1)]),CallExpr(Id(foo),[Id(arg1),StringLiteral(???),CallExpr(Id(foo),[Id(nothing)])])))]))])
===========================

===========================
Testcase#361.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        a = a[c[1][b]][1] < foo(arg1, "???", foo(nothing));
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][Assign(Id(a),BinaryOp(<,ArrayCell(Id(a),[ArrayCell(Id(c),[IntLiteral(1),Id(b)]),IntLiteral(1)]),CallExpr(Id(foo),[Id(arg1),StringLiteral(???),CallExpr(Id(foo),[Id(nothing)])])))]))])
===========================

===========================
Testcase#362.txt
***********TEST*******
Var: a,b,c;
Function: main
Body:
foo(arg1, "???", foo(nothing))[1] = something(foo());
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][Assign(ArrayCell(CallExpr(Id(foo),[Id(arg1),StringLiteral(???),CallExpr(Id(foo),[Id(nothing)])]),[IntLiteral(1)]),CallExpr(Id(something),[CallExpr(Id(foo),[])]))]))])
===========================

===========================
Testcase#363.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        foo(arg1, "???", foo(nothing), {"asdab", {1,2.e2,123e1,"nothing"}});
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][CallStmt(Id(foo),[Id(arg1),StringLiteral(???),CallExpr(Id(foo),[Id(nothing)]),ArrayLiteral(StringLiteral(asdab),ArrayLiteral(IntLiteral(1),FloatLiteral(200.0),FloatLiteral(1230.0),StringLiteral(nothing)))])]))])
===========================

===========================
Testcase#364.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        foo(arg1, "???", foo(nothing), {"asdab", {1,2.e2,123e1,"nothing"}});
        printLn();
        print(arg);
        printStrLn(arg);
        read();
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][CallStmt(Id(foo),[Id(arg1),StringLiteral(???),CallExpr(Id(foo),[Id(nothing)]),ArrayLiteral(StringLiteral(asdab),ArrayLiteral(IntLiteral(1),FloatLiteral(200.0),FloatLiteral(1230.0),StringLiteral(nothing)))]),CallStmt(Id(printLn),[]),CallStmt(Id(print),[Id(arg)]),CallStmt(Id(printStrLn),[Id(arg)]),CallStmt(Id(read),[])]))])
===========================

===========================
Testcase#365.txt
***********TEST*******
Var: a,b,c;
Function: main
Body:
foo(arg1, "???", foo(nothing), {"asdab", {1,2.e2,123e1,"nothing"}});
printLn();
print(arg);
printStrLn(arg);
read();
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][CallStmt(Id(foo),[Id(arg1),StringLiteral(???),CallExpr(Id(foo),[Id(nothing)]),ArrayLiteral(StringLiteral(asdab),ArrayLiteral(IntLiteral(1),FloatLiteral(200.0),FloatLiteral(1230.0),StringLiteral(nothing)))]),CallStmt(Id(printLn),[]),CallStmt(Id(print),[Id(arg)]),CallStmt(Id(printStrLn),[Id(arg)]),CallStmt(Id(read),[])]))])
===========================

===========================
Testcase#366.txt
***********TEST*******
Var: a,b,c;
Function: main
Body:
foo(arg1, "???", foo(nothing), {"asdab", {1,2.e2,123e1,"nothing"}});
printLn();
**print(arg);
printStrLn(arg)**
read();
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][CallStmt(Id(foo),[Id(arg1),StringLiteral(???),CallExpr(Id(foo),[Id(nothing)]),ArrayLiteral(StringLiteral(asdab),ArrayLiteral(IntLiteral(1),FloatLiteral(200.0),FloatLiteral(1230.0),StringLiteral(nothing)))]),CallStmt(Id(printLn),[]),CallStmt(Id(read),[])]))])
===========================

===========================
Testcase#367.txt
***********TEST*******
Var: a,b,c;
Function: main
Body:
foo(a < b + c);
printLn();
a = 1+ 2+2+{1, 2,3};
**print(arg);
printStrLn(arg)**
read();
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][CallStmt(Id(foo),[BinaryOp(<,Id(a),BinaryOp(+,Id(b),Id(c)))]),CallStmt(Id(printLn),[]),Assign(Id(a),BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLiteral(1),IntLiteral(2)),IntLiteral(2)),ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)))),CallStmt(Id(read),[])]))])
===========================

===========================
Testcase#368.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        a = b[something()[a[1]] + 1 ];
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][Assign(Id(a),ArrayCell(Id(b),[BinaryOp(+,ArrayCell(CallExpr(Id(something),[]),[ArrayCell(Id(a),[IntLiteral(1)])]),IntLiteral(1))]))]))])
===========================

===========================
Testcase#369.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        a = b[something()[a[1]] + 1][c + d < 1];
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][Assign(Id(a),ArrayCell(Id(b),[BinaryOp(+,ArrayCell(CallExpr(Id(something),[]),[ArrayCell(Id(a),[IntLiteral(1)])]),IntLiteral(1)),BinaryOp(<,BinaryOp(+,Id(c),Id(d)),IntLiteral(1))]))]))])
===========================

===========================
Testcase#370.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        a = b[something()[a[1]] + 1][c + d < 1] + c *. d[1][21];
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][Assign(Id(a),BinaryOp(+,ArrayCell(Id(b),[BinaryOp(+,ArrayCell(CallExpr(Id(something),[]),[ArrayCell(Id(a),[IntLiteral(1)])]),IntLiteral(1)),BinaryOp(<,BinaryOp(+,Id(c),Id(d)),IntLiteral(1))]),BinaryOp(*.,Id(c),ArrayCell(Id(d),[IntLiteral(1),IntLiteral(21)]))))]))])
===========================

===========================
Testcase#371.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        a = b[something()[a[1]] + 1][c + d < 1] + c *. d[1][21 * 0x21AF];
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][Assign(Id(a),BinaryOp(+,ArrayCell(Id(b),[BinaryOp(+,ArrayCell(CallExpr(Id(something),[]),[ArrayCell(Id(a),[IntLiteral(1)])]),IntLiteral(1)),BinaryOp(<,BinaryOp(+,Id(c),Id(d)),IntLiteral(1))]),BinaryOp(*.,Id(c),ArrayCell(Id(d),[IntLiteral(1),BinaryOp(*,IntLiteral(21),IntLiteral(8623))]))))]))])
===========================

===========================
Testcase#372.txt
***********TEST*******
Var: a,b,c;
Function: main
Body:
a = b[something()[a[1]] + 1][c + d < 1] + c *. d[1.][21 * 0x21A];
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][Assign(Id(a),BinaryOp(+,ArrayCell(Id(b),[BinaryOp(+,ArrayCell(CallExpr(Id(something),[]),[ArrayCell(Id(a),[IntLiteral(1)])]),IntLiteral(1)),BinaryOp(<,BinaryOp(+,Id(c),Id(d)),IntLiteral(1))]),BinaryOp(*.,Id(c),ArrayCell(Id(d),[FloatLiteral(1.0),BinaryOp(*,IntLiteral(21),IntLiteral(538))]))))]))])
===========================

===========================
Testcase#373.txt
***********TEST*******
Var: a,b,c;
Function: main
Body:
a = a + b +. a-a-.a*a*.a\.b%!c&&a||a==b;
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][Assign(Id(a),BinaryOp(==,BinaryOp(||,BinaryOp(&&,BinaryOp(-.,BinaryOp(-,BinaryOp(+.,BinaryOp(+,Id(a),Id(b)),Id(a)),Id(a)),BinaryOp(%,BinaryOp(\.,BinaryOp(*.,BinaryOp(*,Id(a),Id(a)),Id(a)),Id(b)),UnaryOp(!,Id(c)))),Id(a)),Id(a)),Id(b)))]))])
===========================

===========================
Testcase#374.txt
***********TEST*******
Var: a,b,c;
Function: main
Body:
a = (a + b) +. (a-a-.a*a*.a\.b%!c&&a||a==b);
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][Assign(Id(a),BinaryOp(+.,BinaryOp(+,Id(a),Id(b)),BinaryOp(==,BinaryOp(||,BinaryOp(&&,BinaryOp(-.,BinaryOp(-,Id(a),Id(a)),BinaryOp(%,BinaryOp(\.,BinaryOp(*.,BinaryOp(*,Id(a),Id(a)),Id(a)),Id(b)),UnaryOp(!,Id(c)))),Id(a)),Id(a)),Id(b))))]))])
===========================

===========================
Testcase#375.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        b = {{{}}};
        a = (a + b) +. (a-a-.a*a*.a\.b%!c&&a||a==b);
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][Assign(Id(b),ArrayLiteral(ArrayLiteral(ArrayLiteral()))),Assign(Id(a),BinaryOp(+.,BinaryOp(+,Id(a),Id(b)),BinaryOp(==,BinaryOp(||,BinaryOp(&&,BinaryOp(-.,BinaryOp(-,Id(a),Id(a)),BinaryOp(%,BinaryOp(\.,BinaryOp(*.,BinaryOp(*,Id(a),Id(a)),Id(a)),Id(b)),UnaryOp(!,Id(c)))),Id(a)),Id(a)),Id(b))))]))])
===========================

===========================
Testcase#376.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Body:
        b = {{{}}};
        a = (a + b) +. (a-a-.a*a*.a\.b%!c&&a||a==b) % a[1][1];
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][Assign(Id(b),ArrayLiteral(ArrayLiteral(ArrayLiteral()))),Assign(Id(a),BinaryOp(+.,BinaryOp(+,Id(a),Id(b)),BinaryOp(%,BinaryOp(==,BinaryOp(||,BinaryOp(&&,BinaryOp(-.,BinaryOp(-,Id(a),Id(a)),BinaryOp(%,BinaryOp(\.,BinaryOp(*.,BinaryOp(*,Id(a),Id(a)),Id(a)),Id(b)),UnaryOp(!,Id(c)))),Id(a)),Id(a)),Id(b)),ArrayCell(Id(a),[IntLiteral(1),IntLiteral(1)]))))]))])
===========================

===========================
Testcase#377.txt
***********TEST*******
Var: a,b,c;
Function: main
Body:

EndBody.
Function: foo
Body:
main();
If a[1] Then foo(); EndIf.
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[],([][])),FuncDecl(Id(foo)[],([][CallStmt(Id(main),[]),If(ArrayCell(Id(a),[IntLiteral(1)]),[],[CallStmt(Id(foo),[])])]))])
===========================

===========================
Testcase#378.txt
***********TEST*******
Var: a,b,c;
Function: main
Parameter: a, bn
Body:
Return a + bn - a[foo()];
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(bn))],([][Return(BinaryOp(-,BinaryOp(+,Id(a),Id(bn)),ArrayCell(Id(a),[CallExpr(Id(foo),[])])))]))])
===========================

===========================
Testcase#379.txt
***********TEST*******
Function: main
Parameter: a
Body:
a[1] = b[1] + {1,2,3} + append();
EndBody.
************SOL**********
Program([FuncDecl(Id(main)[VarDecl(Id(a))],([][Assign(ArrayCell(Id(a),[IntLiteral(1)]),BinaryOp(+,BinaryOp(+,ArrayCell(Id(b),[IntLiteral(1)]),ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3))),CallExpr(Id(append),[])))]))])
===========================

===========================
Testcase#380.txt
***********TEST*******

        Function: main
        Parameter: a, b[1][100]
        Body:
        While a<b Do
            If a > b Then doNothing(); Break;
            ElseIf !somecon() Then doSomething();
            Else Do something(); While a + foo()[100] EndDo.
            EndIf.
        EndWhile.
        EndBody.
************SOL**********
Program([FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b),[1,100])],([][While(BinaryOp(<,Id(a),Id(b)),[],[If(BinaryOp(>,Id(a),Id(b)),[],[CallStmt(Id(doNothing),[]),Break()])ElseIf(UnaryOp(!,CallExpr(Id(somecon),[])),[],[CallStmt(Id(doSomething),[])])Else([],[Dowhile([],[CallStmt(Id(something),[])],BinaryOp(+,Id(a),ArrayCell(CallExpr(Id(foo),[]),[IntLiteral(100)])))])])]))])
===========================

===========================
Testcase#381.txt
***********TEST*******
Function: main
Parameter: a, b[1][100]
Body:
While a<b Do
If a > b Then doNothing(); Break;
ElseIf !somecon() Then doSomething();
Else Do something(); While a + foo()[100] EndDo.
EndIf.
EndWhile.
EndBody.
************SOL**********
Program([FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b),[1,100])],([][While(BinaryOp(<,Id(a),Id(b)),[],[If(BinaryOp(>,Id(a),Id(b)),[],[CallStmt(Id(doNothing),[]),Break()])ElseIf(UnaryOp(!,CallExpr(Id(somecon),[])),[],[CallStmt(Id(doSomething),[])])Else([],[Dowhile([],[CallStmt(Id(something),[])],BinaryOp(+,Id(a),ArrayCell(CallExpr(Id(foo),[]),[IntLiteral(100)])))])])]))])
===========================

===========================
Testcase#382.txt
***********TEST*******

        Function: main
        Parameter: a, b[1][100]
        Body:
        While a<b Do
            If a > b Then doNothing(); Break;
            ElseIf !somecon() Then doSomething();
            ElseIf a \ 100 -20 Then Continue;
            stop();
            what();
            Else Do something(); While a + foo()[100] EndDo.
            EndIf.
        EndWhile.
        EndBody.
************SOL**********
Program([FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b),[1,100])],([][While(BinaryOp(<,Id(a),Id(b)),[],[If(BinaryOp(>,Id(a),Id(b)),[],[CallStmt(Id(doNothing),[]),Break()])ElseIf(UnaryOp(!,CallExpr(Id(somecon),[])),[],[CallStmt(Id(doSomething),[])])ElseIf(BinaryOp(-,BinaryOp(\,Id(a),IntLiteral(100)),IntLiteral(20)),[],[Continue(),CallStmt(Id(stop),[]),CallStmt(Id(what),[])])Else([],[Dowhile([],[CallStmt(Id(something),[])],BinaryOp(+,Id(a),ArrayCell(CallExpr(Id(foo),[]),[IntLiteral(100)])))])])]))])
===========================

===========================
Testcase#383.txt
***********TEST*******
Function: foo
Body:

If a > b Then doNothing(); Break;

ElseIf !somecon() Then doSomething();

ElseIf a \ 100 -20 Then Continue;
stop();

ElseIf whatever() Then 

ElseIf anything() Then Do something(); While a + foo()[100] EndDo.
EndIf.
EndBody.
Function: main
Parameter: a, b[1][100]
Body:
While a<b Do
EndWhile.
EndBody.
************SOL**********
Program([FuncDecl(Id(foo)[],([][If(BinaryOp(>,Id(a),Id(b)),[],[CallStmt(Id(doNothing),[]),Break()])ElseIf(UnaryOp(!,CallExpr(Id(somecon),[])),[],[CallStmt(Id(doSomething),[])])ElseIf(BinaryOp(-,BinaryOp(\,Id(a),IntLiteral(100)),IntLiteral(20)),[],[Continue(),CallStmt(Id(stop),[])])ElseIf(CallExpr(Id(whatever),[]),[],[])ElseIf(CallExpr(Id(anything),[]),[],[Dowhile([],[CallStmt(Id(something),[])],BinaryOp(+,Id(a),ArrayCell(CallExpr(Id(foo),[]),[IntLiteral(100)])))])])),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b),[1,100])],([][While(BinaryOp(<,Id(a),Id(b)),[],[])]))])
===========================

===========================
Testcase#384.txt
***********TEST*******

        Function: main_123_main
        Parameter: a, b[1][100]
        Body:
        While a<b Do
        EndWhile.
        EndBody.
************SOL**********
Program([FuncDecl(Id(main_123_main)[VarDecl(Id(a)),VarDecl(Id(b),[1,100])],([][While(BinaryOp(<,Id(a),Id(b)),[],[])]))])
===========================

===========================
Testcase#385.txt
***********TEST*******
Function: somwname
Body:

EndBody.
************SOL**********
Program([FuncDecl(Id(somwname)[],([][]))])
===========================

===========================
Testcase#386.txt
***********TEST*******

        Function: nothing
        Body:
        Var: a = {1238,32412, 120};
        EndBody.
        Function: foo
        Parameter: a,b,c
        Body:
        nothing(a[1][1][b[k]]);
        EndBody.
************SOL**********
Program([FuncDecl(Id(nothing)[],([VarDecl(Id(a),ArrayLiteral(IntLiteral(1238),IntLiteral(32412),IntLiteral(120)))][])),FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c))],([][CallStmt(Id(nothing),[ArrayCell(Id(a),[IntLiteral(1),IntLiteral(1),ArrayCell(Id(b),[Id(k)])])])]))])
===========================

===========================
Testcase#387.txt
***********TEST*******

        Function: foo
        Parameter: a,b,c
        Body:
        nothing(a[1][1][b[k]]);
        EndBody.
************SOL**********
Program([FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c))],([][CallStmt(Id(nothing),[ArrayCell(Id(a),[IntLiteral(1),IntLiteral(1),ArrayCell(Id(b),[Id(k)])])])]))])
===========================

===========================
Testcase#388.txt
***********TEST*******
Var: a,b,c;
Function: main
Parameter: a
Body:
While statement  Do something(); EndWhile.
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([][While(Id(statement),[],[CallStmt(Id(something),[])])]))])
===========================

===========================
Testcase#389.txt
***********TEST*******
Var: a,b,c;
Function: main
Parameter: a, b
Body:
While statement Do Break; EndWhile.
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b))],([][While(Id(statement),[],[Break()])]))])
===========================

===========================
Testcase#390.txt
***********TEST*******
Var: a,b,c;
Function: main
Parameter: a
Body:
foo(1+a, b, c)[something][whatever] = 12;
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([][Assign(ArrayCell(CallExpr(Id(foo),[BinaryOp(+,IntLiteral(1),Id(a)),Id(b),Id(c)]),[Id(something),Id(whatever)]),IntLiteral(12))]))])
===========================

===========================
Testcase#391.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        Var: a[5] = {1,4,3,2,0};
        Var: b[2][3]={{1,2,3},{4,5,6}};
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([VarDecl(Id(a),[5],ArrayLiteral(IntLiteral(1),IntLiteral(4),IntLiteral(3),IntLiteral(2),IntLiteral(0))),VarDecl(Id(b),[2,3],ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)),ArrayLiteral(IntLiteral(4),IntLiteral(5),IntLiteral(6))))][]))])
===========================

===========================
Testcase#392.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a
        Body:
        a[3 + foo(2)] = a[b[2][3]] \. -.4;
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a))],([][Assign(ArrayCell(Id(a),[BinaryOp(+,IntLiteral(3),CallExpr(Id(foo),[IntLiteral(2)]))]),BinaryOp(\.,ArrayCell(Id(a),[ArrayCell(Id(b),[IntLiteral(2),IntLiteral(3)])]),UnaryOp(-.,IntLiteral(4))))]))])
===========================

===========================
Testcase#393.txt
***********TEST*******
Var: a,b,c;
Function: main
Parameter: a, a[1][12]
Body:
Var: x[1][2] = {"ab","da"};
a[3 + foo(2)] = a[b[2][3]] + 4;
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(a),[1,12])],([VarDecl(Id(x),[1,2],ArrayLiteral(StringLiteral(ab),StringLiteral(da)))][Assign(ArrayCell(Id(a),[BinaryOp(+,IntLiteral(3),CallExpr(Id(foo),[IntLiteral(2)]))]),BinaryOp(+,ArrayCell(Id(a),[ArrayCell(Id(b),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))]))])
===========================

===========================
Testcase#394.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a, a[1][12]
        Body:
        If expr Then 
        ElseIf expr Then
        Else
        EndIf.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(a),[1,12])],([][If(Id(expr),[],[])ElseIf(Id(expr),[],[])Else([],[])]))])
===========================

===========================
Testcase#395.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a, a[1][12]
        Body:
        If expr Then 
        ElseIf expr Then
        While expr Do EndWhile.
        Do Return; While {{}} EndDo.
        Else
        EndIf.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(a),[1,12])],([][If(Id(expr),[],[])ElseIf(Id(expr),[],[While(Id(expr),[],[]),Dowhile([],[Return()],ArrayLiteral(ArrayLiteral()))])Else([],[])]))])
===========================

===========================
Testcase#396.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a, a[1][12]
        Body:
        If expr Then 
        ElseIf expr Then
        While expr Do EndWhile.
        Do Return; While {{}} EndDo.
        Else nothing(); a=(1==b+a);
        EndIf.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(a),[1,12])],([][If(Id(expr),[],[])ElseIf(Id(expr),[],[While(Id(expr),[],[]),Dowhile([],[Return()],ArrayLiteral(ArrayLiteral()))])Else([],[CallStmt(Id(nothing),[]),Assign(Id(a),BinaryOp(==,IntLiteral(1),BinaryOp(+,Id(b),Id(a))))])]))])
===========================

===========================
Testcase#397.txt
***********TEST*******
Var: a,b,c;
Function: main
Parameter: a, a[1][12]
Body:
If expr Then 
ElseIf expr Then
While expr Do EndWhile.
Do Return; While {{}} EndDo.
Else nothing(); a=b+a; Continue;
EndIf.
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(a),[1,12])],([][If(Id(expr),[],[])ElseIf(Id(expr),[],[While(Id(expr),[],[]),Dowhile([],[Return()],ArrayLiteral(ArrayLiteral()))])Else([],[CallStmt(Id(nothing),[]),Assign(Id(a),BinaryOp(+,Id(b),Id(a))),Continue()])]))])
===========================

===========================
Testcase#398.txt
***********TEST*******
Var: a,b,c;
        Function: main
        Parameter: a, a[1][12]
        Body:
        For(i=expr, a =/= {{}}, "what is that" + 1) Do
        EndFor.
        EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(a),[1,12])],([][For(Id(i),Id(expr),BinaryOp(=/=,Id(a),ArrayLiteral(ArrayLiteral())),BinaryOp(+,StringLiteral(what is that),IntLiteral(1)),[],[])]))])
===========================

===========================
Testcase#399.txt
***********TEST*******
Var: a,b,c;
Function: main
Parameter: a, a[1][12]
Body:
For(i=expr, a =/= {{}}, "what is that" + 1) Do
EndFor.
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(a),[1,12])],([][For(Id(i),Id(expr),BinaryOp(=/=,Id(a),ArrayLiteral(ArrayLiteral())),BinaryOp(+,StringLiteral(what is that),IntLiteral(1)),[],[])]))])
===========================

===========================
Testcase#400.txt
***********TEST*******
Var: a,b,c;
Function: main
Parameter: a, a[1][12]
Body:
For(i=expr, a =/= {{}}, "what is that'"" + 1) Do
Break;Continue;
EndFor.
EndBody.
************SOL**********
Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(a),[1,12])],([][For(Id(i),Id(expr),BinaryOp(=/=,Id(a),ArrayLiteral(ArrayLiteral())),BinaryOp(+,StringLiteral(what is that'"),IntLiteral(1)),[],[Break(),Continue()])]))])
===========================

===========================
Testcase#401.txt
***********TEST*******
Function: main
Body:
For (i = 0x12, a < 2, i + foo((foo()[1 + a[1 + 2]])) + 1) Do something(); EndFor.
EndBody.
************SOL**********
Program([FuncDecl(Id(main)[],([][For(Id(i),IntLiteral(18),BinaryOp(<,Id(a),IntLiteral(2)),BinaryOp(+,BinaryOp(+,Id(i),CallExpr(Id(foo),[ArrayCell(CallExpr(Id(foo),[]),[BinaryOp(+,IntLiteral(1),ArrayCell(Id(a),[BinaryOp(+,IntLiteral(1),IntLiteral(2))]))])])),IntLiteral(1)),[],[CallStmt(Id(something),[])])]))])
===========================

===========================
Testcase#402.txt
***********TEST*******
Var:x = 1, y = 0X5F, z = 0O11, k = True, z = False;
                Var: x = 1e05 , y = 1.e05 , z= 1.25 , k ="Hohoho";
                Var: x =" hehe " , y = {} , z = {1,2,3}, k ={1,{2,3},True};
************SOL**********
Program([VarDecl(Id(x),IntLiteral(1)),VarDecl(Id(y),IntLiteral(95)),VarDecl(Id(z),IntLiteral(9)),VarDecl(Id(k),BooleanLiteral(true)),VarDecl(Id(z),BooleanLiteral(false)),VarDecl(Id(x),FloatLiteral(100000.0)),VarDecl(Id(y),FloatLiteral(100000.0)),VarDecl(Id(z),FloatLiteral(1.25)),VarDecl(Id(k),StringLiteral(Hohoho)),VarDecl(Id(x),StringLiteral( hehe )),VarDecl(Id(y),ArrayLiteral()),VarDecl(Id(z),ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3))),VarDecl(Id(k),ArrayLiteral(IntLiteral(1),ArrayLiteral(IntLiteral(2),IntLiteral(3)),BooleanLiteral(true)))])
===========================
