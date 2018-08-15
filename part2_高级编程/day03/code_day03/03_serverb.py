
from socket import  *


# 浏览器访问本服务器

def response_client(conn):
    buf = conn.recv(1024)
    print(buf)
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n') # 头
    conn.send('Hello, Python'.encode('utf-8'))
    conn.close()


if __name__ == '__main__':
    s = socket(family=AF_INET, type=SOCK_STREAM)

    s.bind(('localhost', 8000))

    s.listen(10)

    while True:
        print("Waiting connection.....")
        conn, raddr = s.accept()
        print("connect successfully:", raddr)
        response_client(conn)
