

fd = open("/home/reala_zhang/python0702/day0a/mysys.py", "rt")

res = ""
while True:
	text = fd.read(10)
	if text == "":
		break
	res += text
print(res)

# readline()
fd.seek(0)
l = fd.readline(5) # 遇到'\n' size参数小于一行的字节个数
print(l)

fd.seek(0)
ls = fd.readlines(50)
print(ls)

# 1.刷新缓存区 2.释放文件流
fd.close()

