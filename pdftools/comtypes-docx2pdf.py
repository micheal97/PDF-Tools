import sys
import os
import comtypes.client

wdFormatPDF = 17

inp = input('Enter an input file path: ')
out = input('Enter an output file path: ')

in_file = os.path.abspath(inp)
out_file = os.path.abspath(out])

word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()
