
import enum

# 创建一个枚举对象
week = enum.Enum("Weekday", ("Sun", "Mon", "Tue"))
print(week)
for name, member in week.__members__.items():
    print(name, member, member.value)

# 枚举十二月
@enum.unique # 保证枚举类型中没有重复的值
class Month(enum.Enum):
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    July = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12

for m in Month:
    print(m, m.value)

'''
m = int(input("请输入你要查询的月份"))
if m == Month.Jan.value:
    print("1月")
'''
# 访问枚举类型中的枚举值
day = Month.Jan
print(type(day))
print(day)
print(Month(1))
print(Month['Jan'])

# Month.Jan.value = 100 不能改变的