

class Animal:
	def tell(self):
		print("animal speak....")

class Dog(Animal):
	def tell(self):
		print("woof woof.....")

class Cat(Animal):
	def tell(self):
		print("Meow Meow.....")

# 鸭子类型
class Computer:
	def tell(self):
		print("Computer speak.....")

# 动物叫两次
def speakTwice(animal):
	animal.tell()
	animal.tell()

dog = Dog()
dog.tell()

cat = Cat()
cat.tell()

speakTwice(dog)
speakTwice(cat)

computer = Computer()
speakTwice(computer)




