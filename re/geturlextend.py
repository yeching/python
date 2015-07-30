#coding=utf-8
import re
def urladdress(url):
  listurls=['.php','.html','.asp','jsp']
  for listurl in listurls:
	address= re.findall(listurl,url)
	if len(address)>0:
		return listurl

url='http://www.zhiboba.com/eg.asp'
a=urladdress(url)
print (a)

