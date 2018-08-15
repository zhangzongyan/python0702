'''管道'''

from multiprocessing import Process, Pipe
from os import getpid
from time import sleep

def child_job(arg):
    recvbuf = arg.recv()
    print("the process [{}], rcv:{}".format(getpid(), recvbuf))


if __name__ == '__main__':
    # 创建用于父子进程间数据交换的管道
    conn1, conn2 = Pipe()
    p = Process(target=child_job, args=(conn1,))
    p.start()

    sleep(3)

    # 写管道
    conn2.send([100, "good morning", "python"])
    p.join()


