import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    def test_escape_sequence(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\t def"  ""","""abc\\t def,<EOF>""",103))

    def test_real_without_e(self):
        """test real without e"""
        self.assertTrue(TestLexer.checkLexeme("12.02", "12.02,<EOF>", 104))

    def test_id_and_real(self):
        self.assertTrue(TestLexer.checkLexeme("abc 12 asdfjh", "abc,12,asdfjh,<EOF>", 105))

    def test_error_token(self):
        self.assertTrue(TestLexer.checkLexeme("absa?sad", "absa,ERROR_CHAR ?", 106))

    def test_sing_quote_string(self):
        self.assertTrue(TestLexer.checkLexeme(""""abc\\'def" """, """abc\\'def,<EOF>""",107))
    
    def test_illegal_esc(self):
        self.assertTrue(TestLexer.checkLexeme(""""abc\\has" """, "ILLEGAL_ESCAPE \"abc\h", 108))

    def test_double_quote_in_str(self):
        self.assertTrue(TestLexer.checkLexeme(""""He asked me: '"What is this?'"." """, """He asked me: '"What is this?'".,<EOF>""",109))
    
    def test_normal_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc" """, """abc,<EOF>""", 110))

    def test_unclose_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc """, """UNCLOSE_STRING abc """, 111))
