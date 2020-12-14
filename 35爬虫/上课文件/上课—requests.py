import requests

# 请求方式
#r = requests.get('http://httpbin.org/get')
#r = requests.post('https://www.baidu.com')


#响应
# text属性 返回的时文本内容
# content属性 返回的二进制内容
# json方法     对json数据进行解码
# r.encoding = 'utf-8'
# print(r.json())

# 请求头
# 传参一定时关键字传参

# headers = {
#     ''
# }
#
# requests.get('https://www.jianshu.com',headers=headers,params=)


# 表单当中多个元素使用同一key的时候，data = (('key1':'value1'),('key1':'value2'))

# data = (('key1','value1'),('key1','value2'))
#
# print(requests.post('http://httpbin.org/post',data=data).cookies)

# 重定向   302 301  重定向

# r = requests.get('http://github.com',allow_redirects=False) # 禁止重定向
# print(r.headers)

# import requests
#
# url = 'http://httpbin.org/bytes/102400000'
#
# r = requests.get(url,stream=True)
#
# #print(r.content)
#
# for chunk in r.iter_content(chunk_size=1024):
#     print(chunk)

# session 会话对象   所有会话对象发出去的请求 会自动保持状态


# 同一主机发送多个请求，重用TCP连接

# import requests
# import time
# import urllib.request
#
# s = requests.session() # session 所有的api和requests都是一样的
#
# start_time = time.time()
# for i in range(50):
#     r = s.get('https://www.baidu.com')
#
# print('耗时:{}秒'.format(time.time()-start_time))


# 手动添加cookies

# headers = {
#     #'Cookie':'SINAGLOBAL=8253644680747.205.1557837860157; SCF=An1Ehww5pL0ULFtScaZuhpWzuVdBKvppnWGDkdy-TjnQIprWRsWucuxz6XWoFhAYHatzl793eE_8PgAnGVHwVrI.; SUHB=0N2kKvtZt0_zHb; ALF=1572097686; SUB=_2A25wiLHGDeRhGeNI4loS9ibNzz2IHXVQct-OrDV8PUJbkNAKLVHFkW1NSBs-t2sIn2d28PJoYFCpJBfc1zQaEsbW; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5jEjLBHlCIhxk14.TPipEV5JpX5oz75NHD95QfSo.Re0qReKBpWs4DqcjRi--ciKnRiK.pi--fiKLhi-2Ri--Ri-2fi-isi--fi-2piK.Ri--Ni-82iKn4i--Xi-i2i-27wrQt; Ugrow-G0=9ec894e3c5cc0435786b4ee8ec8a55cc; wvr=6; YF-V5-G0=95d69db6bf5dfdb71f82a9b7f3eb261a; wb_view_log_5698368141=1920*10801; _s_tentry=www.baidu.com; UOR=,,www.baidu.com; Apache=686057968637.399.1571059662781; ULV=1571059662880:9:1:1:686057968637.399.1571059662781:1569504728437; YF-Page-G0=89906ffc3e521323122dac5d52f3e959|1571059729|1571059660; webim_unReadCount=%7B%22time%22%3A1571059823394%2C%22dm_pub_total%22%3A2%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A38%2C%22msgbox%22%3A0%7D',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
# }
#
# r = requests.get('https://weibo.com/caizicaixukun',headers=headers)
# r.encoding='utf-8'
# print(r.text)

# 代理
#
# proxy = {
#     'http':'221.6.32.206:41816',
#     'https':'221.6.32.206:41816'
# }
#
# print(requests.get('http://httpbin.org/ip',proxies=proxy).json())







# 百度贴吧
#1. 请求首页地址 匹配每一个帖子的详情页url
#2. 翻页请求

# import re
# import requests
# import threading
#
#
# def parse(pn,word):
#     url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'.format(word,pn)
#     r = requests.get(url).content.decode()
#     article_urls = re.findall(r'<a rel="noreferrer" href="(/p/\d+)" title="(.*?)" target=',r,re.S)
#     return article_urls
#
# def parse_detail(article):
#     for article_url in article:
#         article_req = requests.get('https://tieba.baidu.com'+article_url[0]).text
#
#         author = re.findall(r'author: "(.*?)",',article_req,re.S)
#         create_time = re.findall(r'<span class="tail-info">1楼</span><span class="tail-info">(.*?)</span>',article_req,re.S)
#
#         if author and create_time:
#             print('作者:{},标题:{},发布时间:{}'.format(author[0],article_url[1],create_time[0]))
#
# if __name__ == '__main__':
#     word = input('请输入要搜索的贴吧名字:')
#     t_list = []
#     for pn in range(0,201,50):
#         # 先获取详情页url和标题
#         article = parse(pn,word)
#         # 对每一个详情页进行请求
#         t = threading.Thread(target=parse_detail,args=(article,))
#         t_list.append(t)
#
#     # 启动线程
#     for t in t_list:
#         t.start()
#
#     # 等待所有线程结束
#     for t in t_list:
#         t.join()
#































