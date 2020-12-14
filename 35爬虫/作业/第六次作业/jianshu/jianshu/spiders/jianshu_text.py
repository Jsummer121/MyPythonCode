# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy_redis.spiders import RedisCrawlSpider,RedisSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# class JianshuTextSpider(CrawlSpider):
class JianshuTextSpider(RedisCrawlSpider):#改成scrapy_redis组件
    name = 'jianshu_text'
    # allowed_domains = ['dddd']
    # start_urls = ['https://www.jianshu.com/p/372e5ddf6cda']
    redis_key = 'jianshu:start_urls'
    rules = (
        Rule(LinkExtractor(allow=r'https://www.jianshu.com/p/.*?'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # print(response.url,'=========')
        item = {}
        item['title'] = response.xpath('//h1/text()').extract_first()
        # item['author'] = response.xpath('//div[@class="Cqpr1X"]/a[@class="_1OhGeD"]').extract()
        item['author'] = response.xpath('//span[@class="_22gUMi"]/text()').extract_first()
        item['time'] = response.xpath('//time/text()').extract_first()
        # item['read_num'] = response.xpath('//div[@class="s-dsoj"/span[3]/text()').extract()
        item['read_num'] = re.findall(r'<span>阅读 (\d+)</span>',response.text)[0]
        return item