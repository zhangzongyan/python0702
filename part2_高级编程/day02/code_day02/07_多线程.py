
import threading
import time

num = 1

def thread_fun(lk):
    global num

    lk.acquire()
    print("[%s]num:%d" % (threading.current_thread().getName(), num))
    n = num
    time.sleep(3)
    num = n + 1 # num += 1 --> num = num +1
    print("[%s]num:%d" % (threading.current_thread().getName(), num))
    lk.release()

if __name__ == '__main__':
    print("the thread %s is running" % \
          threading.current_thread().getName())

    # 创建锁
    l = threading.Lock()

    # 创建10个线程
    allthread = []
    for i in range(10):
        allthread.append(threading.Thread(target=thread_fun, args=(l, )))
    for i in allthread:
        i.start()
    for i in allthread:
        i.join()

