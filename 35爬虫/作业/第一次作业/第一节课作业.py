import re
import socket

# 首页的url
url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%8A%A8%E6%BC%AB'
base_path = '/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%8A%A8%E6%BC%AB'
base_host = 'image.baidu.com'

def read_content(client):
    # 循环读取响应内容
    res = b''
    data = client.recv(1024)
    while data:
        res += data
        data = client.recv(1024)
    return res

def set_socket(path,host,url):
    '''
    根据参数的域名和路径 创建套接字 发送报文
    :param path:
    :param host:
    :param url:
    :return:
    '''
    client = socket.socket()
    client.connect((host, 80))
    # 构造报文
    request = 'GET {} HTTP/1.0\r\nHost: {}\r\nReferer: {}\r\n\r\n'.format(path, host,url)
    client.send(request.encode())
    return client


client = set_socket(base_path,base_host,url)
# 读取响应
res = read_content(client)
# 通过正则表达式 匹配所有图片的url
image_urls = re.findall(r'"thumbURL":"(.*?)"',res.decode(),re.S)


for image_url in image_urls[:-3]:
    host = image_url.split('//')[-1].split('.com')[0]
    path = image_url.split('//')[-1].split('.com')[-1]

    image_client = set_socket(path,host+'.com',url)
    # 循环读取响应内容
    res = read_content(image_client)

    #通过正则匹配响应头信息后面的数据
    image_content = re.findall(b'\r\n\r\n(.*)',res,re.S)[0]

    image_file_name = path.split('/')[-1]

    with open(image_file_name,'wb') as f:
        f.write(image_content)














