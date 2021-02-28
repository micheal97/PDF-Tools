PDF-Tools README.md




Required Modules:



Requires Python: Download from Microsoft Store, Conda, or Python.org - use Python 3.6+

comtypesdocx2pdf.py: requires comtypes (pip install comtypes)

rename.py: os - included with python

pdfa.bat/pdfa.sh: Ghostscript (download from ghostscript website or HomeBrew - add to PATH)




How these programs take input, work, and what they do:



rename.py takes input(); enter DIRECTORY for the folder - all non-alphanumeric characters (besides whitespace and hyphens) will be removed from filenames

comtypesdocx2pdf.py uses input() - converts .docx (note: may not work with .doc) to .pdf - enter FULL filepath - may INCLUDE MARKUP in original Word document

pdfa.bat/pdfa.sh takes no input - performs PDF/A-1b ISO 19005-1 (unverified) Standard conversion on all .pdf files in the current folder (perform rename.py first)



No Licence!
