import os
import argparse
import sys,os
sys.path.append('./test/')
import subprocess
import unittest
from antlr4 import *
from tqdm import tqdm

#Make sure that ANTLR_JAR is set to antlr-4.8-complete.jar
ANTLR_JAR = os.environ.get('ANTLR_JAR')
TARGET = '../target/main/bkit/parser' if os.name == 'posix' else os.path.normpath('../target/')
locpath = ['./main/bkit/parser/','./main/bkit/astgen/','./main/bkit/utils/']
for p in locpath:
    if not p in sys.path:
        sys.path.append(p)

sys.path.append('../target/main/bkit/parser')

from BKITLexer import BKITLexer
from BKITParser import BKITParser
from lexererr import *
from ASTGeneration import ASTGeneration

SUITE_DIR = r'./test/ASTGenSuite.py'
TESTCASE_FOLDER_DIR = r'./test/testcases/'
SOL_FOLDER_DIR = r'./test/solutions/'

HEADER = """
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    
"""

def gen_function(inp, expect, filename):
    name = "\tdef test_" + filename[:3] + "(self):" + '\n'
    input_line = "\t\tinput = \"\"\"" + inp + "\"\"\"" + '\n'
    expect_line = "\t\texpect = " + expect + '\n'
    assert_line = "\t\tself.assertTrue(TestAST.checkASTGen(input,expect," +filename[:3] + "))" + '\n\n'
    return name + input_line + expect_line + assert_line

def load_input(filename):
    inp = ""
    with open(os.path.join(TESTCASE_FOLDER_DIR, filename), 'r') as f:
        inp = ''.join(list(f))

    return inp

def load_expc(filename):
    expc = ""
    with open(os.path.join(SOL_FOLDER_DIR, filename), 'r') as f:
        expc = ''.join(list(f))
    
    return expc

def ensures_dir(directory: str):
    if len(directory) > 0 and not os.path.exists(directory):
        raise Exception("There is an existing dir")

def gen_sol(testcase_dir, solution_dir):
    test_files = os.listdir(testcase_dir)
    for filename in tqdm(test_files, desc="Build solution"):
        print(filename)
        inputfile = FileStream(os.path.join(testcase_dir,filename))
        dest = open(os.path.join(solution_dir, filename),"w")
        lexer = BKITLexer(inputfile)
        tokens = CommonTokenStream(lexer)
        parser = BKITParser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)
        dest.write(str(asttree))
        dest.close()

def main(args):
    ensures_dir(args.testcase_dir)
    ensures_dir(args.solution_dir)
    ensures_dir(args.suite_dir)

    if args.gen_sol:
        gen_sol(args.testcase_dir, args.solution_dir)
    
    test_files = os.listdir(args.testcase_dir)
    sol_files = os.listdir(args.solution_dir)
    if not (len(list(test_files)) == len(list(sol_files))):
        print("The number of sol file and test file are not the same, check it!".upper())
    file_str = HEADER
    try:
        for filename in tqdm(test_files):
            inp = load_input(filename)
            expc = load_expc(filename)
            
            file_str += gen_function(inp, expc, filename)
        with open(args.suite_dir, 'w') as f:
            f.write(file_str)
    except:
        print("An exception occurred when running gen testcase".upper())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Expect dir for gen process.')
    parser.add_argument('--testcase_dir', type=str, default=TESTCASE_FOLDER_DIR, help="the testcase directory where you store the testcase in *.txt format")
    parser.add_argument('--solution_dir', type=str, default=SOL_FOLDER_DIR, help="the testcase directory where you store the solution in *.txt format if there is no solution, please active the gen_sold")
    parser.add_argument('--suite_dir', type=str, default=SUITE_DIR, help="the testcase directory where you store the solution in *.txt format if there is no solution, please active the gen_sold")
    parser.add_argument('--gen_sol', type=bool, default=False, help="active the gen solution, you need to place the AST_GEN_TEST.py in the same dir with AST.py")

    args = parser.parse_args()
    main(args)