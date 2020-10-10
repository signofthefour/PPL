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
	 * Visit a parse tree produced by {@link BKITParser#primitive_type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimitive_type(BKITParser.Primitive_typeContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#composite_type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComposite_type(BKITParser.Composite_typeContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#bool_op}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBool_op(BKITParser.Bool_opContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#int_op}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInt_op(BKITParser.Int_opContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#float_op}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFloat_op(BKITParser.Float_opContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#if_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIf_stmt(BKITParser.If_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#while_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhile_stmt(BKITParser.While_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#dowhile_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDowhile_stmt(BKITParser.Dowhile_stmtContext ctx);
}