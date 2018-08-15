'''
进程池
'''

from multiprocessing import Pool
from time import sleep
import os


def jobs(arg):
    print("the new process [{}] is running, and the arg is {}".format(os.getpid(), arg))
    sleep(1)
    return arg+100


# arg 子进程函数的返回值  在子进程终止时，父进程调用的该函数
def callback_fun(arg):
    print("[{}] say:{}".format(os.getpid(), arg))


if __name__ == '__main__':
    # 进程池对象
    pool = Pool(5)

    # print(os.cpu_count())
    print("[{}] main is running".format(os.getpid()))

    # 向池中添加新进程
    for i in range(10):
        pool.apply_async(jobs, (i,), callback=callback_fun) # 异步添加
    # 池中不允许在添加
    pool.close()
    pool.join()

