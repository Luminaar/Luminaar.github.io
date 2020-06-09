#! /bin/bash

asciidoctor -a stylesheet=customized.css -a stylesdir=$PWD $1;
output=${1/adoc/html}
python3.7 customize.py $output;
