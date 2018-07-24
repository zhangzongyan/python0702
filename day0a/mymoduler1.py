
import time


def testhello():
	print("hello")


# __name__在本文件中的值是'__main__'，在其他文件中是模块名
if __name__ == '__main__':
	# 列出模块中所有的函数
	print(dir(time))
	print(time.time())

	print(__name__)
	print("this is myself file")
	testhello()
	
