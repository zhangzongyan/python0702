'''
读取邮件
    1.下载
    2.解析(自学)
'''
import poplib

user="python_1989@sina.com"
passwd="python1989"

serverpop = "pop.sina.com"

if __name__ == '__main__':
    # 构建pop对象--->连接pop3服务器
    server = poplib.POP3(serverpop) # port:110
    # 调试信息
    server.set_debuglevel(1)
    # 欢迎信息
    print(server.getwelcome().decode('utf-8'))

    # 登录用户名和密码
    server.user(user)
    server.pass_(passwd)

    # 获取邮件属性(个数，大小)
    print("共%d封邮件，总大小是%d字节" % server.stat())

    # 邮件消息列表
    all = server.list()
    count = len(all[1])

    # 获取最后一封邮件
    reps, lines, ss = server.retr(count)

    msgall = b'\r\n'.join(lines)

    #print(msgall.decode('utf-8'))

    # 解析邮件

    server.quit()

