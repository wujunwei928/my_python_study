#!/usr/bin/env python3

# 选择排序
def selectSort(arr):
	length=len(arr)
	if length <= 1:
		return arr

	for i in range(length):
		for j in range(i+1,length):
			if arr[i] < arr[j]:
				arr[i],arr[j]=arr[j],arr[i]
	return arr

# 冒泡排序
def bubbleSort(arr):
	length = len(arr)
	if length <= 1:
		return arr

	for i in range(length):
		for j in range(length-i-1):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
	return arr

# 插入排序
def insertSort(arr):
	length = len(arr)
	if length <= 1:
		return arr
	for i in range(length):
		for j in range(i+1,0,-1):
			if arr[j] > arr[j-1]:
				arr[j],arr[j-1]=arr[j-1],arr[j]


arr=[9,1,3,8,6,2]
print( selectSort(arr) )
print( bubbleSort(arr) )
print( insertSort(arr) )

# for j in range(2,0,-1):
# 	print(j)
