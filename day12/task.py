from math import pi

'''
圆环是有两个同心不同半径的圆组成的,定义两个类，圆类和圆环类,描述圆环的面积和周长
	圆:Circle
	圆环:Ring
	半径:radius
	面积:area
	周长:perimeter
'''

class Circle:
	'''圆类，提供面积和周长'''
	def __init__(self, r):
		self.radius = r
	def getArea(self):
		return pi * (self.radius ** 2)	
	def getPerimeter(self):
		return 2 * pi * self.radius

class Ring(object): # object是所有类的超类，可省
	'''圆环类'''
	def __init__(self, radius_inside, radius_outside):
		self.inside_circle = Circle(radius_inside)		
		self.outside_circle = Circle(radius_outside)		

	def getRingArea(self):
		return self.outside_circle.getArea() - \
		self.inside_circle.getArea()

	def getRingPerimeter(self):
		return self.outside_circle.getPerimeter() + \
			self.inside_circle.getPerimeter()

if __name__ == '__main__':
	r = Ring(5, 7)
	print("圆环的面积是", r.getRingArea())
	print("周长是", r.getRingPerimeter())



