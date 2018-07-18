
'''
定义以下函数:
	1.求得一个整型数的平方
	2.获取字符串中的最大字符
	3.求得两个整型数的最大公约数
		m, n
		m // n == r
'''

def mysqure(n):
	return n ** 2

def max_in_str(s):
	m = s[0]
	length = len(s)
	for i in range(1, length):
		if s[i] > m:
			m = s[i]
	return m

def max_yue(m, n):
	while True:
		t = m % n
		if t == 0:
			break
		# 没整除
		m = n
		n = t
	return n

print(mysqure(5))

m = 7<F5>
print(max_in_str("Wednesday"))

print(max_yue(24, 16))
print(max_yue(26, 16))
print(max_yue(25, 16))



