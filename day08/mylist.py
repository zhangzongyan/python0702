
'''
打了激素的数组---->列表
	定义
	遍历
	常用运算符
	常用函数
'''
# 定义
ls = ["afternoon", 99, 100, 1.1]

print(type(ls))

# 切片
print(ls[0])
#print(ls[19]) 越界
print(ls[1:4])
print(ls[::2])
print(ls[::-1])

# 切片插入新的元素
ls[1:1] = [1,4,77,88]
print("ls[1:1] = [1,4,77,88]:",ls)

# 切片删除列表中的指定元素
ls[2:5] = []
print(ls)


# 遍历
length = len(ls)
for i in range(length):
	print(ls[i])

for l in ls:
	print(l, end = " ")
print()

i = 0
while i < length:
	print(ls[i], end = " ")
	i += 1
print()

# while l in ls: 不可以

# 常用运算符
newls = [11,22,33,44]
print(ls + newls)

newls = ["hello", "hi", "food", "hi", "a", "b"]
print(min(newls))

print(newls.index("hi", 3, -1))

print(newls.count("hi"))

# 将range类型转换为列表
l = list(range(1, 101, 2))
print(l)










