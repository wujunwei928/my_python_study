#/usr/bin/python
#coding=utf-8		#指定编码类型


# python函数练习


# ①: 定义函数, 用关键字def
#	return语句是可选的，它可以在函数体内任何地方出现，表示函数调用执行到此结束；
#	如果没有return语句，函数会自动返回None，
#	如果有return语句，但是return后面没有接表达式或者值的话也是返回None。
#   (ps: 和php类似, 只不过php的函数在类似情况下返回null )
def printHello ():
	print('hello')

def printNum ():
	for i in range(0,2):	#range(0,2) 生成一个数组,数组元素0,1
		print i
	return
		
def getSum (a,b):
	return a+b
	
print(printHello())		#返回: None
print(printNum())		#返回: None
print(getSum(1,2))		#返回: 3





# ②: 在Python中不允许函数前向引用，即在函数定义之前，不允许调用该函数. 如下:
#aa()	#报错: NameError: name 'aa' is not defined
def aa ():
	print 'aa'
# (ps: 和python不同, 在 javascript 和 php 中, 允许函数前向引用(即可以函数定以前,调用该函数) )





# ③: 在Python中一切皆对象，变量中存放的是对象的引用
# id(object)函数是返回对象object在其生命周期内位于内存中的地址，id函数的参数类型是一个对象
x=2
print id(2)		#输出: 10416132
print id(x)		#输出: 10416132
y='python'
print id(y)				#输出: 11290560
print id('python')		#输出: 11290560
# 解析:
#   在Python中一切皆对象，像2，'hello'这样的值都是对象，
#   只不过5是一个整型对象，而'hello'是一个字符串对象。
#	    上面的x=2，在Python中实际的处理过程是这样的：
#	    先申请一段内存分配给一个整型对象来存储整型值2，然后让变量x去指向这个对象，实际上就是指向这段内存（这里有点和C语言中的指针类似）。
#       而id(2)和id(x)的结果一样，说明id函数在作用于变量时，其返回的是变量指向的对象的地址。
#	    因为变量也是对象，所以在这里可以将x看成是对象2的一个引用。





# ④: python中函数中的参数传递类型( 值传递, 引用传递 )
def modify1 (m,k):
	m=2
	k=[4,5,6]
	return

def modify2 (m,k):
	m=3
	k[0]=9
	return

n=1
l=[1,2,3]
modify1(n,l)
print n			#输出: 1
print l			#输出: [1, 2, 3]
modify2(n,l)
print n			#输出: 1
print l			#输出: [9, 2, 3]
# 结果分析:(仔细理解其中的含义)
#	 (1):因为在Python中参数传递采用的是值传递方式，在执行函数modify1时，先获取n和L的id( )值，
#		然后为形参m和K分配空间，让m和K分别指向对象100和对象[1,2,3]。
#		m=2这句让m重新指向对象2，而K=[4,5,6]这句让K重新指向对象[4,5,6]。
#		这种改变并不会影响到实参n和L，所以在执行modify1之后，n和L没有发生任何改变；
#
#	 (2):在执行函数modify2时，同理，让m和K分别指向对象2和对象[1,2,3]，
#		然而K[0]=0让K[0]重新指向了对象0（注意这里K和L指向的是同一段内存），
#		所以对K指向的内存数据进行的任何改变也会影响到L，因此在执行modify2后，L发生了改变。


	

	
# ⑤: 在函数中调用全局变量, 必须用关键字global进行声明(和php相似)
wjw=28
def growUp ():
	global wjw	# 先用global声明全局变量
	wjw=29		# 给全局变量赋值	

print wjw	#28
growUp()
print wjw   #29
	



# ⑥: 函数参数的传递类型: 位置参数, 关键字参数
def display (a,b):
	print a+' '+b

# 位置参数: 即参数是通过位置进行匹配的，从左到右，依次进行匹配，这个对参数的位置和个数都有严格的要求。
# 一般的编程语言都是这种方式传递参数的, 如:php,js...
display('hello','world')	  #输出: hello world
display('world','hello')	  #输出: world hello

# 关键字参数: 通过指定参数名字传递参数，参数位置对结果是没有影响的。python特色
display(b='world',a='hello')  #输出: hello world





# ⑦: 给函数的参数设置默认值
def display2 (a='hi',b='py'):
	print a+' '+b
	
display2()	#输出: hi py
# 在 参数有默认值的情况下, 以 关键字参数 的方式传递参数
display2(b='python')	#输出: hi python
display2(a='hello')		#输出: hello py
display2(b='python',a='hello')		#输出: hello python





# ⑧: 任意个数参数:  在定义函数时如果无法确定参数的个数，可以使用收集参数，使用收集参数只需在参数前面加上 * 或者 **
# * 和 ** 表示能够接受0到任意多个参数，
# * 表示将没有匹配的值都放在同一个元组中，
# ** 表示将没有匹配的值都放在一个dictionary中。

# 用 * 传递多个参数的接收方法
def storename(name,*nickName):
    print 'real name is %s' %name
    for nickname in nickName:
        print nickname

storename('jack')
storename('詹姆斯','小皇帝')
storename('奥尼尔','大鲨鱼','三不沾')	#依次输出: real name is 奥尼尔     大鲨鱼     三不沾
										
# 用 ** 传递多个参数的接收方法
def printValue (a,**d):
	print 'a=%d' %a
	for x in d:
		print x+'=%d' %d[x]

printValue(1,b=2,c=3)	#依次输出: a=1 c=3 b=2		
	




# ⑨: 函数的多个返回值:
# Python中函数是可以返回多个值的，如果返回多个值，会将多个值放在一个元组或者其他类型的集合中来返回。
def multiReturn ():
	x=2
	y=[8,9]
	return x,y
	
print multiReturn()		#输出: (2, [8, 9])






