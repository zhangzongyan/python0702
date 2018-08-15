import smtplib
from email.mime.text import MIMEText # 邮件正文
from email.mime.multipart import MIMEMultipart # 邮件类(主题，收发人，邮件正文)
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders

class Mail:
    def __init__(self, user, passwd):
        self.user = user
        self.passwd = passwd
    # 设置目的地址
    def setRecvAddr(self, addr):
        self.mailrecv = addr
    # 设置smtp服务器地址
    def setSmtp(self, smtp):
        self.mailserver = smtp
    # 设置主题
    def setTitle(self, t):
        self.mailtitle = t
    # 邮件正文
    def setContent(self, text):
        self.mailcontent = text

    # 指定抄送人
    def setCc(self, cc):
        self.mailcc = cc

    # 私有方法:构建邮件
    def __setmsg(self):
        mime = MIMEMultipart()
        # 主题
        mime['Subject'] = Header(self.mailtitle, 'utf-8')
        mime['From'] = self.user
        mime['To'] = ','.join(self.mailrecv)
        # 抄送
        mime['Cc'] = ','.join(self.mailcc)
        # 邮件正文
        mime.attach(MIMEText(self.mailcontent, 'plain', 'utf-8'))
        return mime

    # 发送邮件
    def send(self):
        server = smtplib.SMTP(self.mailserver, 25)
        # 登录
        server.login(self.user, self.passwd)
        server.sendmail(self.user, self.mailrecv+self.mailcc, self.__setmsg().as_string())
        server.quit()

if __name__ == '__main__':
    # 创建邮件对象
    m = Mail("python_1989@163.com", "python9999")
    m.setRecvAddr(["python_1989@sina.com"])
    m.setCc(["1754590086@qq.com", "zhangzongyan@uplooking.com"])
    m.setTitle("今天是个好日子")
    m.setContent(open("./01_mymail.py", encoding='utf-8').read())
    m.setSmtp("smtp.163.com")
    m.send()

