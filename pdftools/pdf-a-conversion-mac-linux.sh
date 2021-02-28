#!/bin/bash

#This requires Ghostscript

ext="-p"

for filename in *.pdf 
do

	newfilename=${filename%.pdf}
	newfilename+="-p.pdf"
	gs -dPDFA -dBATCH -dNOPAUSE -dUseCIEColor -sProcessColorModel=DeviceCMYK -sPAPERSIZE=a4 -sDEVICE=pdfwrite -sPDFACompatibilityPolicy=1 -sOutputFile=$newfilename $filename
done
