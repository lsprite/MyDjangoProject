import smtplib
from email.mime.text import MIMEText

from_addr = '869740528@qq.com'
# smtp服务器地址
smtp_server = 'smtp.qq.com'
password='odycvqeqnocmbcig'

def send_email(to_addr, subject, msg):
    # 构造邮件，内容为hello world
    msg = MIMEText(msg)
    # 设置邮件主题
    msg["Subject"] = subject
    # 寄件者
    msg["From"] = from_addr
    # 收件者
    msg["To"] = to_addr
    try:
        # smtp协议的默认端口是25，QQ邮箱smtp服务器端口是465,第一个参数是smtp服务器地址，第二个参数是端口，第三个参数是超时设置,这里必须使用ssl证书，要不链接不上服务器
        server = smtplib.SMTP_SSL(smtp_server, 465, timeout=2)
        # 登录邮箱
        server.login(from_addr, password)
        # 发送邮件，第一个参数是发送方地址，第二个参数是接收方列表，列表中可以有多个接收方地址，表示发送给多个邮箱，msg.as_string()将MIMEText对象转化成文本
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print('Faild:%s' % e)
        return False
