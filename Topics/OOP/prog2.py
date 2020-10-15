class Exp:
    def __init__(self, val):
        self.val = val

    def print(self):
        print(str(self.val))

    def get_val(self):
        return self
    
    def eval(self):
        return self.val

class BinExp(Exp):
    def __init__(self, opl, operator, opr):
        self.op = operator
        self.left  = opl
        self.right = opr

    def eval(self):
        if (self.op == '+'): 
            return self.left.eval() + self.right.eval()
        elif (self.op == '-'): 
            return self.left.eval() - self.right.eval()
        elif (self.op == '*'): 
            return self.left.eval() * self.right.eval()
        elif (self.op == '/'): 
            return self.left.eval() / self.right.eval()
    
    def print(self):
        print('============', self.left.eval(), '======', self.right.eval())

    def printPrefix(self):
        if (isinstance(self.left, BinExp)):
            return ()

class UnExp(Exp):
    def __init__(self, op, val):
        self.val = val
        self.op  = op
    
    def  eval(self):
        if (isinstance(self.val, IntLit)):
            if self.op == '+':
                return self.val.eval()      
            elif self.op == '-':
                return (0)-self.val.eval()
        else: 
            if self.op == '+':
                return self.val       
            elif self.op == '-':
                return (0)-self.val
    def printPrefix(self):
        if (isinstance(self.val , IntLit) or (isinstance(self.val, FloatLit))):
            return (str (self.op + '.' + self.val.printPrefix))
        else:
            return (self.val.op + ' ' + self.op + '.' + self.val.printPrefix() )

class IntLit (Exp):
    def __init__(self, val):
        self.val = int(val)

    def eval(self):
        return self.val

    def printPrefix(self):
        return str(self.val)

class FloatLit(Exp): 
    def __init__(self, val):
        self.val = float(val)

    def eval(self):
        return self.val

    def printPrefix(self):
        return str(self.val)


x1 = IntLit(4)
x2 = IntLit(3)
x3 = IntLit(2)
x4 = BinExp(x2, '*', x3)
x5 = BinExp(x1, '+', x4)
x6 = UnExp('-', x5)
x7 = BinExp(x5, '*', UnExp('-', x1))
print(x7.eval())




xa = UnExp('-', x1)
xb = BinExp(x2, '*' , x3)
xc = BinExp(xa, '+', xb)

print(xc.eval())
print(xc.eval())