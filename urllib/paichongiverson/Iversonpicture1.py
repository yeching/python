#coding=utf-8
#获取整个页面数据
import urllib

def getHtml(url):
	#返回一个类文件的python对象
    page = urllib.urlopen(url)
	#与我们操作文件的方法都是一样的
    html = page.read()
    return html

html = getHtml("http://tieba.baidu.com/p/3922648580")

print html