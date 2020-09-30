#!/bin/bash

export CLASSPATH=".:/home/khanh/Documents/schoolLife/201/PPL/antlr-4.8-complete.jar:$CLASSPATH"
export ANTLR_JAR="/home/khanh/Documents/schoolLife/201/PPL/antlr-4.8-complete.jar"

alias antlr4='java -Xmx500M -cp "/home/khanh/Documents/schoolLife/201/PPL/antlr-4.8-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java -Xmx500M -cp "/home/khanh/Documents/schoolLife/201/PPL/antlr-4.8-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'

echo Done!!