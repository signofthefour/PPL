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
	 * Enter a parse tree produced by {@link BKITParser#primitive_type}.
	 * @param ctx the parse tree
	 */
	void enterPrimitive_type(BKITParser.Primitive_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#primitive_type}.
	 * @param ctx the parse tree
	 */
	void exitPrimitive_type(BKITParser.Primitive_typeContext ctx);
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
	 * Enter a parse tree produced by {@link BKITParser#function_body}.
	 * @param ctx the parse tree
	 */
	void enterFunction_body(BKITParser.Function_bodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#function_body}.
	 * @param ctx the parse tree
	 */
	void exitFunction_body(BKITParser.Function_bodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#ids_list_with_type}.
	 * @param ctx the parse tree
	 */
	void enterIds_list_with_type(BKITParser.Ids_list_with_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#ids_list_with_type}.
	 * @param ctx the parse tree
	 */
	void exitIds_list_with_type(BKITParser.Ids_list_with_typeContext ctx);
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
	 * Enter a parse tree produced by {@link BKITParser#ret_stmt}.
	 * @param ctx the parse tree
	 */
	void enterRet_stmt(BKITParser.Ret_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#ret_stmt}.
	 * @param ctx the parse tree
	 */
	void exitRet_stmt(BKITParser.Ret_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#exprs_list}.
	 * @param ctx the parse tree
	 */
	void enterExprs_list(BKITParser.Exprs_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#exprs_list}.
	 * @param ctx the parse tree
	 */
	void exitExprs_list(BKITParser.Exprs_listContext ctx);
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
	 * Enter a parse tree produced by {@link BKITParser#expr0}.
	 * @param ctx the parse tree
	 */
	void enterExpr0(BKITParser.Expr0Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#expr0}.
	 * @param ctx the parse tree
	 */
	void exitExpr0(BKITParser.Expr0Context ctx);
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
	 * Enter a parse tree produced by {@link BKITParser#subexpr}.
	 * @param ctx the parse tree
	 */
	void enterSubexpr(BKITParser.SubexprContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#subexpr}.
	 * @param ctx the parse tree
	 */
	void exitSubexpr(BKITParser.SubexprContext ctx);
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
	 * Enter a parse tree produced by {@link BKITParser#ids_list}.
	 * @param ctx the parse tree
	 */
	void enterIds_list(BKITParser.Ids_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#ids_list}.
	 * @param ctx the parse tree
	 */
	void exitIds_list(BKITParser.Ids_listContext ctx);
}