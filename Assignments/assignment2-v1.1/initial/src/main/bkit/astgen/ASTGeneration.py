from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce
class ASTGeneration(BKITVisitor):
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return Program([VarDecl(Id(ctx.ID().getText()),[],None)])


    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):

        var_inter  = [i for i in ctx.var_declare()]
        func_inter = [i for i in ctx.func_declare()]

        var_list   = list(reduce(lambda x,y: x + [self.visitVar_declare(y)], var_inter, []))
        func_list  = list(reduce(lambda x,y: x + [self.visitVar_declare(y)], func_inter, []))

        return Program(var_list  + func_list)


    # Visit a parse tree produced by BKITParser#var_declare.
    def visitVar_declare(self, ctx:BKITParser.Var_declareContext):

        return self.visitVar_list(ctx.var_list())


    # Visit a parse tree produced by BKITParser#var_list.
    def visitVar_list(self, ctx:BKITParser.Var_listContext):

        a = self.visitChildren(ctx)
        return a


    # Visit a parse tree produced by BKITParser#main_func.
    def visitMain_func(self, ctx:BKITParser.Main_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_declare.
    def visitFunc_declare(self, ctx:BKITParser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_body.
    def visitFunc_body(self, ctx:BKITParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stm_list.
    def visitStm_list(self, ctx:BKITParser.Stm_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stm.
    def visitStm(self, ctx:BKITParser.StmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#non_initted_var.
    def visitNon_initted_var(self, ctx:BKITParser.Non_initted_varContext):
        id = Id(ctx.IDENTIFIER().getText())
        if ctx.INTEGER():
            dim = [int(i.getText()) for i in ctx.INTEGER()]
            return VarDecl(id, dim, None)
        else:

            return VarDecl(id, [], None)


    # Visit a parse tree produced by BKITParser#var_init.
    def visitVar_init(self, ctx:BKITParser.Var_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#para_list.
    def visitPara_list(self, ctx:BKITParser.Para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#composite_ass.
    def visitComposite_ass(self, ctx:BKITParser.Composite_assContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stmt.
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:BKITParser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_call.
    def visitFunc_call(self, ctx:BKITParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stmt.
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_op.
    def visitIndex_op(self, ctx:BKITParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp0.
    def visitExp0(self, ctx:BKITParser.Exp0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp7.
    def visitExp7(self, ctx:BKITParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp8.
    def visitExp8(self, ctx:BKITParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literals.
    def visitLiterals(self, ctx:BKITParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bool_array.
    def visitBool_array(self, ctx:BKITParser.Bool_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_array.
    def visitInt_array(self, ctx:BKITParser.Int_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_array.
    def visitFloat_array(self, ctx:BKITParser.Float_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#string_array.
    def visitString_array(self, ctx:BKITParser.String_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_index.
    def visitArray_index(self, ctx:BKITParser.Array_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_list.
    def visitArray_list(self, ctx:BKITParser.Array_listContext):
        return self.visitChildren(ctx)