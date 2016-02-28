def myReverse(str):
	newStr = ''
	for i in xrange(len(str)-1,-1,-1):
		newStr += str[i]
	return newStr

str = 'wujunwei'
print(myReverse(str))