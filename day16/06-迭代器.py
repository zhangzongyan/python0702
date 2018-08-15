
from collections import Iterable, Iterator

'''
for循环:
    python组合类型：
        list str tuple set dict
    generator生成器
能用next函数取得每一个元素--->Iterator
能用for遍历---->Iterable 
'''

print(isinstance([], Iterator))
print(isinstance([], Iterable))

g = (x for x in range(100))
print(isinstance(g, Iterator))
print(isinstance(g, Iterable))

l = iter([1,2,3])
print(l)
print(next(l))

