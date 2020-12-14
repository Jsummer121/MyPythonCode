# -*- coding: utf-8 -*-
#一共6部

import re
import socket


#创建客户端
client = socket.socket()

#连接百度
client.connect(('www.baidu.com',80))

#创建报文
request = 'GET / HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n'

#消息发送到百度
client.send(request.encode())

#循环接收百度数据
res = b''
data = client.recv(1024)

while data:
    res += data
    data = client.recv(1024)

print(res)#爬取baidu首页的源代码。
# image_content = re.findall(b'\r\n\r\n',res,re.S)
#
# with open('1.jpg','wb') as f:
#     f.write(image_content[0])
