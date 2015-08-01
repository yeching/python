#coding=utf-8
#筛选页面中想要的图片数据
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
	#前面的r作为字符串的前缀
    reg = r'src="(.+?\.jpg)" pic_ext'
	#将正则表达式转换为re的模式对象，更高效率的匹配字符串
    imgre = re.compile(reg)
	#re.findall() 会以列表的形式返回给定模式的所有匹配项。
    imglist = re.findall(imgre,html)
    return imglist      
   
html = getHtml("http://tieba.baidu.com/p/3922648580")
print getImg(html)