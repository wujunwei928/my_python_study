#/usr/bin/python
#coding=utf-8


# 面向对象 之 继承, 多态

# 一: 继承
class UniversityMember:
	def __init__ (self,name,age):
		self.name = name
		self.age  = age

	def getName (self):
		return self.name

	def getAge (self):
		return self.age

# 在定义一个类的时候，可以在类名后面紧跟一对括号，在括号中指定所继承的父类，
# python允许多重继承, 所以如果有多个父类，多个父类名之间用逗号隔开。		
class Student(UniversityMember):
	def __init__ (self,name,age,sno,mark):
		# 显示调用父类的构造方法 (ps: 子类调用父类方法的时候,注意将参数self传过去)
		UniversityMember.__init__(self,name,age)	
		self.sno  = sno
		self.mark = mark

	def getSno (self):
		return self.sno
	
	def getMark (self):
		return self.mark


class Teacher(UniversityMember):

	def __init__ (self,name,age,tno,salary):
		UniversityMember.__init__(self,name,age)
		self.tno = tno
		self.salary = salary

	def getTno (self):
		return self.tno
	
	def getSalary (self):
		return self.salary

# 在大学中的每个成员都有姓名和年龄，而学生有学号和分数这2个属性，老师有教工号和工资这2个属性，
# 从上面的代码中可以看到：
#   1）在Python中，如果父类和子类都重新定义了构造方法__init( )__，在进行子类实例化的时候，子类的构造方法不会自动调用父类的构造方法，必须在子类中显示调用。
#
#　 2）如果需要在子类中调用父类的方法，需要以   父类名.方法  这种方式调用，以这种方式调用的时候，注意要传递self参数过去。
#
#　对于继承关系，子类继承了父类所有的公有属性和方法，可以在子类中通过父类名来调用，而对于私有的属性和方法，子类是不进行继承的，因此在子类中是无法通过父类名来访问的。
#
#  python允许多重继承, 即允许一个类有多个父类
#　对于多重继承，比如 class SubClass(SuperClass1,SuperClass2)
#　此时有一个问题就是如果SubClass没有重新定义构造方法，它会自动调用哪个父类的构造方法？这里记住一点：以第一个父类为中心。如果SubClass重新定义了构造方法，需要显示去调用父类的构造方法，此时调用哪个父类的构造方法由你自己决定；若SubClass没有重新定义构造方法，则只会执行第一个父类的构造方法。并且若SuperClass1和SuperClass2中有同名的方法，通过子类的实例化对象去调用该方法时调用的是第一个父类中的方法。
		
s = Student('小李',18,1001,99)
print s.getName()
print s.getAge()
print s.getSno()
print s.getMark()

s = Teacher('老王',36,101,10000)
print s.getName()
print s.getAge()
print s.getTno()
print s.getSalary()



# 二: 多态

# 观点①:
# python中没有接口interface, 所以有人就说python不支持多态
#
# 观点②:
# 但是也有人根据多态的含义仔细分析, 认为python支持多态:
# 多态即多种形态，在运行时确定其状态，在编译阶段无法确定其类型，这就是多态。
# Python中的多态和Java以及C++中的多态有点不同，
# Python中的变量是弱类型的，在定义时不用指明其类型，它会根据需要在运行时确定变量的类型（个人觉得这也是多态的一种体现），
# 并且Python本身是一种解释性语言，不进行预编译，因此它就只在运行时确定其状态，故也有人说Python是一种多态语言。
# 在Python中很多地方都可以体现多态的特性，
# 比如 内置函数len(object)，len函数不仅可以计算字符串的长度，还可以计算列表、元组等对象中的数据个数
# 这里在运行时通过参数类型确定其具体的计算过程，正是多态的一种体现。
	
		
# 内置函数len(object)，len函数不仅可以计算字符串的长度，还可以计算列表、元组等对象中的数据个数，
# len()函数的具体使用
x = 'hello'
print len(x)	# 计算字符串长度
y = [1,2,4]
print len(y)	# 计算数组的元素个数
	

		
	