
class Car:
	'''这是汽车类'''
	role = "car" # 类属性
	def __init__(self, logo, color):
		self.logo = logo  #实例共有属性
		self.__color = color # 实例私有属性
		self._wheel = 4
	
	def run(self):
		print("在路上跑的{1}的{0}好酷".format(self.logo, self.__getColor()))
		
	def __getColor(self):
		return self.__color

if __name__ == "__main__":
	carcar = Car("迈腾", "灰色")
	carcar.run()
	print(carcar._wheel)

	# 访问私有属性 对象._类名+私有属性名
	print(carcar._Car__color)

