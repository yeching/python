#coding=utf-8
from  Tkinter import *
import json
import urllib
import sys

class Myip():
	def __init__(self):
		#main frame
		self.window=Tk()
		#top frame
		self.top_frame=Frame(self.window)
		#bottom frame
		self.bottom_frame=Frame(self.window)

		self.L1 = Label(self.top_frame, text='       IP 地址:       ')
		self.L1.pack(side='left')
		default_value =StringVar()
		default_value.set('8.8.8.8')
		self.E1 = Entry(self.top_frame, textvariable=default_value, bd=3)
		self.E1.pack(side = LEFT)
		self.B1 = Button(self.top_frame, text='确定', command=self.process_input)
		self.B1.pack(side=RIGHT)

		self.bottom_left =Frame(self.bottom_frame)
		self.bottom_right =Frame(self.bottom_frame)

		self.label1 = Label(self.bottom_left,text="%-10s" % "国家")
		self.label2 = Label(self.bottom_left,text="%-10s" % '区域')
		self.label3 = Label(self.bottom_left,text="%-10s" % '地区')
		self.label4 = Label(self.bottom_left,text="%-10s" % '城市')
		self.label5 = Label(self.bottom_left,text="%-10s" % '县')
		self.label6 = Label(self.bottom_left,text="%-10s" % '运营商')

		self.label1.pack(side='top')
		self.label2.pack(side='top')
		self.label3.pack(side='top')
		self.label4.pack(side='top')
		self.label5.pack(side='top')
		self.label6.pack(side='top')

		self.En1 = Entry(self.bottom_right)
		self.En2 = Entry(self.bottom_right)
		self.En3 = Entry(self.bottom_right)
		self.En4 = Entry(self.bottom_right)
		self.En5 = Entry(self.bottom_right)
		self.En6 = Entry(self.bottom_right)

		self.En1.pack(side='top')
		self.En2.pack(side='top')
		self.En3.pack(side='top')
		self.En4.pack(side='top')
		self.En5.pack(side='top')
		self.En6.pack(side='top')

		self.bottom_left.pack(side='left')
		self.bottom_right.pack(side='right')
		self.top_frame.pack()
		self.bottom_frame.pack()

		self.window.mainloop()
	def get_data(self):
		API = "http://ip.taobao.com/service/getIpInfo.php?ip="
		url = API + self.ipaddr
		ret = urllib.urlopen(url).read()
		self.jsondata = (json.loads(ret))
	def process_data(self):
		if self.jsondata['data']['country']:
		  country = self.jsondata['data']['country']
		else:
		  country = "NULL"

		if self.jsondata['data']['area']:
		  area = self.jsondata['data']['area']
		else:
		  area = "NULL"

		if self.jsondata['data']['region']:
		  region = self.jsondata['data']['region']
		else:
		  region = "NULL"

		if self.jsondata['data']['city']:
		  city = self.jsondata['data']['city']
		else:
		  city = "NULL"

		if self.jsondata['data']['county']:
		  county = self.jsondata['data']['county']
		else:
		  county = "NULL"

		if self.jsondata['data']['isp']:
		  isp= self.jsondata['data']['isp']
		else:
		  isp = "NULL"
		return (country, area, region, city, county, isp)
	def process_input(self):
		self.ipaddr = self.E1.get()
		myjson = self.get_data()
		if myjson == False:
		  return 1
		else:
		  ret = self.process_data()
		  self.En1.delete(0, END)
		  self.En2.delete(0, END)
		  self.En3.delete(0, END)
		  self.En4.delete(0, END)
		  self.En5.delete(0, END)
		  self.En6.delete(0, END)
		  self.En1.insert(0, ret[0])
		  self.En2.insert(0, ret[1])
		  self.En3.insert(0, ret[2])
		  self.En4.insert(0, ret[3])
		  self.En5.insert(0, ret[4])
		  self.En6.insert(0, ret[5])
def main():
	ip=Myip()

if __name__=='__main__':
	main()
