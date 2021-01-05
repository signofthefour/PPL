.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is x [I from Label0 to Label1
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
	aload_0
	iconst_0
	iaload
	iconst_2
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label2
	aload_0
	iconst_1
	iconst_5

	iastore
	goto Label4
Label2:
	aload_0
	iconst_1
	iaload
	iconst_4
	if_icmple Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label3
	aload_0
	iconst_1
	bipush 10

	iastore
	return
	goto Label4
Label3:
	aload_0
	iconst_1
	iconst_3

	iastore
Label4:
	aload_0
	iconst_1
	iaload
	invokestatic io.string_of_int(I)Ljava/lang/String;
	invokestatic io.printStrLn(Ljava/lang/String;)V
	return
Label1:
.limit stack 7
.limit locals 1
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
