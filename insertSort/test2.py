#!/usr/bin/evn python
# coding: utf-8

import pandas as pd
from pandas import DataFrame
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

df1 = DataFrame(columns=['topic_id', 'sku_id', 'rank', 'part'], data=[[1, 100, 2, 1], [1, 101, 3, 1], [2, 201, 1, 1]])

df2 = DataFrame(columns=['topic_id', 'sku_id', 'rank', 'part'], data=[[2, 200, 1, 2], [1, 102, 1, 2], [1, 103, 3, 2], [1, 104, 2, 2]])

# 添加一列new, 用来保存调整后的新 rank
df1['new'] = df1.apply(lambda x: x['rank'], axis=1)
df2['new'] = df2.apply(lambda x: x['rank'], axis=1)

d1 = df1.to_dict('records')
d2 = df2.to_dict('records')

# 方法2: 循环字典
for k1, v1 in enumerate(d1):
    for k2, v2 in enumerate(d2):
        v2['new'] = v2['new'] if v2['topic_id'] == v1['topic_id'] and v2['new'] >= v1['rank'] else v2['new']
        d2[k2] = v2
d1.extend(d2)
