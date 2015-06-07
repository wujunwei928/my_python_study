#!/usr/bin/python
# _*_ coding: utf-8 _*_     # 指定字符编码的上面不能有空行, 否则报错
 
print 'Hello Python'    #老版本直接print
 
print('测试') #新版本要print()函数, 文件中有中文的话, 文件开头要指定utf-8编码
 
 
# python中每条语句结尾的分号,可写可不写
print('hello');
# 但是如果一行中有多条逻辑语句的时候,必须以分号隔开,最后一条语句的分号可以省略
# 在python中, 一般每行语句最后的分号省略不写
print( 1+ 8);print( 3* 6)
 
 
# 定义整型变量
x=y=z=10
print(x*y*z)
 
# ** 幂运算
print( 3** 3) #3**3: 3的3次方
 
 
 
# Python中整除运算最终值取的是中间值的floor值
print( 7/- 3) #输出: -3
print( 7%- 3) #输出: -2
 
 
# python函数,分支结构初探
def getScoreDesc (score):
    if score>=90:        # python中没有switch,没有else if,elseif, 
        print '优秀'  #python中的分支关键字: if, elif, else
    elif score>=60 and score<90:  # python中的逻辑运算符 and, or, not
        print '一般'              # python中没有 &&, || 运算符  
    else:
        print '不及格'
getScoreDesc(90)    # 调用函数
 
 
#python中只有for, while循环, 没有do...while循环