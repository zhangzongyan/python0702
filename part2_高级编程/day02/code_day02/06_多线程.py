
import threading
from threading import Thread
import os


# 线程函数
def thread_job(args):
    print("[%d] new thread %s is running" % \
          (os.getpid(), threading.current_thread().getName()))


if __name__ == '__main__':
    print("[%d] thread %s is running" % (os.getpid(),\
                                         threading.current_thread().getName()))
    # 创建线程
    td = Thread(target=thread_job, args=("new_thread",), name="python")
    # 运行线程
    td.start()
    td.join()

