#!/usr/bin/env python
#coding=utf-8

import requests
from pyquery import PyQuery as pq
import lxml

response = requests.get("http://www.neihan8.com/mm")

#设置编码, 否则下面reponse.text乱码, 因为返回的默认编码是ISO-8859-1
response.encoding='utf-8'

response_text = response.text
d=pq(response_text)
a = d('.pic-column-item')
print(a)
