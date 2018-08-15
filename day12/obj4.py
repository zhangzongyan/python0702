
import obj1

class Test:
	def __init__(self):
		super().__init__() # 父类是object

class Student(obj1.Person):
	def __init__(self, name, age, no, school_tm):
		# 调用父类obj1.Person的__init__方法，构建name和age属性
		# obj1.Person.__init__(self, name, age)
		# super(Student, self).__init__(name, age)
		super().__init__(name, age)
		self.no = no	
		self.school_tm = school_tm

	# 重写
	def getInfo(self):
		# super().getInfo()
		#obj1.Person.getInfo(self)
		print("学号{},{}年入学的".format(self.no, self.school_tm))

s = Student("hello", 11, 1, 2015)
s.sayHello()
s.getInfo()

s.name = "python"
s.getInfo()

t = Test()

