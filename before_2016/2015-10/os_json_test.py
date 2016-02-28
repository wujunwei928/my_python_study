#!/usr/bin/python
#coding:utf-8

import os
import json

json_arr = ['[1,2,3]', 'hello','中国']
json_str = json.dumps(json_arr)
fp = os.popen("php py_use.php '%s'" %(json_str) )
print fp.read()

