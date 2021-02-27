import os

directory = os.getcwd()

for file in os.listdir(directory):

	noext,ext = os.path.splitext(file)

	newfile = ''.join(e for e in noext if e.isalnum() or e == '-' or e == '_')
	newfile = newfile + ext
	os.rename(os.path.join(directory, file), os.path.join(directory, newfile))

