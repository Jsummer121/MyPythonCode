# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spider import RedisSpider
from ..items import items,TweetsItem

class SinaSpider(RedisSpider):
# class SinaSpider(scrapy.Spider):
    name = 'Sina'
    # start_urls = ['https://weibo.cn/5187664653/info']
    redis_key = 'Sina:start_urls'


    def parse(self, response):
        #解析用户个人资料页面
        user_id = re.findall(r'(/d+)/info',response.url)
        # print(response.xpath('//div[@class="c"]//text()').extract())
        text = ';'.join(response.xpath('//div[@class="c"]//text()').extract())
        # print(text)
        Nickname = re.findall(r'昵称:(.*?);',text)
        Gender = re.findall(r'性别:(.*?);',text)
        Address = re.findall(r'地区:(.*?);',text)
        Birthday = re.findall(r'生日:(.*?);',text)
        VIPlevel = re.findall(r'会员等级:(.*?);',text)
        Authentication = re.findall(r'认证信息:(.*?);',text)

        if Nickname:
            items['Nickname'] = Nickname[0]
        if Gender:
            items['Gender'] = Gender[0]
        if Address:
            items['Address'] = Address[0]
        if Birthday:
            items['Birthday'] = Birthday[0]
        if VIPlevel:
            items['VIPlevel'] = VIPlevel[0]
        if Authentication:
            items['Authentication'] = Authentication[0]
        items['user_id'] = user_id

        if user_id:
            yield scrapy.Request(url='https://weibo.cn/{}'.format(user_id[0]),callback=self.parse_index,meta={'items':items})
        #对粉丝关注页面发起请求
        yield scrapy.Request(url='https://weibbo.cn/{}'.format(user_id[0]),callback=self.parse_user_id)


    def parse_index(self,response):
        user_id = (response.url).split('/')[-1]
        # 处理首页的粉丝数与关注数
        items = response.meta.get('items')
        Tewwts_number = re.findall(r'微博\[(\d+)\]',response.text)
        Fellow_number = re.findall(r'关注\[(\d+)\]',response.text)
        Fans_number = re.findall(r'粉丝\[(\d+)\]',response.text)
        if Tewwts_number:
            items['Tewwts_number'] = int(Tewwts_number[0])
        if Fellow_number:
            items['Fellow_number'] = int(Fellow_number[0])
        if Fans_number:
            items['Fans_number'] = int(Fans_number[0])
        yield items

        tweet_items = TweetsItem()
        # 开始解析微博数据
        restult = response.xpath('//div[@class="c"]')
        if not len(restult) > 2:
            return None
        else:
            for item in restult:
                content = item.xpath('./div/span[@class="ctt"]/text').extract_first()
                publish_time = item.xpath('./div/span[@class="ct"]/text').extract_first()
                comment_num = re.findall(r'class="cc">评论\[(\d+)\]<',response.text)[0]
                tweet_items['content'] = content
                tweet_items['publish_time'] = publish_time
                tweet_items['comment_num'] = comment_num
                tweet_items['user_id'] = user_id
            yield tweet_items
            # 翻页
            next_url = response.xpath('//a[text()="下页"]/@href').extract()
            if next_url:
                yield scrapy.Request(url='https://weibo.cn' + next_url[0], callback=self.parse_tweets())


    def parse_tweets(self,response):
        user_id = re.findall(r'https://weibo.cn/(\d+)?',response.url)[0]
        # 从第二页开始
        tweet_items = TweetsItem()
        # 开始解析微博数据
        restult = response.xpath('//div[@class="c"]')
        for item in restult:
            try:
                content = item.xpath('./div/span[@class="ctt"]/text').extract_first()
                publish_time = item.xpath('./div/span[@class="ct"]/text').extract_first()
                comment_num = re.findall(r'class="cc">评论\[(\d+)\]<', response.text)[0]
                tweet_items['content'] = content
                tweet_items['publish_time'] = publish_time
                tweet_items['comment_num'] = comment_num
                tweet_items['user_id'] = user_id
            except IndexError:
                pass
            else:
                yield tweet_items
        # 翻页
        next_url = response.xpath('//a[text()="下页"]/@href').extract()
        if next_url:
            yield scrapy.Request(url='https://weibo.cn' + next_url[0], callback=self.parse_tweets())


    def parse_user_id(self,response):
        #解析用户的id值
        uid_list = re.findall(r'https://weibo.cn/u/(\d+)"',response.text,re.S)

        # 发起其他用户的请求
        for uid in uid_list:
            yield scrapy.Request(url='https://weibo.cn/{}/info'.format(uid))

        # 翻页
        next_url = response.xpath('//a[text()="下页"]/@href').extract()
        if next_url:
            yield scrapy.Request(url='https://weibo.cn'+next_url[0],callback=self.parse_user_id)