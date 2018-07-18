
'''
递归函数：
	调用本函数	
	实现递归:
		1.找递归点
		2.找递归终止条件
'''

# 求给定整型数的前n项和
def sumn(n):
	if n == 0:
		return 0
	return n + sumn(n-1)

print(sumn(100))

'''
汉诺塔问题
'''
cnt = 0
def move(m, n):
	global cnt
	cnt += 1
	print(m,"--->", n)

def hano(n, a, b, c): # 将a上的n个圆盘移动到b
	if n == 1:
		move(a, b)
		return None
	hano(n-1, a, c, b)
	hano(1, a, b, c)
	hano(n-1, c, b, a)

hano(3, 'a', 'b', 'c')
print("共{}次".format(cnt))


'''
rm 

def delfile(path):
	if path是目录 == False:
		del path
		return None
	else:
		是目录
		p = 打开目录---》得到目录下每一个文件的路径
		delfile(p)
'''

