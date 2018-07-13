
'''
练习:由字符串week = "星期一星期二星期三星期四星期五星期六星期日"
	由用户输入，输入1~7之间的任意数字，输出相应的星期
'''
week = "星期一星期二星期三星期四星期五星期六星期日"
# 读入
# num = int(input("输入1~7之间的任意数字:"))
num = eval(input("输入1~7之间的任意数字:")) # eval("7.7")

pos = (num - 1)*3
print(week[pos:pos+3])

# 验证eval()
num1, num2 = eval(input("请输入两个整型数:"))  #"10, 20"
print(num1, num2)


