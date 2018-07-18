
'''
猜字游戏
'''
'''
import random

rand_num = random.randint(0,9)
error_cnt = 0

while True:
	try:
		input_num = int(input("请猜测(10以内整型):"))
	except Exception:
		print("输入有误！请重新输入")
		continue
	if input_num == rand_num:
		print("厉害了！{}次就猜对了!".format(error_cnt+1))	
		break
	else:
		error_cnt += 1
		if error_cnt > 3:
			print("你的3次机会耗尽了！很遗憾")
			break
		if input_num > rand_num:
			print("大了！再来一次，你还有{}次机会".format(3-error_cnt))
		else:
			print("大胆一些，太小了,你还有{}次机会".format(3-error_cnt))	
'''

'''
3个红球，3个蓝球，4个黄球
'''
'''
cnt = 0
# 红球
for red in range(4):
	# 蓝球
	for blue in range(4):
		for yellow in range(5):
			if red + blue + yellow == 8:
				cnt += 1
				print("红球：{}, 蓝球：{}, 黄球：{}".format(red, blue, yellow))
print("共{}种情况".format(cnt))
'''

'''
99乘法表
'''
'''
for i in range(1, 10):
	for j in range(1, i+1):
		print("{}*{}={:>2}".format(j, i, j*i), end=' ')
	print()
'''

'''
猴子吃桃
'''
n = 1
for i in range(10):
	n = (n+1)*2
print("最初桃的个数是{}".format(n))

