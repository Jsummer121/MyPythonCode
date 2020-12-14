# -*- coding: utf-8 -*-
import scrapy
import time
from .password import password


class GithubLogSpider(scrapy.Spider):
    name = 'github_log'
    # allowed_domains = ['ddddd']
    start_urls = ['https://www.github.com/login/']

    def parse(self, response):
        """
        解析token值 构造data 发送post
        :param response: 
        :return: 
        """
        authenticity_token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()
        timestamp_secret = response.xpath('//input[@name="timestamp_secret"]/@value').extract_first()

        formdata = {
            'commit':'Sign in',
            'utf8':'✓',
            'authenticity_token':authenticity_token,
            'ga_id':'10379410.1563805341',
            'login':'jxxaizwt@icloud.com',
            'password':password,
            'webauthn-support':'supported',
            'webauthn-iuvpaa-support':'unsupported',
            'required_field_71b9':'',
            'timestamp':str(int(time.time()) * 1000),
            'timestamp_secret':timestamp_secret,
        }

        yield scrapy.FormRequest(url='https://www.github.com/session',formdata=formdata,callback=self.login_alter)

    def login_alter(self,response):
         if 'Jsummer121' in response.text:
             print('登录成功')



