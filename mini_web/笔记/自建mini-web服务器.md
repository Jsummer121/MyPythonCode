# Mini-Web服务器

## 一、socket

&nbsp;&nbsp;&nbsp;&nbsp;之前的文章有写过socket的一些东西，这次用来做服务器的底层的也是socket来构建。我们重新回到起点，来谈谈我们应该使用TCP还是UDP来进行通信？

### 1.1 TCP与UDP的区别

&nbsp;&nbsp;&nbsp;&nbsp;我们知道，UDP是**面向无连接的**，即发送的信息是在不知道对方是否能接受到消息的情况下。而TCP是**面向连接的**，即发送信息是在已知对方一定能收到信息的情况下发送的。

&nbsp;&nbsp;&nbsp;&nbsp;并且文件是需要确保每个字节都需要发送到，因此如果选用UDP作为传输协议，那么很可能出现丢包的情况，导致传输过来的文件出现缺失。但是TCP就不会出现这样的情况，它的三次握手会确保客户端与服务器连接，并且确保每个字节都能传到。

**下面来整理一下TCP与UDP的区别**：

-   面向连接（确认有创建三方交握，连接已创建才作传输。）
-   有序数据传输
-   重发丢失的数据包
-   舍弃重复的数据包
-   无差错的数据传输
-   阻塞/流量控制

### 1.2 setsockopt

&nbsp;&nbsp;&nbsp;&nbsp;在服务器与客户端断开连接后，通常存在一个时间段，是用来确认被关闭一方能确实收到关闭的信息的，所以这个时候端口是被上一个程序所占用的。因此为了方便，我们需要使用setsockopt来将这个消除。

```python
# 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7890端口
mini_web_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```

### 1.3 TCP的创建流程

- 创建套接字
- 绑定ip
- 改主动为被动
- 设置监听
- 接收/发送数据
- 关闭套接字

&nbsp;&nbsp;&nbsp;&nbsp;那接下来，我们就可以根据这个来做一个自己的mini服务器了。当然在写服务器之前，我们需要了解一下HTTP协议。

## 二、HTTP协议

&nbsp;&nbsp;&nbsp;&nbsp;HTTP协议是网页（客户端）与服务器（服务端）之间的一种连接协议，现在最常用的版本是1.1。具体的在上篇文章有讲，这里就只说一下我们需要用到的两部分，即报文头部和报文主体。报文头部是用来告诉对方自己本次连接自己的一些信息，而报文主体是用来存放传输的数据。

### 2.1 请求GET格式

```python
    GET /path HTTP/1.1
    Header1: Value1
    Header2: Value2
    Header3: Value3
```

&nbsp;&nbsp;&nbsp;&nbsp;每个Header一行一个，换行符是\r\n。

### 2.2 请求POST格式

```python
    POST /path HTTP/1.1
    Header1: Value1
    Header2: Value2
    Header3: Value3

    body data goes here...
```

&nbsp;&nbsp;&nbsp;&nbsp;当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body。

### 2.3 响应格式

```python
    200 OK
    Header1: Value1
    Header2: Value2
    Header3: Value3

    body data goes here...
```

&nbsp;&nbsp;&nbsp;&nbsp;HTTP响应如果包含body，也是通过\r\n\r\n来分隔的。

&nbsp;&nbsp;&nbsp;&nbsp;请再次注意，Body的数据类型由Content-Type头来确定，如果是网页，Body就是文本，如果是图片，Body就是图片的二进制数据。

&nbsp;&nbsp;&nbsp;&nbsp;当存在Content-Encoding时，Body数据是被压缩的，最常见的压缩方式是gzip，所以，看到Content-Encoding: gzip时，需要将Body数据先解压缩，才能得到真正的数据。压缩的目的在于减少Body的大小，加快网络传输。

## 三、实现返回固定内容的服务器

&nbsp;&nbsp;&nbsp;&nbsp;首先，我们可以确定需要使用TCP作为文件传输协议，当我们在浏览器上输入127.0.0.1在加上我们绑定的端口，此时就实现了客户端向服务器发送请求报文，当我们的程序收到报文之后，就获得了一个新的socket对象，我们在根据这个对象返回我们想让浏览器显示的内容即可。

### 3.1代码实现

```python
# -*- coding: utf-8 -*-
import socket


def recv(web_client):
    recv_data = web_client.recv(1024).decode("utf-8")
    request_header_lines = recv_data.splitlines()
    for line in request_header_lines:
        print(line)
    # 组织相应 头信息(header)
    response_headers = "HTTP/1.1 200 OK\r\n"  # 200表示找到这个资源
    response_headers += "\r\n"  # 用一个空的行与body进行隔开
    # 组织 内容(body)
    response_body = "Worker:summer"

    response = response_headers + response_body
    web_client.send(response.encode("utf-8"))
    web_client.close()


def main():
    # 创建套接字
    mini_web_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7890端口
    mini_web_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定端口
    mini_web_server.bind(("", 7890))
    # 主动改被动
    mini_web_server.listen(128)
    while True:
        # 接受相应
        web_client, clint_addr = mini_web_server.accept()
        # 返回参数
        recv(web_client)


if __name__ == '__main__':
    main()

```

### 3.2实现页面

![image-20201227210628459](imgs\image-20201227210628459.png)

### 3.3收到的请求报文

```python
GET / HTTP/1.1
Host: 127.0.0.1:7890
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36
```

## 四、实现返回用户需要的页面

&nbsp;&nbsp;&nbsp;&nbsp;这里主要与上面不同的地方出现在recv的时候，我们知道我们想要的内容是在请求报文的第一段即GET 方法的后面，那我们可以用正则来匹配用户输入的内容即可，然后根据这个内容我们在打开相应的文件然后返回内容即可。如果这个文件存在直接返回即可但是文件不存在，我们可以发送404的响应报文，然后打开404的文件将内容返回即可。

### 4.1 代码实现

```python
# -*- coding: utf-8 -*-
import re
import socket

# 这里配置服务器
DOCUMENTS_ROOT = "./html"


def recv(clint_socket):
    # 获取客户端发送的信息
    global f, response_headers
    recv_data = clint_socket.recv(1024).decode('utf-8')
    # print(recv_data)    # 获取该信息的第一行GET / HTTP/1.1
    request_header_line_0 = recv_data.splitlines()[0]

    # 从客户端发送的信息中获取客户端想要的资源
    get_file_name = re.match(r"[^/]+(/[^ ]*)", request_header_line_0).group(1)
    # print("clint want file_name is %s" % get_file_name)

    if get_file_name == "/":
        file_name = DOCUMENTS_ROOT + "/index.html"
    else:
        file_name = DOCUMENTS_ROOT + get_file_name

    try:
        # 如果存在资源，将资源发送给对方
        f = open(file_name, "rb")
    except IOError:
        # 如果不存在资源，则发送404响应
        response_headers = "HTTP/1.1 404 NOT FOUND\r\n"
        page_404 = DOCUMENTS_ROOT + "/404.html"
        f = open(page_404, "rb")
    else:
        response_headers = "HTTP/1.1 200 OK\r\n"

    finally:
        response_headers += "\r\n"
        resopnse_body = f.read()
        f.close()
        clint_socket.send(response_headers.encode('utf-8'))
        # 再发送body
        clint_socket.send(resopnse_body)
        # 关闭套接字
        clint_socket.close()


def main():
    # 创建套接字
    http_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7890端口
    http_socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定端口
    http_socket_server.bind(("", 7890))
    # 改主动为被动
    http_socket_server.listen(128)
    # 接受客户端响应
    while True:
        clint_socket, clint_addr = http_socket_server.accept()
        # 数据处理
        recv(clint_socket)
    # 关闭套接字
    # http_socket_server.close()


if __name__ == '__main__':
    main()

```

### 4.2 页面实现

![image-20201227211231313](imgs\image-20201227211231313.png)

### 4.3 收到的请求报文

&nbsp;&nbsp;&nbsp;&nbsp;这里将`/`指向了index的页面。

```python
GET / HTTP/1.1
Host: 127.0.0.1:7890
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36
```

## 五、实现多进程版服务器

&nbsp;&nbsp;&nbsp;&nbsp;上面的服务器都是利用单进程显示的，即一次只能服务一个客户，如果有多个客户同时访问，那就只能让先来的客户先服务，后来的先等前面的客户完成了在服务。如果需要实现多进程，我们只需要在数据处理的地方进行多线程即可。

### 5.1 代码实现

```python
# -*- coding: utf-8 -*-
import re
import socket
import multiprocessing

# 这里配置服务器
DOCUMENTS_ROOT = "./html"


def recv(clint_socket):
    # 获取客户端发送的信息
    global f, response_headers
    recv_data = clint_socket.recv(1024).decode('utf-8')
    print(recv_data)    # 获取该信息的第一行GET / HTTP/1.1
    request_header_line_0 = recv_data.splitlines()[0]

    # 从客户端发送的信息中获取客户端想要的资源
    get_file_name = re.match(r"[^/]+(/[^ ]*)", request_header_line_0).group(1)
    # print("clint want file_name is %s" % get_file_name)

    if get_file_name == "/":
        file_name = DOCUMENTS_ROOT + "/index.html"
    else:
        file_name = DOCUMENTS_ROOT + get_file_name

    try:
        # 如果存在资源，将资源发送给对方
        f = open(file_name, "rb")
    except IOError:
        # 如果不存在资源，则发送404响应
        response_headers = "HTTP/1.1 404 NOT FOUND\r\n"
        page_404 = DOCUMENTS_ROOT + "/404.html"
        f = open(page_404, "rb")
    else:
        response_headers = "HTTP/1.1 200 OK\r\n"

    finally:
        response_headers += "\r\n"
        resopnse_body = f.read()
        f.close()
        clint_socket.send(response_headers.encode('utf-8'))
        # 再发送body
        clint_socket.send(resopnse_body)
        # 关闭套接字
        clint_socket.close()


def main():
    # 创建套接字
    http_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7890端口
    http_socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定端口
    http_socket_server.bind(("", 7890))
    # 改主动为被动
    http_socket_server.listen(128)
    # 接受客户端响应
    while True:
        clint_socket, clint_addr = http_socket_server.accept()
        p = multiprocessing.Process(target=recv, args=(clint_socket,))
        # 数据处理
        # recv(clint_socket)
        p.start()
        clint_socket.close()
    # 关闭套接字
    # http_socket_server.close()


if __name__ == '__main__':
    main()

```

之后的页面和请求报文都一样，接下来就不重复输出了。

## 六、实现多线程版服务器

&nbsp;&nbsp;&nbsp;&nbsp;多线程与多进程一样，只是调用不同的东西。

### 6.1 代码实现

```python
# -*- coding: utf-8 -*-
import re
import socket
import threading

# 这里配置服务器
DOCUMENTS_ROOT = "./html"


def recv(clint_socket):
    # 获取客户端发送的信息
    global f, response_headers
    recv_data = clint_socket.recv(1024).decode('utf-8')
    # print(recv_data)    # 获取该信息的第一行GET / HTTP/1.1
    request_header_line_0 = recv_data.splitlines()[0]
    # 从客户端发送的信息中获取客户端想要的资源
    get_file_name = re.match(r"[^/]+(/[^ ]*)", request_header_line_0).group(1)
    # print("clint want file_name is %s" % get_file_name)

    if get_file_name == "/":
        file_name = DOCUMENTS_ROOT + "/index.html"
    else:
        file_name = DOCUMENTS_ROOT + get_file_name

    try:
        # 如果存在资源，将资源发送给对方
        f = open(file_name, "rb")
    except IOError:
        # 如果不存在资源，则发送404响应
        response_headers = "HTTP/1.1 404 NOT FOUND\r\n"
        page_404 = DOCUMENTS_ROOT + "/404.html"
        f = open(page_404, "rb")
        # print(recv_data)
        # print("="*50)
    else:
        response_headers = "HTTP/1.1 200 OK\r\n"

    finally:
        response_headers += "\r\n"
        resopnse_body = f.read()
        f.close()
        clint_socket.send(response_headers.encode('utf-8'))
        # 再发送body
        clint_socket.send(resopnse_body)
        # 关闭套接字
        clint_socket.close()


def main():
    # 创建套接字
    http_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7890端口
    http_socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定端口
    http_socket_server.bind(("", 7890))
    # 改主动为被动
    http_socket_server.listen(128)
    # 接受客户端响应
    while True:
        clint_socket, clint_addr = http_socket_server.accept()
        # 数据处理
        t = threading.Thread(target=recv, args=(clint_socket,))
        t.start()
        # recv(clint_socket)
    # 关闭套接字
    # http_socket_server.close()


if __name__ == '__main__':
    main()

```

## 七、实现协程版服务器

&nbsp;&nbsp;&nbsp;&nbsp;我们知道，进程是分配资源的基本单位，线程是系统调度的基本单位，但是操作系统在进程之间切换需要消耗大量的资源，线程虽然能少一些同样是也需要一定的资源和时间来供他切换，而协程的切换只是利用上下文的信息，所以所消耗的资源非常小。并且协程利用的是阻塞转移（即遇到阻塞就换另一条协程进行操作）。下面是简单的的代码。

### 7.1 代码实现

```python
# -*- coding: utf-8 -*-
import re
import socket
import gevent
from gevent import monkey


# 这里配置服务器
DOCUMENTS_ROOT = "./html"
monkey.patch_all()


def recv(clint_socket):
    # 获取客户端发送的信息
    global f, response_headers
    recv_data = clint_socket.recv(1024).decode('utf-8')
    # print(recv_data)    # 获取该信息的第一行GET / HTTP/1.1
    request_header_line_0 = recv_data.splitlines()[0]
    # 从客户端发送的信息中获取客户端想要的资源
    get_file_name = re.match(r"[^/]+(/[^ ]*)", request_header_line_0).group(1)
    # print("clint want file_name is %s" % get_file_name)

    if get_file_name == "/":
        file_name = DOCUMENTS_ROOT + "/index.html"
    else:
        file_name = DOCUMENTS_ROOT + get_file_name

    try:
        # 如果存在资源，将资源发送给对方
        f = open(file_name, "rb")
    except IOError:
        # 如果不存在资源，则发送404响应
        response_headers = "HTTP/1.1 404 NOT FOUND\r\n"
        page_404 = DOCUMENTS_ROOT + "/404.html"
        f = open(page_404, "rb")
        # print(recv_data)
        # print("="*50)
    else:
        response_headers = "HTTP/1.1 200 OK\r\n"

    finally:
        response_headers += "\r\n"
        resopnse_body = f.read()
        f.close()
        clint_socket.send(response_headers.encode('utf-8'))
        # 再发送body
        clint_socket.send(resopnse_body)
        # 关闭套接字
        clint_socket.close()


def main():
    # 创建套接字
    http_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7890端口
    http_socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定端口
    http_socket_server.bind(("", 7890))
    # 改主动为被动
    http_socket_server.listen(128)
    # 接受客户端响应
    while True:
        clint_socket, clint_addr = http_socket_server.accept()
        # 数据处理
        gevent.spawn(recv, clint_socket)
        # recv(clint_socket)
    # 关闭套接字
    # http_socket_server.close()


if __name__ == '__main__':
    main()

```

## 八、实现单进程、线程、非阻塞的服务器

&nbsp;&nbsp;&nbsp;&nbsp;上面的三个代码总的来说差异不大，只是在信息处理部分调用不同的函数即可，但是我们想，如果利用单进程、线程可以实现协程的操作么（即解决阻塞的问题）？答案是可以的，我们可以使用setblocking，这个可以解决socket的阻塞问题，但是如果设置了这个，当我们在`http_socket_server.accept()`的时候，、如果accept时，恰巧没有客户端connect，那么accept会产生一个异常，所以需要try来进行处理。同样的，当我们得到一个新的socket时，同样需要把它接堵塞，此时也需要利用try来进行判断。为了方便，我们可以引入一个list，把连接的客户端放到这个list里面。遍历这个列表就可以获得需要接收的socket对象，然后把它进行数据处理即可。

### 8.1 代码实现

```python
# -*- coding: utf-8 -*-
import time
import socket
import sys
import re


class WSGIServer(object):
    """定义一个WSGI服务器的类"""
    def __init__(self, port, documents_root):
        # 1. 创建套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2. 绑定本地信息
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("", port))
        # 3. 变为监听套接字
        self.server_socket.listen(128)

        self.server_socket.setblocking(False)
        self.client_socket_list = list()

        self.documents_root = documents_root

    def run_forever(self):
        """运行服务器"""

        # 等待对方链接
        while True:

            # time.sleep(0.5)  # for test

            try:
                new_socket, new_addr = self.server_socket.accept()
            except Exception as ret:
                pass
                # print("-----1----", ret)  # for test
            else:
                new_socket.setblocking(False)
                self.client_socket_list.append(new_socket)

            for client_socket in self.client_socket_list:
                try:
                    request = client_socket.recv(1024).decode('utf-8')
                except Exception as ret:
                    pass
                    # print("------2----", ret)  # for test
                else:
                    if request:
                        self.recv(client_socket, request)
                    else:
                        client_socket.close()
                        self.client_socket_list.remove(client_socket)

            # print(self.client_socket_list)

    def recv(self, clint_socket, recv_data):
        # 获取客户端发送的信息
        global f, response_headers
        # print(recv_data)    # 获取该信息的第一行GET / HTTP/1.1
        request_header_line_0 = recv_data.splitlines()[0]

        # 从客户端发送的信息中获取客户端想要的资源
        get_file_name = re.match(r"[^/]+(/[^ ]*)", request_header_line_0).group(1)
        # print("clint want file_name is %s" % get_file_name)

        if get_file_name == "/":
            file_name = self.documents_root + "/index.html"
        else:
            file_name = self.documents_root + get_file_name

        try:
            # 如果存在资源，将资源发送给对方
            f = open(file_name, "rb")
        except IOError:
            # 如果不存在资源，则发送404响应
            response_headers = "HTTP/1.1 404 NOT FOUND\r\n"
            page_404 = self.documents_root + "/404.html"
            f = open(page_404, "rb")
        else:
            response_headers = "HTTP/1.1 200 OK\r\n"

        finally:
            response_headers += "\r\n"
            resopnse_body = f.read()
            f.close()
            clint_socket.send(response_headers.encode('utf-8'))
            # 再发送body
            clint_socket.send(resopnse_body)
            # 关闭套接字
            clint_socket.close()


# 设置服务器服务静态资源时的路径
DOCUMENTS_ROOT = "./html"


def main():
    port = 7890
    http_server = WSGIServer(port, DOCUMENTS_ROOT)
    http_server.run_forever()


if __name__ == "__main__":
    main()

```

## 九、实现单进程、线程、非阻塞、长连接版服务器

&nbsp;&nbsp;&nbsp;&nbsp;以上所有的代码仔细看，都是在发送完一次信息之后就将这个socket由服务器主动关闭，此时就相当于HTTP1.0版本的短连接，即发送完一次信息就四次挥手，下次有新的需求之后在三次握手，发送信息，四次挥手。这样是非常浪费服务器资源的，我们如果想要让我们的服务器也实现长连接，我们只需要在响应头部加上一个`Content-Length`即可，这个表示本次数据传输所传输的所有数据总长度。当接收完所有数据之后，就可以利用现在的socket继续发送下一次的报文。不用在重复的三次挥手即可。

### 9.1 代码实现

```python
# -*- coding: utf-8 -*-
import re
import socket

# 这里配置服务器
DOCUMENTS_ROOT = "./html"


def recv(clint_socket, recv_data):
    # 获取客户端发送的信息
    global f, response_headers
    # print(recv_data)    # 获取该信息的第一行GET / HTTP/1.1
    request_header_line_0 = recv_data.splitlines()[0]

    # 从客户端发送的信息中获取客户端想要的资源
    get_file_name = re.match(r"[^/]+(/[^ ]*)", request_header_line_0).group(1)
    # print("clint want file_name is %s" % get_file_name)

    if get_file_name == "/":
        file_name = DOCUMENTS_ROOT + "/index.html"
    else:
        file_name = DOCUMENTS_ROOT + get_file_name

    try:
        # 如果存在资源，将资源发送给对方
        f = open(file_name, "rb")
    except IOError:
        # 如果不存在资源，则发送404响应
        response_headers = "HTTP/1.1 404 NOT FOUND\r\n"
        page_404 = DOCUMENTS_ROOT + "/404.html"
        f = open(page_404, "rb")
    else:
        response_headers = "HTTP/1.1 200 OK\r\n"
    finally:
        resopnse_body = f.read()
        f.close()
        response_headers += "Content-Length: %d\r\n" % (len(resopnse_body))
        response_headers += "\r\n"

        clint_socket.send(response_headers.encode('utf-8'))
        # 再发送body
        clint_socket.send(resopnse_body)


def main():
    # 创建套接字
    http_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7890端口
    http_socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定端口
    http_socket_server.bind(("", 7890))
    # 改主动为被动
    http_socket_server.setblocking(False)
    http_socket_server.listen(128)
    clint_socket_list = list()
    # 接受客户端响应
    while True:
        try:
            new_socket, clint_addr = http_socket_server.accept()
        except Exception as ret:
            pass
        else:
            new_socket.setblocking(False)
            clint_socket_list.append(new_socket)

        for clint_socket in clint_socket_list:
            try:
                # 数据处理
                recv_data = clint_socket.recv(1024).decode('utf-8')
            except Exception as ret:
                pass
            else:
                if recv_data:
                    recv(clint_socket, recv_data)
                else:
                    clint_socket.close()
                    clint_socket_list.remove(clint_socket)
                    # print(clint_socket, "已经关闭")


if __name__ == '__main__':
    main()

```

## 十、使用epoll完成服务器

&nbsp;&nbsp;&nbsp;&nbsp;如果使用非阻塞来实现服务器，我们就需要无数次的遍历list来判断，那我们有没有一种方法，来实现监听一个内存，然后把所有的连接的socket放入这个内存，如果有一个socket需要解堵塞来接受数据，那么就给我们一个事件，然后让我们知道某个socket可以接收了。我们在利用它实现后续就好了。同样的我们可以使用epoll来实现，但是需要在linux上实现，win上一些东西不支持或者说得换一个东西，这里就不在说了。具体的可以看这篇文章：

。

&nbsp;&nbsp;&nbsp;&nbsp;在说之前我们需要再了解一个知识点：**文件描述符(fd)**。在linux中一切东西皆文件，所以当一个进程开始的时候，就会有一些fd被存入内存，而epoll需要这些fd作为传输来进行实现他的基本操作。比如我们在开启了服务器，然后一个新的连接过来，我们就创建了一个socket那么这个socket在内存中就可以根据一个特有的fd来找出这个文件。

### 10.1 代码实现

```python
import socket
import re
import select


class WSGIServer(object):
    """定义一个WSGI服务器的类"""

    def __init__(self, port, documents_root):

        # 1. 创建套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2. 绑定本地信息
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("", port))
        # 3. 变为监听套接字
        self.server_socket.listen(128)

        self.documents_root = documents_root

        # 创建epoll对象
        self.epoll = select.epoll()
        # 将tcp服务器套接字加入到epoll中进行监听
        self.epoll.register(self.server_socket.fileno(), select.EPOLLIN | select.EPOLLET)

        # 创建添加的fd对应的套接字
        self.fd_socket = dict()

    def run_forever(self):
        """运行服务器"""

        # 等待对方链接
        while True:
            # epoll 进行 fd 扫描的地方 -- 未指定超时时间则为阻塞等待
            epoll_list = self.epoll.poll()

            # 对事件进行判断
            for fd, event in epoll_list:
                # 如果是服务器套接字可以收数据，那么意味着可以进行accept
                if fd == self.server_socket.fileno():
                    new_socket, new_addr = self.server_socket.accept()
                    # 向 epoll 中注册 连接 socket 的 可读 事件
                    self.epoll.register(new_socket.fileno(), select.EPOLLIN | select.EPOLLET)
                    # 记录这个信息
                    self.fd_socket[new_socket.fileno()] = new_socket
                # 接收到数据
                elif event == select.EPOLLIN:
                    request = self.fd_socket[fd].recv(1024).decode("utf-8")
                    if request:
                        self.recv(self.fd_socket[fd], request)
                    else:
                        # 在epoll中注销客户端的信息
                        self.epoll.unregister(fd)
                        # 关闭客户端的文件句柄
                        self.fd_socket[fd].close()
                        # 在字典中删除与已关闭客户端相关的信息
                        del self.fd_socket[fd]

    def recv(self, clint_socket, recv_data):
        # 获取客户端发送的信息
        global f, response_headers
        # print(recv_data)    # 获取该信息的第一行GET / HTTP/1.1
        request_header_line_0 = recv_data.splitlines()[0]

        # 从客户端发送的信息中获取客户端想要的资源
        get_file_name = re.match(r"[^/]+(/[^ ]*)", request_header_line_0).group(1)
        # print("clint want file_name is %s" % get_file_name)

        if get_file_name == "/":
            file_name = self.documents_root + "/index.html"
        else:
            file_name = self.documents_root + get_file_name

        try:
            # 如果存在资源，将资源发送给对方
            f = open(file_name, "rb")
        except IOError:
            # 如果不存在资源，则发送404响应
            response_headers = "HTTP/1.1 404 NOT FOUND\r\n"
            page_404 = self.documents_root + "/404.html"
            f = open(page_404, "rb")
        else:
            response_headers = "HTTP/1.1 200 OK\r\n"

        finally:
            resopnse_body = f.read()
            f.close()
            response_headers += "Content-Length: %d\r\n" % (len(resopnse_body))
            response_headers += "\r\n"

            clint_socket.send(response_headers.encode('utf-8'))
            # 再发送body
            clint_socket.send(resopnse_body)


# 设置服务器服务静态资源时的路径
DOCUMENTS_ROOT = "./html"


def main():
    port = 7890

    # print("http服务器使用的port:%s" % port)
    http_server = WSGIServer(port, DOCUMENTS_ROOT)
    http_server.run_forever()


if __name__ == "__main__":
    main()

```

&nbsp;&nbsp;&nbsp;&nbsp;至此，我们自己的一个mini-web服务器也就全部创建完毕了，如果有时间就可以以这个作为模板，在此基础上开枝散叶，写一个适合自己的web服务器也就从此开始了。

