import os, sys, zipfile

def zipFiles():
	zf = zipfile.ZipFile('output.zip', 'w')
	howMany = eval(input('How many files do you need to zip? '))
	for i in range(0, howMany):
		filename = input('Please give me the location of the file: ')
		filetoZip = os.path.abspath(filename)
		print('Now zipping filetoZip')
		zf.write(filetoZip,os.path.basename(filetoZip))
	print('All files have been zipped! Enjoy')
	zf.close()

zipFiles()