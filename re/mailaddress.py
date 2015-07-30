#coding=utf-8
import re

def mail(e):
	if re.match(("[a-zA-Z0-9]+\@[a-zA-Z0-9]+\.com"),e)!=None:
		print ("邮箱格式正确")

email=raw_input("请输入email:")
print( email)
a= (mail(email))
print(a)
