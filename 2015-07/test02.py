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

arr=[9,1,3,8,6,2]
print( selectSort(arr) )