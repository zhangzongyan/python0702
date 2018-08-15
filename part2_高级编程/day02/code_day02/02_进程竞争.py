'''
创建20个进程，都做打开当前目录下的test文件，将文件中的内容读出来 +1 写回去,
主进程创建子进程之前保证文件存在，并文件中只有0
'''
from multiprocessing import Process, Lock
from time import sleep

FILEPATH="./test"

# 子进程
def job(lock):
    f = open(FILEPATH, "r+")

    # 临界区：多进程竞争的代码---->锁
    lock.acquire() # 加锁
    readbuf = f.read()
    f.seek(0, 0)
    f.write(str(int(readbuf)+1))
    #sleep(1) 放大故障
    f.close()
    lock.release() # 解锁

if __name__ == '__main__':
    f = open(FILEPATH, "w")
    f.write("0")
    f.close()

    # 创建锁
    l = Lock()

    # 创建20个任务进程
    process_all = []
    for i in range(20):
        process_all.append(Process(target=job, args=(l, )))

    for p in process_all:
        p.start()

    for p in process_all:
        p.join()

