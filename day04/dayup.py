'''
"好好学习，天天向上"
1,好好学习每天进步1%o, 堕落每天退步1%o, 对比一年后好好学习力
(1+0.001) ** 365  (1-0.001) ** 365   

python基本数据类型----->数值类型(整型，浮点，复数)
变量：动态类型
变量名:由字母数字下划线组成，数字不能开头,最好顾名思义
'''
a = 10
print(type(a)) # type(变量) 
a = 1.1
print(type(a)) # type(变量) 
a = 1+2j
print(type(a))

a = 10; b = -2 #多条语句在同一行 ";"隔开
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)
print(a % b)
print(-a)
print(+a)

a = a + b
print(a, b)
a = 10; b = -2
a += b
print(a, b)

# 好好学习， 天天向上---->每周日不进步，周一到周六努力
# 遍历每一天，判断是否是周日
day = 1
dayup = 1
while day < 366:
	if day % 7 == 0:
		# 不要进步
		dayup = dayup * (1-0.01)
	else:
		# 努力学习
		dayup = dayup * (1+0.01)
	day += 1

# 不好好学习
daydown = (1-0.01) ** 365
print(dayup)
print(daydown)


