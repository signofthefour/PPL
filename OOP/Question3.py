class Expr:
    pass

class Var(Expr):
    def __init__(self, _name):
        self.name = _name
    
    def get_val(self):
        return Number(float(1))

class Number(Expr):
    def __init__(self, _number):
        self.number = _number

    def print(self):
        print(str(self.number))

    def get_val(self):
        return self

    def __add__(self, op):
        return Number(self.number + op.number)

    def __sub__(self, op):
        return Number(self.number - op.number)
    
    def __mul__(self, op):
        return Number(self.number * op.number)
    
    def __div__(self, op):
        return Number(self.number / op.number)

class UnOp(Expr):
    def __init__(self, _op, _arg):
        self.operator = _op
        self.arg = _arg
    
    def eval(self):

        if isinstance(self.arg, (Var, Number)):
            self.arg = self.arg.get_val()
        else: self.arg = self.arg.eval()

        if self.operator == "+":
            return self.arg
        
        if self.operator == "-":
            return Number(0)-self.arg
    

class BinOp(Expr):
    def __init__(self, _op, _left, _right):
        self.operator = _op
        self.left = _left
        self.right = _right

    def eval(self):
        if isinstance(self.left, (Var, Number)):
            self.left = self.left.get_val()
        else: self.left = self.left.eval()

        if isinstance(self.right, (Var, Number)):
            self.right = self.right.get_val()
        else: self.right = self.right.eval()

        if self.operator == "+":
            return self.left + self.right
        
        if self.operator == "-":
            return self.left - self.right

        if self.operator == "*":
            return self.left * self.right

        if self.operator == "/":
            return self.left / self.right


x = Var("x")
v = BinOp("+", x, Number(0.2))
t = BinOp("*", v, Number(3))
k = UnOp('-', UnOp('+', Number(1)))
t.eval().print()
k.eval().print()