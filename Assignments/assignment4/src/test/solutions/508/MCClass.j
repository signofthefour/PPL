.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is x I from Label0 to Label1
Label0:
	iconst_1
	istore_0
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static foo(I[I)I
.var 1 is z [I from Label0 to Label1
.var 0 is y I from Label0 to Label1
.var 2 is x I from Label0 to Label1
Label0:
	iconst_1
	istore_2
	iload_2
	istore_0
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	astore_1
Label1:
	iconst_1
	ireturn
.limit stack 5
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
