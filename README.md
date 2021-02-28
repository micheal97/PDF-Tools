PDF-Tools README.md




Required Modules:



Requires Python: Download from Microsoft Store, Conda, or Python.org - use Python 3.6+

comtypesdocx2pdf.py: requires comtypes (pip install comtypes)

rename.py: os - included with python

pdfa.bat/pdfa.sh: Ghostscript (download from ghostscript website or HomeBrew - add to PATH)

append.py: Py2PDF2 (or legacy Py2PDF)




How these programs take input, work, and what they do:



rename.py takes no input - all non-alphanumeric characters (besides whitespace and hyphens) will be removed from filenames

comtypesdocx2pdf.py uses input() - converts .docx (note: may not work with .doc) to .pdf - enter FULL filepath - may INCLUDE MARKUP in original Word document

pdfa.bat/pdfa.sh takes no input - performs PDF/A-1b ISO 19005-1 (unverified) Standard conversion on all .pdf files in the current folder (perform rename.py first)

append.py takes no input - performs append action on all folders in a directory

