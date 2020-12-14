#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/26 19:16
import pymongo


# 1.建立连接
client = pymongo.MongoClient()
# 2.指定数据库
db = client["py_49"]
# 3.指定集合
col = db["student"]

# 1.添加文档
# col.insert_one({"name": "lee", "age": 18, "sex": "M"})
# col.insert_many([
#     {"name": "tomas", "age": 15, "sex": "M"},
#     {"name": "misa", "age": 18, "sex": "F"},
#     {"name": "meng", "age": 15, "sex": "F"},
#     {"name": "meixi", "age": 16, "sex": "M"},
#     {"name": "que", "age": 20, "sex": "M"},
# ])
# 2.查找文档
# res = col.find_one()
# print(res)
# res = col.find()
# print(res)  # <pymongo.cursor.Cursor object at 0x7f1213e26668>
# for i in res:
    # print(i)

# 3.修改文档
# col.update_one({"name": "misa"}, {"$set": {"age": 15}})
# col.update_many({"age": 15}, {"$set": {"age": 88}})

# 4.删除文档
# col.delete_one({"name": "misa"})
# col.delete_many({"age": 88})
col.delete_many({"$or": [{'name': 'lee'}, {'name': 'meixi'}, {'name': 'que'}]})

res = col.find()
for i in res:
    print(i)


