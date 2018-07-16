'''
循环：
循环变量初始化
while 条件:
	循环体
	循环变量改变
else:
	执行体

for 循环变量 in 序列:
	循环体
else:
	执行体
'''

s = "Python"
i = 0 # 循环变量
while i < len(s):
	if s[i] == 't':
		# break
		i += 1
		continue # 终止本次循环，继续下一次循环(循环条件)
	print(s[i], end='')
	i += 1
else: # 当循环的终止是由于循环条件不满足而终止的，不是break终止的
	print("执行结束")
print('') # 换行

for i in s:
	if i == 't':
		# break 终止整个循环
		continue	
	print(i, end='')
else:
	print('执行结束')	
print()

print(range(10))# [0,10)
i = 0
for i in range(len(s)):
	print(i)

# range()
for i in range(10):
	print(i)

for i in range(5, 10):
	print(i)

for i in range(1, 10, 2):
	print(i)

