#!/usr/bin/python
# -*- coding:utf-8 -*-

# python 中去除字符串 首尾 的空白字符			
# lstrip 去除字符串开头的空白字符				类似于php 的 ltrim
# rstrip 去除字符串结尾的空白字符				类似于php 的 rtrim
# strip  去除字符串 开头 和 结尾 的 空白字符	类似于php 的 trim
str = '   中国   '
print '|',str.lstrip(),'|',str.rstrip(),'|',str.strip(),'|'		#输出: | 中国    |    中国 | 中国 |


# test.txt 文件, 一行一个id, 将txt文件中的id读取出来, 以 id1,id2,id3... 的格式 写入一个新文件
fp1 = open('string_strip.txt');
arr = fp1.readlines()		# 将文本的内容读到一个list中, list每个元素的值是文本中的一行, 相当于php的 file()
print arr

fp2 = open('string_strip_2.txt','a');	# 以追加方式打开文件
for i in arr:
	fp2.write(i.strip()+',');	# 往文件中写内容	strip:去除字符串首尾处的空白字符
	
fp1.close()		#关闭文件指针
fp2.close()
