.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is y [I from Label0 to Label1
.var 1 is x I from Label0 to Label1
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
.var 2 is x I from Label0 to Label1
	iconst_1
	istore_2
Label4:
	iload_2
	invokestatic io.string_of_int(I)Ljava/lang/String;
	invokestatic io.printStrLn(Ljava/lang/String;)V
	aload_0
	iconst_1
	aload_0
	iconst_1
	iaload
	iconst_1
	iadd

	iastore
	aload_0
	iconst_1
	iaload
	bipush 10
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	goto Label4
Label5:
	return
Label1:
.limit stack 6
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
