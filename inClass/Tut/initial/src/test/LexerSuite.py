import unittest
from TestUtils import TestLexer

class   LexerSuite(unittest.TestCase):

#testcases for question 1:
    def test_question1_identifier_1(self):
        """test question1"""
        self.assertTrue(TestLexer.checkLexeme("a123ax","a123ax,<EOF>",1))

    def test_question1_identifier_2(self):
        self.assertTrue(TestLexer.checkLexeme("asd","asd,<EOF>",2))

    def test_question1_identifier_3(self):
        self.assertTrue(TestLexer.checkLexeme("a","a,<EOF>",3))

    def test_question1_identifier_4(self):
        self.assertTrue(TestLexer.checkLexeme("khanh123","khanh123,<EOF>",4))

    def test_question1_identifier_5(self):
        self.assertTrue(TestLexer.checkLexeme("ko0021","koro0012,<EOF>",5))

    def test_question1_identifier_6(self):
        self.assertTrue(TestLexer.checkLexeme("ok1","ok1,<EOF>",6))

    def test_question1_identifier_7(self):
        self.assertTrue(TestLexer.checkLexeme("ok2","ok2,<EOF>",7))

    def test_question1_identifier_8(self):
        self.assertTrue(TestLexer.checkLexeme("unh1","unh1,<EOF>",8))

    def test_question1_identifier_9(self):
        self.assertTrue(TestLexer.checkLexeme("km82","km82,<EOF>",9))

    def test_question1_identifier_10(self):
        self.assertTrue(TestLexer.checkLexeme("a12","a12,<EOF>",10))

#testcases for question 2: 
    def test_question2_identifier_1(self):
        """test question1"""
        self.assertTrue(TestLexer.checkLexeme("a123ax","a123ax,<EOF>",1))

    def test_question2_identifier_2(self):
        self.assertTrue(TestLexer.checkLexeme("asd","asd,<EOF>",2))

    def test_question2_identifier_3(self):
        self.assertTrue(TestLexer.checkLexeme("a","a,<EOF>",3))

    def test_question2_identifier_4(self):
        self.assertTrue(TestLexer.checkLexeme("khanh123","khanh123,<EOF>",4))

    def test_question2_identifier_5(self):
        self.assertTrue(TestLexer.checkLexeme("ko0021","koro0012,<EOF>",5))

    def test_question2_identifier_6(self):
        self.assertTrue(TestLexer.checkLexeme("ok1","ok1,<EOF>",6))

    def test_question2_identifier_7(self):
        self.assertTrue(TestLexer.checkLexeme("ok2","ok2,<EOF>",7))

    def test_question2_identifier_8(self):
        self.assertTrue(TestLexer.checkLexeme("unh1","unh1,<EOF>",8))

    def test_question2_identifier_9(self):
        self.assertTrue(TestLexer.checkLexeme("km82","km82,<EOF>",9))

    def test_question2_identifier_10(self):
        self.assertTrue(TestLexer.checkLexeme("a12","a12,<EOF>",10))
