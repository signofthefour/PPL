from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class Program(AST):
    def __init__(self, _stmt_lsts):
        self.stmt_lsts = _stmt_lsts

class Stmt(AST):
    pass

class Exp(AST):
    pass

class Var_declare(AST):
    def __init__(self, _var_declare):
        self.var_declare = _var_declare  

class Id(Exp):
    def __init__(self, _id):
        self.id  =  _id

class ASTGeneration(BKITVisitor):
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return Program([Var_declare(Id(ctx.var_declare..getText()),[],None)])

