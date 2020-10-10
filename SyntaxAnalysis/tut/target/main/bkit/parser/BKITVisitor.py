# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_declare.
    def visitVar_declare(self, ctx:BKITParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_declare.
    def visitFunction_declare(self, ctx:BKITParser.Function_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_body.
    def visitFunction_body(self, ctx:BKITParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ids_list_with_type.
    def visitIds_list_with_type(self, ctx:BKITParser.Ids_list_with_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt.
    def visitStmt(self, ctx:BKITParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stmt.
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ret_stmt.
    def visitRet_stmt(self, ctx:BKITParser.Ret_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr.
    def visitExpr(self, ctx:BKITParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#subexpr.
    def visitSubexpr(self, ctx:BKITParser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr0.
    def visitExpr0(self, ctx:BKITParser.Expr0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr1.
    def visitExpr1(self, ctx:BKITParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr2.
    def visitExpr2(self, ctx:BKITParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ids_list.
    def visitIds_list(self, ctx:BKITParser.Ids_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#primitive_type.
    def visitPrimitive_type(self, ctx:BKITParser.Primitive_typeContext):
        return self.visitChildren(ctx)



del BKITParser