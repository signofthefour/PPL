# Generated from BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete listener for a parse tree produced by BKITParser.
class BKITListener(ParseTreeListener):

    # Enter a parse tree produced by BKITParser#program.
    def enterProgram(self, ctx:BKITParser.ProgramContext):
        pass

    # Exit a parse tree produced by BKITParser#program.
    def exitProgram(self, ctx:BKITParser.ProgramContext):
        pass


    # Enter a parse tree produced by BKITParser#var_declare.
    def enterVar_declare(self, ctx:BKITParser.Var_declareContext):
        pass

    # Exit a parse tree produced by BKITParser#var_declare.
    def exitVar_declare(self, ctx:BKITParser.Var_declareContext):
        pass


    # Enter a parse tree produced by BKITParser#function_declare.
    def enterFunction_declare(self, ctx:BKITParser.Function_declareContext):
        pass

    # Exit a parse tree produced by BKITParser#function_declare.
    def exitFunction_declare(self, ctx:BKITParser.Function_declareContext):
        pass


    # Enter a parse tree produced by BKITParser#stmt_list.
    def enterStmt_list(self, ctx:BKITParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by BKITParser#stmt_list.
    def exitStmt_list(self, ctx:BKITParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by BKITParser#stmt.
    def enterStmt(self, ctx:BKITParser.StmtContext):
        pass

    # Exit a parse tree produced by BKITParser#stmt.
    def exitStmt(self, ctx:BKITParser.StmtContext):
        pass


    # Enter a parse tree produced by BKITParser#if_stmt.
    def enterIf_stmt(self, ctx:BKITParser.If_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#if_stmt.
    def exitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#var_declare_stmt.
    def enterVar_declare_stmt(self, ctx:BKITParser.Var_declare_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#var_declare_stmt.
    def exitVar_declare_stmt(self, ctx:BKITParser.Var_declare_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#for_stmt.
    def enterFor_stmt(self, ctx:BKITParser.For_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#for_stmt.
    def exitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#while_stmt.
    def enterWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#while_stmt.
    def exitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#dowhile_stmt.
    def enterDowhile_stmt(self, ctx:BKITParser.Dowhile_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#dowhile_stmt.
    def exitDowhile_stmt(self, ctx:BKITParser.Dowhile_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#assign_stmt.
    def enterAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#assign_stmt.
    def exitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#break_stmt.
    def enterBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#break_stmt.
    def exitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#continue_stmt.
    def enterContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#continue_stmt.
    def exitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#call_stmt.
    def enterCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#call_stmt.
    def exitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#return_stmt.
    def enterReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#return_stmt.
    def exitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#expr.
    def enterExpr(self, ctx:BKITParser.ExprContext):
        pass

    # Exit a parse tree produced by BKITParser#expr.
    def exitExpr(self, ctx:BKITParser.ExprContext):
        pass


    # Enter a parse tree produced by BKITParser#expr1.
    def enterExpr1(self, ctx:BKITParser.Expr1Context):
        pass

    # Exit a parse tree produced by BKITParser#expr1.
    def exitExpr1(self, ctx:BKITParser.Expr1Context):
        pass


    # Enter a parse tree produced by BKITParser#expr2.
    def enterExpr2(self, ctx:BKITParser.Expr2Context):
        pass

    # Exit a parse tree produced by BKITParser#expr2.
    def exitExpr2(self, ctx:BKITParser.Expr2Context):
        pass


    # Enter a parse tree produced by BKITParser#expr3.
    def enterExpr3(self, ctx:BKITParser.Expr3Context):
        pass

    # Exit a parse tree produced by BKITParser#expr3.
    def exitExpr3(self, ctx:BKITParser.Expr3Context):
        pass


    # Enter a parse tree produced by BKITParser#expr4.
    def enterExpr4(self, ctx:BKITParser.Expr4Context):
        pass

    # Exit a parse tree produced by BKITParser#expr4.
    def exitExpr4(self, ctx:BKITParser.Expr4Context):
        pass


    # Enter a parse tree produced by BKITParser#expr5.
    def enterExpr5(self, ctx:BKITParser.Expr5Context):
        pass

    # Exit a parse tree produced by BKITParser#expr5.
    def exitExpr5(self, ctx:BKITParser.Expr5Context):
        pass


    # Enter a parse tree produced by BKITParser#expr6.
    def enterExpr6(self, ctx:BKITParser.Expr6Context):
        pass

    # Exit a parse tree produced by BKITParser#expr6.
    def exitExpr6(self, ctx:BKITParser.Expr6Context):
        pass


    # Enter a parse tree produced by BKITParser#array_cell.
    def enterArray_cell(self, ctx:BKITParser.Array_cellContext):
        pass

    # Exit a parse tree produced by BKITParser#array_cell.
    def exitArray_cell(self, ctx:BKITParser.Array_cellContext):
        pass


    # Enter a parse tree produced by BKITParser#expr7.
    def enterExpr7(self, ctx:BKITParser.Expr7Context):
        pass

    # Exit a parse tree produced by BKITParser#expr7.
    def exitExpr7(self, ctx:BKITParser.Expr7Context):
        pass


    # Enter a parse tree produced by BKITParser#expr8.
    def enterExpr8(self, ctx:BKITParser.Expr8Context):
        pass

    # Exit a parse tree produced by BKITParser#expr8.
    def exitExpr8(self, ctx:BKITParser.Expr8Context):
        pass


    # Enter a parse tree produced by BKITParser#operand.
    def enterOperand(self, ctx:BKITParser.OperandContext):
        pass

    # Exit a parse tree produced by BKITParser#operand.
    def exitOperand(self, ctx:BKITParser.OperandContext):
        pass


    # Enter a parse tree produced by BKITParser#function_call.
    def enterFunction_call(self, ctx:BKITParser.Function_callContext):
        pass

    # Exit a parse tree produced by BKITParser#function_call.
    def exitFunction_call(self, ctx:BKITParser.Function_callContext):
        pass


    # Enter a parse tree produced by BKITParser#index_op.
    def enterIndex_op(self, ctx:BKITParser.Index_opContext):
        pass

    # Exit a parse tree produced by BKITParser#index_op.
    def exitIndex_op(self, ctx:BKITParser.Index_opContext):
        pass


    # Enter a parse tree produced by BKITParser#array.
    def enterArray(self, ctx:BKITParser.ArrayContext):
        pass

    # Exit a parse tree produced by BKITParser#array.
    def exitArray(self, ctx:BKITParser.ArrayContext):
        pass


    # Enter a parse tree produced by BKITParser#primitive_data.
    def enterPrimitive_data(self, ctx:BKITParser.Primitive_dataContext):
        pass

    # Exit a parse tree produced by BKITParser#primitive_data.
    def exitPrimitive_data(self, ctx:BKITParser.Primitive_dataContext):
        pass


    # Enter a parse tree produced by BKITParser#array_lit.
    def enterArray_lit(self, ctx:BKITParser.Array_litContext):
        pass

    # Exit a parse tree produced by BKITParser#array_lit.
    def exitArray_lit(self, ctx:BKITParser.Array_litContext):
        pass


    # Enter a parse tree produced by BKITParser#var_list.
    def enterVar_list(self, ctx:BKITParser.Var_listContext):
        pass

    # Exit a parse tree produced by BKITParser#var_list.
    def exitVar_list(self, ctx:BKITParser.Var_listContext):
        pass


    # Enter a parse tree produced by BKITParser#var_init.
    def enterVar_init(self, ctx:BKITParser.Var_initContext):
        pass

    # Exit a parse tree produced by BKITParser#var_init.
    def exitVar_init(self, ctx:BKITParser.Var_initContext):
        pass


    # Enter a parse tree produced by BKITParser#var_non_init.
    def enterVar_non_init(self, ctx:BKITParser.Var_non_initContext):
        pass

    # Exit a parse tree produced by BKITParser#var_non_init.
    def exitVar_non_init(self, ctx:BKITParser.Var_non_initContext):
        pass


    # Enter a parse tree produced by BKITParser#composite_var.
    def enterComposite_var(self, ctx:BKITParser.Composite_varContext):
        pass

    # Exit a parse tree produced by BKITParser#composite_var.
    def exitComposite_var(self, ctx:BKITParser.Composite_varContext):
        pass


    # Enter a parse tree produced by BKITParser#composite_init.
    def enterComposite_init(self, ctx:BKITParser.Composite_initContext):
        pass

    # Exit a parse tree produced by BKITParser#composite_init.
    def exitComposite_init(self, ctx:BKITParser.Composite_initContext):
        pass


    # Enter a parse tree produced by BKITParser#primitive_init.
    def enterPrimitive_init(self, ctx:BKITParser.Primitive_initContext):
        pass

    # Exit a parse tree produced by BKITParser#primitive_init.
    def exitPrimitive_init(self, ctx:BKITParser.Primitive_initContext):
        pass


    # Enter a parse tree produced by BKITParser#params_list.
    def enterParams_list(self, ctx:BKITParser.Params_listContext):
        pass

    # Exit a parse tree produced by BKITParser#params_list.
    def exitParams_list(self, ctx:BKITParser.Params_listContext):
        pass



del BKITParser