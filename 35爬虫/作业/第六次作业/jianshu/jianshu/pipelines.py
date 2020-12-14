# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymongo

class JianshuPipeline(object):

    # def __init__(self):
    #     #打开sql数据库
    #     self.client = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='summer',database='jianshu',charset='utf8')
    #     self.cursor = self.client.cursor()
    # -------------华丽分割线

    def __init__(self):
        self.client = pymongo.MongoClient(host='127.0.0.1',port=27017)
        #建库
        self.db = self.client['jianshu']
        #建表
        self.connection = self.db['article']

    def process_item(self, item, spider):
        #sql语句 item就是要存储的数据
        # sql = 'insert into table_name value (item.get("title"),%s,%s,%s)'
        # sql = 'insert into jianshu values (%s,%s,%s,%s)'
        # sql = 'insert into jianshu values (item.get("title"),item.get("author"),item.get("time"),item.get("read_num"))'
        # self.cursor.execute(sql,[item.get("title"),item.get("author"),item.get("time"),item.get("read_num")])
        # self.cursor.execute('insert into jianshu values (item.get("title"),item.get("author"),item.get("time"),item.get("read_num"))')
        #-------------华丽分割线
        # self.connection.insert()
        self.connection.save(item)
        return item


    # def close_spider(self,spider):
    #     #关闭数据库
    #     self.cursor.close()
    #     self.client.close()
    # -------------华丽分割线
