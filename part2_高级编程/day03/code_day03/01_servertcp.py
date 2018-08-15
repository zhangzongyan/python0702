import socket
from multiprocessing import Pool
import time

'''tcp  server'''

def handler(newsd):
    time.sleep(10)
    newsd.send("hello world".encode('utf-8'))
    newsd.close()

if __name__ == '__main__':
    # 创建套接字对象
    sd = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    # 绑定服务器的本地地址 "0.0.0.0"所有网卡地址
    sd.bind(('0.0.0.0', 9999))

    # 处于监听状态
    sd.listen(5)

    # 创建用户处理客户端请求的进程池
    p = Pool(2)

    # 接收链接
    while True:
        # conn链接成功后的新套接字，用户数据交换 addr 对端地址
        conn, addr = sd.accept()
        print("successfully:", addr)

        # 创建新任务进程
        p.apply_async(handler, (conn,))




