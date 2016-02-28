#/usr/bin/python
#_*_ coding:utf-8 _*_


def bubbleSort (arr):
	for i in range(len(arr)):
		for j in range(0,len(arr)-i-1):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]	#python中简便的交换两个变量的方法: x,y=y,x
	return arr


def selectSort (arr):
	for i in range(len(arr)-1):
		for j in range(i+1,len(arr)):
			if arr[i]<arr[j]:
				arr[i],arr[j]=arr[j],arr[i]
	return arr

def swap (x,y):
	tmp = x
	x = y
	y = tmp	
			

		
	