#conding=utf-8
import os,re,datetime
filename='output_1981.10.21.txt'
gettime=re.search('\d{4}\.\d{2}\.\d{2}\.',filename)
filetime=gettime.group(0)
print( filetime)
date=datetime.date(1981,10,21)
w=date.weekday()+1
W=str(w)
#print("output_1981-10-21-"+W+".txt")
os.rename("output_1981.10.21.txt", "output_1981-10-21-" + W + ".txt")

