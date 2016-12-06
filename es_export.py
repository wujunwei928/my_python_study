#!/usr/bin/env python
# coding=utf-8

from datetime import datetime
from elasticsearch import Elasticsearch
import pandas as pd


# 创建es连接
es = Elasticsearch([
    # {'host': 'localhost'},  # 测试环境
    {'host': '10.140.70.125'},    # 正式环境
])


# 添加es文档
# doc = {
#     'author': 'kimchy',
#     'text': 'Elasticsearch: cool. bonsai cool.',
#     'timestamp': datetime.now(),
# }
# res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
# print(res['created'])


# 获取es文档信息
# res = es.get(index="test-index", doc_type='tweet', id=1)
# print(res['_source'])


# es.indices.refresh(index="test-index")

# 5115569
csv_file_name = 'gidStat.csv'

# 用from size的方式从es取数据, 默认只能取到10000,  采用scroll方式可以一直滚动的取下去
res = es.search(
    index = "stat-res-201612",
    doc_type = "gidStat",
    search_type = 'scan',
    scroll = '2m',
    size = 1000,
    body = {
        "query" : {
            "bool" : {
                "must" : {
                    "bool" : {
                        "must" : [
                            {
                                "range" : {
                                    "time" : {
                                        "from" : "2016-12-05T18:00:00.000+0800",
                                        "to" : "2016-12-06T16:00:00.000+0800"
                                    }
                                }
                            }
                        ]
                    }
                }
            }
        }
    }
)

# tmpRes = map(lambda x: x['_source'], res['hits']['hits']) 
# tmpDf = pd.DataFrame(tmpRes)
# del tmpDf['@timestamp']
# del tmpDf['@version']

# # 第一次插入csv, 需要header
# tmpDf.to_csv(csv_file_name, mode='a', index=False, header=True)


sid = res['_scroll_id']
scroll_size = res['hits']['total']
print(sid, scroll_size)

# Start scrolling
to_csv_header = True
while(scroll_size > 0):
    print "Scrolling..."
    res = es.scroll(scroll_id = sid, scroll ='2m')
    # Update the scroll ID
    sid = res['_scroll_id']
    # Get the number of results that we returned in the last scroll
    scroll_size = len(res['hits']['hits'])
    print "scroll size: "+ str(scroll_size)
    # Do something with the obtained res
    
    tmpRes = map(lambda x: x['_source'], res['hits']['hits']) 
    tmpDf = pd.DataFrame(tmpRes)
    del tmpDf['@timestamp']
    del tmpDf['@version']

    # 后续插入csv, 不需要header
    tmpDf.to_csv(csv_file_name, mode='a', index=False, header=to_csv_header)

    if to_csv_header:
        to_csv_header = False