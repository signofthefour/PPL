
from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
#from AST_GEN_TEST import * 
from functools import reduce


class ASTGeneration(BKITVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        var_inter  = [i for i in ctx.var_declare()]
        func_inter = [i for i in ctx.func_declare()]

        var_list   = list(reduce(lambda x,y: x + self.visitVar_declare(y), var_inter, []))
        func_list  = list(reduce(lambda x,y: x + [self.visitFunc_declare(y)], func_inter, []))

        return Program(var_list  + func_list)


    # Visit a parse tree produced by BKITParser#var_declare.
    def visitVar_declare(self, ctx:BKITParser.Var_declareContext):
        return self.visitVar_list(ctx.var_list())


    # Visit a parse tree produced by BKITParser#var_list.
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        decl_inter = [i for i in ctx.decl()]
        decl_list  = list(reduce(lambda x,y: x + [self.visitDecl(y)], decl_inter, []))
        return decl_list

    # Visit a parse tree produced by BKITParser#decl.
    def visitDecl(self, ctx:BKITParser.DeclContext):
        return self.visitVar_init(ctx.var_init()) if ctx.var_init() else self.visitNon_initted_var(ctx.non_initted_var())


    # Visit a parse tree produced by BKITParser#main_func.
    def visitMain_func(self, ctx:BKITParser.Main_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_declare.
    def visitFunc_declare(self, ctx:BKITParser.Func_declareContext):
        id      = Id(ctx.IDENTIFIER().getText())
        param   = self.visitPara_list(ctx.para_list()) if ctx.PARAMETER() else []
        body    = self.visitFunc_body(ctx.func_body())


        return FuncDecl(id, param, body)


    # Visit a parse tree produced by BKITParser#func_body.
    def visitFunc_body(self, ctx:BKITParser.Func_bodyContext):
        #print (self.visitStm_list(ctx.stm_list()))
        return  self.visitStm_list(ctx.stm_list())


    # Visit a parse tree produced by BKITParser#stm_list.
    def visitStm_list(self, ctx:BKITParser.Stm_listContext):
        decl_inter  = [i for i in ctx.var_declare()]
        stmt_inter  = [i for i in ctx.stm()]

        decl_list   = list(reduce(lambda x,y: x + self.visitVar_declare(y), decl_inter, []))
        stmt_list   = list(reduce(lambda x,y: x + [self.visitStm(y)], stmt_inter, []))
        
        
        return tuple((decl_list, stmt_list))
        

    # Visit a parse tree produced by BKITParser#stm.
    def visitStm(self, ctx:BKITParser.StmContext):
        #print(type(ctx))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#non_initted_var.
    def visitNon_initted_var(self, ctx:BKITParser.Non_initted_varContext):
        id = Id(ctx.IDENTIFIER().getText())
        if ctx.INTEGER():
            dim = [int(i.getText(), 0) for i in ctx.INTEGER()]
            return VarDecl(id, dim, None)
        else:

            return VarDecl(id, [], None)


    # Visit a parse tree produced by BKITParser#var_init.
    def visitVar_init(self, ctx:BKITParser.Var_initContext):
        id  = Id(ctx.IDENTIFIER().getText())
        lit = self.visitLiterals(ctx.literals())
        if ctx.INTEGER():
            dim = [int(i.getText(), 0) for i in ctx.INTEGER()]
            return VarDecl(id, dim, lit)
        else:   
            return VarDecl(id, [], lit)


    # Visit a parse tree produced by BKITParser#para_list.
    def visitPara_list(self, ctx:BKITParser.Para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        exp_lst = [self.visitExpression(i) for i in ctx.expression()]
        stm_lst = [self.visitStm_list(i) for i in ctx.stm_list()]

        ifelse_list  = [tuple((exp_lst[i],stm_lst[i][0], stm_lst[i][1])) for i in range(0,int(len(exp_lst)))]
        
        return If(ifelse_list,stm_lst[-1]) if (ctx.ELSE()) else If(ifelse_list,tuple(([],[])))


    # Visit a parse tree produced by BKITParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        #print(type(ctx))
        lhs = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visitIndex_op(ctx.index_op())
        rhs = self.visitExpression(ctx.expression())
        
        return Assign(lhs, rhs)

    # Visit a parse tree produced by BKITParser#for_stmt.
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        id = Id(ctx.IDENTIFIER().getText())
        expr1 = self.visitExpression(ctx.expression(0))
        expr2 = self.visitExpression(ctx.expression(1))
        expr3 = self.visitExpression(ctx.expression(2))
        loop  = self.visitStm_list(ctx.stm_list())

        return For(id, expr1, expr2, expr3, loop)

    # Visit a parse tree produced by BKITParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        expr = self.visitExpression(ctx.expression())
        sl   = self.visitStm_list(ctx.stm_list())


        return While(expr, sl)

    # Visit a parse tree produced by BKITParser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:BKITParser.Do_while_stmtContext):
        expr = self.visitExpression(ctx.expression())
        sl   = self.visitStm_list(ctx.stm_list())

        return Dowhile(sl, expr)

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
        return self.visitExp1(ctx.exp1(0))


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        
        if ctx.BAND():
            return BinaryOp(ctx.BAND().getText(), self.visitExp1(ctx.exp1()), self.visitExp2(ctx.exp2()))
        if ctx.BOR(): 
            return BinaryOp(ctx.BOR().getText(), self.visitExp1(ctx.exp1()), self.visitExp2(ctx.exp2()))
        return self.visitExp2(ctx.exp2())


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        if ctx.FSUBOP():
            return BinaryOp(ctx.FSUBOP().getText(), self.visitExp2(ctx.exp2()), self.visitExp3(ctx.exp3()))
        elif ctx.ISUBOP():
            return BinaryOp(ctx.ISUBOP().getText(), self.visitExp2(ctx.exp2()), self.visitExp3(ctx.exp3()))
        elif ctx.FADDOP():
            return BinaryOp(ctx.FADDOP().getText(), self.visitExp2(ctx.exp2()), self.visitExp3(ctx.exp3()))
        elif ctx.IADDOP():
            return BinaryOp(ctx.IADDOP().getText(), self.visitExp2(ctx.exp2()), self.visitExp3(ctx.exp3()))
        return self.visitExp3(ctx.exp3())


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        if ctx.MULDIV():
            return BinaryOp(ctx.MULDIV().getText(), self.visitExp3(ctx.exp3()), self.visitExp4(ctx.exp4()))

        return self.visitExp4(ctx.exp4())


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        if ctx.BNEG():
            return UnaryOp(ctx.BNEG().getText(), self.visitExp4(ctx.exp4()))
        return self.visitExp5(ctx.exp5())


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        if ctx.FSUBOP():
            return UnaryOp(ctx.FSUBOP().getText(), self.visitExp5(ctx.exp5()))
        if ctx.ISUBOP():
            return UnaryOp(ctx.ISUBOP().getText(), self.visitExp5(ctx.exp5()))
        return self.visitExp6(ctx.exp6())


    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        if ctx.index_op():
            return self.visitIndex_op(ctx.index_op())
        return self.visitExp7(ctx.exp7())

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
            return IntLiteral(int(ctx.INTEGER().getText(), 0))
        elif ctx.FLOAT():
            return FloatLiteral(float(ctx.FLOAT().getText()))
        elif ctx.BOLEAN():
            return BooleanLiteral(True) if (ctx.BOLEAN().getText() == "True") else BooleanLiteral(False)
        elif ctx.LSTRING():
            return StringLiteral((ctx.LSTRING().getText()))
        else: 
            return self.visitArraylit(ctx.arraylit())


    # Visit a parse tree produced by BKITParser#bool_array.
    def visitBool_array(self, ctx:BKITParser.Bool_arrayContext):
        a = [bool(i.getText()) for i in ctx.BOLEAN()]
        lst = [BooleanLiteral(n) for n in a]
        return lst


    # Visit a parse tree produced by BKITParser#int_array.
    def visitInt_array(self, ctx:BKITParser.Int_arrayContext):
        a = [int(i.getText(), 0) for i in ctx.INTEGER()]
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
        lst = [i for i in ctx.element()]
        return reduce(lambda x,y: x + self.visitElement(y), lst, [])


    # Visit a parse tree produced by BKITParser#element.
    def visitElement(self, ctx:BKITParser.ElementContext):
        return self.visitArray_index(ctx.array_index()) if ctx.array_index() else [ArrayLiteral(self.visitArray_list(ctx.array_list()))]

        # Visit a parse tree produced by BKITParser#arraylit.
    def visitArraylit(self, ctx:BKITParser.ArraylitContext):
        return ArrayLiteral(self.visitArray_list(ctx.array_list()))
        
        