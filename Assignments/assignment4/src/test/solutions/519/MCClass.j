.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is x I from Label0 to Label1
Label0:
	iconst_1
	istore_0
	return
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static foo(Z)I
.var 0 is z Z from Label0 to Label1
.var 1 is y Z from Label0 to Label1
.var 2 is x I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_1
	istore_2
Label2:
	iload_0
	ifle Label3
.var 3 is x F from Label0 to Label1
	iconst_0
	istore_1
	goto Label3
	goto Label2
Label3:
	iconst_1
	ireturn
Label1:
.limit stack 3
.limit locals 4
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
