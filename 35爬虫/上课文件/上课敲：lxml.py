# -*- coding: utf-8 -*-
from lxml import etree
import requests

# html = requests.get('https://www.baidu.com').content.decode()
#
# selector = etree.HTML(html)
# print(selector.xpath('..'))#查看父节点
# print(selector.xpath('.'))#查看当前节点
# print(selector.xpath('/html/body/div'))#[]
# print(selector.xpath('/html/body/div/text()'))#[' ',' ']
# # print(selector.xpath('/html/body/div//text()'))#[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '新闻', ' ', 'hao123', ' ', '地图', ' ', '视频', ' ', '贴吧', ' ', ' ', '登录', ' ', ' ', 'document.write(\'<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u=\'+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ \'" name="tj_login" class="lb">登录</a>\');\r\n                ', ' ', '更多产品', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '关于百度', ' ', 'About Baidu', ' ', ' ', '©2017\xa0Baidu\xa0', '使用百度前必读', '\xa0 ', '意见反馈', '\xa0京ICP证030173号\xa0 ', ' ', ' ', ' ', ' ']
# print(selector.xpath('//text()'))#[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '新闻', ' ', 'hao123', ' ', '地图', ' ', '视频', ' ', '贴吧', ' ', ' ', '登录', ' ', ' ', 'document.write(\'<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u=\'+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ \'" name="tj_login" class="lb">登录</a>\');\r\n                ', ' ', '更多产品', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '关于百度', ' ', 'About Baidu', ' ', ' ', '©2017\xa0Baidu\xa0', '使用百度前必读', '\xa0 ', '意见反馈', '\xa0京ICP证030173号\xa0 ', ' ', ' ', ' ', ' ']
# print(selector.xpath('//div[@id="u-sp"]'))



####不成熟

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
}
html = requests.get('https://www.jianshu.com',headers = headers)
selecton = etree.HTML(html.content.decode())
print(selecton.xpath('//ul[@class="note-list"]/li/div[@class="content"]/a/text()'))
ids = selecton.xpath('//ul[@class="note-list"]/li/@data-note-id')
params = {
    'seen_snote_ids[]':','.join(ids),
    'page':'2',

}

next_url = 'https://www.jianshu.com'


html = requests.get(next_url,params=params,headers = headers)

print(selecton.xpath('//ul[@class="note-list"]/li/div[@class="content"]/a/text()'))




