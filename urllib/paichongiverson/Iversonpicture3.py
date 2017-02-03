#coding=utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    
	#用到了urllib.urlretrieve()方法，直接将远程数据下载到本地
	#通过一个for循环对获取的图片连接进行遍历，为了使图片的文件名看
	#上去更规范，对其进行重命名，命名规则通过x变量加1。保存的位置默认为程序的存放目录。
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1


html = getHtml("http://tieba.baidu.com/p/3922648580")

print getImg(html)
