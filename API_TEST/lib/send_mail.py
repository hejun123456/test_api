import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import time
import os
def send_mail(file_new):
    with open(file_new,'rb') as f:
        mail_body = f.read()

    # 配置第三方服务
    host='smtp.qq.com'              #设置服务器
    username = '1084276061@qq.com'  #发件箱用户名
    password = 'bkxukkiwpnwribid'   #发件箱密码
    sender = '1084276061@qq.com'    #发件人邮箱
    receiver=['2945170175@qq.com']  #收件人邮箱

     #邮件正文是MIMEText
    msg = MIMEText(mail_body, 'HTML', 'utf-8')
    # 邮件对象
    msg['Subject'] = Header("接口自动化测试报告", 'utf-8').encode()
    msg['From'] = Header(u'测试负责人 <%s>'%sender)
    msg['To'] = Header(u'项目负责人 <%s>'%sender)
    msg['date'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    #发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(host,25)              # 邮箱服务器
    smtp.login(username, password)      # 登录邮箱
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送者和接收者
    smtp.quit()
    print("邮件已发出！注意查收。")



#此处为将HTML文件夹中的所有文件返回并取最新的一个HTML文件
def new_file(test_dir):
    #列举test_dir目录下的所有文件，结果以列表形式返回。
    lists=os.listdir(test_dir)
    #print(lists)
    file_path=os.path.join(test_dir,lists[-1])
    return file_path


