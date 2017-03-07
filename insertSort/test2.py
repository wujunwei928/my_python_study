#!/usr/bin/evn python
# coding: utf-8

"""
需求: 将字典d1 和 d2 合并, d1的元素保持不变, 
d2中元素的rank值如果被d1中对应topic_id的元素占用, 其rank值相应的往后移
"""

d1 = [
    {'topic_id': 1, 'sku_id': 100, 'rank': 2, 'part': 1},
    {'topic_id': 1, 'sku_id': 101, 'rank': 3, 'part': 1},
    {'topic_id': 2, 'sku_id': 201, 'rank': 1, 'part': 1}
]

d2 = [
    {'topic_id': 2, 'sku_id': 200, 'rank': 1, 'part': 2},
    {'topic_id': 1, 'sku_id': 102, 'rank': 1, 'part': 2},
    {'topic_id': 1, 'sku_id': 103, 'rank': 3, 'part': 2},
    {'topic_id': 1, 'sku_id': 104, 'rank': 2, 'part': 2}
]

# 为d1, d2的子字典元素, 添加new字段, 和rank相等
[x.setdefault('new', x['rank']) for x in d1]
[x.setdefault('new', x['rank']) for x in d2]

# 循环字典d1, d2, 更新d2中的new字段
for k1, v1 in enumerate(d1):
    for k2, v2 in enumerate(d2):
        v2['new'] = v2['new'] + 1 if v2['topic_id'] == v1['topic_id'] and v2['new'] >= v1['rank'] else v2['new']
        d2[k2] = v2
d1.extend(d2)

# python sorted 多个字段排序
sorted_d1 = sorted(d1, key=lambda x:(x['topic_id'], x['new']))

# 取相应的字段, 得到最终的字典
d3 = [{'topic_id':x['topic_id'], 'sku_id':x['sku_id'], 'final_rank':x['new']} for x in sorted_d1]
