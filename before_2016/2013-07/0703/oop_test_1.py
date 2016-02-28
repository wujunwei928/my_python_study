#!/usr/bin/python
#coding=utf-8			#两种指定编码的格式
#_*_ coding: utf-8 _*_


# 面向对象 之 封装


class People:

	# 在Python中没有 public 和 private 这些关键字来区别公有和私有，它是以命名方式来区分，
	# 如果在属性名前面加了2个下划线'__'，则表明该属性是私有属性，否则为公有属性（方法也是一样)
	name = 'jack'		#共有属性
	__age = 28			#私有属性: 	
	__salary = 8000		#私有属性

	# 定义类的方法用def关键字，
	# 类的方法至少会有一个参数，一般以名为'self'的变量作为该参数（用其他名称也可以），而且需要作为第一个参数
	# 这个'self'参数在调用函数的时候,是不需要传递的
	# 公有方法
	def getAge (self):		
		print self.__age
		self.__getSalary()	# 在调用类的方法的时候, 参数'self'不需要传递
	
	# 私有方法
	def __getSalary (self):
		print self.__salary
		

p = People()
print p.name
#print p.__age   # 调用私有属性, 报错
p.getAge()
#p.__getSalary()	 # 调用私有方法, 报错	

		

class People2:
	name = 'jim'
	country = 'china'

	# 构造方法:
	def __init__ (self,age):
		self.__age=age

	# 类方法:
	# 是类对象所拥有的方法，需要用修饰器"@classmethod"来标识其为类方法，
	# 对于类方法，第一个参数必须是类对象，一般以"cls"作为第一个参数
	#（当然可以用其他名称的变量作为其第一个参数，但是大部分人都习惯以'cls'作为第一个参数的名字，就最好用'cls'了），
	# 能够通过实例对象和类对象去访问。
	@classmethod
	def getCountry (cls):
		return cls.country

	# 实例方法: 
	# 在类中最常定义的成员方法，
	# 它至少有一个参数并且必须以实例对象作为其第一个参数，一般以名为'self'的变量作为第一个参数
	# 在类外实例方法只能通过实例对象去调用，不能通过其他方式去调用。
	def getAge (self):
		return self.__age

	# 静态方法:
	@staticmethod
	def getName ():		#静态方法不需要多定义参数
		return People2.name

	# 析构函数:
	def __del__ (sel):
		pass
			
peo = People2(18)
peo.sex = '男'		# 给对象动态的添加属性
print peo.sex
#del peo.name		# 删除对象的属性
print peo.name

# 类方法: 实例对象和类对象都可访问
print People2.getCountry()
print peo.getCountry()

# 实例方法: 只能由类的实例化对象调用
print peo.getAge()
#print People2.getAge()	#报错

# 静态方法,实例对象和类对象都可访问
print peo.getName()
print People2.getName()



# del释放变量
x=2
print x
del	x	  # del删除变量, (相当于php中的unset)
#print x   # 上面删除后,再打印报错 NameError: name 'x' is not defined





