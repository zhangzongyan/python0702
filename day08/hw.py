
'''
七段数码管---》显示日期
'''
import datetime
from turtle import *

# 每根数码管间隙
def space():
	penup()
	fd(5)
	pendown()

def draw(state):
	space()
	pendown() if state else penup()
	fd(20)
	space()
	right(90)

'''
	画七段数码管---》呈现数字
'''
def drawDigit(num):
	if num == 2 or num == 3 or num == 4 or num == 5 \
		or num == 6 or num == 8 or num == 9:
		draw(True)
	else:
		draw(False)
	draw(True) if num in (0,1,3,4,5,6,7,8,9) else draw(False)
	draw(True) if num in (2,3,5,6,8,9,0) else draw(False)
	draw(True) if num in (2,6,8,0) else draw(False)
	left(90)
	draw(True) if num in (4,5,6,7,8,9,0) else draw(False)
	draw(True) if num in (2,3,5,6,7,8,9,0) else draw(False)
	draw(True) if num in (1,2,3,4,7,8,9,0) else draw(False)
	
	penup()
	left(180)
	fd(10)
	pendown()

'''
	画日期
'''
def drawDate(date_string):
	setup(800, 300, 20, 20)
	penup()
	bk(200)
	pendown()
	pensize(5)
	speed(0)
	for s in date_string:
		if s in ("年", "月", "日"):
			penup()
			fd(5)
			pendown()
			write(s, font=("Arial", 18, "normal"))
			penup()
			fd(25)
			pendown()
		else:
			# 画数字	
			drawDigit(eval(s))

def main():
	# 获取当前日期---》格式化字符串"xxx年xxx月xxxx日"
	tstring = datetime.datetime.now().strftime("%Y年%m月%d日")
	#画日期 
	drawDate(tstring)	
	done()

main()

