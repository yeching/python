#coding=utf-8

import urllib

url1='http://m.weather.com.cn/data5/city.xml' 
content=urllib.urlopen(url1).read()   #爬取网页获取内容
print content 

provinces=content.split(',') #内容为字符串，通过逗号切片划分形成一个列表
result='city{\n'     #最后将获得内容放到字典中，和后面的对应
print provinces

url = 'http://m.weather.com.cn/data3/city%s.xml'
for p in provinces:
   p_code = p.split('|')[0]#通过|切片取列表的第一个元素
   url3 = url % p_code #取代url中的%s，形成新的url3
   content2 = urllib.urlopen(url3).read()
   #print content2
   cities = content2.split(',')
   #print cities
   for c in cities[:1]:#因为能容多，只取一个看看

     c_code = c.split('|')[0]

     url3 = url % c_code

     content3 = urllib.urlopen(url3).read()

     districts = content3.split(',')
     for d in districts:

       d_pair = d.split('|')

       d_code = d_pair[0]

       name = d_pair[1]

       url4 = url % d_code

       content4 = urllib.urlopen(url4).read()

       code = content4.split('|')[1]
       line = "    '%s': '%s',\n" % (name, code)

       result += line
       print  name + ':' + code
result +='}'
f=file('/home/yeqing/python/WeatherForcast/city/cites.py','w')
f.write(result)
f.close()





