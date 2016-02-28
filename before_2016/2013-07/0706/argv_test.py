#/usr/bin/python
# -- coding:utf-8 --


# argv用来接收操作者在命令行模式下传给脚本的参数
# 命令行模式下给脚本传参数格式: python argv_test.py a1 b2 ...

# 引入 argv 功能
from sys import argv

# argv 是所谓的“参数变量(argument variable)”，这个变量包含了你传递给Python 的参数。
# argv 是一个非常标准的编程术语。在其他的编程语言里你也可以看到它(如: php中的$argv )


# argv 是一个数组, 数组的第一个参数是被执行的文件名, 后面的是参数
print argv	#输出: ['argv_test.py', 'a1', 'b2', 'c3']

# 把argv 中的东西解包，将所有的参数依次赋予左边的变量名
script, first, second, third =argv		# 既然这样解包了, 那在命令行下执行文件的时候,包含文件名要传4个参数, 多一个,少一个都不行

print script	#第一个参数永远是文件名 xxx.py
print first
print second
print third
