'''
作业:
	2.比较字符串的大小
'''

'''
s1, s2 = input("请输入两个字符串（空格隔开）:").split()
i, j = 0, 0
flag = True

# 遍历字符串的每一个字符 "his" "hisa"
while i < len(s1) and j < len(s2):
	if ord(s1[i]) > ord(s2[j]):
		print("{}大于{}".format(s1, s2))
		flag = False
		break
	elif ord(s1[i]) < ord(s2[j]):
		print("{}小于{}".format(s1, s2))
		flag = False
		break
	else:
		i += 1
		j += 1

if len(s1) > len(s2) and flag == True:
	print("{}大于{}".format(s1, s2))
elif len(s1) < len(s2) and flag == True:
	print("{}小于{}".format(s1, s2))
elif flag == True:
	print("{}等于{}".format(s1, s2))	
'''

'''
读入字符串，统计大写，小写，数字个数
'''
'''
s = input("请输入一个字符串")

up_cnt = 0
lower_cnt = 0
digit_cnt = 0
i = 0
while i < len(s):
	if s[i].isupper():
		up_cnt += 1	
	elif s[i].islower():
		lower_cnt += 1
	elif s[i].isdigit():
		digit_cnt += 1
	i += 1
print("大写字母{}个, 小写字母{}个, 数字字符{}个".format(up_cnt, lower_cnt, digit_cnt))
'''
'''
将字符串首字母大写，其余小写
'''
s = input("请输入一个字符串:")

# print(s.title())
i = 0
flag = True

while i < len(s):
	if ord('A') <= ord(s[i]) <= ord('Z') or \
		ord('a') <= ord(s[i]) <= ord('z'): # 字母
		if flag:# 首字母
			print(s[i].upper(), end='')
			flag = False
		else:
			print(s[i].lower(), end='')
	elif s[i] == ' ':
		flag = True
		print(s[i], end='')
	else:
		print(s[i], end='')

	i += 1
print()





