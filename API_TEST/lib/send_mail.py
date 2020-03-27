import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import time
import os
def send_mail(file_new):
    with open(file_new,'r',encoding='utf-8') as f:
        mail_body = f.read()

    # 第三方 SMTP 服务
    mail_host='smtp.qq.com'   # 设置服务器
    mail_user="1084276061@qq.com"
    mail_pass="bkxukkiwpnwribid"    # 服务端授权码，不是邮箱的密码
    sender=mail_user
    receivers=["2945170175@qq.com"] # 接收邮件
    mail_msg="""
    <p>Python 邮件测试</p >
    <p><a href=" baidu.com">百度链接</a ></p >
    """

    message=MIMEMultipart()     # 创建一个带附件的实例
    message['From']=Header("测试邮件标题",'utf-8')
    message['To']=";".join(receivers)
    subject="Python SMTP 邮件测试"
    message['Subject']=Header(subject,'utf-8')

    # 邮件正文内容
    message.attach(MIMEText(mail_msg,'html','utf-8'))
    # 构造附件1
    att1=MIMEText(mail_body,'base64','utf-8')
    att1["Content-Type"]='application/octet-stream'
    att1["Content-Disposition"]='attachment; filename = "test"'
    message.attach(att1)

    try:
        smtpObj=smtplib.SMTP()
        smtpObj.connect(mail_host,25)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender,receivers,message.as_string())
        smtpObj.close()
        print("邮件发送成功")
    except Exception as e:
        print("Error: 无法发送邮件")
        print(str(e))


#此处为将HTML文件夹中的所有文件返回并取最新的一个HTML文件
def new_file(test_dir):
    #列举test_dir目录下的所有文件，结果以列表形式返回。
    lists=os.listdir(test_dir)
    #print(lists)
    file_path=os.path.join(test_dir,lists[-1])
    return file_path


