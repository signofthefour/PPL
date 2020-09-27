#!/bin/bash

rm  ./$1/*.class ./$1/*.java ./$1/*.tokens ./$1/*.interp
rm -r ./$1/.antlr

echo clean!