import time
'''魔法方法'''
# 斐波那契数列：1 1 2 3 5 8 13 21......
class Feb:
    count = 0
    __slots__ = ("current", "prev") # 魔法属性，限定属性
    def __init__(self): # 构造方法
        self.prev, self.current = 0,1
    def __len__(self):
        if Feb.count == 0:
            return 0
        return Feb.count-1
    def __str__(self):
        return "object class name is Feb"
    # 如果能循环遍历的对象，一定要实现__iter__
    def __iter__(self):
        #print("__iter__")
        return self

    def __next__(self):
        #print("__next__")
        self.prev, self.current = self.current, self.prev+self.current
        Feb.count += 1
        #if Feb.count > 10:
        if self.prev > 10000:
            raise StopIteration()
        return self.prev

    # 索引
    def __getitem__(self, n):
        if isinstance(n, int): # 索引
            self.prev, self.current = 0, 1
            for i in range(n+1):
                self.prev, self.current = self.current, self.prev+self.current
            return self.prev
        if isinstance(n, slice): # 切片
            # print(n.start, n.stop)
            res = []
            start = n.start
            end = n.stop
            if n.start == None:
                start = 0
            a, b = 0, 1
            for i in range(end): # [2:5]
                if i >= start:
                    res.append(b)
                a, b = b, a+b
            return res
f = Feb()
# print(len(f))
# print(Feb())
# print(f)
# f.m = 11
print("对象的长度是:", len(f))
for i in f:
    print(i, end=" ")
    #time.sleep(1)
print()
print("对象的长度是:", len(f))

print(f[0],f[2], f[5], f[8])
print(f[2:5:2]) # slice(2, 5, None)
print(f[:8])
  


