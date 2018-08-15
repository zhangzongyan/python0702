
import socket

# 创建套接字
sd = socket.socket()

# 请求链接
sd.connect(('192.168.100.142', 9999))

recvdata = sd.recv(1024)
recvdata = recvdata.decode('utf-8')
print("recv:%s" % recvdata)

