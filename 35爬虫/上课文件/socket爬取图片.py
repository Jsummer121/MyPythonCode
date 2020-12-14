#导入库
import re
import socket

#  创建一个客户端
client = socket.socket()

# 连接百度
client.connect(('timgsa.baidu.com',80)) #里面是url加端口

# 构造报文
#报文的一般结构 'GET / HTTP/1.0(1.1)\r\nHost: www.baidu.com\r\n\r\n' #两个\r\n表示结束会话，一个表示进入下一个，如果出现403则需要在Host后面再加上\r\nReferer: www.baidu.com(这里需要的是的访问页面的上一级页面)
request = 'GET /timg?image&quality=80&size=b9999_10000&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201804%2F03%2F2018040395557_rlZFY.thumb.700_0.jpeg HTTP/1.0\r\nHost: timgsa.baidu.com\r\n\r\n'

# 发送消息给到百度
client.send(request.encode())

# 循环接受百度返回的数据
res = b''#bytes类型
data = client.recv(1024)

while data:
    res += data
    data = client.recv(1024)  # 最后一次 读取的时候 会返回一个空

image_content = re.findall(b'\r\n\r\n(.*)',res,re.S)#将图片中的\r\n\r\n后面的读取，re.S则是使他可以读取\。
#上面得到的是一个列表需要剪切才可以使用里面的字符串。

# 把图片写入到本地
with open('capt.jpg','wb') as f:
    f.write(image_content[0])










