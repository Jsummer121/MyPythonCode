# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from .items import SinaspiderItem,TweetsItem

class SinaspiderPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(host='127.0.0.1',port=27017)
        db = client['Sina']
        self.Information = db['Information']
        self.Tweets = db['tweets']

    def process_item(self, item, spider):
        # 判断item类型 然后入库
        if isinstance(item,SinaspiderItem):
            self.Information.insert(dict(item))
        else:
            self.Tweets.insert(dict(item))
        return item

