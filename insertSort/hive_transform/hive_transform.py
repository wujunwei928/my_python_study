#!/usr/bin/env python
# coding=utf-8

"""
1: 本地测试运行
cat sku.txt | python custom_order_hive_transform.py

2: hive中使用python脚本做Map-Reduce
    2.1: hql 语句中 使用python脚本 作为输出用来创建新表
    hive> add file custom_order_hive_transform.py
    2.2:
    # 下面这种情况, 会有多个reducer执行, 脚本会被多次执行, 每个reducer处理一部分数据, 然后再统一输出, 与你预期的结果不一致
    hive> create table new_table as select transform (rankstrs) using 'python custom_order_hive_transform.py' as (topic_id, sku_id, final_rank) from app.phoenix_topic_sku_insert_sort_4

3: 参考资料
Hive + Python 数据分析入门: http://leanote.com/blog/view/539276d41a91080a06000002/
Hive使用TRANSFORM运行Python脚本总结: http://www.th7.cn/Program/Python/201405/197929.shtml
hive优化之------控制hive任务中的map数和reduce数: http://www.dataguru.cn/article-3269-1.html
"""

import sys

if __name__ == "__main__":

    # 表2 中 sort_order字段的 值
    d2_sort_order_value = 0

    # 解析每一行数据
    for line in sys.stdin:
        # 略过空行
        if not line or not line.strip():
            continue

        # record_list 用来记录表记录
        record_list = []

        all_record_in_one_line = line.strip().split(";")
        for one_record in all_record_in_one_line:

            # 这里用try 避免特殊行解析错误导致全部出错
            try:
                topic_id, sku_id, sort_order, final_score = [x for x in one_record.strip().split(":")]    # 保存的时候, 统一使用int值, 便于比较
            except:
                continue
            # 保存相关记录
            record_list.append({'topic_id': int(topic_id), 'sku_id': sku_id, 'sort_order': int(sort_order), 'final_score': float(final_score)})

        all_rank_list = range(1, len(record_list) + 1)
        # print(all_rank_list)
        # d1表中的rank值 就是其 sort_order 的值
        d1 = [{
            'topic_id': x['topic_id'],
            'sku_id': x['sku_id'],
            'rank': x['sort_order'],
        } for x in record_list if int(x['sort_order']) != d2_sort_order_value]
        d2 = [x for x in record_list if int(x['sort_order']) == d2_sort_order_value]
        del(record_list)

        # d2
        d1_rank_list = [x['rank'] for x in d1]
        d2_rank_list = list(set(all_rank_list) ^ set(d1_rank_list))

        d2 = sorted(d2, key=lambda x: x['final_score'], reverse=True)
        [v.setdefault('rank', d2_rank_list[k]) for k, v in enumerate(d2)]
        # print(d1, d2)

        # 对调整rank值之后, 两个表的数据再组合起来, 进行排序
        d1.extend(d2)
        del(d2)
        # python sorted 多个字段排序
        sorted_record_list = sorted(d1, key=lambda x: (x['topic_id'], x['rank']))

        # 打印输出
        for k, v in enumerate(sorted_record_list):
            print('%s\t%s\t%s' % (v['topic_id'], v['sku_id'], v['rank']))
