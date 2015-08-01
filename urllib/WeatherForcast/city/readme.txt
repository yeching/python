天气网并没有直接给出所有城市代码的对应关系，而是给了3个接口：


1. http://m.weather.com.cn/data5/city.xml

获取所有省/直辖市的编号，如“01|北京,02|上海,03|天津”


2. http://m.weather.com.cn/data5/city省编号.xml

获取二级地区编号，如江苏是：city19.xml


3. http://m.weather.com.cn/data5/city二级编号.xml

获取三级编号，如南京是：city1901.xml


得到最终的三级编号之后，再加上中国101的前缀，就得到了城市代码，如南京市区就是“101190101”


所以，你可以选择，再写一个python程序，事先把这些复杂的编码全部抓取下来，整理成你要的格式；或者，偷懒一下，跳过这个过程，直接拿我抓好的编码。我放在了网盘里：

http://pan.baidu.com/share/link?shareid=1471212773&uk=204484850

文件中的三个程序分别是抓取 省份     城市    地区
	       	例如：	   江西省   上饶市  上饶县
	 （国家前缀）101   24        03      08       

**************************************************************
下面是源程序的解释

天气网的城市代码信息结构比较复杂，所有代码按层级放在了很多xml为后缀的文件中。而这些所谓的“xml”文件又不符合xml的格式规范，导致在浏览器中无法显示，给我们的抓取又多加了一点难度。


首先，抓取省份的列表：

url1 = 'http://m.weather.com.cn/data5/city.xml'

content1 = urllib2.urlopen(url1).read()

provinces = content1.split(',')


输出content1可以查看全部省份代码：

01|北京,02|上海,03|天津,...


对于每个省，抓取城市列表：

url = 'http://m.weather.com.cn/data3/city%s.xml'

for p in provinces:

   p_code = p.split('|')[0]

   url2 = url % p_code

   content2 = urllib2.urlopen(url2).read()

   cities = content2.split(',')


输出content2可以查看此省份下所有城市代码：

1901|南京,1902|无锡,1903|镇江,...


再对于每个城市，抓取地区列表：

for c in cities[:3]:

   c_code = c.split('|')[0]

   url3 = url % c_code

   content3 = urllib2.urlopen(url3).read()

   districts = content3.split(',')


content3是此城市下所有地区代码：

190101|南京,190102|溧水,190103|高淳,...


最后，对于每个地区，我们把它的名字记录下来，然后再发送一次请求，得到它的最终代码：

for d in districts:

   d_pair = d.split('|')

   d_code = d_pair[0]

   name = d_pair[1]

   url4 = url % d_code

   content4 = urllib2.urlopen(url4).read()

   code = content4.split('|')[1]


name和code就是我们最终要得到的城市代码信息。它们格式化到字符串中，最终保存在文件里：

line = "    '%s': '%s',\n" % (name, code)

result += line


同时你也可以输出它们，以便在抓取的过程中查看进度：

print  name + ':' + code
如果你只是想抓几个测试一下，并不用全部抓下来，在provices后面加上[:3]，抓3个省的试试看就好了。



