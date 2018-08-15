
class Student:
    def __init__(self, age, score):
        self.__age = age
        self.__score = score

    def get_age(self):
        return self.__age

    def get_course(self):
        return max(self.__score)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, nm):
        if nm == "":
            raise ValueError("同学，你的名字不能为空")
        self.__name = nm

s1 = Student(20, [80,99,56])
s1.name = "帅博博"
print("姓名：{}, 年龄:{}, 最高分是:{}".format(s1.name, s1.get_age(), s1.get_course()))
