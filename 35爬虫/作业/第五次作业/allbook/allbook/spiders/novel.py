# -*- coding: utf-8 -*-
import scrapy
from ..items import AllbookItem

class NovelSpider(scrapy.Spider):
    name = 'novel'
    # allowed_domains = ['ddddd']

    # start_urls = ['http://www.quanshuwang.com/list/1_1.html']

    # 第一种
    def start_requests(self):
        for i in range(1,100):
            next_pages = 'http://www.quanshuwang.com/list/1_{}.html'.format(i)
            yield scrapy.Request(url=next_pages)

    def parse(self, response):
        novel_name_list = response.xpath('//a[@class="clearfix stitle"]/@title').extract()
        novel_writer_list = response.xpath('//span[@class="l"]/a[2]/text()').extract()
        novel_url_list = response.xpath('//ul[@class="seeWell cf"]/li/a[1]/@href').extract()

        for novel_name,novel_writer,novel_url in zip(novel_name_list,novel_writer_list,novel_url_list):
            items = {}
            items['novel_name'] = novel_name
            items['novel_writer'] = novel_writer
            items['novel_url'] = novel_url
            yield items

        # 实现翻页功能
        # next_url = response.xpath('//a[@class="next"]/@href').extract()
        # if next_url:
        #     yield scrapy.Request(url=next_url[0])