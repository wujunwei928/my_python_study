#/usr/bin/python
#coding=utf-8

import math		# 引入模块

print math.sqrt(2)	#调用模块中的方法,必须带模块名  求平方根: 1.414...



# 有时候我们只需要用到模块中的某个函数，只需要引入该函数即可，此时可以通过下面语句执行
# from 模块名 import 函数名1,函数名2....      #这样引用的时候,就不用带模块名,直接调用函数名即可

# PS:应该避免使用from..import而使用import语句，因为这样可以使你的程序更加易读，也可以避免名称的冲突。

# 二. 定义自己的模块
from sort_test import bubbleSort    #引入sort_test.py文件中的bubbleSort方法, 会生成一个扩展名为.pyc的文件
arr=[1,9,2,8,3,6]			
print bubbleSort(arr)
#print selectSort(arr)	#报错

