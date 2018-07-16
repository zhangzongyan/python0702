'''
if 条件:
	执行体
条件非0即为真

if 条件:
	执行体
else:
	执行体

if 条件:
	执行体
elif 条件2:
	执行体
....
else:
	执行体
'''

num = eval(input("请输入一个整型数:"))

# if num % 2 == 0:
if not(num % 2):
	print("{}是一个偶数".format(num))
else:
	print("{}是一个奇数".format(num))

print("{0}{1}一个偶数".format(num, "不是" if num % 2 else "是"))

