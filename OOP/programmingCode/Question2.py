class Exp:
    pass

class IntLit(Exp):
    def __init__(self, _val):
        self.val = int(_val)
    
    def accept(self, visitor):
        return visitor.intlit(self.val)


class FloatLit(Exp):
    def __init__(self, _num):
        self.val = float(_num)

    def accept(self, visitor):
        return visitor.floatlit(self.val)

class UnExp(Exp):
    def __init__(self, _op, _arg):
        self.operator = _op
        self.arg = _arg
    
    def accept(self, visitor):
        return visitor.unexp(self.operator, self.arg)

class BinExp(Exp):
    def __init__(self, _left, _op, _right):
        self.operator = _op
        self.left = _left
        self.right = _right

    def accept(self, visitor):
        return visitor.binexp(self.left, self.operator, self.right)

class Eval(Exp):
    def __init__(self):
        pass

    def intlit(self, x):
        return x

    def floatlit(self, x):
        return x

    def binexp(self, _left, _op, _right):

        if _op == '+':
            return _left.accept(Eval()) + _right.accept(Eval())
        elif _op == '-':
            return _left.accept(Eval()) - _right.accept(Eval())
        elif _op == '*':
            return _left.accept(Eval()) * _right.accept(Eval())
        elif _op == '/':
            return _left.accept(Eval()) / _right.accept(Eval())
    
    def unexp(self, _op, _arg):
        if _op == '+':
            return _arg.accept(Eval())
        elif _op == '-':
            return - _arg.accept(Eval())

class PrintPrefix():
    def __init__(self):
        pass

    def intlit(self, _val):
        return str(_val)

    def floatlit(self, _val):
        return str(_val)

    def binexp(self, _left, _op, _right):
        return _op + ' ' + _left.accept(PrintPrefix()) + ' ' + _right.accept(PrintPrefix())

    def unexp(self, _op, _arg):
        return _op + '.' + ' ' + _arg.accept(PrintPrefix())

class PrintPostfix():
    def __init__(self):
        pass

    def intlit(self, _val):
        return str(_val)

    def floatlit(self, _val):
        return str(_val)

    def binexp(self, _left, _op, _right):
        return _left.accept(PrintPostfix()) + ' ' + _right.accept(PrintPostfix()) + ' ' + _op

    def unexp(self, _op, _arg):
        return _arg.accept(PrintPostfix()) + ' ' + _op + '.'


x1 = IntLit(3)
x2 = IntLit(4)
x3 = FloatLit(2.0)

x4 = BinExp(x2, '*', x3)
x5 = BinExp(x1, '+', x4)
x6 = UnExp('-', x5)
# -(3 + 4 * 2.0)
x7 = BinExp(x5, '*', UnExp('-', x1))
# 3 + 4 * 2.0 * -3
x8 = BinExp(UnExp('-', x1), '*', x5)

x9 = BinExp(x1, "+", x2)

# print(x6.eval())
# print(x6.printPrefix())
print(x9.accept(Eval()))
print(x7.accept(Eval()))
print(x7.accept(PrintPrefix()))
print(x7.accept(PrintPostfix()))

print(x8.accept(Eval()))
print(x8.accept(PrintPrefix()))
print(x8.accept(PrintPostfix()))