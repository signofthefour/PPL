339
343
350
351
352
353
354
355
356
357
358
340
359
360
361
363
364
365
366
367
368
341
LINE: Program([FuncDecl(Id(foo)[VarDecl(Id(n))],([][Assign(Id(c),Id(a))]))])
EXPC: Program([FuncDecl(Id(foo)[VarDecl(Id(n))],([][Assign(Id(c),UnaryOp(-.,Id(a)))]))])
369
370
371
372
373
374
375
376
377
378
342
379
380
381
382
383
384
385
386
387
388
344
389
390
391
392
393
395
396
397
398
345
399
346
347
348
329
330
334
335
331
326
327
327
328
336
332
333
318
319
323
324
309
310
312
313
314
315
316
LINE: Program([FuncDecl(Id(foo)[VarDecl(Id(a))],([][Assign(Id(x),IntLiteral(3))]))])
EXPC: Program([FuncDecl(Id(foo)[VarDecl(Id(a))],([][Assign(Id(x),UnaryOp(-,IntLiteral(3)))]))])
317
326
337
338
300
301
302
303
304
305
306
307
308
Program([VarDecl(Id(b),BooleanLiteral(true)),VarDecl(Id(c),BooleanLiteral(false))])
311
322
325
Tests run  97
Errors  [(<ASTGenSuite.ASTGenSuite testMethod=test_21>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 683, in test_21\n    self.assertTrue(TestAST.checkASTGen(input,expect,360))\n  File "./test/TestUtils.py", line 99, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/nguyendat/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 437, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 12, in visitProgram\n    funcs_decls = list(reduce(lambda y,x: y + [self.visitFunction_declare(x)], [item for item in ctx.function_declare()], []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 12, in <lambda>\n    funcs_decls = list(reduce(lambda y,x: y + [self.visitFunction_declare(x)], [item for item in ctx.function_declare()], []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 21, in visitFunction_declare\n    stmt = list(reduce(lambda y, x: y + [self.visitStmt(x)], ctx.stmt(), []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 21, in <lambda>\n    stmt = list(reduce(lambda y, x: y + [self.visitStmt(x)], ctx.stmt(), []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 88, in visitStmt\n    return self.visitAssign_stmt(ctx.assign_stmt())\n  File "./main/bkit/astgen/ASTGeneration.py", line 142, in visitAssign_stmt\n    rhs = self.visitExpr(ctx.expr())\n  File "./main/bkit/astgen/ASTGeneration.py", line 177, in visitExpr\n    return self.visitExpr1(ctx.expr1(0))\n  File "./main/bkit/astgen/ASTGeneration.py", line 182, in visitExpr1\n    if ctx.BIN_LOGICAL_OP():\nAttributeError: \'NoneType\' object has no attribute \'BIN_LOGICAL_OP\'\n')]
[(<ASTGenSuite.ASTGenSuite testMethod=test_3>,
  'Traceback (most recent call last):\n'
  '  File "./test/ASTGenSuite.py", line 478, in test_3\n'
  '    self.assertTrue(TestAST.checkASTGen(input,expect,341))\n'
  'AssertionError: False is not true\n'),
 (<ASTGenSuite.ASTGenSuite testMethod=test_func_declare6>,
  'Traceback (most recent call last):\n'
  '  File "./test/ASTGenSuite.py", line 148, in test_func_declare6\n'
  '    self.assertTrue(TestAST.checkASTGen(input,expect,316))\n'
  'AssertionError: False is not true\n')]
Test output
 .............E.......F..........................................................F................
======================================================================
ERROR: test_21 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 683, in test_21
    self.assertTrue(TestAST.checkASTGen(input,expect,360))
  File "./test/TestUtils.py", line 99, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/nguyendat/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 437, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 12, in visitProgram
    funcs_decls = list(reduce(lambda y,x: y + [self.visitFunction_declare(x)], [item for item in ctx.function_declare()], []))
  File "./main/bkit/astgen/ASTGeneration.py", line 12, in <lambda>
    funcs_decls = list(reduce(lambda y,x: y + [self.visitFunction_declare(x)], [item for item in ctx.function_declare()], []))
  File "./main/bkit/astgen/ASTGeneration.py", line 21, in visitFunction_declare
    stmt = list(reduce(lambda y, x: y + [self.visitStmt(x)], ctx.stmt(), []))
  File "./main/bkit/astgen/ASTGeneration.py", line 21, in <lambda>
    stmt = list(reduce(lambda y, x: y + [self.visitStmt(x)], ctx.stmt(), []))
  File "./main/bkit/astgen/ASTGeneration.py", line 88, in visitStmt
    return self.visitAssign_stmt(ctx.assign_stmt())
  File "./main/bkit/astgen/ASTGeneration.py", line 142, in visitAssign_stmt
    rhs = self.visitExpr(ctx.expr())
  File "./main/bkit/astgen/ASTGeneration.py", line 177, in visitExpr
    return self.visitExpr1(ctx.expr1(0))
  File "./main/bkit/astgen/ASTGeneration.py", line 182, in visitExpr1
    if ctx.BIN_LOGICAL_OP():
AttributeError: 'NoneType' object has no attribute 'BIN_LOGICAL_OP'

======================================================================
FAIL: test_3 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 478, in test_3
    self.assertTrue(TestAST.checkASTGen(input,expect,341))
AssertionError: False is not true

======================================================================
FAIL: test_func_declare6 (ASTGenSuite.ASTGenSuite)
Simple program: int main() {}
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 148, in test_func_declare6
    self.assertTrue(TestAST.checkASTGen(input,expect,316))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 97 tests in 2.844s

FAILED (failures=2, errors=1)

