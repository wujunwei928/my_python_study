#/usr/bin/python
#coding=utf-8

import sys

# 将argv中的东西解包
script,filename = sys.argv

##############################################################################
#			
#	python文件函数详解:
#
#	open() 打开文件 
#		 打开方式:
#			r	只读方式	the file will only be read
#			w	只写方式	only writing (an existing file with the same name will be erased)
#			r+
#			a	追加方式: for appending; any data written to the file is automatically added to the end
#
#	close()  关闭文件。跟你编辑器的文件-> 保存.. 一个意思。
#
#	read – 读取文件内容。你可以把结果赋给一个变量。
#
#	readline – 读取文本文件中的一行。
#	
#	truncate – 清空文件，请小心使用该命令。
#	
#	write(stuff) – 将stuff 写入文件。
#
#
#
#
#
#
#
##############################################################################


##打开文件 相当于php的fopen()  
#fp = open(filename,'r')  # open(文件名, 打开方式), 打开方式 r:只读, w:只写 a:追加  r+: 读写  
fp = open(filename)		# 第二个参数省略的时候, 默认打开方式为: r(只读)

print "here's your file %r:" % filename
print fp.read()		#读取文件内容, 可以把结果赋给一个变量


# 输入新文件名
print "Type the filename again:"
file_again = raw_input('> ')

# 以 w只写 方式打开文件
fp_again = open(file_again,'r+')

#print fp_again.read()  #报错: IOError: File not open for reading  只写方式打开文件,不能读

fp_again.write('\nwhat\'s your name');




















