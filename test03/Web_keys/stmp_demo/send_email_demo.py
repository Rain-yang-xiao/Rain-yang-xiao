import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

class Mail:
    def send_email(self,file_new):
        with open(file_new, 'rb') as f:
            mail_body = f.read()
        # 发送者账号
        sender = '2256146351@qq.com'
        # 发送者密码
        password = 'xktauzbqskwaebef'
        # 接收者账号
        receiver = '1404654767@qq.com'
        try:
            # 发送邮件正文
            body = MIMEText(mail_body, 'html', 'utf-8')

            # 定义附件对象
            message = MIMEMultipart()
            message['From'] = formataddr(['安徒生的女王', sender])
            message['To'] = formataddr(['Will', receiver])
            message['Subject'] = Header('自动化测试报告', 'utf-8')
            message.attach(body)

            # 添加附件
            att1 = MIMEText(mail_body, 'base64', 'utf-8')
            att1['Content-Type'] = 'application/octet-stream'
            att1['Content-Disposition'] = 'attachment;filename="report.html"'
            message.attach(att1)

            server = smtplib.SMTP_SSL('smtp.qq.com', 465)
            server.login(sender, password)
            server.sendmail(sender, receiver, message.as_string())
            server.quit()
        except smtplib.SMTPException:
            print('邮件发送失败')



