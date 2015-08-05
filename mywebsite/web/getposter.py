#coding=utf-8
import urllib
import json
import time
import web
#抓取一部分图片
response = urllib.urlopen('http://api.douban.com/v2/movie/top250')
data = response.read()
data_json=json.loads(data)
movie250 = data_json['subjects']

#抓取所有图片
for index in range(0, 250 ,50):
 print index
 response = urllib.urlopen('http://api.douban.com/v2/movie/top250?start=%d&count=50' % index)
 data = response.read()
 data_json = json.loads(data)
 movie250 = data_json['subjects']


 for movie in movie250:
 
 	print movie['title']
 	imgurl=movie['images']['large']
 	urllib.urlretrieve(imgurl,'%s.jpg' %movie['id'])
print '*****completed*******'
