#!/usr/bin/env python
#_*_ coding=utf-8 _*_

import re

def replace(search_text,replace_text,input_file,output_file):
    '''将一个字符替换为另一个字符'''
    in_file = open(input_file)
    out_file = open(output_file, 'w')

    for word in in_file:
        out_file.write(word.replace(search_text, replace_text))
    in_file.close()
    out_file.close()
    print('-----completed-----')

def del_blank_line(input_file):
    '''删除空行'''
    input_file = open(input_file,output_file)
    output_file = open(output_file, 'w')
    lines=input_file.readlines()
    for word in lines:
       if word.split():
           output_file.write(word)
    input_file.close()
    output_file.close()
    print('-----completed-----')

def del_line_start(input_file,output_file):
    ''' 删除每行开头的序数 1. 2. 3. ... '''
    input_file = open(input_file)
    output_file = open(output_file, 'w')
    lines=input_file.readlines()
    for word in lines:
       newline=re.sub(r'\d{1,4}\D',"",word)
       output_file.write(newline)
    input_file.close()
    output_file.close()
    print('-----completed-----')

def del_blank_space(input_file,output_file):
    '''删除空格'''
    input_file = open(input_file)
    output_file = open(output_file, 'w')
    lines=input_file.readlines()
    for word in lines:
       newline=re.sub(r'\s+(?!$)',"",word)
       output_file.write(newline)
    input_file.close()
    output_file.close()
    print('-----completed-----')

	
