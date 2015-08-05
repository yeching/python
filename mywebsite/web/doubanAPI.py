#coding=utf-8
import urllib
import json
import time
import web

db = web.database(dbn='sqlite', db='MovieSite.db')
#抓取所有电影
for index in range(0, 250 ,50):
 print index
 response = urllib.urlopen('http://api.douban.com/v2/movie/top250?start=%d&count=50' % index)
 data = response.read()
 data_json = json.loads(data)
 movie250 = data_json['subjects']

#先抓取一部分试试
#response = urllib.urlopen('http://api.douban.com/v2/movie/top250')
#data = response.read()
#data_json=json.loads(data)
#movie250 = data_json['subjects']

 for movie in movie250:
	 print movie['title']

	 db.insert('movie',
	 id=int(movie['id']),
	 title=movie['title'],
	 origin=movie['original_title'],
	 url=movie['alt'],
	 rating=movie['rating']['average'],
	 image=movie['images']['large'],
	 directors=','.join([d['name'] for d in movie['directors']]),
	 casts=','.join([c['name'] for c in movie['casts']]),
	 year=movie['year'],
	 genres=','.join(movie['genres']),

	 )
print '****completed*****'
