import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

import os, sys
import datetime
import readConfig
import getpathInfo

read_conf = readConfig.ReadConfig()
subject = read_conf.get_email('subject')  # 从配置文件中读取，邮件主题
app = str(read_conf.get_email('app'))  # 从配置文件中读取，邮件类型
address = read_conf.get_email('address')  # 从配置文件中读取，邮件收件人
cc = read_conf.get_email('cc')  # 从配置文件中读取，邮件抄送人
fromaddr = read_conf.get_email('from')  # 从配置文件中读取，邮件发送人
mail_path = os.path.join(getpathInfo.get_Path(), 'result', 'report.html')  # 获取测试报告路径


class send_email():
    def sendMail(self):

        # fromaddr = 'leehom_27@163.com'
        password = 'caonima123'
        toaddrs = ['leehom_27@163.com', '1043571015@qq.com']

        content = """
                        执行测试中……
                        测试已完成！！
                        生成报告中……
                        报告已生成……
                        报告已邮件发送！！
                        """
        textApart = MIMEText(content)

        zipApart = MIMEApplication(open(mail_path, 'rb').read())
        zipApart.add_header('Content-Disposition', 'attachment', filename='report.html')

        m = MIMEMultipart()
        m['From'] = fromaddr
        m['To'] = address
        m['CC'] = cc
        m['Subject'] = str(datetime.datetime.now())[0:19] + '%s' % subject  # 邮件主题
        m.attach(textApart) #添加邮件内容
        m.attach(zipApart)
        toaddrs = [address, cc]

        try:
            server = smtplib.SMTP('smtp.163.com')
            server.login(fromaddr, password)
            server.sendmail(fromaddr, toaddrs, m.as_string())
            print('success')
            server.quit()
        except smtplib.SMTPException as e:
            print('error:', e)  # 打印错误


if __name__ == '__main__':  # 运营此文件来验证写的send_email是否正确
    print(subject)
    send_email().sendMail()
    print("send email ok!!!!!!!!!!")
