
import multiprocessing as mp
import os, time

globnum = 1

# 子进程函数
def child_job(arg):
    global globnum
    globnum = 100 # 不会影响父进程的变量
    print("the child process[{}] is running, args:{}"\
          .format(os.getpid(), arg))
    time.sleep(3)
    print("Bye")

if __name__ == '__main__':
    # 调用进程
    print("the calling process is %d" % os.getpid())

    # 实例化进程对象
    p = mp.Process(target=child_job, args=("hello, child",))

    # 使能子进程的daemon属性--->守护进程
    p.daemon = True

    # 子进程运行
    p.start()
    # 收尸
    #p.join()

    time.sleep(1)

    print("parent:", globnum)

    print("done")

