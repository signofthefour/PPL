class O: 
    pass

class A(O): 
    def foo(self): 
        print('in A')

class C(O):
    def foo(self):
        print('in C')

class B(O):
    pass

class D(B, A):
    pass

class E(C, A):
    pass

class F(E, D, B):
    pass

if __name__ == '__main__':
    print(F.mro())
    F().foo() # invoked C because C  appears before A in class resolutions of mro algo