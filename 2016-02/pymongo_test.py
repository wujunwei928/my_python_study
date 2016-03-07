#coding=utf-8
import pymongo
# client = pymongo.mongo_client.MongoClient() 
#与以下两种方式等同
client = pymongo.mongo_client.MongoClient("localhost", 27017)
# client = pymongo.mongo_client.MongoClient("mongodb://localhost:27017/")

# db = client.test_db