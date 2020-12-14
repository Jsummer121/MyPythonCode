# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TencentPipeline(object):

    def __init__(self):
        self.f =open('result_json','w',encoding='utf-8')

    def process_item(self, item, spider):
        self.f.write(str(item)+'\n')
        return item


    def close_spider(self,spider):
        self.f.close()