'''
已知1990.1.1是星期一,用户输入一个90年后的年月,打印出相应的日历
'''

# 读入用户输入的年月(y, m)
m, y = eval(input("请输入1990年后的任意年月(月, 年):"))
sumdays = 0

# 1990.1.1~y/m/1有多少天 == 1990.1.1 ~ y-1.12.31 + y.1.1~y.m.1
for i in range(1990, y):
	if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
		sumdays += 366
	else:
		sumdays += 365
	# sumdays += (365+(i % 4 == 0 and i % 100 != 0) or (i % 400 == 0))
	# sumdays += (366 if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0) else 365)
for i in range(1, m):
	if i == 1 or i == 3 or i == 5 or \
		i == 7 or i == 8 or i == 10 or i == 12:
		sumdays += 31
	elif i == 4 or i == 6 or i == 9 or i == 11:
		sumdays += 30
	else:
		# 2
		sumdays += (28 + (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0))
sumdays += 1 # y.m.1
# y/m/1是星期几 
week = sumdays % 7

# y/m有多少天
if m == 1 or m == 3 or m == 5 or \
	m == 7 or m == 8 or m == 10 or m == 12:
	monthdays = 31
elif m == 4 or m == 6 or m == 9 or m == 11:
	monthdays = 30
else:
	# 2
	monthdays = (28 + (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0))

# 打印日历
titlestr = "{}月 {}".format(m, y)
print(titlestr.center(20))
print("日 一 二 三 四 五 六")
# 打印星期之前的空格
for i in range(week):
	print("   ", end='')
for d in range(1, monthdays+1):
	print("{:>2}".format(d), end="\n" if (week+d)%7 == 0 else " ")
print()

