# STMP发送邮件
"""
SMTP(Simple Mail Transfer Protocol) 即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则,由它来控制信件的中转方式
python 的 smtplib 提供了一种很方便的途径发送电子邮件,它对 SMTP 协议进行了简单的封装

import smtplib
smtpobj = smtplib.SMTP([host, [,post [, local_hostname]]])
host             SMTP 服务器主机.你可以指定主机的 ip 地址或者域名如:baidu.com,这个是可选参数
post             如果你提供了 host 参数,你需要指定 SMTP 服务使用的端口号,一般情况下 SMTP 端口号为 25
local_hostname   如果 SMTP 在你本机上,你只需要指定服务器地址为 localhost 即可

python SMTP对象使用 sendmail 方法发送邮件,语法如下:
SMTP.sendnail(from_addr,to_addrs,msg[, mail_options, rcpt_options])
from_addr:邮件发送者地址
to_addrs:字符串列表,邮件发送地址
msg:发送信息,本质是字符串,表示邮件.邮件一般由标题,发件人,收件人,邮件内容,附件等构成,发送邮件时要注意 msg 格式(即 SMTP 协议中定义的格式)
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '444543565@qq.com'
receivers = ['502725964@qq.com']

mail_msg = """
<p>拿限定版角色皮肤!火爆预约中...</p>
<p>Python 邮件发送测试...</p>
<p>a href="https://bs.qq.com">这是一个链接</a></p>
"""
message = MIMEText('', 'html', 'utf-8')  # 文本内容   plain :文本格式| html : html 格式    编码
message['From'] = Header("腾讯游戏，用钱创造快乐", 'utf-8')  # 邮件发送者名字
message['To'] = Header('女神', 'utf-8')  # 邮件接收者名字

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')  # 邮件主题

try:
    mail = smtplib.SMTP()
    mail.connect("smtp.qq.com")  # 连接邮箱
    mail.login(sender, "pkdqnqxhsdymbieh")  # 账号和授权码
    mail.sendmail(sender, receivers, message.as_string())  # 发送账号、接收账号和邮件信息
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")

# 带图片、附件略
