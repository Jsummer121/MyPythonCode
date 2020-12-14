#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/27 20:33
import pymongo


class MyMongoDB:
    def __init__(self, db, collection):
        self.client = pymongo.MongoClient()
        self.db = self.client[db]
        self.col = self.db[collection]

    def my_insert(self, data, flag=True):
        if flag:
            self.col.insert_one(data)
        else:
            self.col.insert_many(data)

    def my_find(self, flag=True):
        if flag:
            print("查询单条数据结果为：{}".format(self.col.find_one()))
        else:
            print("查询全部的结果为：")
            for i in self.col.find():
                print(i)

    def my_update(self, data, query, flag=True):
        if flag:
            self.col.update_one(data, query)
        else:
            self.col.update_many(data, query)

    def my_delete(self, data, flag=True):
        if flag:
            self.col.delete_one(data)
        else:
            self.col.delete_many(data)
