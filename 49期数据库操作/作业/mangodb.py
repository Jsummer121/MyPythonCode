# -*- coding: utf-8 -*-
import pymongo

class mgo():
    def __init__(self):
        client = pymongo.MongoClient()
        db = client['py_49']
        self.col = db['student']

    def m_find_one(self):
        rec = self.col.find_one()
        print(rec)

    def m_find(self):
        rec = self.col.find()
        for i in rec:
            print(i)

    def m_insert_one(self,a):
        self.col.insert_one(a)

    def m_insert_many(self,b):
        self.col.insert_many(b)

    def m_delete_one(self,c):
        self.col.delete_one(c)

    def m_delete_many(self,d):
        self.col.delete_many(d)

    def m_updata_one(self,*args):
        self.col.update_one(*args)

    def m_update_many(self,*args):
        self.col.update_many(*args)


mgo=mgo()
# mgo.m_insert_many([{'name':'summer','age':15},{'name':'zwt','age':16},{'name':'green','age':18},{'name':'blue','age':18}])
# mgo.m_find_one()
# mgo.m_updata_one({"name": "summer"}, {"$set": {"age": 18}})
mgo.m_delete_many({'age':18})
mgo.m_find()