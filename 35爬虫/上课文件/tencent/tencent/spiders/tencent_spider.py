# -*- coding: utf-8 -*-
import scrapy
from ..items import TencentItem

class TencentSpiderSpider(scrapy.Spider):
    name = 'tencent_spider'

    # allowed_domains = ['dddd']
    start_urls = ['https://ke.qq.com/course/list/pyhon']

    def parse(self, response):
        """
        解析数据  返回items 并没有返回新的request
        :param response: 
        :return: 
        """
        title_list = response.xpath('//ul[@class="course-card-list"]/li/h4/a/text()').extract()#.extract()把select对象序列化成字符串
        link_url_list = response.xpath('//ul[@class="course-card-list"]/li/h4/a/@href').extract()
        image_url_list = response.xpath('//ul[@class="course-card-list"]/li/a/img[@class="item-img"]/@src').extract()


        # 正常情况
        # for title,link_url,image_url in zip(title_list,link_url_list,image_url_list):
        #     items = TencentItem()
        #     items['title'] = title
        #     items['link_url'] = link_url
        #     items['image_url'] = image_url
        #     yield items


        # 当出现详情页需要获取更多的值时：
        for title,link_url,image_url in zip(title_list,link_url_list,image_url_list):
            items = TencentItem()
            items['title'] = title
            items['link_url'] = link_url
            items['image_url'] = image_url
            yield scrapy.Request(url = link_url,callback=self.parse_price,meta={'items':items})



    def parse_price(self,response):
        items = response.meta.get('items')
        price = 9999
        items['price'] = price
        yield items