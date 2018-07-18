
'''
python全局变量和局部变量
	全局:函数外部
	局部:函数内（形式参数）
'''

n = 100
m = 987

def test(a, b):
	global n # global关键字 使得在函数内使用全局
	print(m) # 在函数内没有定义新的变量，直接访问，自动访问全局变量
	n = a + b # 在test函数内变量，新的局部变量
	return n

test(10, 20)
print(n)
#print(a, b)

