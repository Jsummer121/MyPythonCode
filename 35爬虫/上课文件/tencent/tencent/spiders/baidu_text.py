# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BaiduTextSpider(CrawlSpider):
    name = 'baidu_text'
    # allowed_domains = ['dddd']
    # start_urls = ['https://www.baidu.com']
    #
    # rules = (
    #     Rule(LinkExtractor(allow=r'http.*?'), callback='parse_item', follow=True),
    #     Rule(LinkExtractor(restrict_xpaths='//a'), callback='a_item', follow=True),
    # )
    #
    # def parse_item(self, response):
    #     print(response.url,'======')
    #     item = {}
    #     return item
    #
    # def a_item(self, response):
    #     print(response.url, '======')
    #     item = {}
    #     return item


    # 查看代理是否成功
    start_urls = ['https://httpbin.org/ip']

    def parse(self, response):
        print(response.text,'=====================')



    # 取消去重
    # def parse(self, response):
    #     print(response,'=========')
    #     yield scrapy.Request(url='https://www.baidu.com',dont_filter=True)