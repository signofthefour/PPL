class Rational:
    def __init__(self, n=0, d=1):
        g = self.__gcd(n, d)
        self.number = int(n / g)
        self.denom = int(d / g)
    
    def __gcd(self, n, d):
        if d == 0:
            return n
        else:
            return self.__gcd(d, n%d)

    def __add__(self, op):
        if isinstance(op, int):
            return self + Rational(op)
        return Rational((int(self.number * op.denom) + int(self.denom * op.number)), int(self.denom * op.denom))

    def toString(self):
        return str(self.number) + "/" + str(self.denom)

a = Rational(6, 4)
b = 2
c = a + b
print(a.toString())
print(c.toString())