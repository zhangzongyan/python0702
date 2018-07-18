'''
已知1990.1.1是星期一,用户输入一个90年后的年月,打印出相应的日历
'''

'''
判断给定年份是否为闰年
def 函数名(参数列表):
	函数体
	return 返回列表

参数列表:可以有0个或多个,用于完成函数功能需要的已知值的存储
返回值列表:可以没有return,也可以return 1个或多个值,使用函数得到的值
	一个函数的结束：如果函数内有return则立即结束,允许return None
					如果函数内没有return,执行到函数体完成所有的语句
'''
def isleap(year):
	return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

'''
判断月份有多少天
'''
def dayofmonth(month, year):
	ret = -1
	if month == 1 or month == 3 or month == 5 or \
		month == 7 or month == 8 or month == 10 or month == 12:
		ret = 31
	elif month == 4 or month == 6 or month == 9 or month == 11:
		ret = 30
	elif month == 2:
		# 2
		ret = 28+isleap(year)
	return ret

# 读入用户输入的年月(y, m)
while True:
	try:
		m, y = eval(input("请输入1990年后的任意年月(月, 年):"))
		if not(1<= m <= 12 and y >= 1990):
			raise Exception #抛出异常 
	except Exception:
		print("请重新输入")
	else:
		break

sumdays = 0
# 1990.1.1~y/m/1有多少天 == 1990.1.1 ~ y-1.12.31 + y.1.1~y.m.1
for i in range(1990, y):
	'''
		函数的调用
			ret = 函数名(传递的参数值)
	'''
	if isleap(i):
		sumdays += 366
	else:
		sumdays += 365

for i in range(1, m):
	sumdays += dayofmonth(i, y)

sumdays += 1 # y.m.1
# y/m/1是星期几 
week = sumdays % 7

# y/m有多少天
monthdays = dayofmonth(m, y)

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

