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
	 * Enter a parse tree produced by {@link BKITParser#main_func}.
	 * @param ctx the parse tree
	 */
	void enterMain_func(BKITParser.Main_funcContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#main_func}.
	 * @param ctx the parse tree
	 */
	void exitMain_func(BKITParser.Main_funcContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#func_declare}.
	 * @param ctx the parse tree
	 */
	void enterFunc_declare(BKITParser.Func_declareContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#func_declare}.
	 * @param ctx the parse tree
	 */
	void exitFunc_declare(BKITParser.Func_declareContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#func_body}.
	 * @param ctx the parse tree
	 */
	void enterFunc_body(BKITParser.Func_bodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#func_body}.
	 * @param ctx the parse tree
	 */
	void exitFunc_body(BKITParser.Func_bodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#stm_list}.
	 * @param ctx the parse tree
	 */
	void enterStm_list(BKITParser.Stm_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#stm_list}.
	 * @param ctx the parse tree
	 */
	void exitStm_list(BKITParser.Stm_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#stm}.
	 * @param ctx the parse tree
	 */
	void enterStm(BKITParser.StmContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#stm}.
	 * @param ctx the parse tree
	 */
	void exitStm(BKITParser.StmContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#non_initted_var}.
	 * @param ctx the parse tree
	 */
	void enterNon_initted_var(BKITParser.Non_initted_varContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#non_initted_var}.
	 * @param ctx the parse tree
	 */
	void exitNon_initted_var(BKITParser.Non_initted_varContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#initted_var}.
	 * @param ctx the parse tree
	 */
	void enterInitted_var(BKITParser.Initted_varContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#initted_var}.
	 * @param ctx the parse tree
	 */
	void exitInitted_var(BKITParser.Initted_varContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#scalar_init}.
	 * @param ctx the parse tree
	 */
	void enterScalar_init(BKITParser.Scalar_initContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#scalar_init}.
	 * @param ctx the parse tree
	 */
	void exitScalar_init(BKITParser.Scalar_initContext ctx);
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
	 * Enter a parse tree produced by {@link BKITParser#para_list}.
	 * @param ctx the parse tree
	 */
	void enterPara_list(BKITParser.Para_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#para_list}.
	 * @param ctx the parse tree
	 */
	void exitPara_list(BKITParser.Para_listContext ctx);
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
	 * Enter a parse tree produced by {@link BKITParser#composite_ass}.
	 * @param ctx the parse tree
	 */
	void enterComposite_ass(BKITParser.Composite_assContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#composite_ass}.
	 * @param ctx the parse tree
	 */
	void exitComposite_ass(BKITParser.Composite_assContext ctx);
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
	 * Enter a parse tree produced by {@link BKITParser#do_while_stmt}.
	 * @param ctx the parse tree
	 */
	void enterDo_while_stmt(BKITParser.Do_while_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#do_while_stmt}.
	 * @param ctx the parse tree
	 */
	void exitDo_while_stmt(BKITParser.Do_while_stmtContext ctx);
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
	 * Enter a parse tree produced by {@link BKITParser#func_call}.
	 * @param ctx the parse tree
	 */
	void enterFunc_call(BKITParser.Func_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#func_call}.
	 * @param ctx the parse tree
	 */
	void exitFunc_call(BKITParser.Func_callContext ctx);
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
	 * Enter a parse tree produced by {@link BKITParser#index_op}.
	 * @param ctx the parse tree
	 */
	void enterIndex_op(BKITParser.Index_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#index_op}.
	 * @param ctx the parse tree
	 */
	void exitIndex_op(BKITParser.Index_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(BKITParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(BKITParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#exp0}.
	 * @param ctx the parse tree
	 */
	void enterExp0(BKITParser.Exp0Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#exp0}.
	 * @param ctx the parse tree
	 */
	void exitExp0(BKITParser.Exp0Context ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#exp1}.
	 * @param ctx the parse tree
	 */
	void enterExp1(BKITParser.Exp1Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#exp1}.
	 * @param ctx the parse tree
	 */
	void exitExp1(BKITParser.Exp1Context ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#exp2}.
	 * @param ctx the parse tree
	 */
	void enterExp2(BKITParser.Exp2Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#exp2}.
	 * @param ctx the parse tree
	 */
	void exitExp2(BKITParser.Exp2Context ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#exp3}.
	 * @param ctx the parse tree
	 */
	void enterExp3(BKITParser.Exp3Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#exp3}.
	 * @param ctx the parse tree
	 */
	void exitExp3(BKITParser.Exp3Context ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#exp4}.
	 * @param ctx the parse tree
	 */
	void enterExp4(BKITParser.Exp4Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#exp4}.
	 * @param ctx the parse tree
	 */
	void exitExp4(BKITParser.Exp4Context ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#exp5}.
	 * @param ctx the parse tree
	 */
	void enterExp5(BKITParser.Exp5Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#exp5}.
	 * @param ctx the parse tree
	 */
	void exitExp5(BKITParser.Exp5Context ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#exp6}.
	 * @param ctx the parse tree
	 */
	void enterExp6(BKITParser.Exp6Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#exp6}.
	 * @param ctx the parse tree
	 */
	void exitExp6(BKITParser.Exp6Context ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#exp7}.
	 * @param ctx the parse tree
	 */
	void enterExp7(BKITParser.Exp7Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#exp7}.
	 * @param ctx the parse tree
	 */
	void exitExp7(BKITParser.Exp7Context ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#exp8}.
	 * @param ctx the parse tree
	 */
	void enterExp8(BKITParser.Exp8Context ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#exp8}.
	 * @param ctx the parse tree
	 */
	void exitExp8(BKITParser.Exp8Context ctx);
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
	 * Enter a parse tree produced by {@link BKITParser#literals}.
	 * @param ctx the parse tree
	 */
	void enterLiterals(BKITParser.LiteralsContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#literals}.
	 * @param ctx the parse tree
	 */
	void exitLiterals(BKITParser.LiteralsContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#int_array}.
	 * @param ctx the parse tree
	 */
	void enterInt_array(BKITParser.Int_arrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#int_array}.
	 * @param ctx the parse tree
	 */
	void exitInt_array(BKITParser.Int_arrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#float_array}.
	 * @param ctx the parse tree
	 */
	void enterFloat_array(BKITParser.Float_arrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#float_array}.
	 * @param ctx the parse tree
	 */
	void exitFloat_array(BKITParser.Float_arrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#string_array}.
	 * @param ctx the parse tree
	 */
	void enterString_array(BKITParser.String_arrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#string_array}.
	 * @param ctx the parse tree
	 */
	void exitString_array(BKITParser.String_arrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#array_index}.
	 * @param ctx the parse tree
	 */
	void enterArray_index(BKITParser.Array_indexContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#array_index}.
	 * @param ctx the parse tree
	 */
	void exitArray_index(BKITParser.Array_indexContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#array_list}.
	 * @param ctx the parse tree
	 */
	void enterArray_list(BKITParser.Array_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#array_list}.
	 * @param ctx the parse tree
	 */
	void exitArray_list(BKITParser.Array_listContext ctx);
}