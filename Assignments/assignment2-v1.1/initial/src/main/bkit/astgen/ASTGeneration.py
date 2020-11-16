from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce
class ASTGeneration(BKITVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        print("hello")
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#main_func.
    def visitMain_func(self, ctx:BKITParser.Main_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_declare.
    def visitFunc_declare(self, ctx:BKITParser.Func_declareContext):
        id      = Id(ctx.IDENTIFIER().getText())
        param   = self.visitPara_list(ctx.para_list) if ctx.PARAMETER() else []
        body    = self.visitFunc_body(ctx.func_body())

        return FuncDecl(id, param, body)


    # Visit a parse tree produced by BKITParser#func_body.
    def visitFunc_body(self, ctx:BKITParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stm_list.
    def visitStm_list(self, ctx:BKITParser.Stm_listContext):
        decl_inter  = [i for i in ctx.var_declare()]
        stmt_inter  = [i for i in ctx.smt()]

        decl_list   = list(reduce(lambda x,y: x + [self.visitVar_declare(y)], decl_inter, []))
        stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))

        return tuple((decl_list, stmt_list))       


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
        id  = Id(ctx.IDENTIFIER().getText())
        lit = self.visitLiterals(ctx.literals())
        if ctx.INTEGER():
            dim = [int(i.getText()) for i in ctx.INTEGER()]
            return VarDecl(id, dim, lit)
        else:   
            return VarDecl(id, [], lit)


    # Visit a parse tree produced by BKITParser#para_list.
    def visitPara_list(self, ctx:BKITParser.Para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(self.index_op())
        rhs = self.visitExpression(ctx.expression())
        
        return Assign(lhs, rhs)

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
        return Break()


    # Visit a parse tree produced by BKITParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return Continue()


    # Visit a parse tree produced by BKITParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        if ctx.expression():
            return Return(self.visitExpression(ctx.expression()))
        return Return(None)


    # Visit a parse tree produced by BKITParser#func_call.
    def visitFunc_call(self, ctx:BKITParser.Func_callContext):
        id = Id(ctx.IDENTIFIER().getText())
        expr_inter = [i for i in ctx.expression()]
        expr_list  = list(reduce(lambda x,y: x + [self.visitExpression(y)], expr_inter, []))

        return tuple((id, expr_list))


    # Visit a parse tree produced by BKITParser#call_stmt.
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        call = self.visitFunc_call(ctx.func_call())
        return CallStmt(call[0], call[1])


    # Visit a parse tree produced by BKITParser#index_op.
    def visitIndex_op(self, ctx:BKITParser.Index_opContext):
        if ctx.IDENTIFIER(): 
            name = Id(ctx.IDENTIFIER().getText())
        else:
            call = self.visitFunc_call(ctx.func_call())
            name = CallExpr(call[0], call[1])
        expr_inter = [i for i in ctx.expression()]
        expr_list  = list(reduce(lambda x,y: x + [self.visitExpression(y)], expr_inter, []))

        return ArrayCell(name, expr_list)


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp0.
    def visitExp0(self, ctx:BKITParser.Exp0Context):
        if ctx.RELATION_OP():
            return BinaryOp(ctx.RELATION_OP().getText(), self.visitExp1(ctx.exp1(0)), self.visitExp1(ctx.exp1(1)))
        return self.visitExp1(ctx.exp1())


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        if ctx.BAND(): 
            return BinaryOp(ctx.BAND().getText(), self.visitExp1(ctx.exp1()), self.visitExp2(ctx.exp2()))
        if ctx.BOR(): 
            return BinaryOp(ctx.BOR().getText(), self.visitExp1(ctx.exp1()), self.visitExp2(ctx.exp2()))
        return self.visitExp2(ctx.exp2())


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        if ctx.ADDSUB():
            return BinaryOp(ctx.ADDSUB().getText(), self.visitExp2(ctx.exp2()), self.visitExp3(ctx.exp3()))
        return self.visitExp3(ctx.exp3())


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        if ctx.MULDIV():
            return BinaryOp(ctx.MULDIV().getText(), self.visitExp3(ctx.ex3()), self.visitExp4(ctx.exp4()))

        return self.visitExp4(ctx.exp4())


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        if ctx.BNEG():
            return UnaryOp(ctx.BNEG().getText(), self.visitExp4(ctx.exp4()))
        return self.visitExp5(ctx.exp5())


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        if ctx.NEGSIGN():
            return UnaryOp(ctx.NEGSIGN().getText(), self.visitExp5(ctx.exp5()))
        return self.visitExp6(ctx.exp6())


    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        if ctx.index_op():
            return self.visitIndex_op(ctx.index_op())
        return self.visitExp7(self.exp7())

    # Visit a parse tree produced by BKITParser#exp7.
    def visitExp7(self, ctx:BKITParser.Exp7Context):
        if ctx.func_call():
            call = self.visitFunc_call(ctx.func_call())
            return CallExpr(call[0], call[1])
        return self.visitExp8(ctx.exp8())


    # Visit a parse tree produced by BKITParser#exp8.
    def visitExp8(self, ctx:BKITParser.Exp8Context):
        if ctx.LP():
            return self.visitExpression(ctx.expression())
        return self.visitOperand(ctx.operand())


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        return self.visitLiterals(ctx.literals())


    # Visit a parse tree produced by BKITParser#literals.
    def visitLiterals(self, ctx:BKITParser.LiteralsContext):
        if ctx.INTEGER():
            return IntLiteral(int(ctx.INTEGER().getText()))
        elif ctx.FLOAT():
            return FloatLiteral(float(ctx.FLOAT().getText()))
        elif ctx.BOLEAN():
            return BooleanLiteral(bool(ctx.BOLEAN(),getText()))
        elif ctx.LSTRING():
            return StringLiteral(bool(ctx.LSTRING().getText()))
        else: 
            return self.visitArray_list(ctx.array_list())


    # Visit a parse tree produced by BKITParser#bool_array.
    def visitBool_array(self, ctx:BKITParser.Bool_arrayContext):
        a = [bool(i.getText()) for i in ctx.BOLEAN()]
        lst = [BooleanLiteral(n) for n in a]
        return lst


    # Visit a parse tree produced by BKITParser#int_array.
    def visitInt_array(self, ctx:BKITParser.Int_arrayContext):
        a = [int(i.getText()) for i in ctx.INTEGER()]
        lst = [IntLiteral(n) for n in a]
        return lst
        
    # Visit a parse tree produced by BKITParser#float_array.
    def visitFloat_array(self, ctx:BKITParser.Float_arrayContext):
        a =  [float(i.getText()) for i in ctx.FLOAT()]
        lst = [FloatLiteral(n) for n in a]
        return lst

    # Visit a parse tree produced by BKITParser#string_array.
    def visitString_array(self, ctx:BKITParser.String_arrayContext):
        a = [i.getText() for i in ctx.LSTRING()]
        lst = [StringLiteral(n) for n in a]
        return lst
        
    # Visit a parse tree produced by BKITParser#array_index.
    def visitArray_index(self, ctx:BKITParser.Array_indexContext):
        if ctx.int_array():
            return self.visitInt_array(ctx.int_array())
        if ctx.float_array():
            return self.visitFloat_array(ctx.float_array())
        if ctx.string_array():
            return self.visitString_array(ctx.string_array())
        if ctx.bool_array():
            return self.visitBool_array(ctx.bool_array())

    # Visit a parse tree produced by BKITParser#array_list.
    def visitArray_list(self, ctx:BKITParser.Array_listContext):
        print("hello")
        if ctx.array_index():
            a = self.visitArray_index(ctx.array_index(0))
            return ArrayLiteral([i for i in a])