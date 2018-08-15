

from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

# 从网络中通过server注册队列名， 绑定关系
QueueManager.register('get_send_queue')
QueueManager.register('get_recv_queue')

# 构建manager对象，链接server端
server_ip = "192.168.100.142"
manager = QueueManager(address=(server_ip, 8888), authkey=b'hello')

manager.connect()

# 获取到队列
recv = manager.get_send_queue()
send = manager.get_recv_queue()

# 使用队列
while True:
    n = recv.get()
    print("recv the task:%d" % n)
    sendbuf = "%d*%d=%d"%(n, n, n**2)
    send.put(sendbuf)
