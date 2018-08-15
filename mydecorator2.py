
import  functools

def log(text):
    def decorator(fun):
        @functools.wraps(fun) #wrapper.__name__ = fun.__name__
        def wrapper(*args, **kwargs):
            print("我就是想装饰一下%s, %s" % (fun.__name__, text))
            return fun(*args, **kwargs)
        return wrapper
    return decorator

# sum2num = log(text)(sum2num)
@log('python是最好的语言') # sum2num=decorator(sum2num)
def sum2num(a, b):
    return a + b
print(sum2num(10, 20))

print(sum2num.__name__)