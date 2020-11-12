from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
# from AST_GEN_TEST import *
from functools import reduce

class ASTGeneration(BKITVisitor):

    def visitProgram(self,ctx:BKITParser.ProgramContext):
        var_decls = list(reduce(lambda y,x: y + self.visitVar_declare(x), [item for item in ctx.var_declare()], []))
        funcs_decls = list(reduce(lambda y,x: y + self.visitFunction_declare(x), [item for item in ctx.function_declare()], []))
        return Program(var_decls + funcs_decls)


    # Visit a parse tree produced by BKITParser#function_declare.
    def visitFunction_declare(self, ctx:BKITParser.Function_declareContext):
        funcName = Id(ctx.ID().getText())
        params = self.visitParams_list(ctx.params_list())
        declare = list(reduce(lambda y, x: y + self.visitVar_declare_stmt(x), ctx.var_declare_stmt(), []))
        stmt = list(reduce(lambda y, x: y + self.visitStmt(x), ctx.stmt(), []))
        return [FuncDecl(funcName, params, tuple((declare,stmt)))]


    # Visit a parse tree produced by BKITParser#primitive_data.
    def visitPrimitive_data(self, ctx:BKITParser.Primitive_dataContext):
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText()))
        if ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        if ctx.STRING_LIT():
            return StringLiteral(str(ctx.STRING_LIT().getText()))
        if ctx.BOOL_LIT():
            return BooleanLiteral(bool(ctx.BOOL_LIT().getText()))


    # Visit a parse tree produced by BKITParser#array_lit.
    def visitArray_lit(self, ctx:BKITParser.Array_litContext):
        if ctx.primitive_data():
            return ArrayLiteral(list(map(lambda datum: self.visitPrimitive_data(datum), ctx.primitive_data())))
        else:
            return ArrayLiteral(list(map(lambda datum: self.visitArray_lit(datum), ctx.array_lit())))


    # Visit a parse tree produced by BKITParser#var_list.
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        var_non_init = list(map(lambda decl: self.visitVar_non_init(decl), ctx.var_non_init()))
        var_init = list(map(lambda decl: self.visitVar_init(decl), ctx.var_init()))
        return var_non_init + var_init

    # Visit a parse tree produced by BKITParser#var_non_init.
    def visitVar_non_init(self, ctx:BKITParser.Var_non_initContext):
        if ctx.getChildCount() == 1:
            decl = VarDecl(Id(ctx.ID().getText()), [], None)
            if isinstance(decl, VarDecl):
                return decl
        else:
            dim = map(lambda x: int(x), [lit.getText() for lit in ctx.INT_LIT()])
            decl = VarDecl(Id(ctx.ID().getText()), dim, None)
            if isinstance(decl, VarDecl):
                return decl


    # Visit a parse tree produced by BKITParser#var_init.
    def visitVar_init(self, ctx:BKITParser.Var_initContext):
        if ctx.LEFT_BRACKET():
            dim = map(lambda x: int(x), [lit.getText() for lit in ctx.INT_LIT()])
            decl = VarDecl(Id(ctx.ID().getText()), dim, self.visitArray_lit(ctx.array_lit()))
            if isinstance(decl, VarDecl):
                return decl
        else:
            decl = VarDecl(Id(ctx.ID().getText()), [], self.visitPrimitive_data(ctx.primitive_data()))
            if isinstance(decl, VarDecl):
                return decl


    # Visit a parse tree produced by BKITParser#params_list.
    def visitParams_list(self, ctx:BKITParser.Params_listContext):
        params_list =  [self.visitVar_non_init(x) for x in ctx.var_non_init()]
        return params_list


    # Visit a parse tree produced by BKITParser#stmt_list.
    def visitStmt_list(self, ctx:BKITParser.Stmt_listContext):
        declare = reduce(lambda y, x: y + self.visitVar_declare_stmt(x), ctx.var_declare_stmt(), [])
        stmt = reduce(lambda y, x: y + self.visitStmt(x), ctx.stmt(), [])
        return list(declare), list(stmt)

    def visitStmt(self, ctx:BKITParser.StmtContext):
        if ctx.if_stmt():
            return self.visitIf_stmt(ctx.if_stmt())
        if ctx.for_stmt():
            return self.visitFor_stmt(ctx.for_stmt())
        if ctx.while_stmt():
            return self.visitWhile_stmt(ctx.while_stmt())
        if ctx.dowhile_stmt():
            return self.visitDowhile_stmt(ctx.dowhile_stmt())
        if ctx.assign_stmt():
            return self.visitAssign_stmt(ctx.assign_stmt())
        if ctx.break_stmt():
            return self.visitBreak_stmt(ctx.break_stmt())
        if ctx.continue_stmt():
            return self.visitContinue_stmt(ctx.continue_stmt())
        if ctx.call_stmt():
            return self.visitCall_stmt(ctx.call_stmt())
        if ctx.return_stmt():
            return self.visitReturn_stmt(ctx.return_stmt())

    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        if_then_stmt = []
        else_stmt = []
        num_of_expr = len(ctx.expr())
        for idx in range(num_of_expr):
            expr = self.visitExpr(ctx.expr(idx))
            if ctx.stmt_list(idx):
                var_decls, stmt_list = self.visitStmt_list(ctx.stmt_list(idx))
            else:
                var_decls, stmt_list = [], []
            if_then_stmt += [tuple((expr, var_decls, stmt_list))]
        else_stmt = tuple(())
        if ctx.ELSE():
            var_decls, stmt_list = self.visitStmt_list(ctx.stmt_list(num_of_expr))
            else_stmt = tuple(var_decls, stmt_list)
        return [If(if_then_stmt, else_stmt)]


    # Visit a parse tree produced by BKITParser#for_stmt.
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        iter_var = ctx.ID().getText()
        expr1 = self.visitExpr(ctx.expr(0))
        expr2 = self.visitExpr(ctx.expr(1))
        expr3 = self.visitExpr(ctx.expr(2))
        loop = tuple(self.visitStmt_list(ctx.stmt_list()))
        return [For(iter_var, expr1, expr2, expr3, loop)]

    # Visit a parse tree produced by BKITParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        expr = self.visitExpr(ctx.expr())
        sl = self.visitStmt_list(tuple(ctx.stmt_list()))
        return [While(expr, sl)]

    # Visit a parse tree produced by BKITParser#dowhile_stmt.
    def visitDowhile_stmt(self, ctx:BKITParser.Dowhile_stmtContext):
        expr = self.visitExpr(ctx.expr())
        sl = self.visitStmt_list(tuple(ctx.stmt_list()))
        return [DoWhile(sl, expr)]

    # Visit a parse tree produced by BKITParser#assign_stmt
    def visitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        lhs = None
        if ctx.ID():
            lhs = Id(ctx.ID().getText())
        else:
            lhs = self.visitArray_cell(ctx.array_cell())
        rhs = self.visitExpr(ctx.expr())
        return [Assign(lhs, rhs)]

    # Visit a parse tree produced by BKITParser#array_cell.
    def visitArray_cell(self, ctx:BKITParser.Array_cellContext):
        expr_list = list(map(lambda x: self.visitExpr(x), ctx.expr()))
        return ArrayCell(expr_list[0], expr_list[1:])

    # Visit a parse tree produced by BKITParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return [Break()]

    # Visit a parse tree produced by BKITParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return [Continue()]


    # Visit a parse tree produced by BKITParser#call_stmt.
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        return self.visitFunction_call(ctx)


    # Visit a parse tree produced by BKITParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        return [Return(self.visitExpr(ctx.expr()))]

    # Visit a parse tree produced by BKITParser#expr.
    def visitExpr(self, ctx:BKITParser.ExprContext):
        if ctx.REL_OP():
            return BinaryOp(ctx.REL_OP().getText(), self.visitExpr1(ctx.expr1(0)), self.visitExpr1(ctx.expr1(1)))
        return self.visitExpr1(ctx.expr1(0))


    # Visit a parse tree produced by BKITParser#expr1.
    def visitExpr1(self, ctx:BKITParser.Expr1Context):
        if ctx.BIN_LOGICAL_OP():
            return BinaryOp(ctx.BIN_LOGICAL_OP().getText(), self.visitExpr1(ctx.expr1()), self.visitExpr2(ctx.expr2()))
        return self.visitExpr2(ctx.expr2())


    # Visit a parse tree produced by BKITParser#expr2.
    def visitExpr2(self, ctx:BKITParser.Expr2Context):
        if ctx.ADD_OP():
            return BinaryOp(ctx.ADD_OP().getText(), self.visitExpr2(ctx.expr2()), self.visitExpr3(ctx.expr3()))
        return self.visitExpr3(ctx.expr3())


    # Visit a parse tree produced by BKITParser#expr3.
    def visitExpr3(self, ctx:BKITParser.Expr3Context):
        if ctx.MUL_OP():
            return  BinaryOp(ctx.MUL_OP().getText(), self.visitExpr3(ctx.expr3()), self.visitExpr4(ctx.expr4()))
        return self.visitExpr4(ctx.expr4())


    # Visit a parse tree produced by BKITParser#expr4.
    def visitExpr4(self, ctx:BKITParser.Expr4Context):
        if ctx.UN_LOGICAL_OP():
            return UnaryOp(ctx.UN_LOGICAL_OP().getText(), self.visitExpr4(ctx.expr4()))
        return self.visitExpr5(ctx.expr5())


    # Visit a parse tree produced by BKITParser#expr5.
    def visitExpr5(self, ctx:BKITParser.Expr5Context):
        if ctx.UN_OP():
            return UnaryOp(ctx.UN_OP().getText(), self.visitExpr5(ctx.expr5()))
        return self.visitExpr6(ctx.expr6())


    # Visit a parse tree produced by BKITParser#expr6.
    def visitExpr6(self, ctx:BKITParser.Expr6Context):
        if ctx.array_cell():
            return self.visitArray_cell(ctx.array_cell())
        return self.visitExpr7(ctx.expr7())


    # Visit a parse tree produced by BKITParser#expr7.
    def visitExpr7(self, ctx:BKITParser.Expr7Context):
        if ctx.function_call():
            return self.visitCall_stmt(ctx.function_call())
        return self.visitExpr8(ctx.expr8())

    # Visit a parse tree produced by BKITParser#expr8.
    def visitExpr8(self, ctx:BKITParser.Expr8Context):
        if ctx.operand():
            return self.visitOperand(ctx.operand())
        if ctx.LEFT_PAREN:
            return self.visitExpr(ctx.expr())

    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.primitive_data():
            return self.visitPrimitive_data(ctx.primitive_data())
        if ctx.array_lit():
            return self.visitArray_lit(ctx.array_lit())

    # Visit a parse tree produced by BKITParser#function_call.
    def visitFunction_call(self, ctx:BKITParser.Function_callContext):
        expr_list = []
        if ctx.expr():
            expr_list = list(map(lambda x: self.visitExpr(x), ctx.expr()))
        return CallStmt(Id(ctx.ID().getText()), expr_list)
        