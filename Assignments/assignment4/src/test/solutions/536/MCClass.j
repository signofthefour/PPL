.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is y [I from Label0 to Label1
.var 1 is z I from Label0 to Label1
.var 2 is x I from Label0 to Label1
Label0:
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	astore_0
	bipush 10
	istore_1
	iconst_1
	istore_2
.var 3 is z I from Label0 to Label1
	iconst_1
	istore_3
Label2:
	iload_2
	bipush 10
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_2
	invokestatic io.string_of_int(I)Ljava/lang/String;
	invokestatic io.printStrLn(Ljava/lang/String;)V
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
	return
Label1:
.limit stack 5
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
