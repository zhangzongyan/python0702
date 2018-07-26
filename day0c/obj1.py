
'''
类的定义:
'''
class Person:
	# 属性 特征
	role = "super_person" # 类属性
	def __init__(self, nm, ag=20): # 不需要主动调用，创建对象时自动调用的----》构造方法
		print("Person构造方法调用了....")
		self.name = nm	# self.name 实例属性 self当前对象
		self.__age = ag # 私有属性

	def __del__(self): # 当对象销毁的时候，自动调用的方法--->析构方法 
		print("请记住我.....")
		
	# 方法(函数) 技能
	def sayHello(self):
		'''获取类属性'''
		print("我属于{}".format(Person.role), end=",")
		print("hello")
	def getName(self):
		'''打印实例属性'''
		print("我是{}".format(self.name))
	def getInfo(self):
		print("我叫{}, 我今年{}了".format(self.name, self.__age))

if __name__ == "__main__":
	'''
	类--->对象  实例化
	对象
	'''
	person1 = Person("小智")
	person2 = Person("小白")
	
	Person.role = "Superman"
	
	'''
	使用方法
	'''
	person1.sayHello()
	person1.getName()
	
	person2.sayHello()
	
	'''
	类外部访问和修改属性
	'''
	person1.name = "小小"
	person1.getName()
	
	#print(person1.__age)
	person1.getInfo()
	
	# 销毁对象
	#del person1
	
	while True:
		pass
	
