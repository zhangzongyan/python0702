

class Foo(object):
	pass

class Bar(Foo):
	pass

'''
判断对象类型时type和isinstance有什么差别?
	继承关系	
'''
l = list()
b = Bar()
print(type(b) == Bar)
print(type(b) == Foo)

print(isinstance(b, Bar))
print(isinstance(b, Foo))
print(isinstance(l, list))

# 类和子类关系
print(issubclass(Bar, Foo))
print(issubclass(Bar, object))

