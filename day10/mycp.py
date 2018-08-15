'''
实现类似cp的功能
python mycp.py ./mysys.py ps
'''
import sys

def mycp(src_path, dest_path):
	f1 = open(src_path)
	f2 = open(dest_path, "w")
	while True:
		rtext = f1.read(50)
		if rtext == "":
			break
		f2.write(rtext)
	f1.close()
	f2.close()	

def main():
	if not(len(sys.argv) >= 3):
		print("至少需要两个参数")
	else:
		mycp(sys.argv[1], sys.argv[2])
if __name__ == "__main__":
	main()

