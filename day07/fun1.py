
# 函数的传参方式: 固定参数 可变参数 默认参数

'''
两个整型数的差
'''
def sub2num(m, n):
	return m - n

print(sub2num(n=10, m=20))


'''
# 计算给定一个数的n次方

默认参数
	形参(形式参数):函数定义的时候，参数列表中的所有的参数
	实参(实际参数):函数调用的时候，传递的参数
'''
def sumn(n, m = 2):
	return n ** m	

print(sumn(10))
print(sumn(10, m=3))

'''
统计所有形参的和

可变参数
'''
def sumall(*arg):
	s = 0
	for i in arg:
		#print(i)
		s += i
	return s 

print(sumall(1,2,6,3,9,5))
print(sumall())


# !!!!当一个函数内同时有默认参数和可变参数,先可变后默认,调用函数时默认参数最后通过参数名传参

def test(arg1, *arg3, arg2=100):
	print(arg1, arg2)
	for i in arg3:
		print(i)

test(1, 1, 2, 3, 4, 5, arg2=999)


