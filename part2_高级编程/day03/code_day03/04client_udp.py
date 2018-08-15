
from socket import *

if __name__ == '__main__':
    s = socket(type=SOCK_DGRAM)

    # 可省略bind

    msg = input("你的梦想是什么:")

    s.sendto(msg.encode('utf-8'), ('192.168.100.142', 8765))

    s.close()
