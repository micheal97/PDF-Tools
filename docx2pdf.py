from docx2pdf import convert

ques = input('File name or file path: ')
ques1 = input('File name or file path without extension: ')

while True:
	if ques.endswith('.docx'):
		try:
			convert(ques,ques1 + "-p.pdf")
		except:
			continue
	elif ques.endwith('.doc'):
		print('Set file extension to ".docx".')
	else:
		print('Please enter a valid file or directory.')
	break

print('\nDone!')
