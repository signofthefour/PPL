// Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link BKITParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface BKITVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link BKITParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(BKITParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitType(BKITParser.TypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#ids_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIds_list(BKITParser.Ids_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#var_declare}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVar_declare(BKITParser.Var_declareContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#func_declare}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunc_declare(BKITParser.Func_declareContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#func_body}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunc_body(BKITParser.Func_bodyContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(BKITParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#assign_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssign_stmt(BKITParser.Assign_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#call_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCall_stmt(BKITParser.Call_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#rt_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRt_stmt(BKITParser.Rt_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(BKITParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#exp0}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp0(BKITParser.Exp0Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#exp1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp1(BKITParser.Exp1Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#exp2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp2(BKITParser.Exp2Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#operand}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOperand(BKITParser.OperandContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#sub_exp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSub_exp(BKITParser.Sub_expContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#expression_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression_list(BKITParser.Expression_listContext ctx);
}