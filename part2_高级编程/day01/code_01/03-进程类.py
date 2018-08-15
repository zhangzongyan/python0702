import time
import multiprocessing as mp
import os

# 子类
class Childprocess(mp.Process):
    def __init__(self, name):
        super().__init__()
        self.name = name
    # 子类运行自动调用的方法
    def run(self):
        print(time.ctime())
        print("my name is %s, and pid %d, ppid:%d" % \
              (self.name, os.getpid(), os.getppid()))

if __name__ == '__main__':
    p = Childprocess("python")

    p.start() # 自动调用run
    p.join()

    print("the calling process[%d] end....." % os.getpid())
