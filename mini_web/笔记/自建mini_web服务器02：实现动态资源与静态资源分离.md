# Mini_Web服务器（2）实现动态资源请求

## 一、回顾

​		在上一篇文章中我们从一开始的使用socket建立tcp连接，然后到利用浏览器访问我们自己写的单进程单线程的服务器再到服务器升级成多线程、多进程乃至协程到最后的epoll。接下来这篇我们在多进程服务器的基础上实现更多的新功能。

## 二、面向函数改为面向对象

上次的代码使用的是面向函数编程，下面的代码是在之前的基础上将其变为面向对象：

```python
# -*- coding: utf-8 -*-
# @Author  : summer
import re
import socket
import multiprocessing

# 这里配置服务器
DOCUMENTS_ROOT = "./html"


class WSGIServer:
	def __init__(self):
		# 创建套接字
		self.http_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7890端口
		self.http_socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		# 绑定端口
		self.http_socket_server.bind(("", 7890))
		# 改主动为被动
		self.http_socket_server.listen(128)
	
	def run_forever(self):
		# 接受客户端响应
		while True:
			clint_socket, clint_addr = self.http_socket_server.accept()
			p = multiprocessing.Process(target=self.recv, args=(clint_socket,))
			p.start()
			clint_socket.close()
	
	def recv(clint_socket):
		# 获取客户端发送的信息
		global f, response_headers
		recv_data = clint_socket.recv(1024).decode('utf-8')
		print(recv_data)  # 获取该信息的第一行GET / HTTP/1.1
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
	web_server = WSGIServer()
	web_server.run_forever()


if __name__ == '__main__':
	main()

```

## 三、WSGI协议

之前也谈到过，WSGI是服务器与应用框架之间沟通的协议，因此为了使得我们的服务器能实现动态资源请求，我们也利用WSGI协议来构建自己的mini应用框架。

下图是整个请求过程，具体细节已在上篇文章讲过这里就不说了。

![img](imgs/Snip20161117_8-1610171933225.png)

### 3.1简易的web_frame框架

```python
import time

def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    return str(environ) + '==Hello world from a simple WSGI application!--->%s\n' % time.ctime()

```

## 四、实现基本的web动态服务器

### 4.0服务器的基本架构图：

![web服务器示意图.002](imgs/web服务器示意图.002.jpeg)

### 4.1 文件格式

```python
├── web_server.py
├── web
│   └── my_web.py
└── html
    └── index.html
```

### 4.2 web/mini_frame.py

```python
import time

def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    return str(environ) + '==Hello world from a simple WSGI application!--->%s\n' % time.ctime()
```

这里的写法并没有什么特别的，只是遵循了WSGI协议，首先有一个application函数，然后一个字典参数和一个函数引用传入。最后返回值即可。

### 4.3 web_server.py

​		我们既然已经确立了，只要访问html文件的，就将他交给框架处理，而访问静态资源（jpg，phg等）就由服务器自行处理，那只需要在原来框架的打开文件寻找该页面之前加个判断，查看结尾是否以html结尾即可。

```python
        # 2. 返回http格式的数据，给浏览器
        # 2.1 如果请求的资源不是以.py结尾，那么就认为是静态资源（css/js/png，jpg等）
        if not file_name.endswith(".html"):
            try:
                f = open(self.static_path + file_name, "rb")
				....
        else:
            # 2.2 如果是以.html结尾，那么就认为是动态资源的请求
            ...
```

​		同时，因为我们使用WSGI协议，自己的服务器内部就需要创建一个函数引用传入，我们可以把整个函数设置为生成响应头部的函数即可。这里的`status, headers`皆由应用框架传入。status用来存放响应码，而headers用来存放相应的参数

```python
    def set_response_header(self, status, headers):
        self.status = status
        self.headers = [("server", "mini_web v8.8")]
        self.headers += headers
```

​		当函数完成之后，我们就可以在else的内部进行相应的处理即可

```python
        else:
            # 2.2 如果是以.html结尾，那么就认为是动态资源的请求

            env = dict()  # 这个字典中存放的是web服务器要传递给 web框架的数据信息
            env['PATH_INFO'] = file_name
            # {"PATH_INFO": "/index.html"}
            # body = dynamic.mini_frame.application(env, self.set_response_header)
            body = self.application(env, self.set_response_header)

            header = "HTTP/1.1 %s\r\n" % self.status

            for temp in self.headers:
                header += "%s:%s\r\n" % (temp[0], temp[1])

            header += "\r\n"

            response = header+body
            # 发送response给浏览器
            new_socket.send(response.encode("utf-8"))
```

​		整个这样看已经差不多了，但再回想一下啊，上篇文章中还说过一个长连接的方式，现在的整个框架使用的还是短连接即发送一次就断开一次，严重影响效率，我们还是可以在获取body之后，在头部加入`Content-Length`即可。以下就是基础版的完整代码：

```python
import select
import time
import socket
import sys
import re
import multiprocessing


class WSGIServer(object):
    """定义一个WSGI服务器的类"""

    def __init__(self, port, app, documents_root):

        # 1. 创建套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2. 绑定本地信息
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("", port))
        # 3. 变为监听套接字
        self.server_socket.listen(128)

        # 设定资源文件的路径
        self.documents_root = documents_root

        # 设定web框架可以调用的函数(对象)
        self.app = app

    def run_forever(self):
        """运行服务器"""

        # 等待对方链接
        while True:
            new_socket, new_addr = self.server_socket.accept()
            # 创建一个新的进程来完成这个客户端的请求任务
            new_socket.settimeout(3)  # 3s
            new_process = multiprocessing.Process(target=self.deal_with_request, args=(new_socket,))
            new_process.start()
            new_socket.close()

    def deal_with_request(self, client_socket):
        """以长链接的方式，为这个浏览器服务器"""

        while True:
            try:
                request = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                print("========>", ret)
                client_socket.close()
                return

            # 判断浏览器是否关闭
            if not request:
                client_socket.close()
                return

            request_lines = request.splitlines()
            for i, line in enumerate(request_lines):
                print(i, line)

            # 提取请求的文件(index.html)
            # GET /a/b/c/d/e/index.html HTTP/1.1
            ret = re.match(r"([^/]*)([^ ]+)", request_lines[0])
            if ret:
                print("正则提取数据:", ret.group(1))
                print("正则提取数据:", ret.group(2))
                file_name = ret.group(2)
                if file_name == "/":
                    file_name = "/index.html"

            # 如果不是以py结尾的文件，认为是普通的文件
            if not file_name.endswith(".html"):

                # 读取文件数据
                try:
                    f = open(self.documents_root+file_name, "rb")
                except:
                    response_body = "file not found, 请输入正确的url"

                    response_header = "HTTP/1.1 404 not found\r\n"
                    response_header += "Content-Type: text/html; charset=utf-8\r\n"
                    response_header += "Content-Length: %d\r\n" % (len(response_body))
                    response_header += "\r\n"

                    response = response_header + response_body

                    # 将header返回给浏览器
                    client_socket.send(response.encode('utf-8'))

                else:
                    content = f.read()
                    f.close()

                    response_body = content

                    response_header = "HTTP/1.1 200 OK\r\n"
                    response_header += "Content-Length: %d\r\n" % (len(response_body.encode("utf-8")))
                    response_header += "\r\n"

                    # 将header返回给浏览器
                    client_socket.send(response_header.encode('utf-8') + response_body)

            # 以.html结尾的文件，就认为是浏览需要动态的页面
            else:
                # 准备一个字典，里面存放需要传递给web框架的数据
                env = {}
                # 存web返回的数据
                response_body = self.app(env, self.set_response_headers)

                # 合并header和body
                response_header = "HTTP/1.1 {status}\r\n".format(status=self.headers[0])
                response_header += "Content-Type: text/html; charset=utf-8\r\n"
                response_header += "Content-Length: %d\r\n" % len(response_body)
                for temp_head in self.headers[1]:
                    response_header += "{0}:{1}\r\n".format(*temp_head)

                response = response_header + "\r\n"
                response += response_body

                client_socket.send(response.encode('utf-8'))

    def set_response_headers(self, status, headers):
        """这个方法，会在 web框架中被默认调用"""
        response_header_default = [
            ("Data", time.ctime()),
            ("Server", "ItCast-python mini web server")
        ]

        # 将状态码/相应头信息存储起来
        # [字符串, [xxxxx, xxx2]]
        self.headers = [status, response_header_default + headers]


# 设置静态资源访问的路径
g_static_document_root = "./html"
# 设置动态资源访问的路径
g_dynamic_document_root = "./web"

def main():
    """控制web服务器整体"""
    # python3 xxxx.py 7890
    if len(sys.argv) == 3:
        # 获取web服务器的port
        port = sys.argv[1]
        if port.isdigit():
            port = int(port)
        # 获取web服务器需要动态资源时，访问的web框架名字
        web_frame_module_app_name = sys.argv[2]
    else:
        print("运行方式如: python3 xxx.py 7890 my_web_frame_name:application")
        return

    print("http服务器使用的port:%s" % port)

    # 将动态路径即存放py文件的路径，添加到path中，这样python就能够找到这个路径了
    sys.path.append(g_dynamic_document_root)

    ret = re.match(r"([^:]*):(.*)", web_frame_module_app_name)
    if ret:
        # 获取模块名
        web_frame_module_name = ret.group(1)
        # 获取可以调用web框架的应用名称
        app_name = ret.group(2)

    # 导入web框架的主模块
    web_frame_module = __import__(web_frame_module_name)
    # 获取那个可以直接调用的函数(对象)
    app = getattr(web_frame_module, app_name) 

    # print(app)  # for test

    # 启动http服务器
    http_server = WSGIServer(port, g_static_document_root, app)
    # 运行http服务器
    http_server.run_forever()


if __name__ == "__main__":
    main()
```

上面在main函数中的代码前几行是控制在linux终端中运行命令的正确性和动态的获取客户的访问路径与函数（对象）应为每个人的代码并不可能写的完全一样，函数名有许多差异，因此在这里需要用户先输入端口号、应用框架文件名与应用框架函数名。`python3 web_server.py 7890 mini_frame:application`

## 五、修改服务器的文件结构

### 5.1 文件结构

为了使得服务器向Django等框架靠拢，我们也可以使用相应的文件结构：

```python
├── dynamic ---存放py模块
│   └── mini_frame.py
├── templates ---存放模板文件
│   ├── center.html
│   ├── index.html
│   ├── location.html
│   └── update.html
├── static ---存放静态的资源文件
│   ├── css
│   │   ├── bootstrap.min.css
│   │   ├── main.css
│   │   └── swiper.min.css
│   └── js
│       ├── a.js
│       ├── bootstrap.min.js
│       ├── jquery-1.12.4.js
│       ├── jquery-1.12.4.min.js
│       ├── jquery.animate-colors.js
│       ├── jquery.animate-colors-min.js
│       ├── jquery.cookie.js
│       ├── jquery-ui.min.js
│       ├── server.js
│       ├── swiper.jquery.min.js
│       ├── swiper.min.js
│       └── zepto.min.js
└── web_server.py ---mini web服务器
```

### 5.2 dynamic/mini_frame.py

```python
import time

def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    return str(environ) + '==Hello world from a simple WSGI application!--->%s\n' % time.ctime()
```

### 5.3 web_server.py

​		整个服务器的代码就只需要将原先`g_static_document_root = "./html" `和`g_dynamic_document_root = "./web"`改为`"./static"`和`"./dynamic"`即可。

## 六、显示页面

### 6.1 dayamic/mini_frame.py

现在，页面显示的功能已经全部放在了dynamic的mini_frame.py上，因此我们只需要在上面修改即可。

```python
import re


def index():
	with open("./templates/index.html") as f:
		content = f.read()
	
	my_stock_info = "哈哈哈哈 这是你的本月名称....."
	
	content = re.sub(r"\{%content%\}", my_stock_info, content)
	
	return content


def center():
	with open("./templates/center.html") as f:
		content = f.read()
	
	my_stock_info = "这里是从mysql查询出来的数据。。。"
	
	content = re.sub(r"\{%content%\}", my_stock_info, content)
	
	return content


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    
    file_name = env['PATH_INFO']
    # file_name = "/index.py"

    if file_name == "/index.py":
        return index()
    elif file_name == "/center.py":
        return center()
    else:
        return 'Hello World! 我爱你中国....'
```

具体的做法与其他的方法并无二样，都是打开相应的文件然后读取内容，进行内容传递即可。

## 七、添加shell

shell可以帮助我们运行python程序，只需要在终端中写入相应的python语句即可

### run.sh

```python
python3 web_server.py 7890 mini_frame:application
```

### 注意：

在写完以后，你的这个文件是没有x执行权限的，需要添加权限：`chomd +x run.sh`

完成以后就可以在终端运行`./run.sh`即可

## 八、添加README.MD

READMD这个可加可不加，为的是防止自己以后会忘了如何运行时加上的一个说明。

```python
# Mini-Web-Server
这是一个利用python写的mini-web服务器

auther:summer
python版本：3.8
IDE：pycharm
系统：调试win10、运行ubuntu20
运行方式：./run.sh 或 python3 xxxx.py 【端口号】 【框架模板】:运行函数 -- python3 web_server.py 7890 mini_frame:application
```

## 九、添加配置文件

回看一下web_server.py代码，发现配置文件的信息是放在py文件内部的，这样还是不能有效的解耦，因此我们可以创建一个配置文件来存放相应的配置文件信息例如:my.conf等

### web_server.conf

注意，下面的文件里面的东西是字符串而不是字典

```conf
{
    "static_path":"./static",
    "dynamic_path":"./dynamic"
}

```

### web_server.py

```python
import socket
import re
import multiprocessing
import sys


class WSGIServer(object):
	def __init__(self, port, app, static_path):
		# 1. 创建套接字
		self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		
		# 2. 绑定
		self.tcp_server_socket.bind(("", port))
		
		# 3. 变为监听套接字
		self.tcp_server_socket.listen(128)
		
		self.application = app
		self.static_path = static_path
	
	def service_client(self, new_socket):
		"""为这个客户端返回数据-长连接"""
		
		# 1. 接收浏览器发送过来的请求 ，即http请求
		# GET / HTTP/1.1
		# .....
		request = new_socket.recv(1024).decode("utf-8")
		# print(">>>"*50)
		# print(request)
		
		request_lines = request.splitlines()
		print("")
		print(">" * 20)
		print(request_lines)
		
		# GET /index.html HTTP/1.1
		# get post put del
		file_name = ""
		ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
		if ret:
			file_name = ret.group(1)
			# print("*"*50, file_name)
			if file_name == "/":
				file_name = "/index.html"
		
		# 2. 返回http格式的数据，给浏览器
		# 2.1 如果请求的资源不是以.py结尾，那么就认为是静态资源（html/css/js/png，jpg等）
		if not file_name.endswith(".html"):
			try:
				f = open(self.static_path + file_name, "rb")
			except:
				response_body = "file not found, 请输入正确的url"
				
				response_header = "HTTP/1.1 404 not found\r\n"
				response_header += "Content-Type: text/html; charset=utf-8\r\n"
				response_header += "Content-Length: %d\r\n" % (len(response_body))
				response_header += "\r\n"
				
				response = response_header + response_body
				
				# 将header返回给浏览器
				new_socket.send(response.encode('utf-8'))
			else:
				response_body = f.read()
				f.close()
				
				response_header = "HTTP/1.1 200 OK\r\n"
				response_header += "Content-Length: %d\r\n" % (len(response_body))
				response_header += "\r\n"
				# 将header返回给浏览器
				new_socket.send(response_header.encode('utf-8') + response_body)
		else:
			# 2.2 如果是以.html结尾，那么就认为是动态资源的请求
			
			env = dict()  # 这个字典中存放的是web服务器要传递给 web框架的数据信息
			env['PATH_INFO'] = file_name
			# {"PATH_INFO": "/index.py"}
			# body = dynamic.mini_frame.application(env, self.set_response_header)
			body = self.application(env, self.set_response_header)
			
			header = "HTTP/1.1 %s\r\n" % self.status
			
			for temp in self.headers:
				header += "%s:%s\r\n" % (temp[0], temp[1])
			header += "Content-Length: %d\r\n" % (len(body.encode("utf-8")))
			
			header += "\r\n"
			
			response = header + body
			# 发送response给浏览器
			new_socket.send(response.encode("utf-8"))
		
		# 关闭套接
		new_socket.close()
	
	def set_response_header(self, status, headers):
		self.status = status
		self.headers = [("server", "mini_web v8.8")]
		self.headers += headers
	
	def run_forever(self):
		"""用来完成整体的控制"""
		
		while True:
			# 4. 等待新客户端的链接
			new_socket, client_addr = self.tcp_server_socket.accept()
			
			# 5. 为这个客户端服务
			p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
			p.start()
			
			new_socket.close()
		
		# 关闭监听套接字
		self.tcp_server_socket.close()


def main():
	"""控制整体，创建一个web 服务器对象，然后调用这个对象的run_forever方法运行"""
	if len(sys.argv) == 3:
		try:
			port = int(sys.argv[1])  # 7890
			frame_app_name = sys.argv[2]  # mini_frame:application
		except Exception as ret:
			print("端口输入错误。。。。。")
			return
	else:
		print("请按照以下方式运行:")
		print("python3 xxxx.py 7890 mini_frame:application")
		return
	
	# mini_frame:application
	ret = re.match(r"([^:]+):(.*)", frame_app_name)
	if ret:
		frame_name = ret.group(1)  # mini_frame
		app_name = ret.group(2)  # application
	else:
		print("请按照以下方式运行:")
		print("python3 xxxx.py 7890 mini_frame:application")
		return
	
	with open("./web_server.conf") as f:
		conf_info = eval(f.read())
	
	# 此时 conf_info是一个字典里面的数据为：
	# {
	#     "static_path":"./static",
	#     "dynamic_path":"./dynamic"
	# }
	
	sys.path.append(conf_info['dynamic_path'])
	
	# import frame_name --->找frame_name.py
	frame = __import__(frame_name)  # 返回值标记这 导入的这个模板
	app = getattr(frame, app_name)  # 此时app就指向了 dynamic/mini_frame模块中的application这个函数
	
	# print(app)
	
	wsgi_server = WSGIServer(port, app, conf_info['static_path'])
	wsgi_server.run_forever()


if __name__ == "__main__":
	main()

```

至此，我们现在的服务器已经可以实现访问动态资源并且在一定程度上解耦了。