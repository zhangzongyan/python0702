
'''
BMI
'''
'''
height, weight = eval(input("兄弟，多高多重啊!(逗号区分):"))

bmi = weight / (height**2)
print(bmi)
if bmi < 18.5:
	print("多吃点吧！太瘦了")
elif 18.5 <= bmi < 24:
	print("完美！不用减肥了") 
elif 24 <= bmi < 28:
	print("不能再喝奶茶了！控制")
elif 28<= bmi <= 32:
	print("可能考虑要减减肥了")
else:
	print("不能再胖了")
'''
'''
计算输入整型数的前n项和
'''
'''
n = eval(input("请输入一个整型数:"))

sumall = 0
for i in range(1, n+1):
	sumall += i
print("{}的前n项和是{}".format(n, sumall))
'''

money = eval(input("你多钱买的呀:"))

discount = 0
if 100>= money >= 50:
	discount = money * 0.1
elif money > 100:
	discount = money * 0.2	
last = money - discount
print("此商品原件{},折扣{},最终{}".format(money, discount, last))



