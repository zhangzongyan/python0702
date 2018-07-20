
'''
集合:
	无序
'''

# 定义
s = {1,2,3,3,4,3,4,4,4,3}
print(type(s))
print(s)
print(len(s))

l = [1,2,1,2,"hello", "world", "hello"]
l = list(set(l))
print(l)


s.update({11,22,33})
print(s)

# 增加一个新的元素
s.add('a')
print(s)

s.remove(11)
print(s)

s.pop()
print(s)

