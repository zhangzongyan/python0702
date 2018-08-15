
from socket import *


if __name__ == '__main__':
    # 创建报式套接字
    s = socket(family=AF_INET, type=SOCK_DGRAM)

    # 绑定地址
    s.bind(('192.168.100.142', 8765))

    # 收发消息
    while True:
        print("waiting for udp.....")
        data, addr = s.recvfrom(1024)
        print("recive successfully, addr:{}, data:{}".\
              format(addr, data.decode('utf-8')))

