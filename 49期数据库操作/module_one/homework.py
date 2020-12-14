#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/30 20:00

# redis 列表操作封装成类
import redis

# 创建连接
con = redis.StrictRedis(db=2, decode_responses=True)

# 列表操作（增删改查）
# con.rpush('list_k', 'v1', 'v2', 'misa', 'tomas')  # 尾部添加
# con.lpush('list_k', 'rish', '011')  # 头部添加
# print(con.lrange('list_k', 0, 10))  # 通过索引范围查询
# print(con.lindex("list_k", 5))  # 通过制定索引查值
# con.lset('list_k', 5, "tomas")  # 修改指定索引值
# res = con.lpop('list_k')  # 删除头部第一个值并返回
# print(res)
# res = con.rpop("list_k")  # 删除尾部第一个值并返回
# print(res)


class MyRedisList:
    def __init__(self, db=0, decode_responses=False):
        self.con = redis.StrictRedis(db=db, decode_responses=decode_responses)

    def my_push(self, key, *values, flag="r"):
        if flag == "r":
            self.con.rpush(key, *values)
        else:
            self.con.lpush(key, *values)

    def my_search(self, key, start, end=None):
        if end:
            print(self.con.lrange(key, start, end))
        else:
            print(self.con.lindex(key, start))

    def my_set(self, key, index, value):
        self.con.lset(key, index, value)





