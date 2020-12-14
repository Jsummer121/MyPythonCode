# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BaiduSpider(scrapy.Spider):
    name = 'BaiDu'
    # allowed_domains = ['ddddd']
    start_urls = ['https://pan.baidu.com/share/init?surl=_MeZcwsgRSUW3fIor9zcug']


    def parse(self, response):
        pass
