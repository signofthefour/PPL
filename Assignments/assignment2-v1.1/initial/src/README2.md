# AST TREE GEN

## TEST_GEN_TOOL

**Download files: AST_GEN_TEST.py, gen_test.py then place them in the same folder with AST.py and run.py respectively**

You need to install some module if not installed, like this one:

```bash
pip install tqdm
```

To generate the ASTGenSuite.py, you need to write all testcases in format .txt which are store a same <test_folder_dir>. After prepare all the testcase, or some of them, you can gen by the gen_test.py. To see help:

```bash
python gen_test.py -h

optional arguments:
  -h, --help            show this help message and exit
  --testcase_dir TESTCASE_DIR
                        the testcase directory where you store the testcase in *.txt format
  --solution_dir SOLUTION_DIR
                        the testcase directory where you store the solution in *.txt format if there is no solution, please active the gen_sold
  --suite_dir SUITE_DIR
                        the testcase directory where you store the solution in *.txt format if there is no solution, please active the gen_sold
  --gen_sol GEN_SOL     active the gen solution, you need to place the AST_GEN_TEST.py in the same dir with AST.py
```

For the first time, you have to active the --gen_sol by True value to generate the solution in full options in the <sol_folder_dir>.

```bash
python gen_test.py --testcase_dir <test_folder_dir> --solution_dir <sol_folder_dir> --suite_dir ASTGenSuite.py --gen_sol True
```

You can also ignore any of them if you satisfy with the default of them below:

<suite_dir>: './test/ASTGenSuite.py'

<test_folder_dir>: './test/testcases/'

<sol_folder_dir>: './test/solutions/'

<gen_sol>: False

## GEN TESTCASE

First of all, let replace the AST module by the AST_GEN_TEST.py:

```python
# from AST import *
from AST_GEN_TEST import * 
```

Then run something like:

```bash
python gen_test.py --gen_sol True
```

After this, there will be a full of testcases ASTGenSuite.py. Inactive the AST_GEN_TEST and active AST:

```python
from AST import *
# from AST_GEN_TEST import * 
```

Now, you can use this AST_GEN_SUITE to check your ASTGeneration as normal as nothing happen.

```bash
python run.py test ASTGenSuite
```

**DISCLAIMER:** I write this tool in only 1 hour so be careful with the error. Please commit you repo before use this tool in order to avoid any problem. If you see some bugs of the gen processs, please fix it yourself or report it to my [facebook](fb.com/sotfdat) for help (I rarely reply the message from stranger).