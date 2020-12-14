# data = {
#     "name": "菲菲",
#     "age": 18,
#     "feature" : ["白", "富", "美"]
# }
# print(data["feature"][1])


# import urllib.request
# a = urllib.request.urlopen('http://jandan.net/zoo//wx4.sinaimg.cn/mw600/00745YaMgy1g7ve6llnm6j30kk0fwwfg.jpg/g')
# b = a.read()
# with open('图片.jpg','wb') as c:
#     c.write(b)

# num = int(input())
# s = []
# for i in range(num):
#     s.append(input())
import requests

url = 'https://tutu-dns.com/meitui/20170908/891/101170.jpg'


res = requests.get(url)
# with open()














