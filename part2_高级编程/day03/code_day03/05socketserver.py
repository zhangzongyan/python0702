
import socketserver

class Mysocket(socketserver.BaseRequestHandler):
    # 重写handle()
    def handle(self):
        print("client is comming:{}".format(self.client_address))
        # 套接字对象
        sd = self.request
        recvbuf = sd.recv(100)
        print(recvbuf.decode('utf-8'))
        sd.send(recvbuf.upper())


if __name__ == '__main__':
    # 同时处理多个连接请求
    s = socketserver.ThreadingTCPServer(('192.168.100.142', 4567), Mysocket)
    s.serve_forever() # 服务器一直执行

