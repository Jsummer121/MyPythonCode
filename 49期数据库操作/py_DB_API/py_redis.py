#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/29 21:41
import redis
import time

# 1.建立连接
con = redis.StrictRedis(decode_responses=True)

# 使用redis命令
# print(con.get("k2").decode('utf-8'))
# print(con.get("k2"))
# con.set("k2", "朦胧")  # utf-8
# con.delete("k1")
# 1.key 操作
# res = con.keys("*")
# print(res)
# con.rename('hash_a', 'hash_b')
# res = con.keys("*")
# print(res)
# con.expire('k1', 10)
# con.expire("list_a", 100)
# print(con.ttl('list_a'))
# time.sleep(5)
# print(con.ttl('list_a'))
# con.persist('list_a')
# 2.string/list/hash/set/sorted set
# con.hset("hash_test", "f1", "v1")
# con.hmset("hash_test", {'name': 'lee', 'age': 18})
# print(con.hgetall('hash_test'))
# print(con.hvals('hash_test'))
# print(con.hkeys('hash_test'))
# lpush
# rpush
# lpop
# rpop
# lrange
# lindex
# lset


