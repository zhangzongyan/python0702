
'''
try:
	xxxx
except 异常类:
	xxxx
'''

try:
	n = int(input("输入一个整型数:"))
except ValueError as e: # e就是当出现ValueError异常时对应的出错字符串
	print("傻不傻！不是告诉你输入一个整型数吗")	
	print(e)
else:
	if n % 2 == 0:
		print("偶数")
	else:
		print("奇数")


