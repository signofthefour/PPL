# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_declare.
    def visitVar_declare(self, ctx:BKITParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#main_function_declare.
    def visitMain_function_declare(self, ctx:BKITParser.Main_function_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_declare.
    def visitFunction_declare(self, ctx:BKITParser.Function_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array.
    def visitArray(self, ctx:BKITParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#primitive_data.
    def visitPrimitive_data(self, ctx:BKITParser.Primitive_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#composite_data.
    def visitComposite_data(self, ctx:BKITParser.Composite_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_list.
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#scalar_var.
    def visitScalar_var(self, ctx:BKITParser.Scalar_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#composite_var.
    def visitComposite_var(self, ctx:BKITParser.Composite_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_non_init.
    def visitVar_non_init(self, ctx:BKITParser.Var_non_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_init.
    def visitVar_init(self, ctx:BKITParser.Var_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#composite_init.
    def visitComposite_init(self, ctx:BKITParser.Composite_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#primitive_init.
    def visitPrimitive_init(self, ctx:BKITParser.Primitive_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#params_list.
    def visitParams_list(self, ctx:BKITParser.Params_listContext):
        return self.visitChildren(ctx)


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


    # Visit a parse tree produced by BKITParser#boolean_type_expr.
    def visitBoolean_type_expr(self, ctx:BKITParser.Boolean_type_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_expr1.
    def visitInt_expr1(self, ctx:BKITParser.Int_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_expr2.
    def visitInt_expr2(self, ctx:BKITParser.Int_expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_expr3.
    def visitInt_expr3(self, ctx:BKITParser.Int_expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_expr4.
    def visitInt_expr4(self, ctx:BKITParser.Int_expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_expr5.
    def visitInt_expr5(self, ctx:BKITParser.Int_expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_expr6.
    def visitInt_expr6(self, ctx:BKITParser.Int_expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_operand.
    def visitInt_operand(self, ctx:BKITParser.Int_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_expr1.
    def visitFloat_expr1(self, ctx:BKITParser.Float_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_expr2.
    def visitFloat_expr2(self, ctx:BKITParser.Float_expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_expr3.
    def visitFloat_expr3(self, ctx:BKITParser.Float_expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_expr4.
    def visitFloat_expr4(self, ctx:BKITParser.Float_expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_expr5.
    def visitFloat_expr5(self, ctx:BKITParser.Float_expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_expr6.
    def visitFloat_expr6(self, ctx:BKITParser.Float_expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_operand.
    def visitFloat_operand(self, ctx:BKITParser.Float_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#constant.
    def visitConstant(self, ctx:BKITParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#boolean_expr.
    def visitBoolean_expr(self, ctx:BKITParser.Boolean_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#boolean_expr1.
    def visitBoolean_expr1(self, ctx:BKITParser.Boolean_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#boolean_expr2.
    def visitBoolean_expr2(self, ctx:BKITParser.Boolean_expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#boolean_expr3.
    def visitBoolean_expr3(self, ctx:BKITParser.Boolean_expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#boolean_expr4.
    def visitBoolean_expr4(self, ctx:BKITParser.Boolean_expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_func_call.
    def visitInt_func_call(self, ctx:BKITParser.Int_func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_func_call.
    def visitFloat_func_call(self, ctx:BKITParser.Float_func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#boolean_func_call.
    def visitBoolean_func_call(self, ctx:BKITParser.Boolean_func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_op.
    def visitIndex_op(self, ctx:BKITParser.Index_opContext):
        return self.visitChildren(ctx)



del BKITParser