

# 默认打开方式是“rt“ , ("r" "r+")不创建 "w" "w+" "a" "a+" "b" "t"
# "w" / "w+"打开一个文件如果文件不存在创建，如果存在将文件截短为0
fd = open("test", "w+")# "wt+"

#print(fd.read())
fd.write("hello   \nworld\n")
print("当前文件的偏移量:{}".format(fd.tell()))

# 从文件开头的位置将文件偏移量设置为0
# fd.seek(0, 0)
print("当前文件的偏移量:{}".format(fd.seek(6, 0))) # 如果打开文件方式是"t"方式（默认),只允许在文件开头开始偏移

r = fd.read()
print(r)

fd.close()

# 不需要关闭
with open("test", "a") as f:
	print(f.tell())

