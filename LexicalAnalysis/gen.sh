#!/bin/bash

if [ $# -eq 0 ]
	then 
		read -p 'Grammar name : ' grammar_name
	else
		grammar_name=$1
fi

java -jar $ANTLR_JAR $grammar_name.g4
javac $grammar_name*.java
echo $grammar_name 
