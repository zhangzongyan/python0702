
import os

print(os.getcwd()) # 获取当前工作路径

f = open("test.py")
print(f.read())
f.close()

'''
os.chdir("/home/reala_zhang/") # 切换工作路径
f = open("test.py")
f.close()
'''

#print(os.environ) #获取环境变量

#os.mkdir("newdir2")
#os.rmdir("newdir")

#os.removedirs("newdir/a/b")

file_stat = os.stat("test")
print(file_stat.st_size)

list_dir = os.listdir("/") # 获取给定路径下的所有的文件
print(list_dir)

'''os.path'''
if not os.path.exists("test"): # 判断文件是否存在
	with open("test", "w") as f:
		f.write("hello")

path = "/"
if os.path.isfile(path): # 判断是否是普通文件 
	print("{}是一个普通文件".format(path))
elif os.path.isdir(path):
	print("{}是一个目录文件".format(path))
else:
	print("不知道")

print(os.path.join("/etc", "passwd")) # 组成一个文件的路径
r = os.path.split("/home/reala_zhang/python0702/day0a/test.py") # 切割出文件名
print(r)
		

