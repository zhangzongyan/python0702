
import sys
import mymoduler1

def main():
	mymoduler1.testhello()
	print(mymoduler1.__name__)

	return 1
	#sys.exit(0) 终止进程
	# python模块的环境变量
	print(sys.path)
	return 0

if __name__ == '__main__':
	main()
	print("last.....")

