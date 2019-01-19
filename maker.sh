#!/bin/bash

NAME=`echo $1 | rev | cut -c 5- | rev`
PDF="${NAME}.pdf"
TEX="${NAME}.tex"
python ./spell_conv.py $1 && pdflatex $TEX && open $PDF