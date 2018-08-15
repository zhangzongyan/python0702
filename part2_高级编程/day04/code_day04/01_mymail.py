
import smtplib
from email.mime.text import MIMEText # 邮件正文
from email.mime.multipart import MIMEMultipart # 邮件类(主题，收发人，邮件正文)
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders

sender = "之后的月亮"

# 收发地址
from_addr = "python_1989@163.com"
to_addr = "1754590086@qq.com"
from_pwd = "python9999"

# smtp服务地址
smtp_server = "smtp.163.com"

title="这是一封测试的邮件"
context = "Dear: 今天是星期三！下了大雨"

# 添加附件
def add_other(msg):
    # 创建附件对象
    mb = MIMEBase('image', 'jpg', filename="images.jpg")
    # 必要头信息
    mb.add_header('Content-Disposition', 'attachment', filename="img.jpg")
    # 添加附件文件内容
    f = open("./img.jpg", "rb")
    mb.set_payload(f.read())
    # base64编码
    encoders.encode_base64(mb)
    # 邮件对象绑定
    msg.attach(mb)


def mail_msg():

    # 邮件对象
    msg = MIMEMultipart()
    # 邮件主题
    msg['Subject'] = Header(title, 'utf-8')
    msg['From'] = Header(sender, 'utf-8')
    msg['To'] = Header(to_addr)

    # 邮件正文
    text = MIMEText(context, "plain", "utf-8")
    msg.attach(text)

    # 添加附件
    add_other(msg)

    return msg


if __name__ == '__main__':
    # smtp对象
    server = smtplib.SMTP(smtp_server, 25)
    # 打印信息
    server.set_debuglevel(1)
    # 登录邮箱
    server.login(from_addr, from_pwd)
    # 发送邮件
    server.sendmail(from_addr, [to_addr], mail_msg().as_string())
    # 断开服务
    server.quit()
