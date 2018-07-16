
'''
模拟进度条
'''
import time

i = 0
scale = 10

print("开始下载".center(20, '-')) # 将给定字符串居中，占20宽度，不够补"-"
while i <= scale:
	js = i * '##'	
	ws = (scale-i) * '--'
	'''
	python中的转移字符
		\n 换行
		\r 回车 
		\t Tab制表符
		\b 退格
	'''
	print("\r{:^3.0f}%[{}{}]\" \\ \ta\bb".format(i/scale*100, js, ws), end='')
	i += 1
	time.sleep(0.5)
print()
print("下载完成".center(20, '-'))

