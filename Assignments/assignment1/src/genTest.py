import sys,os

def gen_lexer_testcase():
    f = open("./test/LexerSuite.py", "a")
    done = False
    idx = int(input("Start index: "))
    while not done:
        print("Enter the input (type donein to end the input, stop to end the genprocess): ")
        lines = []
        line_idx=1
        while True:
            line = input("#" + str(line_idx)  + ": ",)
            line_idx+=1
            if line == "stop":
                f.close()
                return
            if line != "donein":
                lines.append(line)
            else:
                break
        input_str = '\n'.join(lines)
        expect_str = str(input("Enter the expected tokens separates by comma without <EOF>: ")) + ",<EOF>"
        testcase_name = str(input("Enter the name without prefix test_: "))
        testcase = "\n    def test_" + testcase_name + "(self):\n        input=\"\"\"" + input_str  + "\"\"\"\n        expect=\"\"\""+ expect_str + "\"\"\"\n        num="+str(idx) + "\n        self.assertTrue(TestLexer.checkLexeme(input, expect, num))\n\n"
        idx+=1
        f.write(testcase)
    f.close()

def gen_parser_testcase():
    f = open("./test/ParserSuite.py", "a")
    done = False
    idx = int(input("Start index: "))
    while not done:
        print("Enter the input (type donein to end the input, stop to end the genprocess): ")
        lines = []
        line_idx=1
        while True:
            line = input("#" + str(line_idx)  + ": ",)
            line_idx+=1
            if line == "stop":
                f.close()
                return
            if line != "donein":
                lines.append(line)
            else:
                break
        input_str = '\n'.join(lines)
        expect_str = str(input("Enter the expected result: "))
        testcase_name = str(input("Enter the name without prefix test_: "))
        testcase = "\n    def test_" + testcase_name + "(self):\n        input=\"\"\"" + input_str  + "\"\"\"\n        expect=\"\"\""+ expect_str + "\"\"\"\n        num="+str(idx) + "\n        self.assertTrue(TestParser.checkParser(input, expect, num))\n\n"
        idx+=1
        f.write(testcase)
    f.close()

def main(argv):
    if len(argv) < 1:
        argv.append(str(input("Please enter mode (lexer/parser): ")))

    if argv[0] == "lexer":
        gen_lexer_testcase()

    if argv[0] == "parser":
        gen_parser_testcase()

if __name__ =="__main__":
    main(sys.argv[1:])
