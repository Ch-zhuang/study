import os
#出现一个逻辑错误就是我程序路径和保存路径一致时会增量添加，因为walk会将原来的再走一遍,然后我就采取了先删除在遍历

def del_dir(path):
	os.chdir(path)
	lists = os.listdir()
	print(os.listdir())
	for i in lists:
		if os.path.isfile(i):
			os.remove(i)
		else :
			del_dir(i)
	os.chdir('..')
	os.removedirs(path)
	print("删除成功！")
	
def searchpdf(path):
	if os.path.isdir(os.path.join(os.getcwd(),'photo')) :
		del_dir(os.path.join(os.getcwd(),'photo'))
	file_name = []
	#遍历所有盘
	for root, dirs, files in os.walk(path):
		for filepath in files:
			pat = os.path.join(root,filepath)
			if (os.path.splitext(pat)[1] == '.jpg') | (os.path.splitext(pat)[1] == '.png'):
				print(path)
				file_name.append(pat)
	f = open('1.txt', 'w')
	for file in file_name :
		f.write(file + '\n')
	f.close()
	print('生成文档成功！')
	print(path)

	#打开图片,将图片保存到一个文件夹下
	'''
	a = os.path.join(os.getcwd(),'photo')
	if os.path.isdir(a):
		os.chdir(a)
		print(os.listdir())
		for i in os.listdir():
			if os.path.isfile(i):
				os.remove(i)
		os.chdir('..')
		os.rmdir(a)
		print("删除成功！")
	'''
	#会在当前运行目录下创建photo
	os.mkdir('photo')
	os.chdir('photo')
	print("创建成功")
	a = 1
	for file in file_name :
		f = open(file,'rb')
		fo = open(str(a)+os.path.splitext(file)[1],'ab')
		fo.write(f.read())
		a = a + 1
	fo.close()
	f.close()		
	print('保存完毕')

path = input('请输入路径：比如C:\\Users\lenovo\Desktop:')
searchpdf(path)
