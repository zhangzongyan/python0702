
'''
tuple:
	不可变类型
'''
# 定义
t = (1,2,3,"hello")
print(type(t))

t = ()
print(type(t))

# 只有一个元素的元祖
t = (1,)
print(type(t))
l = [1,2,3]
t = tuple(l)
print(t)

# 索引 / 切割
print(t[0])
print(t[:3])

t2 = ("a","b")
t3 = t + t2
print(t3)

print(max((88,11,34,25)))
print(min((88,11,34,25)))
print(t.index(2))
print(t.count(3))




