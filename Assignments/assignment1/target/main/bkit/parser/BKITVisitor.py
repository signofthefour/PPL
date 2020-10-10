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


    # Visit a parse tree produced by BKITParser#primitive_data.
    def visitPrimitive_data(self, ctx:BKITParser.Primitive_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#composite_data.
    def visitComposite_data(self, ctx:BKITParser.Composite_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_list.
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_non_init.
    def visitVar_non_init(self, ctx:BKITParser.Var_non_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_init.
    def visitVar_init(self, ctx:BKITParser.Var_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#composite_init.
    def visitComposite_init(self, ctx:BKITParser.Composite_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#primitive_init.
    def visitPrimitive_init(self, ctx:BKITParser.Primitive_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bool_op.
    def visitBool_op(self, ctx:BKITParser.Bool_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_op.
    def visitInt_op(self, ctx:BKITParser.Int_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_op.
    def visitFloat_op(self, ctx:BKITParser.Float_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dowhile_stmt.
    def visitDowhile_stmt(self, ctx:BKITParser.Dowhile_stmtContext):
        return self.visitChildren(ctx)



del BKITParser