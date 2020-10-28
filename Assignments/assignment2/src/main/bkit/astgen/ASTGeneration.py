from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce

class ASTGeneration(BKITVisitor):

    def visitProgram(self,ctx:BKITParser.ProgramContext):
        var_decls = list(reduce(lambda y,x: y + self.visitVar_declare(x), [item for item in ctx.var_declare()], []))
        funcs_decls = list(reduce(lambda y,x: self.visitFunction_declare(x), [item for item in ctx.function_declare()], []))
        return Program(var_decls + funcs_decls)

    # Visit a parse tree produced by BKITParser#var_declare.
    def visitVar_declare(self, ctx:BKITParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_declare.
    def visitFunction_declare(self, ctx:BKITParser.Function_declareContext):
        funcName = Id(ctx.ID().getText())
        params = self.visitParams_list(ctx.params_list())
        body = self.visitVar_declare_stmt() + self.visitStmt()
        return FuncDecl(funcName, params, body)


    # Visit a parse tree produced by BKITParser#array.
    def visitArray(self, ctx:BKITParser.ArrayContext):
        return self.visitChildren(ctx)


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
        

    # Visit a parse tree produced by BKITParser#composite_data.
    def visitComposite_data(self, ctx:BKITParser.Composite_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_lit.
    def visitArray_lit(self, ctx:BKITParser.Array_litContext):
        if ctx.primitive_data():
            return list(map(lambda datum: self.visitPrimitive_data(datum), ctx.primitive_data()))
        else:
            return list(map(lambda datum: self.visitComposite_data(datum), ctx.composite_data()))


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
        if ctx.INT_LIT():
            dim = map(lambda x: int(x), [lit.getText() for lit in ctx.INT_LIT()])
            decl = VarDecl(Id(ctx.ID().getText()), dim, self.visitComposite_data(ctx.composite_data()))
            if isinstance(decl, VarDecl):
                return decl
        else:
            decl = VarDecl(Id(ctx.ID().getText()), [], self.visitPrimitive_data(ctx.primitive_data()))
            if isinstance(decl, VarDecl):
                return decl



    # Visit a parse tree produced by BKITParser#composite_init.
    def visitComposite_init(self, ctx:BKITParser.Composite_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#primitive_init.
    def visitPrimitive_init(self, ctx:BKITParser.Primitive_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#params_list.
    def visitParams_list(self, ctx:BKITParser.Params_listContext):
        params_list =  [self.visitVar_non_init(x) for x in ctx.var_non_init()]
        return params_list


    # Visit a parse tree produced by BKITParser#stmt_list.
    def visitStmt_list(self, ctx:BKITParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt.
    def visitStmt(self, ctx:BKITParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_declare_stmt.
    def visitVar_declare_stmt(self, ctx:BKITParser.Var_declare_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stmt.
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dowhile_stmt.
    def visitDowhile_stmt(self, ctx:BKITParser.Dowhile_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stmt.
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#init_for.
    def visitInit_for(self, ctx:BKITParser.Init_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#con_for.
    def visitCon_for(self, ctx:BKITParser.Con_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#update_for.
    def visitUpdate_for(self, ctx:BKITParser.Update_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr.
    def visitExpr(self, ctx:BKITParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr1.
    def visitExpr1(self, ctx:BKITParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr2.
    def visitExpr2(self, ctx:BKITParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr3.
    def visitExpr3(self, ctx:BKITParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr4.
    def visitExpr4(self, ctx:BKITParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr5.
    def visitExpr5(self, ctx:BKITParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr6.
    def visitExpr6(self, ctx:BKITParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr7.
    def visitExpr7(self, ctx:BKITParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr8.
    def visitExpr8(self, ctx:BKITParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_call.
    def visitFunction_call(self, ctx:BKITParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_op.
    def visitIndex_op(self, ctx:BKITParser.Index_opContext):
        return self.visitChildren(ctx)
        