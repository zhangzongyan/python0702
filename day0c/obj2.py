
import types

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

	# python 类默认属性
	print(Car.__name__)
	print(Car.__doc__)
	print(Car.__module__)
	print(Car.__dict__)	

	# 类的外部添加实例属性 
	carcar.owner = "小鑫"
	print(carcar.owner)

	setattr(carcar, "age", 1)
	print("汽车%d年了" % carcar.age)

	# 类的外部添加类属性
	Car.count = 1
	print(Car.count)

	# 类外部添加方法
	def jiayou(self):
		print("加满了...")
	
	Car.jiayou = types.MethodType(jiayou, carcar)
	carcar.jiayou()

	car2 = Car("奔驰", "黑色")
	car2.jiayou()

	print("汽车对象{}logo属性".format("有" if hasattr(carcar, "logo") else "没有"))	





