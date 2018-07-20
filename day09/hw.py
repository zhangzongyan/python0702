
'''
1.读入10个学生的成绩，要求在0~100之间，定义一个函数,
统计10个学生成绩的平均分，最高分，和最低分
'''
'''
def opScore(score=[]):
	n = len(score)
	if n == 0:
		return -1

	maxSco = score[0]
	minSco = score[0]
	sumall = score[0]
	for i in range(1, n):
		sumall += score[i]
		if score[i] > maxSco:
			maxSco = score[i]
		if score[i] < minSco:
			minSco = score[i]
	return maxSco,minSco,sumall/n

def main():
	sc = []	
	i = 0	
	while i < 10:
		try:
			n = int(input("请输入第{}人的成绩".format(i+1)))
			if not(0<= n <= 100):
				print("请输入一个百分制的成绩")
				continue
		except Exception:
			print("不能是字符串")
			continue
		sc.append(n)
		i += 1
	maxValue, minValue, avgValue = opScore(sc)
	print("最高分：{}, 最低分：{}, 平均分:{}".format(maxValue, minValue, avgValue))
		
main()
'''

'''
2.随机产生10个10以内的整型数，存放到列表中，将列表中的最大值放在列表的最后。
'''
import random

'''
l = []
for i in range(10):
	l.append(random.randint(0, 10))
m = max(l)
l.remove(m)
l.append(m)
'''

'''
3.随机产生密码：
	在26个大小写字母和10个数字组成的列表中，随机生成10个8位密码
'''
# 产生一个列表，列表中存放所有的大写字母
ls = []
for i in range(26):
	ls.append(chr(ord('A')+i))
# 小写
for i in range(26):
	ls.append(chr(ord('a')+i))
# 数字
for i in range(10):
	ls.append(str(i)) 
print(ls)

for i in range(10):
	pwd = ''
	for j in range(8):
		pwd += ls[random.randint(0,61)]
	print(pwd)	

import string

'''
s = string.ascii_letters+string.digits # string.ascii_letters产生所有的字符字符串
print(s)
print(random.choice(s))
'''
def getPasswd(n, pwdstr = string.ascii_letters+string.digits):
	pwd=''	
	for i in range(n):
		pwd+=random.choice(pwdstr)
	return pwd

print(getPasswd(10, pwdstr=string.ascii_uppercase+string.digits))

'''
统计数值分布
'''
# 用户统计每一个段的数值个数
cnt = [0] * 11 
num = []
for i in range(20):
	num.append(random.randint(0, 100))
	print(num[i], end=' ')
	cnt[num[i]//10] += 1
print()

print("100:", end=' ')
print(cnt[10]*"*")
for i in range(9,-1,-1):
	print("{}~{}:".format(i*10, i*10+9), end=' ')
	print(cnt[i]*"*")



