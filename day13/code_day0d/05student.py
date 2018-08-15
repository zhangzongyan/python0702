
class Student:
    def __init__(self):
        pass

    @property   # 获取实例属性方法
    def score(self):
        return self.__score

    @score.setter  # 设置实例属性值
    def score(self, s):
        if not isinstance(s, int):
            raise ValueError('Must be a integer')
        if not(100 >= s >= 0):
            raise ValueError('Must between 0 and 100')
        self.__score = s


s1 = Student()
#s1.setScore("100") # s1.score = 11
#print(s1.getScore())

s1.score = 99 # set
print(s1.score) # get



