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
	 * Visit a parse tree produced by {@link BKITParser#var_declare}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVar_declare(BKITParser.Var_declareContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#function_declare}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunction_declare(BKITParser.Function_declareContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#function_body}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunction_body(BKITParser.Function_bodyContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#ids_list_with_type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIds_list_with_type(BKITParser.Ids_list_with_typeContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStmt(BKITParser.StmtContext ctx);
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
	 * Visit a parse tree produced by {@link BKITParser#ret_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRet_stmt(BKITParser.Ret_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#exprs_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprs_list(BKITParser.Exprs_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr(BKITParser.ExprContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#expr0}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr0(BKITParser.Expr0Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#expr1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr1(BKITParser.Expr1Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#expr2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr2(BKITParser.Expr2Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#subexpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubexpr(BKITParser.SubexprContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#operand}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOperand(BKITParser.OperandContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#ids_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIds_list(BKITParser.Ids_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#primitive_type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimitive_type(BKITParser.Primitive_typeContext ctx);
}