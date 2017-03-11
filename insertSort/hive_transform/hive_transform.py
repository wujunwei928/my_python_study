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

if __name__ == "__main__":

    # 表1 中 part字段的 值
    d1_part_value = 1

    # 解析每一行数据
    for line in sys.stdin:
        # 略过空行
        if not line or not line.strip():
            continue

        # record_list 用来记录表记录
        record_list = []

        # 记录每个topic_id对应的rank关系表, 用来推断表2中相应记录的rank变化
        # 最初只记录 表1 中 相应topic_id对应的rank值列表, 后续会补充 表2 中 产生变化的rank值
        rank_relationship = {}

        all_record_in_one_line = line.strip().split(";")

        for one_record in all_record_in_one_line:

            # 这里用try 避免特殊行解析错误导致全部出错
            try:
                topic_id, sku_id, rank, part = [int(x) for x in one_record.strip().split(":")]    # 保存的时候, 统一使用int值, 便于比较
            except:
                continue
            # 保存相关记录
            record_list.append({'topic_id': topic_id, 'sku_id': sku_id, 'rank': rank, 'part': part})

            # 保存表1 中 每个topic_id对应的rank值列表
            if part == d1_part_value:
                rank_relationship.setdefault(topic_id, [])
                rank_relationship[topic_id].append(rank)

        # 将表1 和 表2 的数据分离出来
        d1 = [x for x in record_list if int(x['part']) == d1_part_value]
        d2 = [x for x in record_list if int(x['part']) != d1_part_value]
        del(record_list)

        # 针对表2对topic_id,rank值排序, 便于比较改变表2中相应的rank值
        d2 = sorted(d2, key=lambda x: (x['topic_id'], x['rank']))    # python sorted 多个字段排序

        # # 这步比较建立在上面排序的基础上, 一定要先排序, 再进行下面改变rank值操作
        for k2, v2 in enumerate(d2):
            tmp_rank = v2['rank']
            tmp_rank_list = rank_relationship.get(v2['topic_id'], [])
            # 如果表2中记录的rank值在对应的rank列表中, 自增1, 直到不在对应的rank列表中
            # 假设表1中topic_id=1 有对应的rank 1, 2, 3  表2中有1, 2, 3
            # 1 在 [1, 2, 3] 中, 自增变为2, 2还在[1, 2, 3]中, 自增变为3, 3还在[1, 2, 3]中, 自增变为4, 4不在[1,2,3], 终止循环,
            # 同时将4补充到rank关系列表中, 变为[1, 2, 3, 4]
            # 接下来比较2, 2在[1, 2, 3, 4]中, 自增为3, 3在[1, 2, 3, 4]中, 自增为4, 4在[1, 2, 3, 4]中, 自增为5
            # 这里可以看到, 如果不将表2中对应变化的rank值补充到rank关系列表中, 后面判断可能会导致同一个topic_id下会出现相同的rank值
            if tmp_rank in tmp_rank_list:
                while tmp_rank in tmp_rank_list:
                    tmp_rank += 1
                rank_relationship[v2['topic_id']].append(tmp_rank)    # 将变化的rank值保存起来, 便于后续rank值变化比较
                d2[k2]['rank'] = tmp_rank

        # 对调整rank值之后, 两个表的数据再组合起来, 进行排序
        d1.extend(d2)
        del(d2)
        # sorted 针对多个字段排序, 默认是升序, 如果想哪个字段降序, 前面加-
        sorted_record_list = sorted(d1, key=lambda x: (x['topic_id'], x['rank']))
        # 像上面:先针对topic_id升序, 再针对rank升序;  如下面: 先针对topic_id降序, 再针对rank升序
        # sorted_record_list = sorted(d1, key=lambda x: (-x['topic_id'], x['rank']))

        # 打印输出
        for k, v in enumerate(sorted_record_list):
            print('%d\t%d\t%d' % (v['topic_id'], v['sku_id'], v['rank']))
