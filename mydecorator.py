import functools
# 在不修改函数内容的基础上，给函数添加功能 ----> 装饰器

def log(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        '''装饰语句'''
        print("the function %s is called" % fun.__name__)
        print("这是一个装饰器")
        return fun(*args, **kwargs)
    return wrapper

@log   # now = log(now)
def now():
    print("2018-07-30")

now()
print(now.__name__)


