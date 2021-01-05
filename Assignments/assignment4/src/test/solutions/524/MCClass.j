.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is x I from Label0 to Label1
Label0:
	iconst_1
	istore_0
	iload_0
	invokestatic MCClass.foo(I)V
	ldc "abs"
	invokestatic io.printStrLn(Ljava/lang/String;)V
	return
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static foo(I)V
.var 0 is z I from Label0 to Label1
.var 1 is y Z from Label0 to Label1
.var 2 is x I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_1
	istore_2
	ldc "abs"
	invokestatic io.printStrLn(Ljava/lang/String;)V
	return
Label1:
.limit stack 2
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
