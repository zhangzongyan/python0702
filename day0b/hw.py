import os
import sys
# 1
def cpyfile(src, dest, n, s):
	f1 = open(src)
	f2 = open(dest, "w")
	nextline = 1 
	for l in f1:
		f2.write(l)
		nextline += 1
		if nextline == n:
			f2.write(s)
	f1.close()
	f2.close()

# 2
def cmp2file(file1, file2):
	f1 = open(file1)	
	f2 = open(file2)
	res = []
	linecnt = 0 

	for l1 in f1:
		linecnt += 1
		l2 = f2.readline()
		if l1 != l2:
			res.append(linecnt)			
	# file2如果没有结束的话....
	while l2 != "":
		l2 = f2.readline()	
		if l2 != "":
			linecnt += 1
			res.append(linecnt)
	f1.close()
	f2.close()
	return res

# 3
def showfile(filepath, line):
	f = open(filepath)
	for i in range(line):
		print(f.readline(), end="")
	f.close()

# 4 在path及其子目录中查找是否有filename文件
def findfile(filename, path):
	print(path)
	os.chdir(path)
	# 获取path下所有的文件名
	for name in os.listdir(path):
		if name == filename:
			return True
		if os.path.isdir(name):
			newpath = os.path.join(path, name) # 拼接子目录的路径
			if findfile(filename, newpath) == True:
				return True
			os.chdir(os.pardir) # os.pardir ---》".." 
	return False

def main():
	'''
	if len(sys.argv) < 4:
		print("至少四个参数")	
	else:
		cpyfile(sys.argv[1], sys.argv[2], 3, sys.argv[3])
	'''
	'''
	if len(sys.argv) < 2:
		print("比较两个文件")
	else:
		dif = cmp2file(sys.argv[1], sys.argv[2])
		if len(dif) == 0:
			print("两个文件没有不一样的地方")
		else:
			for i in dif:
				print("第%d行不一样" % i)
	'''
	'''
	get_input = input("请输入要显示的文件名和行数（文件名:行数）")
	filename, line = get_input.split(":")	
	showfile(filename, int(line))	
	'''
	if len(sys.argv) < 3:
		print("至少三个参数")
	else:
		if findfile(sys.argv[1], sys.argv[2]):
			print("找到了%s" % sys.argv[1])
		else:
			print("在%s下没有%s文件" % (sys.argv[2], sys.argv[1]))

main()






	

