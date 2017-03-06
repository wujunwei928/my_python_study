#!/usr/bin/evn python
# coding: utf-8

import pandas as pd
from pandas import DataFrame
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

df1 = DataFrame(columns=['topic_id', 'sku_id', 'rank', 'part'], data=[[1, 100, 2, 1], [1, 101, 3, 1], [2, 201, 1, 1]])

df2 = DataFrame(columns=['topic_id', 'sku_id', 'rank', 'part'], data=[[2, 200, 1, 2], [1, 102, 1, 2], [1, 103, 3, 2], [1, 104, 2, 2]])


# d1 = df1.to_dict('records')
# d2 = df2.to_dict('records')

# 添加一列new, 用来保存调整后的新 rank
df1['new'] = df1.apply(lambda x: x['rank'], axis=1)
df2['new'] = df2.apply(lambda x: x['rank'], axis=1)

# 循环df1, 然后修改df2中符合条件的记录的new值
for k, v in df1.iterrows():
    # 如果df2中topic_id等于df1中某记录的topic_id的值, 并且df2中的new值 >= df1中该记录的rank值
    # 将df2中对应的new值 + 1; 否则new值保持不变
    df2['new'] = df2.apply(lambda x: x['new'] + 1 if x['topic_id'] == v['topic_id'] and x['new'] >= v['rank'] else x['new'], axis=1)

df3 = pysqldf('select topic_id, sku_id, new as final_rank from (select * from df1 union select * from df2) order by topic_id, new')
