#!/usr/bin/env python
#_*_ coding=utf-8 _*_
'''
#/*=========================================================================*/
# File Name: search-replace.py
# Author: yeqing
# mail: yq08051035@163.com
# Created Time: 2015年11月14日 星期六 08时26分35秒
# Version: V1.0
# Function: a script tool to achieve  text replacement
# Usage:
# Descripion:
#/*=========================================================================*/
'''

import sys
if len(sys.argv) <= 4:
    print("usage: %s search_text replace_text [infilename [outfilename]]" % (sys.argv[0]))

def replace():
     search_text = sys.argv[1]
     replace_text = sys.argv[2]
     if len(sys.argv) > 4:
         input_file = open(sys.argv[3])
         output_file = open(sys.argv[4], 'w')

         for word in input_file:
             output_file.write(word.replace(search_text, replace_text))
 
         input_file.close()
         output_file.close()
     print('-----completed-----')

if __name__ == '__main__':
    replace()
