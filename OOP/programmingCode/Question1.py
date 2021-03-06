class Exp:
    def accept(self, func):
        pass

class IntLit(Exp):
    def __init__(self, _val):
        self.val = int(_val)
    
    def eval(self):
        return self.val

    def printPrefix(self):
        return str(self.val)
    
    def printPostfix(self):
        return str(self.val)


class FloatLit(Exp):
    def __init__(self, _num):
        self.val = float(_num)

    def eval(self):
        return self.val

    def printPrefix(self):
        return str(self.val)

    def printPostfix(self):
        return str(self.val)

class UnExp(Exp):
    def __init__(self, _op, _arg):
        self.operator = _op
        self.arg = _arg
    
    def eval(self):
        if self.operator == '+':
            return self.eval()
        
        if self.operator == '-':
            return 0 - self.arg.eval()
    
    def printPrefix(self):
        return self.operator + '.' + ' ' + self.arg.printPrefix()

    def printPostfix(self):
        return self.arg.printPostfix() + " ." + self.operator
    

class BinExp(Exp):
    def __init__(self, _left, _op, _right):
        self.operator = _op
        self.left = _left
        self.right = _right

    def eval(self):
        if self.operator == '+':
            return self.left.eval() + self.right.eval()
        
        if self.operator == '-':
            return self.left.eval() - self.right.eval()

        if self.operator == '*':
            return self.left.eval() * self.right.eval()

        if self.operator == '/':
            return self.left.eval() / self.right.eval()
        else:
            return None

    def printPrefix(self):
        return self.operator + ' ' + self.left.printPrefix() + ' ' + self.right.printPrefix()

# class PrintPostfix():
    
#     def printPostfix(self):
#         return self.left.printPostfix() + ' ' + self.right.printPostfix() + ' ' + self.operator

x0 = IntLit(1)
x1 = UnExp("+", x0)
x2 = IntLit(1)
x3 = IntLit(2)
x4 = BinExp(x2, "*", x3)
print(x4.printPrefix())
# print(x5.printPostfix())
# print(x5.accept(x5.printPostfix))