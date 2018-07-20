
'''
字典:
	无序的 映射类型
	字典的key一定可哈希(hash())
'''
# 定义
d1 = {'shuaibobo':180, 'gaozhiyuan':185}
print(type(d1))
print(d1)

d2 = dict(age=18, name='zhaochao')
print(d2)

z = zip(['one', 'two', 'three'], [1,2,3])
print(z)
d3 = dict(z)
print(d3)

d4 = dict([('one', 1), ('three', 3), ('two', 2)])
print(d4)
if d3 == d4:
	print("字典是无序的")

d5 = {1:2, 100:3, (3,4,5):"abc"}
print(d5)

# 添加
d1['gaoxin'] = 165
print(d1)

# 遍历
print(d1.keys())
for k in d1.keys():
	print(d1[k])

print(d1.items())
for item in d1.items():
	print("key:{}".format(item[0]))
	print("values:{}".format(item[1]))

for d in d1: # d1.keys()
	print(d)

print(d1.values())

