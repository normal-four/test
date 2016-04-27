#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
#邮件信息配置
# sender = 'wzp_test@126.com'
# receiver = '1269325139@qq.com'
# subject = 'python email test'
# smtpserver = 'smtp.126.com'
# username = 'wzp_test@126.com'
# password = 'a1269325139'
# #HTML 形式的文件内容
# msg = MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
# msg['Subject'] = subject
# msg['From'] = 'test<wzp_test@126.com>'
# msg['To'] = "1269325139@qq.com"
# smtp = smtplib.SMTP()
# smtp.connect('smtp.126.com')
# smtp.login(username, password)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()



mailto_list="1269325139@qq.com"
mail_host="smtp.126.com" #设置服务器
mail_user="wzp_test@126.com" #用户名
mail_pass="a1269325139" #口令
mail_postfix="126.com" #发件箱的后缀


def send_mail(to_list,sub,content): #to_list：收件人；sub：主题；content：邮件内容
    mail_host="smtp.126.com" #设置服务器
    mail_user="wzp_test@126.com" #用户名
    mail_pass="a1269325139" #口令

    me= "hello"+"<"+mail_user+"@"+mail_postfix+">" #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,'html','utf-8') #创建一个实例，这里设置为html格式邮件
    #print msg
    msg['Subject'] = sub #设置主题
    msg['From'] = 'test<wzp_test@126.com>'
    msg['To'] = "1269325139@qq.com"
    #print msg.as_string()
    try:
        s = smtplib.SMTP()
        s.connect(mail_host) #连接smtp服务器
        s.login(mail_user,mail_pass) #登陆服务器
        s.sendmail(me, to_list, msg.as_string()) #发送邮件
        s.quit()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    if send_mail(mailto_list,"hello","<html><h1>你好！</h1></html>"):
       print u"发送成功"
    else:
       print u"发送失败"

# sender = 'wzp_test@126.com'
# receiver = '1269325139@qq.com'
# subject = '放假通知'
# smtpserver = 'smtp.126.com'
# username = 'wzp_test@126.com'
# password = 'a1269325139'
#
# msg = MIMEText('大家关好窗户','plain','utf-8')#中文需参数‘utf-8'，单字节字符不需要
# msg['Subject'] = Header(subject, 'utf-8')
# msg['From'] = 'test<wzp_test@126.com>'
# msg['To'] = "1269325139@qq.com"
# smtp = smtplib.SMTP()
# smtp.connect('smtp.126.com')
# smtp.login(username, password)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()