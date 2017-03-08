#!/usr/bin/env python
# coding=utf-8

"""
1: 本地测试运行
cat sku.txt | python hive_transform.py

2: hive中使用python脚本做Map-Reduce

    2.1: hql 语句中 使用python脚本 作为输出用来创建新表
    hive> add file hive_transform.py

    2.2: 
    # 下面这种情况, 会有多个reducer执行, 脚本会被多次执行, 每个reducer处理一部分数据, 然后再统一输出, 与你预期的结果不一致
    hive> create table new_table as select transform (topic_id, sku_id, rank, part) using 'python hive_transform.py' as (topic_id, sku_id, final_rank) from sku_table_3

    2.3:
    # 要想python脚本一次获得所有输出, 要使用 order by, 确保数据在同一个reducer 上 执行
    hive> create table wcx_2 as select transform (topic_id, sku_id, rank, part) using 'python hive_transform.py' as (topic_id, sku_id, final_rank) from (select * from wcx_1 order by topic_id) tmp

3: 参考资料
Hive + Python 数据分析入门: http://leanote.com/blog/view/539276d41a91080a06000002/
Hive使用TRANSFORM运行Python脚本总结: http://www.th7.cn/Program/Python/201405/197929.shtml
hive优化之------控制hive任务中的map数和reduce数: http://www.dataguru.cn/article-3269-1.html

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
            d3[k2] = v2

    # python sorted 多个字段排序
    sorted_d3 = sorted(d3, key=lambda x:(x['topic_id'], x['rank']))

    # 打印输出
    for k, v in enumerate(sorted_d3):
        print( str(v['topic_id']) + "\t" + str(v['sku_id']) + "\t" + str(v['rank']) )