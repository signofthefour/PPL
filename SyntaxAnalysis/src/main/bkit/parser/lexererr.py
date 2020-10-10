
class LexerError(Exception):
    pass

class ErrorToken(LexerError):
    def __init__(self,s):
        self.message = "ERROR_CHAR "+ s

class UncloseString(LexerError):
    def __init__(self,s):
        self.message = "UNCLOSE_STRING "+ s

class IllegalEscape(LexerError):
    def __init__(self,s):
        self.message = "ILLEGAL_ESCAPE "+ s

class UnterminatedComment(LexerError):
    def __init__(self):
        self.message = "UNTERMINATED_COMMENT"



