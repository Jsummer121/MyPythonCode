# -*- coding: utf-8 -*-

import urllib.request


# #爬取图片
# req = urllib.request.urlopen('http://www.weimeitupian.com/wp-content/uploads/2019/06/20190604074219709.gif')
# data = req.read()
# with open('1.jpg','wb') as f:
#     f.write(data)


# 1发起请求
# data = urllib.request.urlopen('https://www.taobao.com')#拿到的是urllib.response的对象,需要read才可以查看二进制码,并且read只能读取一次.
# print(data)


#2添加headers 伪装成浏览器访问

#客户端信息
#Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36     正常为：python-urllib/3.7

# herders = {
#     'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
# }
# req = urllib.request.Request('https:www.jianshu.com',headers = herders) #实例
# #发送请求
# urllib.request.urlopen(req).read().decode()



#3.Cookies操作
# from http import cookiejar
# #创建一个cookies对象
# cookies = cookiejar.CookieJar()
#
# #创建一个cookies处理器
# req = urllib.request.HTTPCookieProcessor(cookies)
#
# #创建一个opener对象
# opener = urllib.request.build_opener(req)
#
# data = urllib.request.urlopen('https://www,baidu.com')
# print(data.info())
#
#
#
# data = opener.open('https://www,baidu.com')
# print(data.info())

# #代理
# #创建代理
# proxy = {'http':'221.6.32.206:41816'}
#
# #创建一个代理处理器
# proxies = urllib.request.ProxyHandler(proxy)
# #创建一个opener对象
# opener = urllib.request.build_opener(proxies)
#
#
# # print(urllib.request.urlopen('http://httpbin.org/ip').read().decode())
# print(opener.open('http://httpbin.org/ip').read().decode())

#url里的编码与解码
from urllib import parse

params = '夏天'
print(parse.quote(params)) #编码
#%E5%A4%8F%E5%A4%A9

print(parse.parse_qs('wd=%E5%A4%8F%E5%A4%A9'))


print(parse.unquote('%E5%A4%8F%E5%A4%A9'))
print(parse.unquote('%E5%A4%8F%E5%A4%A9'))#单独解码

print(parse.urlencode({'wd': ['夏天']}))#他可以接受字典



#
# import urllib3
# # http = urllib3.PoolManager()
# #
# # res = http.request('GET','https://www.baidu.com')
# # print(res.data.decode())
#
#
#
# #用文件的形式下载
# # http = urllib3.PoolManager()
# # data = http.request('GET','http://httpbin/bytes/1024000')
# # print(data.data)
#
# #文件上传
# http = urllib3.PoolManager()
# with open('capt.jpg','rb') as f:
#     image_content = f.read()
#
# r = http.requets('post','http://httpbin.org/post',body=image_content)