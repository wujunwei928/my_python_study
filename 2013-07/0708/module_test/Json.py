#!/usr/bin/python
# -*- coding:utf-8 -*-

#
import json

arr1 = [1,2,3]
arr2 = {'name':'吴军伟','age':28,'sex':'男'}

print json.dumps(arr1)

# json.dumps(): 将 python对象 转成 json字符串
json_str = json.dumps(arr2,sort_keys=True)
print type(arr2)		# 输出: <type 'dict'>
print type(json_str)	# 输出: <type 'str'>
print json_str			# 输出: {"age": 28, "name": "\u5434\u519b\u4f1f", "sex": "\u7537"}

# json.loads(): 将 json字符串 转为 python对象
for i in json.loads('[1, 2, 3]'):	# 将json 转为 list
	print i

arr3 = json.loads(json_str);
for key in arr3:
	print arr3[key]
	
	











