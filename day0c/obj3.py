
class Student:
	pass

class XiaoStudent(Student):
	'''XiaoStudent类称为派生类 Student基类，父类，超类'''
	pass

s1 = Student()
print(Student.__dict__)
print(Student.__name__)
print(Student.__module__)
print(Student.__doc__)
print(Student.__bases__)


s2 = XiaoStudent()
print(XiaoStudent.__bases__)

