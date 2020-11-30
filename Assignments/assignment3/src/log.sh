#!/bin/bash
TEST_DIR="./test/testcases"
SOL_DIR="./test/solutions"

if [ $# -eq 1 ]
	then 
		echo -e "\n==========================="
        echo -e "Testcase#"$1 
        echo "***********TEST*******"
        cat $TEST_DIR/$1.txt
        echo
        echo "************SOL**********"
        cat $SOL_DIR/$1.txt
        echo -e "\n==========================="
	else
		for file in $TEST_DIR/*; do
            echo -e "\n==========================="
            echo -e "Testcase#"${file##*/} 
            echo "***********TEST*******"
            cat $TEST_DIR/${file##*/}
            echo
            echo "************SOL**********"
            cat $SOL_DIR/${file##*/}
            echo -e "\n==========================="
        done
fi