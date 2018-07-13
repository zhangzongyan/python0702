
'''字符串常用函数 unicode编码'''

s = "python程序设计"
print(len(s))
print(ord('a'))
print(ord('b'))
print(ord('A'))
print(ord('0'))
print(ord('张'))

print(chr(65))


# 读入用户输入的字符串，大写转小写，小写转大写
#s = input("请输入一个字符串:")
s = 'test'

i = 0
while i < len(s):
	if ord('a') <= ord(s[i]) <= ord('z'):
		# 转大写
		print(chr(ord(s[i]) - (ord('a') - ord('A'))))
	else:
		print(chr(ord(s[i]) + (ord('a') - ord('A'))))
	i += 1

s1 = s.swapcase() # 大写转小写, 小写转大写
print(s1)

if s.islower():
	print('小写')
elif s.isdigit():
	print('数字')
elif s.isupper():
	print('大写')
else:
	print('不认识')

s = str(234)
print(type(s))

# s.index(sub)
s = "hello py1thonpy1hello"
t = "py"
print(s.index(t))

t = "py1"
print(s.find(t))
print(s.count(t))

# s.split()
s = "    hello, boys,girls   "
print(s.split(","))

'''
# s.format()
num1, num2 = eval(input("输入两个整型数:"))
s = "{1:.2f}+{0:.2f} = {2:.2f}".format(num1, num2, num1+num2)
print(s)
'''

s = "python"
print("{:*>30}".format(s))
print("{:-^30}".format(s))
print("{:#<30}".format(s))










