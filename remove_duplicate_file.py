import zipfile
import sys
import os
import csv
import shutil

zippath = sys.argv[1]
if zippath is '':
	print('first parameter need to input the zip file path')
	sys.exit()

if not zipfile.is_zipfile(zippath):
	print('Cannot load zip file in ' + zippath)
	sys.exit()

z = zipfile.ZipFile(zippath, 'r')
z.extract('duplicate_file.csv', './')
z.close()

if not os.path.exists('./duplicate_file.csv'):
	print('Extract duplicate_file.csv error')
	sys.exit()

backPath = 'backup'

if not os.path.exists(backPath):
	os.mkdir(backPath)

SIZE = '大小(Byte)'
SIZE_IDX = 3
PATH = '文件'
PATH_IDX = 2
ALL = '群组\t共享文件夹\t文件\t大小(Byte)\t修改时间'

with open('duplicate_file.csv', 'r', encoding='utf-16') as f:
	reader = csv.DictReader(f,delimiter='\t')
	beforeRowArr =  None
	for row in reader:
		print(row)
		# rowArr = row[0].split('\t')
		# rowArr = row[ALL].split('\t')
		rowArr = row
		print(rowArr)
		try:
			# if beforeRowArr is not None and beforeRowArr[SIZE_IDX] == rowArr[SIZE_IDX]:
			# 	shutil.move(rowArr[PATH_IDX].replace('"',''), backPath + '/')
			if beforeRowArr is not None and beforeRowArr[SIZE] == rowArr[SIZE]:
				shutil.move(rowArr[PATH].replace('"',''), backPath + '/')
		except Exception as e:
			print('Catch exception:', e) 
		beforeRowArr = rowArr


