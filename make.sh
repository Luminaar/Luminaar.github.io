#! /bin/bash

asciidoctor $1;
output=${1/adoc/html}
python3.7 customize.py $output;
