#coding=utf-8
#计算昨天和明天的日期
import datetime
today=datetime.date.today()
print (today)
yesterday=today-datetime.timedelta(days=1)
print (yesterday)
tomorrow=today+datetime.timedelta(days=1)
print (tomorrow)
print "昨天：%s,今天：%s,明天：%s"%(yesterday,today,tomorrow)
