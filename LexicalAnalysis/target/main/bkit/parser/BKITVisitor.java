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
	 * Visit a parse tree produced by {@link BKITParser#var_declaration}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVar_declaration(BKITParser.Var_declarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#number}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNumber(BKITParser.NumberContext ctx);
}