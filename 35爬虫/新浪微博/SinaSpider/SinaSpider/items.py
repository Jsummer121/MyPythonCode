# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    user_id = scrapy.Field()
    Nickname = scrapy.Field() #昵称
    Gender = scrapy.Field()#性别
    Address = scrapy.Field()#地区
    Birthday = scrapy.Field()#生日
    VIPlevel = scrapy.Field()#vip等级
    Authentication = scrapy.Field()#认证信息
    Tewwts_number = scrapy.Field()#微博数
    Fellow_number = scrapy.Field()#关注数
    Fans_number = scrapy.Field()#粉丝数


# 用户的微博信息
class TweetsItem(scrapy.Item):
    user_id = scrapy.Field()
    content = scrapy.Field()
    publish_time = scrapy.Field()
    comment_num = scrapy.Field()
    # like_num = scrapy.Field()






