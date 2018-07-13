
# 循环
while True:
	# 交互---》输入
	story = input("说出你的故事:")
	
	# 要求:要求故事不能超过6了字
	if len(story) <= 6:
		# 输出
		print("人生苦短，我用Python!!", story)
		# 终止循环
		break
	else:
		print("墨迹死了！重新说")

print("很好！你的故事很精彩....")
		
