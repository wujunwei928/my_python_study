#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# coding: utf-8

# print('中文')
# print('hello, %s') % 'world'
# print('Hi, %s, you have $%d.') %('wujunwei', 10000)
# print('%2d-%02d') %(3,1)
# print('%.2f') % 3.1415926
# print('Age: %s. Gender: %s') % (25, True)
# print('growth rate: %d %%') % 8

classmates = ['michael', 'bob', 'tracy']
# print(classmates)
# print(len(classmates))
# print(classmates[0])
# print(classmates[6])  #error 没有对应的数组元素

# 在Ubuntu上用 python test01.py运行得时候报错, 
# 找了半天原因, 最后终于想明白了, input是python3的函数
# python3 test01.py  或  chmod a+x test01.py  ./test01.py
# studentName = input('please enter your name: ')
# print('hello', studentName)


# python函数测试

""" 获取一个数字得绝对值 """
def getAbsolute(a):
	if a >= 0:
		print(a)
	else:
		print(-a)
# getAbsolute(10)
# getAbsolute(-99)

