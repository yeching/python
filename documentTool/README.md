##功能：
删除空格 空行 替换字符  删除每行开头的序数

##API usage:

###1.替换字符

* replace(search_text,replace_text,input_file,output_file)

###2.删除空行

* del_blank_line(input_file):

###3.删除每行开头的序数

* del_line_start(input_file,output_file):

###4.删除空格

* del_blank_space(input_file,output_file):
    
##Demo:删除文件每行开头的序数,将test文档中开头的序数删除,输出结果到result文件中

```
文件名：test

1.adgf ffff
2.dgfg
3.ghg
4.ghsh
5.hthh
6.hddddddd
7.shhhhhhhhh
```
```
import documentTool
documentTool.del_line_start("test","result")
```
```
文件名：result
adgf ffff
dgfg
ghg
ghsh
hthh
hddddddd
shhhhhhhhh
```
