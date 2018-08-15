import time
import multiprocessing as mp
import queue

# 读队列
def read_queue(q):
    while True:
        try:
            rd = q.get(timeout=2)
            print(rd)
        except queue.Empty as e:
            print("all done:%s" % e)
            break


def write_queue(q):
    for i in range(5):
        q.put(time.ctime())
        time.sleep(1)

if __name__ == '__main__':
    # 创建队列
    queue = mp.Queue()

    # 创建两个用于读写队列的进程
    p1 = mp.Process(target=write_queue, args=(queue,))
    p2 = mp.Process(target=read_queue, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
