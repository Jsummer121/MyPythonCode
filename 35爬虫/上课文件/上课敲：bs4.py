# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re


res = requests.get('https://www.baidu.com').content.decode()

soup = BeautifulSoup(res,'lxml')#后面的lxml是解析器，如果不指定默认为.html.parser


print(soup.div)#获取第一个div标签下的数据
print(soup.div.get_text())#获取div标签下的所有文本内容
print(soup.title.name)#获取title标签的标签名
print(soup.title.string)#获取title标签的文字内容
print(soup.title.parent.name)#获取title标签父标签的标签名
print(soup.p['class'])#获取第一个p标签的类的值
print(soup.find_all('a'))#获取所有的a标签
print(soup.find(id='fff'))#找到id等于ddd的标签
print(soup.find_all(text='新闻'))#通过文本查找
print(soup.find_all(re.compile(r'^b')))#通过正则表达式进行搜索----查找以b开头的东西
print(soup.find_all('div',id='u1'))#class是python里的关键字，所以在使用的时候需要加关键字。
print(soup.select('div > a'))
print(soup.select('div#u1'))
print(soup.select('a > .mnav'))
print(soup.select("a[class='mnav']"))
print(soup.select('a[class="mnav')[0].get_text())#获取文本内容，因为它返回的是一个列表所以需要进行切片-

