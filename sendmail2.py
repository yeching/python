#!/usr/bin/env python
#_*_ coding=utf-8 _*_
#/*=========================================================================*/
# File Name: sendmail2.py
# Author: yeqing
# mail: yq08051035@163.com
# Created Time: 2015年11月08日 星期日 19时56分53秒
# Version: V1.0
# Function:use python to sendmail 
#/*=========================================================================*/ 
"""
注意：获得所需要使用的邮箱的host地址和port端口号，（本文使用的是163邮箱，对应的smtp服务器地址：mail.163.com，端口号25），
你需要在163.com有一个账号，且开通smtp服务
"""
import smtplib

from email.mime.text import MIMEText

mailto_list=['XXXXXXXXX@qq.com']           #收件人(列表)

mail_host="smtp.163.com"            #使用的邮箱的smtp服务器地址

mail_user="XXXXXXXXXX"                           #用户名

mail_pass="XXXXXXXXXXXXXXXX"                             #密码

mail_postfix="163.com"                     #邮箱的后缀

def send_mail(to_list,sub,content):

    me="ubuntu"+"<"+mail_user+"@"+mail_postfix+">"

    msg = MIMEText(content,_subtype='plain')

    msg['Subject'] = sub

    msg['From'] = me

    msg['To'] = ";".join(to_list)                #将收件人列表以‘；’分隔

    try:

        server = smtplib.SMTP()

        server.connect(mail_host)                            #连接服务器

        server.login(mail_user,mail_pass)               #登录操作

        server.sendmail(me, to_list, msg.as_string())

        server.close()

        return True

    except Exception, e:

        print str(e)

        return False

if send_mail(mailto_list,"test python sendmail","nice to meet you"):  #邮件主题和邮件内容
      print "done!"
else:
      print "failed!"
