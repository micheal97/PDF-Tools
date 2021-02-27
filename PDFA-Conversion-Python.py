ext = "-p.pdf"

import os

cwd = os.getcwd()

directory = os.fsencode(cwd)
    


import os
import ghostscript

directory = os.fsencode(directory)
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".pdf"): 
        length = len(filename)
        filename = filename[:length-4]
        args = ['-dPDFA','-dBATCH','-dNOPAUSE','-dUseCIEColor',
        '-sProcessColorModel=DeviceCMYK','-sPAPERSIZE=a4',
        '-aDEVICE=pdfwrite','-sPDFACompatibilityPolicy=1',
        '-sOutputFile='+filename+ext,filename+'.pdf']
        ghostscript.Ghostscript(args)
        continue
    else:
        continue
gs.exit()


