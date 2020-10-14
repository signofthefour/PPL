class Rational:
    def __init__(self, n, d = 1):
        if (d != 0):
            self.n = n
            self.d = d
            g = self.__gcd__(n, d)
            self.numer = int(n / g)
            self.denom = int(d / g)
    
    
    def __gcd__(self, a, b):
        if b == 0:
            return a
        else:
            return self.__gcd__(b, a%b)

    def __print__(self): #check data
        print(self.__gcd__(1,2))
        print("n = ", self.n)
        print("d = ", self.d)
        print(self.numer)
        print(self.denom)

    def __add__(self, operator):
        if isinstance(operator, int):
            return self + Rational(operator)
        return Rational((int(self.numer * operator.denom) + int(self.denom * operator.numer)), int(self.denom * operator.denom))

    def toString(self):
        return str(self.numer) + "/" +  str(self.denom)

obj = Rational(18,27)
obj.__print__()
b = 2
c = obj + b
print(c.toString())
print(obj.toString())