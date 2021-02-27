PDF-Tools README.md





Requires Python: Download from Microsoft Store or Python.org - use Python 3.6+



Required Modules:



docx2pdf.py: docx2pdf module (pip install docx2pdf - add to PATH)

comtypesdocx2pdf.py: requires comtypes (pip install comtypes)

rename.py: os - included with python

pdfa.bat/pdfa.sh: Ghostscript (download from ghostscript website or HomeBrew - add to PATH)




rename.py takes input(); enter DIRECTORY for the folder - all non-alphanumeric characters (besides whitespace and hyphens) will be removed from filenames

docx2pdf takes input() - enter a file or directory - converts .docx (note: does not work with .doc) to .pdf - includes markup

comtypesdocx2pdf.py uses sys.argv[] - type commands in command line while running program - converts .docx (note: does not work with .doc) to .pdf - enter FULL filepath - includes markup

pdfa.bat/pdfa.sh takes no input - performs PDF/A-1b ISO 19005-1 (unverified) Standard conversion on all .pdf files in the current folder (unless they have invalid characters or spaces - perform rename.py first)



No Licence!
