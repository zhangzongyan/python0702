

'''
嘻嘻哈哈哈
'''

def func():
	'''	此函数没有功能，注释 '''
	print("这是一个测试")

# 匿名函数
f = lambda x, y : x + y
print(type(f))

print(f(10, 20))

f2 = lambda n : print("偶数") if not(n % 2) else print("奇数")
f2(100)

func()
print(func.__doc__)


# 关键字传参
def rgs(name, age, sex='f', **kw):
	print(name, age, sex)
	print(type(kw))
	print(kw)

rgs("python", 28, heigth=180, weight=70, sex='m')







