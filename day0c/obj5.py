
'''
python支持多继承, 但不推荐使用
	
当继承多个类的时候，并且父类中有名字一样的方法，则继承的是第一个父类方法
super()获取的只是第一个父类
'''

class A:
	def __init__(self):
		print("init A...")
	def say(self):
		print("A.....")

class B:
	def __init__(self):
		print("init B....")
	def say(self):
		print("B.....")

class C(A, B):
	def __init__(self):
		'''
		A.__init__(self)
		B.__init__(self)
		'''
		super().__init__()

c = C()
c.say()

