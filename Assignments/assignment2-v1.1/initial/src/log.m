Tests run  100
Errors  [(<ASTGenSuite.ASTGenSuite testMethod=test_371>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 948, in test_371\n    self.assertTrue(TestAST.checkASTGen(input,expect,371))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_380>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 1018, in test_380\n    self.assertTrue(TestAST.checkASTGen(input,expect,380))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1310, in accept\n    return visitor.visitAssign_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 111, in visitAssign_stmt\n    lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())\nAttributeError: \'ASTGeneration\' object has no attribute \'index_op\'\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_382>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 1030, in test_382\n    self.assertTrue(TestAST.checkASTGen(input,expect,382))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1310, in accept\n    return visitor.visitAssign_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 111, in visitAssign_stmt\n    lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())\nAttributeError: \'ASTGeneration\' object has no attribute \'index_op\'\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_assignment_statement_10>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 129, in test_assignment_statement_10\n    self.assertTrue(TestAST.checkASTGen(input,expect,310))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1310, in accept\n    return visitor.visitAssign_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 111, in visitAssign_stmt\n    lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())\nAttributeError: \'ASTGeneration\' object has no attribute \'index_op\'\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_assignment_statement_11>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 142, in test_assignment_statement_11\n    self.assertTrue(TestAST.checkASTGen(input,expect,311))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1310, in accept\n    return visitor.visitAssign_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 111, in visitAssign_stmt\n    lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())\nAttributeError: \'ASTGeneration\' object has no attribute \'index_op\'\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_assignment_statement_2>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 25, in test_assignment_statement_2\n    self.assertTrue(TestAST.checkASTGen(input,expect,302))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1310, in accept\n    return visitor.visitAssign_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 111, in visitAssign_stmt\n    lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())\nAttributeError: \'ASTGeneration\' object has no attribute \'index_op\'\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_assignment_statement_7>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 86, in test_assignment_statement_7\n    self.assertTrue(TestAST.checkASTGen(input,expect,307))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1310, in accept\n    return visitor.visitAssign_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 111, in visitAssign_stmt\n    lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())\nAttributeError: \'ASTGeneration\' object has no attribute \'index_op\'\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_assignment_statement_9>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 116, in test_assignment_statement_9\n    self.assertTrue(TestAST.checkASTGen(input,expect,309))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_break_statement_2>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 200, in test_break_statement_2\n    self.assertTrue(TestAST.checkASTGen(input,expect,314))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1489, in accept\n    return visitor.visitWhile_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 129, in visitWhile_stmt\n    sl   = self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_continue_statement_3>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 316, in test_continue_statement_3\n    self.assertTrue(TestAST.checkASTGen(input,expect,323))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1408, in accept\n    return visitor.visitFor_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 122, in visitFor_stmt\n    loop  = self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_do_while_statement_3>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 365, in test_do_while_statement_3\n    self.assertTrue(TestAST.checkASTGen(input,expect,327))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1554, in accept\n    return visitor.visitDo_while_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 137, in visitDo_while_stmt\n    sl   = self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1554, in accept\n    return visitor.visitDo_while_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 137, in visitDo_while_stmt\n    sl   = self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_do_while_statement_5>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 406, in test_do_while_statement_5\n    self.assertTrue(TestAST.checkASTGen(input,expect,329))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1554, in accept\n    return visitor.visitDo_while_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 137, in visitDo_while_stmt\n    sl   = self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_for_statement_10>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 582, in test_for_statement_10\n    self.assertTrue(TestAST.checkASTGen(input,expect,963))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1408, in accept\n    return visitor.visitFor_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 122, in visitFor_stmt\n    loop  = self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 59, in visitStm_list\n    decl_inter  = [i for i in ctx.var_declare()]\nAttributeError: \'NoneType\' object has no attribute \'var_declare\'\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_for_statement_5>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 514, in test_for_statement_5\n    self.assertTrue(TestAST.checkASTGen(input,expect,961))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1408, in accept\n    return visitor.visitFor_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 122, in visitFor_stmt\n    loop  = self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_for_statement_8>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 557, in test_for_statement_8\n    self.assertTrue(TestAST.checkASTGen(input,expect,337))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1408, in accept\n    return visitor.visitFor_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 122, in visitFor_stmt\n    loop  = self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1408, in accept\n    return visitor.visitFor_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 122, in visitFor_stmt\n    loop  = self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1310, in accept\n    return visitor.visitAssign_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 111, in visitAssign_stmt\n    lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())\nAttributeError: \'ASTGeneration\' object has no attribute \'index_op\'\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_full_program_1>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 614, in test_full_program_1\n    self.assertTrue(TestAST.checkASTGen(input,expect,920))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1408, in accept\n    return visitor.visitFor_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 122, in visitFor_stmt\n    loop  = self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1554, in accept\n    return visitor.visitDo_while_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 137, in visitDo_while_stmt\n    sl   = self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1489, in accept\n    return visitor.visitWhile_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 129, in visitWhile_stmt\n    sl   = self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1310, in accept\n    return visitor.visitAssign_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 111, in visitAssign_stmt\n    lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())\nAttributeError: \'ASTGeneration\' object has no attribute \'index_op\'\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_full_program_2>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 649, in test_full_program_2\n    self.assertTrue(TestAST.checkASTGen(input,expect,339))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_if_statement_1>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 712, in test_if_statement_1\n    self.assertTrue(TestAST.checkASTGen(input,expect,351))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_if_statement_10>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 843, in test_if_statement_10\n    self.assertTrue(TestAST.checkASTGen(input,expect,360))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 104, in visitIf_stmt\n    stm_lst = [self.visitStm_list(i) for i in ctx.stm_list()]\n  File "./main/bkit/astgen/ASTGeneration.py", line 104, in <listcomp>\n    stm_lst = [self.visitStm_list(i) for i in ctx.stm_list()]\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_if_statement_11>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 866, in test_if_statement_11\n    self.assertTrue(TestAST.checkASTGen(input,expect,362))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_if_statement_12>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 879, in test_if_statement_12\n    self.assertTrue(TestAST.checkASTGen(input,expect,366))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_if_statement_2>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 727, in test_if_statement_2\n    self.assertTrue(TestAST.checkASTGen(input,expect,352))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_if_statement_3>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 742, in test_if_statement_3\n    self.assertTrue(TestAST.checkASTGen(input,expect,353))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 104, in visitIf_stmt\n    stm_lst = [self.visitStm_list(i) for i in ctx.stm_list()]\n  File "./main/bkit/astgen/ASTGeneration.py", line 104, in <listcomp>\n    stm_lst = [self.visitStm_list(i) for i in ctx.stm_list()]\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 104, in visitIf_stmt\n    stm_lst = [self.visitStm_list(i) for i in ctx.stm_list()]\n  File "./main/bkit/astgen/ASTGeneration.py", line 104, in <listcomp>\n    stm_lst = [self.visitStm_list(i) for i in ctx.stm_list()]\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_if_statement_4>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 757, in test_if_statement_4\n    self.assertTrue(TestAST.checkASTGen(input,expect,354))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BooleanLiteral\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_if_statement_5>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 769, in test_if_statement_5\n    self.assertTrue(TestAST.checkASTGen(input,expect,355))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BooleanLiteral\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_if_statement_6>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 780, in test_if_statement_6\n    self.assertTrue(TestAST.checkASTGen(input,expect,356))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BooleanLiteral\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_if_statement_7>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 793, in test_if_statement_7\n    self.assertTrue(TestAST.checkASTGen(input,expect,357))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_if_statement_8>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 808, in test_if_statement_8\n    self.assertTrue(TestAST.checkASTGen(input,expect,358))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_if_statement_9>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 824, in test_if_statement_9\n    self.assertTrue(TestAST.checkASTGen(input,expect,359))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 104, in visitIf_stmt\n    stm_lst = [self.visitStm_list(i) for i in ctx.stm_list()]\n  File "./main/bkit/astgen/ASTGeneration.py", line 104, in <listcomp>\n    stm_lst = [self.visitStm_list(i) for i in ctx.stm_list()]\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_while_statement_10>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 1305, in test_while_statement_10\n    self.assertTrue(TestAST.checkASTGen(input,expect,409))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1489, in accept\n    return visitor.visitWhile_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 129, in visitWhile_stmt\n    sl   = self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_while_statement_2>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 1170, in test_while_statement_2\n    self.assertTrue(TestAST.checkASTGen(input,expect,400))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1489, in accept\n    return visitor.visitWhile_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 129, in visitWhile_stmt\n    sl   = self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_while_statement_4>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 1196, in test_while_statement_4\n    self.assertTrue(TestAST.checkASTGen(input,expect,403))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1489, in accept\n    return visitor.visitWhile_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 129, in visitWhile_stmt\n    sl   = self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept\n    return visitor.visitIf_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\n  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>\n    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]\nTypeError: list indices must be integers or slices, not BinaryOp\n'), (<ASTGenSuite.ASTGenSuite testMethod=test_while_statement_8>, 'Traceback (most recent call last):\n  File "./test/ASTGenSuite.py", line 1271, in test_while_statement_8\n    self.assertTrue(TestAST.checkASTGen(input,expect,407))\n  File "./test/TestUtils.py", line 98, in checkASTGen\n    asttree = ASTGeneration().visit(tree)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit\n    return tree.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept\n    return visitor.visitProgram(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>\n    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare\n    body    = self.visitFunc_body(ctx.func_body())\n  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body\n    return  self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1489, in accept\n    return visitor.visitWhile_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 129, in visitWhile_stmt\n    sl   = self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1408, in accept\n    return visitor.visitFor_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 122, in visitFor_stmt\n    loop  = self.visitStm_list(ctx.stm_list())\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>\n    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))\n  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm\n    return self.visitChildren(ctx)\n  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren\n    childResult = c.accept(self)\n  File "../target/main/bkit/parser/BKITParser.py", line 1310, in accept\n    return visitor.visitAssign_stmt(self)\n  File "./main/bkit/astgen/ASTGeneration.py", line 111, in visitAssign_stmt\n    lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())\nAttributeError: \'ASTGeneration\' object has no attribute \'index_op\'\n')]
[]
Test output
 .....E........EE...EE..E....E.E.E.......E..E.E...E...E..E.EE.....EEEEEEEEEEEE..............EE.E...E.
======================================================================
ERROR: test_371 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 948, in test_371
    self.assertTrue(TestAST.checkASTGen(input,expect,371))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_380 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 1018, in test_380
    self.assertTrue(TestAST.checkASTGen(input,expect,380))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1310, in accept
    return visitor.visitAssign_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 111, in visitAssign_stmt
    lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())
AttributeError: 'ASTGeneration' object has no attribute 'index_op'

======================================================================
ERROR: test_382 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 1030, in test_382
    self.assertTrue(TestAST.checkASTGen(input,expect,382))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1310, in accept
    return visitor.visitAssign_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 111, in visitAssign_stmt
    lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())
AttributeError: 'ASTGeneration' object has no attribute 'index_op'

======================================================================
ERROR: test_assignment_statement_10 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 129, in test_assignment_statement_10
    self.assertTrue(TestAST.checkASTGen(input,expect,310))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1310, in accept
    return visitor.visitAssign_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 111, in visitAssign_stmt
    lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())
AttributeError: 'ASTGeneration' object has no attribute 'index_op'

======================================================================
ERROR: test_assignment_statement_11 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 142, in test_assignment_statement_11
    self.assertTrue(TestAST.checkASTGen(input,expect,311))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1310, in accept
    return visitor.visitAssign_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 111, in visitAssign_stmt
    lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())
AttributeError: 'ASTGeneration' object has no attribute 'index_op'

======================================================================
ERROR: test_assignment_statement_2 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 25, in test_assignment_statement_2
    self.assertTrue(TestAST.checkASTGen(input,expect,302))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1310, in accept
    return visitor.visitAssign_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 111, in visitAssign_stmt
    lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())
AttributeError: 'ASTGeneration' object has no attribute 'index_op'

======================================================================
ERROR: test_assignment_statement_7 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 86, in test_assignment_statement_7
    self.assertTrue(TestAST.checkASTGen(input,expect,307))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1310, in accept
    return visitor.visitAssign_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 111, in visitAssign_stmt
    lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())
AttributeError: 'ASTGeneration' object has no attribute 'index_op'

======================================================================
ERROR: test_assignment_statement_9 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 116, in test_assignment_statement_9
    self.assertTrue(TestAST.checkASTGen(input,expect,309))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_break_statement_2 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 200, in test_break_statement_2
    self.assertTrue(TestAST.checkASTGen(input,expect,314))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1489, in accept
    return visitor.visitWhile_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 129, in visitWhile_stmt
    sl   = self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_continue_statement_3 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 316, in test_continue_statement_3
    self.assertTrue(TestAST.checkASTGen(input,expect,323))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1408, in accept
    return visitor.visitFor_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 122, in visitFor_stmt
    loop  = self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_do_while_statement_3 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 365, in test_do_while_statement_3
    self.assertTrue(TestAST.checkASTGen(input,expect,327))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1554, in accept
    return visitor.visitDo_while_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 137, in visitDo_while_stmt
    sl   = self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1554, in accept
    return visitor.visitDo_while_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 137, in visitDo_while_stmt
    sl   = self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_do_while_statement_5 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 406, in test_do_while_statement_5
    self.assertTrue(TestAST.checkASTGen(input,expect,329))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1554, in accept
    return visitor.visitDo_while_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 137, in visitDo_while_stmt
    sl   = self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_for_statement_10 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 582, in test_for_statement_10
    self.assertTrue(TestAST.checkASTGen(input,expect,963))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1408, in accept
    return visitor.visitFor_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 122, in visitFor_stmt
    loop  = self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 59, in visitStm_list
    decl_inter  = [i for i in ctx.var_declare()]
AttributeError: 'NoneType' object has no attribute 'var_declare'

======================================================================
ERROR: test_for_statement_5 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 514, in test_for_statement_5
    self.assertTrue(TestAST.checkASTGen(input,expect,961))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1408, in accept
    return visitor.visitFor_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 122, in visitFor_stmt
    loop  = self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_for_statement_8 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 557, in test_for_statement_8
    self.assertTrue(TestAST.checkASTGen(input,expect,337))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1408, in accept
    return visitor.visitFor_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 122, in visitFor_stmt
    loop  = self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1408, in accept
    return visitor.visitFor_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 122, in visitFor_stmt
    loop  = self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1310, in accept
    return visitor.visitAssign_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 111, in visitAssign_stmt
    lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())
AttributeError: 'ASTGeneration' object has no attribute 'index_op'

======================================================================
ERROR: test_full_program_1 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 614, in test_full_program_1
    self.assertTrue(TestAST.checkASTGen(input,expect,920))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1408, in accept
    return visitor.visitFor_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 122, in visitFor_stmt
    loop  = self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1554, in accept
    return visitor.visitDo_while_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 137, in visitDo_while_stmt
    sl   = self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1489, in accept
    return visitor.visitWhile_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 129, in visitWhile_stmt
    sl   = self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1310, in accept
    return visitor.visitAssign_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 111, in visitAssign_stmt
    lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())
AttributeError: 'ASTGeneration' object has no attribute 'index_op'

======================================================================
ERROR: test_full_program_2 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 649, in test_full_program_2
    self.assertTrue(TestAST.checkASTGen(input,expect,339))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_if_statement_1 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 712, in test_if_statement_1
    self.assertTrue(TestAST.checkASTGen(input,expect,351))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_if_statement_10 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 843, in test_if_statement_10
    self.assertTrue(TestAST.checkASTGen(input,expect,360))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 104, in visitIf_stmt
    stm_lst = [self.visitStm_list(i) for i in ctx.stm_list()]
  File "./main/bkit/astgen/ASTGeneration.py", line 104, in <listcomp>
    stm_lst = [self.visitStm_list(i) for i in ctx.stm_list()]
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_if_statement_11 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 866, in test_if_statement_11
    self.assertTrue(TestAST.checkASTGen(input,expect,362))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_if_statement_12 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 879, in test_if_statement_12
    self.assertTrue(TestAST.checkASTGen(input,expect,366))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_if_statement_2 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 727, in test_if_statement_2
    self.assertTrue(TestAST.checkASTGen(input,expect,352))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_if_statement_3 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 742, in test_if_statement_3
    self.assertTrue(TestAST.checkASTGen(input,expect,353))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 104, in visitIf_stmt
    stm_lst = [self.visitStm_list(i) for i in ctx.stm_list()]
  File "./main/bkit/astgen/ASTGeneration.py", line 104, in <listcomp>
    stm_lst = [self.visitStm_list(i) for i in ctx.stm_list()]
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 104, in visitIf_stmt
    stm_lst = [self.visitStm_list(i) for i in ctx.stm_list()]
  File "./main/bkit/astgen/ASTGeneration.py", line 104, in <listcomp>
    stm_lst = [self.visitStm_list(i) for i in ctx.stm_list()]
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_if_statement_4 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 757, in test_if_statement_4
    self.assertTrue(TestAST.checkASTGen(input,expect,354))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BooleanLiteral

======================================================================
ERROR: test_if_statement_5 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 769, in test_if_statement_5
    self.assertTrue(TestAST.checkASTGen(input,expect,355))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BooleanLiteral

======================================================================
ERROR: test_if_statement_6 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 780, in test_if_statement_6
    self.assertTrue(TestAST.checkASTGen(input,expect,356))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BooleanLiteral

======================================================================
ERROR: test_if_statement_7 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 793, in test_if_statement_7
    self.assertTrue(TestAST.checkASTGen(input,expect,357))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_if_statement_8 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 808, in test_if_statement_8
    self.assertTrue(TestAST.checkASTGen(input,expect,358))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_if_statement_9 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 824, in test_if_statement_9
    self.assertTrue(TestAST.checkASTGen(input,expect,359))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 104, in visitIf_stmt
    stm_lst = [self.visitStm_list(i) for i in ctx.stm_list()]
  File "./main/bkit/astgen/ASTGeneration.py", line 104, in <listcomp>
    stm_lst = [self.visitStm_list(i) for i in ctx.stm_list()]
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_while_statement_10 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 1305, in test_while_statement_10
    self.assertTrue(TestAST.checkASTGen(input,expect,409))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1489, in accept
    return visitor.visitWhile_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 129, in visitWhile_stmt
    sl   = self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_while_statement_2 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 1170, in test_while_statement_2
    self.assertTrue(TestAST.checkASTGen(input,expect,400))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1489, in accept
    return visitor.visitWhile_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 129, in visitWhile_stmt
    sl   = self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_while_statement_4 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 1196, in test_while_statement_4
    self.assertTrue(TestAST.checkASTGen(input,expect,403))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1489, in accept
    return visitor.visitWhile_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 129, in visitWhile_stmt
    sl   = self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1221, in accept
    return visitor.visitIf_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in visitIf_stmt
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
  File "./main/bkit/astgen/ASTGeneration.py", line 105, in <listcomp>
    ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in exp_lst]
TypeError: list indices must be integers or slices, not BinaryOp

======================================================================
ERROR: test_while_statement_8 (ASTGenSuite.ASTGenSuite)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./test/ASTGenSuite.py", line 1271, in test_while_statement_8
    self.assertTrue(TestAST.checkASTGen(input,expect,407))
  File "./test/TestUtils.py", line 98, in checkASTGen
    asttree = ASTGeneration().visit(tree)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 34, in visit
    return tree.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 401, in accept
    return visitor.visitProgram(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in visitProgram
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 15, in <lambda>
    func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 45, in visitFunc_declare
    body    = self.visitFunc_body(ctx.func_body())
  File "./main/bkit/astgen/ASTGeneration.py", line 54, in visitFunc_body
    return  self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1489, in accept
    return visitor.visitWhile_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 129, in visitWhile_stmt
    sl   = self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1408, in accept
    return visitor.visitFor_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 122, in visitFor_stmt
    loop  = self.visitStm_list(ctx.stm_list())
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in visitStm_list
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 63, in <lambda>
    stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
  File "./main/bkit/astgen/ASTGeneration.py", line 71, in visitStm
    return self.visitChildren(ctx)
  File "/home/khanh/.local/lib/python3.8/site-packages/antlr4/tree/Tree.py", line 44, in visitChildren
    childResult = c.accept(self)
  File "../target/main/bkit/parser/BKITParser.py", line 1310, in accept
    return visitor.visitAssign_stmt(self)
  File "./main/bkit/astgen/ASTGeneration.py", line 111, in visitAssign_stmt
    lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())
AttributeError: 'ASTGeneration' object has no attribute 'index_op'

----------------------------------------------------------------------
Ran 100 tests in 1.176s

FAILED (errors=33)

