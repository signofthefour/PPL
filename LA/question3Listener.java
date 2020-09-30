// Generated from question3.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link question3Parser}.
 */
public interface question3Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link question3Parser#real}.
	 * @param ctx the parse tree
	 */
	void enterReal(question3Parser.RealContext ctx);
	/**
	 * Exit a parse tree produced by {@link question3Parser#real}.
	 * @param ctx the parse tree
	 */
	void exitReal(question3Parser.RealContext ctx);
	/**
	 * Enter a parse tree produced by {@link question3Parser#string}.
	 * @param ctx the parse tree
	 */
	void enterString(question3Parser.StringContext ctx);
	/**
	 * Exit a parse tree produced by {@link question3Parser#string}.
	 * @param ctx the parse tree
	 */
	void exitString(question3Parser.StringContext ctx);
}