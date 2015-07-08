#/usr/bin/python
# -- coding:utf-8 --


# 格式化字符串
# python不像php, php可以把双引号中的变量解析为变量对应的值
# 在python中,双引号"" 和 单引号的作用完全一样, 都和php的单引号用法类似

# 要想
my_name = 'wjw'
my_sex  = 'man'
my_age  = 28
my_height = 167
my_weight = 58


# python不会自动解析引号中的变量 如:
print "My name is my_name"		#输出: My name is my_name  

# 解决方法:

# ①: 用字符串连接符 + 
print 'my name is '+my_name+', and my sex is '+my_sex
# 局限, + 只能连接字符串, 如下面连接数字报错
#print 'my age is '+my_age   #报错: TypeError: cannot concatenate 'str' and 'int' objects

# ②: 由于 + 的局限性, 所以python中一般用%来格式化字符串

# %s能格式化 字符串,数字,列表,字典...
print "My name is %s." %my_name		# %s 字符串
print "My age is %s" %my_age
print "%s" %[1,2,3]
print "%s" %{'name':'小李','age':18}

# %d 只能格式化 数字
print "My age is %d" %(my_age) 
#print "My name is %d" %my_name  # 报错: TypeError: %d format: a number is required, not str

# 一行格式化多个变量
print "My height is %d, and my weight is %d" %(my_height,my_weight) 

# %r 含义: '不管什么都打印出来' 
print '%r' %100
print '%r' %'jim'
print '%r' %[1,2,3]
print '%r' %{'name':'lilei'}
x = 'my name is %s' %my_name
print 'I say: %r'%x		#输出: I say: 'my name is wjw'
print 'I say: %s'%x		#输出: I say: my name is wjw