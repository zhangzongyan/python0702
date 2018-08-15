
class Student:
    __slots__ = ("name", "age") # 限制实例属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("小p", 20)
s1.no = 1
print(s1.name, s1.age, s1.no)




