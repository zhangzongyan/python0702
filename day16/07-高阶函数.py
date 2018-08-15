
from collections import Iterator, Iterable

from functools import reduce

# 函数可以作为参数传递
'''
def sum2num(x, y, f):
    return f(x) + f(y)

print(abs(-10))

f = abs
res = f(-100)
print(res)

res = sum2num(-5, 3, abs)
print(res)
'''

# map(fun, Iterable)
r = map(abs, [1, -2,-4, 3, 4, -5, -6])
print(isinstance(r, Iterable))
print(isinstance(r, Iterator))
print(r)

for i in r:
    print(i)

# reduce
def fn(x, y):
    return x*10 + y

r = reduce(fn, [1,2,3,4,5])
print(r)

# "12345"---> 12345
def char2int(c):
    return ord(c)-ord('0')

def str2int(s):
    return reduce(fn, map(char2int, s))
print(str2int("987"))

# filter 过滤器 函数返回值(True, False)
l = list(range(10))
t = tuple(filter(lambda x : x % 2 == 0, l))
print(t)

# sorted()
l = [-5, 2, 10, 1, -8, 100, -93]
res = sorted(l, reverse=True, key=abs)
print(res)

l = ["python", "C", "java", "net", "Go"]
res = sorted(l, key=str.upper)
print(res)
