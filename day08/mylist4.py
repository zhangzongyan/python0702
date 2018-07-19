
'''
列表生成式	
'''

l = list(range(1, 101))
print(l)

l = []
for i in range(1, 11):
	l.append(i*i)
print(l)

# 列表生成式
l2 = [i * i for i in range(1, 11)]
print(l2)

l3 = [i * i for i in range(1, 11) if i % 2]
print(l3)

# "ABCD" "MNOP"
l4 = [i+j for i in "ABCD" for j in "MNOP"]
print(l4)



