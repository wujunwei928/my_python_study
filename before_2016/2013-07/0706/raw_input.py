#/usr/bin/pythong
# -- coding:utf-8 --


# raw_input 接收用户的输入

print "How old are you?",	# print语句的结尾加 逗号',' 的话, print打印之后就不会换行
age = raw_input()
print "how tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()
print "So, you're %r old, %r tall and %r heavy." %(age,height,weight)

# 上面用raw_input()接收用户参数的语句, 可以用以下格式简写
age = raw_input('How old are you?')
height = raw_input('How tall are you?')
weight = raw_input('How much do you weight?')
# \ 用来转义字符
print 'So, you\'re %r old, %r tall and %r heavy.' %(age,height,weight)