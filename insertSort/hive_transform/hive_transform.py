#!/usr/bin/env python
# coding=utf-8

"""
1: 本地测试运行
cat sku.txt | python hive_transform.py

2: hive中使用python脚本做Map-Reduce
hql 语句中 使用python脚本 作为输出用来创建新表
> add file hive_transform.py
> create table new_table as select transform (topic_id, sku_id, rank, part) using 'python hive_transform.py' as (topic_id, sku_id, final_rank) from sku_table_3
"""

import sys
       
if __name__=="__main__":

    d3 = []
    # 解析每一行数据
    for line in sys.stdin:
        # 略过空行
        if not line or not line.strip():
            continue

        # 这里用try 避免特殊行解析错误导致全部出错
        try:
            topic_id, sku_id, rank, part = line.strip().split("\t")
        except:
            continue

        d3.append({'topic_id':topic_id, 'sku_id':sku_id, 'rank':rank, 'part':part})

    d1 = [x for x in d3 if int(x['part']) == 1]

    for k1, v1 in enumerate(d1):
        for k2, v2 in enumerate(d3):
            v2['rank'] = int(v2['rank'])
            if (v2['part'] != v1['part']) and (v2['topic_id'] == v1['topic_id']) and (v2['rank'] >= v1['rank']):
                v2['rank'] += 1

    # python sorted 多个字段排序
    sorted_d3 = sorted(d3, key=lambda x:(x['topic_id'], x['rank']))

    # 打印输出
    for k, v in enumerate(sorted_d3):
        print( str(v['topic_id']) + "\t" + str(v['sku_id']) + "\t" + str(v['rank']) )