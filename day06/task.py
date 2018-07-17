
'''
# 1 回文整型
num = eval(input("请输入一个整型数:"))

new_num = 0
save = num
while num:
	# 得到num的最低位 985
	new_num = new_num*10 + num % 10
	# 舍去最低位
	num //= 10	
if new_num == save:
	print("{}是一个回文整型".format(save))
else:
	print("{}不是一个回文整型".format(save))
'''	

'''
# 2 100~1000之前有多少质数
cnt = 0

# 遍历100~1000之间的每一个数
for i in range(100, 1001):
	# 判断i是否为质数
	flag = True
	for j in range(2, i):
		if i % j == 0:
			flag = False
			break
	if flag:
		cnt += 1
print("100到1000之间的所有的质数有{}个".format(cnt))
'''

name = input("请输入你的名字:")

'''
在while的循环条件中尽量避免函数的调用
i = 0
l = len(name)
while i < l:
	print(name[i])
	i += 1
'''
for s in name:
	if not(s.isalpha() or s.isdigit() or s == '_'):
		print("对不起！你的名字无效")
		break
else:
	print("成功读入")


