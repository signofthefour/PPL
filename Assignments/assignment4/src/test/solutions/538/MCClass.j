.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 1 is args [Ljava/lang/String; from Label0 to Label1
.var 0 is x I from Label0 to Label1
Label0:
	iconst_1
	istore_0
	iconst_1
	iload_0
	iconst_1
	invokestatic MCClass.foo(II)I
	invokestatic MCClass.foo(II)I
	invokestatic io.string_of_int(I)Ljava/lang/String;
	invokestatic io.printStrLn(Ljava/lang/String;)V
	return
Label1:
.limit stack 8
.limit locals 2
.end method

.method public static foo(II)I
.var 1 is y I from Label0 to Label1
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 2
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

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
