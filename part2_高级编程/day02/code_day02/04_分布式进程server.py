
'''
先运行一端---》server
'''

from multiprocessing import Queue
import multiprocessing.managers as mg
import queue

# 创建用户进程间通讯的队列
send_queue = Queue()  # 分发任务的queue
recv_queue = Queue()  # 接受结果的queue


class QueueManager(mg.BaseManager):
    pass


# 返回send_queue队列
def return_send_queue():
    global send_queue
    return send_queue

def return_recv_queue():
    global recv_queue
    return recv_queue


def main():
    # 将队列注册到网络
    QueueManager.register('get_send_queue', callable=return_send_queue)
    QueueManager.register('get_recv_queue', callable=return_recv_queue)

    # 创建manager对象 将服务端地址绑定
    manager = QueueManager(address=("192.168.100.142", 8888), authkey=b'hello')

    # 启动manager
    manager.start()

    # 使用网络队列:不能直接通过send_queue recv_queue直接访问
    task_queue=manager.get_send_queue()
    result_queue = manager.get_recv_queue()

    for i in range(1, 11):
        task_queue.put(i)
        print("server write %d in task_queue" % i)
    # 读结果
    while True:
        try:
            rcv = result_queue.get(timeout=10)
            print("server get result is [%s]" % rcv)
        except:
            break

if __name__ == '__main__':
    main()



