import os
from PyPDF2 import PdfFileMerger

x = [a for a in os.listdir() if a.endswith(".pdf")]

merger = PdfFileMerger()

for pdf in x:
    with open(pdf, 'rb') as pdf:                #just added this to close the file again
        merger.append(pdf)                      #else there was no problem for me. 

#if i put some pdf files into this directory and put PyPDF2 there, too, it should work fine

with open("result.pdf", "wb") as fout:
    merger.write(fout)
    
