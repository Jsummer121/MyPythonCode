# -*- coding: utf-8 -*-
import scrapy


class AreaSpider(scrapy.Spider):
    name = 'area'
    # allowed_domains = ['dddd']
    start_urls = ['https://www.aqistudy.cn/historydata/daydata.php?city=成都&month=201404']

    def parse(self, response):
        print(response.text)
