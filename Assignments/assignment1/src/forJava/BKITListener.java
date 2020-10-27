// Generated from BKIT.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link BKITParser}.
 */
public interface BKITListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link BKITParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(BKITParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(BKITParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#var_declare}.
	 * @param ctx the parse tree
	 */
	void enterVar_declare(BKITParser.Var_declareContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#var_declare}.
	 * @param ctx the parse tree
	 */
	void exitVar_declare(BKITParser.Var_declareContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#function_declare}.
	 * @param ctx the parse tree
	 */
	void enterFunction_declare(BKITParser.Function_declareContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#function_declare}.
	 * @param ctx the parse tree
	 */
	void exitFunction_declare(BKITParser.Function_declareContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#array}.
	 * @param ctx the parse tree
	 */
	void enterArray(BKITParser.ArrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#array}.
	 * @param ctx the parse tree
	 */
	void exitArray(BKITParser.ArrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#primitive_data}.
	 * @param ctx the parse tree
	 */
	void enterPrimitive_data(BKITParser.Primitive_dataContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#primitive_data}.
	 * @param ctx the parse tree
	 */
	void exitPrimitive_data(BKITParser.Primitive_dataContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#composite_data}.
	 * @param ctx the parse tree
	 */
	void enterComposite_data(BKITParser.Composite_dataContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#composite_data}.
	 * @param ctx the parse tree
	 */
	void exitComposite_data(BKITParser.Composite_dataContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#array_lit}.
	 * @param ctx the parse tree
	 */
	void enterArray_lit(BKITParser.Array_litContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#array_lit}.
	 * @param ctx the parse tree
	 */
	void exitArray_lit(BKITParser.Array_litContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#var_list}.
	 * @param ctx the parse tree
	 */
	void enterVar_list(BKITParser.Var_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#var_list}.
	 * @param ctx the parse tree
	 */
	void exitVar_list(BKITParser.Var_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#scalar_var}.
	 * @param ctx the parse tree
	 */
	void enterScalar_var(BKITParser.Scalar_varContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#scalar_var}.
	 * @param ctx the parse tree
	 */
	void exitScalar_var(BKITParser.Scalar_varContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#var_non_init}.
	 * @param ctx the parse tree
	 */
	void enterVar_non_init(BKITParser.Var_non_initContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#var_non_init}.
	 * @param ctx the parse tree
	 */
	void exitVar_non_init(BKITParser.Var_non_initContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#composite_var}.
	 * @param ctx the parse tree
	 */
	void enterComposite_var(BKITParser.Composite_varContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#composite_var}.
	 * @param ctx the parse tree
	 */
	void exitComposite_var(BKITParser.Composite_varContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#var_init}.
	 * @param ctx the parse tree
	 */
	void enterVar_init(BKITParser.Var_initContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#var_init}.
	 * @param ctx the parse tree
	 */
	void exitVar_init(BKITParser.Var_initContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#composite_init}.
	 * @param ctx the parse tree
	 */
	void enterComposite_init(BKITParser.Composite_initContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#composite_init}.
	 * @param ctx the parse tree
	 */
	void exitComposite_init(BKITParser.Composite_initContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#primitive_init}.
	 * @param ctx the parse tree
	 */
	void enterPrimitive_init(BKITParser.Primitive_initContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#primitive_init}.
	 * @param ctx the parse tree
	 */
	void exitPrimitive_init(BKITParser.Primitive_initContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#params_list}.
	 * @param ctx the parse tree
	 */
	void enterParams_list(BKITParser.Params_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#params_list}.
	 * @param ctx the parse tree
	 */
	void exitParams_list(BKITParser.Params_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#stmt_list}.
	 * @param ctx the parse tree
	 */
	void enterStmt_list(BKITParser.Stmt_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#stmt_list}.
	 * @param ctx the parse tree
	 */
	void exitStmt_list(BKITParser.Stmt_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterStmt(BKITParser.StmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitStmt(BKITParser.StmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void enterIf_stmt(BKITParser.If_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void exitIf_stmt(BKITParser.If_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#var_declare_stmt}.
	 * @param ctx the parse tree
	 */
	void enterVar_declare_stmt(BKITParser.Var_declare_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#var_declare_stmt}.
	 * @param ctx the parse tree
	 */
	void exitVar_declare_stmt(BKITParser.Var_declare_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#for_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFor_stmt(BKITParser.For_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#for_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFor_stmt(BKITParser.For_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#while_stmt}.
	 * @param ctx the parse tree
	 */
	void enterWhile_stmt(BKITParser.While_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#while_stmt}.
	 * @param ctx the parse tree
	 */
	void exitWhile_stmt(BKITParser.While_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#dowhile_stmt}.
	 * @param ctx the parse tree
	 */
	void enterDowhile_stmt(BKITParser.Dowhile_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#dowhile_stmt}.
	 * @param ctx the parse tree
	 */
	void exitDowhile_stmt(BKITParser.Dowhile_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#assign_stmt}.
	 * @param ctx the parse tree
	 */
	void enterAssign_stmt(BKITParser.Assign_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#assign_stmt}.
	 * @param ctx the parse tree
	 */
	void exitAssign_stmt(BKITParser.Assign_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#break_stmt}.
	 * @param ctx the parse tree
	 */
	void enterBreak_stmt(BKITParser.Break_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#break_stmt}.
	 * @param ctx the parse tree
	 */
	void exitBreak_stmt(BKITParser.Break_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#continue_stmt}.
	 * @param ctx the parse tree
	 */
	void enterContinue_stmt(BKITParser.Continue_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#continue_stmt}.
	 * @param ctx the parse tree
	 */
	void exitContinue_stmt(BKITParser.Continue_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#call_stmt}.
	 * @param ctx the parse tree
	 */
	void enterCall_stmt(BKITParser.Call_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#call_stmt}.
	 * @param ctx the parse tree
	 */
	void exitCall_stmt(BKITParser.Call_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#return_stmt}.
	 * @param ctx the parse tree
	 */
	void enterReturn_stmt(BKITParser.Return_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#return_stmt}.
	 * @param ctx the parse tree
	 */
	void exitReturn_stmt(BKITParser.Return_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#init_for}.
	 * @param ctx the parse tree
	 */
	void enterInit_for(BKITParser.Init_forContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#init_for}.
	 * @param ctx the parse tree
	 */
	void exitInit_for(BKITParser.Init_forContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#con_for}.
	 * @param ctx the parse tree
	 */
	void enterCon_for(BKITParser.Con_forContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#con_for}.
	 * @param ctx the parse tree
	 */
	void exitCon_for(BKITParser.Con_forContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#update_for}.
	 * @param ctx the parse tree
	 */
	void enterUpdate_for(BKITParser.Update_forContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#update_for}.
	 * @param ctx the parse tree
	 */
	void exitUpdate_for(BKITParser.Update_forContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(BKITParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(BKITParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#expr1}.
	 * @param ctx the parse tree
	 */
	void enterExpr1(BKITParser.Expr1Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#expr1}.
	 * @param ctx the parse tree
	 */
	void exitExpr1(BKITParser.Expr1Context ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#expr2}.
	 * @param ctx the parse tree
	 */
	void enterExpr2(BKITParser.Expr2Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#expr2}.
	 * @param ctx the parse tree
	 */
	void exitExpr2(BKITParser.Expr2Context ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#expr3}.
	 * @param ctx the parse tree
	 */
	void enterExpr3(BKITParser.Expr3Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#expr3}.
	 * @param ctx the parse tree
	 */
	void exitExpr3(BKITParser.Expr3Context ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#expr4}.
	 * @param ctx the parse tree
	 */
	void enterExpr4(BKITParser.Expr4Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#expr4}.
	 * @param ctx the parse tree
	 */
	void exitExpr4(BKITParser.Expr4Context ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#expr5}.
	 * @param ctx the parse tree
	 */
	void enterExpr5(BKITParser.Expr5Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#expr5}.
	 * @param ctx the parse tree
	 */
	void exitExpr5(BKITParser.Expr5Context ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#expr6}.
	 * @param ctx the parse tree
	 */
	void enterExpr6(BKITParser.Expr6Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#expr6}.
	 * @param ctx the parse tree
	 */
	void exitExpr6(BKITParser.Expr6Context ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#expr7}.
	 * @param ctx the parse tree
	 */
	void enterExpr7(BKITParser.Expr7Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#expr7}.
	 * @param ctx the parse tree
	 */
	void exitExpr7(BKITParser.Expr7Context ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#expr8}.
	 * @param ctx the parse tree
	 */
	void enterExpr8(BKITParser.Expr8Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#expr8}.
	 * @param ctx the parse tree
	 */
	void exitExpr8(BKITParser.Expr8Context ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#operand}.
	 * @param ctx the parse tree
	 */
	void enterOperand(BKITParser.OperandContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#operand}.
	 * @param ctx the parse tree
	 */
	void exitOperand(BKITParser.OperandContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#function_call}.
	 * @param ctx the parse tree
	 */
	void enterFunction_call(BKITParser.Function_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#function_call}.
	 * @param ctx the parse tree
	 */
	void exitFunction_call(BKITParser.Function_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#index_op}.
	 * @param ctx the parse tree
	 */
	void enterIndex_op(BKITParser.Index_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#index_op}.
	 * @param ctx the parse tree
	 */
	void exitIndex_op(BKITParser.Index_opContext ctx);
}