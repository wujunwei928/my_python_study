#/usr/bin/python
# -*- coding:utf-8 -*-

import cgi

# 在向CGI脚本返回结果时, 须先返回一个适当的HTTP头文件才会返回html页面
# 进一步说, 为了区分这些 头文件 和 结果HTML页面
# 必须在声明 Content-type: text/html 头文件后 加 至少一个 换行符\n
resHtml = '''Content-type: text/html\n
<html><head><title>
python web programming test
</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head>
<body>your name is %s<br/>
your age is %s<br/>
your sex is %s<br/>
</body></html>''';		# 三引号''', """可以定义多行字符串


# 获取表单提交的值, 无论get, post方式提交的数据, 都是这样获取
form = cgi.FieldStorage()
name = form['name'].value
age = form['age'].value
sex = form['sex'].value

print resHtml % (name, age, sex)

















