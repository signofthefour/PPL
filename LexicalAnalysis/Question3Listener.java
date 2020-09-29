// Generated from Question3.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link Question3Parser}.
 */
public interface Question3Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link Question3Parser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(Question3Parser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link Question3Parser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(Question3Parser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link Question3Parser#number}.
	 * @param ctx the parse tree
	 */
	void enterNumber(Question3Parser.NumberContext ctx);
	/**
	 * Exit a parse tree produced by {@link Question3Parser#number}.
	 * @param ctx the parse tree
	 */
	void exitNumber(Question3Parser.NumberContext ctx);
	/**
	 * Enter a parse tree produced by {@link Question3Parser#string}.
	 * @param ctx the parse tree
	 */
	void enterString(Question3Parser.StringContext ctx);
	/**
	 * Exit a parse tree produced by {@link Question3Parser#string}.
	 * @param ctx the parse tree
	 */
	void exitString(Question3Parser.StringContext ctx);
}