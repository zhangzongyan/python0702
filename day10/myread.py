
import time
'''
	读文件
'''

with open("./mycp.py") as f:
	for line in f:
		print(line, end='')
		time.sleep(0.3)	


