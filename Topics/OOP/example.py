class Emplyee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Emplyee.empCount += 1

    @classmethod
    def __create__(cls, n, s):
        print(cls.empCount)
        return cls(n, s)

    def __print__(self):
        print("Name : ", self.name, ", Salary : " , self.salary)

    @staticmethod
    def __isHighSal__():
        print("heeloos")

obj = Emplyee.__create__( "Khanh", 500)
Emplyee.__isHighSal__()



class A:
    def __foo__(self, x):
        print(x)

    def foo2(self, x):
        print(x + 2)

class B(A):
    def foo(self, x):
        super().__foo__(x)

B().foo(3)
x = B()
print (type(x) is A)
print (isinstance(x, A))