#!/usr/bin/env python
# coding:utf-8

arr = {}
for line in open("test.txt"):
    tmpArr = line.strip().split(' ')
    if tmpArr[0] in arr:
        arr[tmpArr[0]].append(tmpArr[1])
    else:
        arr[tmpArr[0]] = [tmpArr[1]]
print arr

maxChindNum = 0
for k, v in arr.items():
    v.sort()
    arr[k] = v
    if len(v) > maxChindNum:
        maxChindNum = len(v)
# print maxChindNum
print arr

arr2 = []
n = 2  # qu qian liang ming
for i in range(0, maxChindNum, n):
    for k, v in arr.items():
        tmp = map(lambda x: "%s-%s" % (k, x), v[i:i + n])
        arr2.extend(tmp)

print arr2
