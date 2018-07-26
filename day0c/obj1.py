
'''
类的定义:
'''
class Person:
	# 属性 特征
	role = "super_person" # 类属性
	def __init__(self, nm): # 不需要主动调用，创建对象时自动调用的----》构造方法
		self.name = nm	# self.name 实例属性 self当前对象
		
	# 方法(函数) 技能
	def sayHello(self):
		'''获取类属性'''
		print("我属于{}".format(Person.role), end=",")
		print("hello")
	def getName(self):
		'''打印实例属性'''
		print("我是{}".format(self.name))

'''
类--->对象  实例化
对象
'''
person1 = Person("小智")
'''
使用方法
'''
person1.sayHello()
person1.getName()



