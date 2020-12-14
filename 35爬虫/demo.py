import re
import socket

#首页的url
url = 'http://image.baidu.com/search/index?tn=baiduimage&word=%E5%8A%A8%E6%BC%AB'

#  创建一个客户端
client = socket.socket()

# 连接百度
client.connect(('image.baidu.com',80))


# 构造报文
request = 'GET /search/index?tn=baiduimage&word=%E5%8A%A8%E6%BC%AB HTTP/1.0\r\nHost: image.baidu.com\r\n\r\n'

# 发送消息给到百度
client.send(request.encode())

# 循环接受百度返回的数据
res = b''
data = client.recv(1024)

while data:
    res += data
    data = client.recv(1024)  # 最后一次 读取的时候 会返回一个空


#通过正则表达式 匹配所有图片的url
image_urls = re.findall(r'"thumbURL":"(.*?)"',res.decode(),re.S)

for image_url in image_urls[:-3]:
    host = image_url.split('//')[-1].split('.com')[0]
    path = image_url.split('//')[-1].split('.com')[-1]

    #在获取到host和path的情况下进行第二次爬取

    image_client = socket.socket()
    image_client.connect((host+'.com',80))
    image_request = 'GET {} HTTP/1.0\r\nHost: {}\r\nReferer: {}\r\n\r\n'.format(path,host+'.com',url)#出现403 需要加上Referer来伪造上级网页
    #发送网页请求
    image_client.send(image_request.encode())

    #循环接受数据
    res = b''
    data = image_client.recv(1024)
    while data:
        res += data
        data = image_client.recv(1024)


    # 通过正则匹配响应头部信息后面的数据
    image_content = re.findall(b'\r\n\r\n(.*)', res, re.S)[0]
    image_file_name = path.split('/')[-1]

    # 把图片写入到本地
    with open('socket图片收集/'+image_file_name, 'wb') as f:
        f.write(image_content)