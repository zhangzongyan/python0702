
# 交互---》输入
story = input("说出你的故事:")

# 要求:要求故事不能超过6了字
if len(story) <= 6:
	# 输出
	print("人生苦短，我用Python!!", story)
else:
	print("墨迹死了！重新说")
	
