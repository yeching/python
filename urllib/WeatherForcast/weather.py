#coding=utf-8
'''
   这是一个查询天气的程序
   来源corssin编程教室
'''
import city
import urllib 
import json
cityname=raw_input('你想查那个城市的天气？\n')
citycode=city.city.get(cityname)
if citycode:
    try:
	url=('http://www.weather.com.cn/data/cityinfo/%s.html' %citycode)
	content=urllib.urlopen(url).read()
	print content
	data=json.loads(content)
	#data=json.decode(content)
	print data
	result=data['weatherinfo']
	str_temp=("%s\n%s ~ %s")%(result['weather'],result['temp1'],result['temp2'])
	print (str_temp)
    except:
	print ('查询失败')

else:
	print ('没有找到该城市')

