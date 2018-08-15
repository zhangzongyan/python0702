import sys

def add2num(num1, num2):
	return num1 + num2

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("参数不够")
	else:
		print(add2num(int(sys.argv[1]), int(sys.argv[2])))

