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
        self.left  = opl.eval()
        self.right = opr.eval()

    def eval(self):
        if (self.op == '+'): 
            return self.left + self.right
        elif (self.op == '-'): 
            return self.left - self.right
        elif (self.op == '*'): 
            return self.left * self.right
        elif (self.op == '/'): 
            return self.left / self.right
    
    def print(self):
        print('============', self.left, '======', self.right)

class UnExp(Exp):
    def __init__(self, op, val):
        self.val = val.eval()
        self.op  = op
    
    def  eval(self):
        if self.op == '+':
            return self.val
        
        if self.op == '-':
            return (0)-self.val

class IntLit (Exp):
    def __init__(self, val):
        self.val = int(val)


    def eval(self):
        return self.val

class FloatLit(Exp): 
    def __init__(self, val):
        self.val = float(val)
    

    def eval(self):
        return self.val

x1 = IntLit(3)
x2 = IntLit(4)
x3 = FloatLit(2.0)
x4 = BinExp(x2, '*', x3)
x5 = BinExp(x1, '+', x4)
x6 = UnExp('-', x5)
x5.print()
print(x5.eval())
print(x6.eval())