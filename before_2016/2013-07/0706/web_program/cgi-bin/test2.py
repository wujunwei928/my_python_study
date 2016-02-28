#!/usr/bin/python
#coding=utf-8
# 上面的 coding=utf-8 是指定python文件的编码, 在.py文件中有中文编码

import cgi

# 指定html头文件的同时, 指定生成html文件的编码, 
# 也可以像test1.py那样在下面的formHtml中用meta标签声明html页面的编码
header = 'Content-type:text/html;Charset=utf-8\n\n'

formHtml ='''<html><head><title>CGI DEMO</title></head>
<body>
	<form action='/cgi-bin/test2.py'>
		姓名:<input type="text" name='name' /><br/>
		年龄:<input type="text" name='age' /><br/>
		性别:<input type="text" name='sex' /><br/>
		<input type='submit' value='提交' />
	</form>
</body></html>'''

print header+formHtml


