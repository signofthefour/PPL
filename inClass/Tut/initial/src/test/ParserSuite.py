import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_var_declare(self):
        """Simple variable declare"""
        input = """int a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1))
    
    def test_simple_var_declare_2(self):
        """Simple variable declare 2"""
        input = """int a,b,c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,2))

    def test_simple_var_declare_3(self):
        """Simple variable declare 3"""
        input = """int a,b,c; float a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,3))

    def test_simple_func_call_err(self):
        """Simple func call"""
        input = """int a ();"""
        expect = "Error on line 1 col 8: ;"
        self.assertTrue(TestParser.checkParser(input,expect,4))

    def test_simple_func_call_2(self):
        """Simple func call"""
        input = """a (1);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,5))

    def test_simple_func_call_3(self):
        """Simple func call 2"""
        input = """a (1, a, b, 5);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,6))

    def test_simple_func_call_4(self):
        """Simple func call 2"""
        input = """a (1, a+3*x, b(5), 5); """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,7))
    
    def test_simple_exp(self):
        """Simple func exp"""
        input = """a (a); """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,8))

    def test_simple_pro(self):
        """Simple program"""
        input = """ int a , b , c ;
                    float foo ( int a ; float c, d ) {
                    int e ;
                    e = a + 4 ;
                    c = a*d/2.0 ;
                    return c + 1 ;
                }
                float goo(float a , b ) {
                    return foo ( 1 , a , b ) ;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,9))


    def test_simple_pro_2(self):
        """Simple program 2"""
        input = """int main(int a; float b,c) {
                    run(a + b, (a*0), func1());
                    int e, d;
                    e = (a*(a-c + d)) * foo(c);
                    d = a +  c - d / e;               
                    return e + d;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,10))
    def test_input (self):
        """Simple program 2"""
        input = """hello a;"""
        expect = "Error on line 1 col 0: hello"
        self.assertTrue(TestParser.checkParser(input,expect,11))