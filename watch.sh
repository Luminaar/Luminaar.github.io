#! /bin/bash

# Requires `entr` binary - http://eradman.com/entrproject/

echo $1 | entr ./make.sh $1

