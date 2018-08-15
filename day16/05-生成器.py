
import time

# 列表生成式
l = [x for x in range(1, 101) if x % 2 == 0]
print(l)

# 生成器generator
g = (x for x in range(1, 20) if x % 2 == 0)
print(g)

# while True:
#     try:
#         print(next(g))
#     except StopIteration as e:
#         print("all done %s" % e.value)
#         break
#     time.sleep(0.1)

for i in g:
    print(i)

# 函数生成器
def test_g():
    print("step1")
    yield 1
    print("step2")
    yield 2
    print("step3")
    yield 3

t = test_g()
print(t)
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))

for x in t:
    print(x)

# 斐波那契数列前n项
def fib(n):
    a, b = 0, 1
    for i in range(n):
        #print(b)
        yield b
        a, b = b, a+b

f = fib(10)
for res in f:
    print(res)













