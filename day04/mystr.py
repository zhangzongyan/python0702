'''

字符串: '不能换行' / "与''没有差别的" 
'''
#	可以换行
'''

练习:由字符串week = "星期一星期二星期三星期四星期五星期六星期日"
	由用户输入，输入1~7之间的任意数字，输出相应的星期

'''
s1 = "good afternoon"
s2 = "noon1"

# in   /    not in
if s2 not in s1:
	print(s2, "不在", s1, "中")
else:
	print(s2, "在", s1, "中")
	
# +
s3 = s1 + s2
print(s1)
print(s2)
print(s3)

# * number
s3 = s1 * 5
print(s3)

# 切片: 索引正向递增(0, )， 反向递减(, -1)
print(s1[0])
print(s1[-1], s1[13])
print(s1[-2])
print(s1[0:5])
print(s1[2:-2])
print(s1[0:5:2])
print(s1[::-1])



