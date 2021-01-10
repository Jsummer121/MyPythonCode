# Mini_Web服务器（3）添加路由功能

## 一、回顾

&nbsp;&nbsp;&nbsp;&nbsp;第一次我们使用socket套接字创建了同时处理各种业务的服务器，然后在第二次我们将动态资源分离出来单独写了一个框架，但是框架很是简陋也没有将数据库的知识放入，接下来我们就来实现这个功能。

## 二、路由

&nbsp;&nbsp;&nbsp;&nbsp;路由即url（统一资源定位符），是浏览器访问服务器时的钥匙，通过这个浏览器告诉服务器我想要什么，而服务器可以准确的给与浏览器这个东西。那么我们的路由应该放在我们的服务器内部还是客户端呢？

&nbsp;&nbsp;&nbsp;&nbsp;回看一下，我们的服务器将只要是.html后缀的文件都交给了客户端来处理，而我们主要请求的东西就是这个，因此打死我也得把路由放在客户端来写。

这是现在的客户端代码：

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

&nbsp;&nbsp;&nbsp;&nbsp;可以发现，我们将所有的url处理都放在了application中的if-else语句，试想一下当我们的页面多到上千个的时候，岂不是要写上千条if-else语句？

&nbsp;&nbsp;&nbsp;&nbsp;那我们是否可以把这个url给取出来，然后放到一个空间去存放，如果存在这个那就直接取出来就好了？答案是可以，并且我们这里使用一个字典来存储【应为字典的存放是按照hash来存的，查找的时间复杂度为O（1）。并且以url为key，函数引用为value即可实现现在的if-else功能】

## 三、实现路由功能

话不多说，先来实现一个简单的路由版功能

-   现在开头创建一个dict
-   将我们知道的键值对放入即可，然后在application函数中做相应的引用即可

```python
import re

g_url_route = dict()

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

g_url_route = {
    "/index.html": index,
    "/center.html": center
}  # 放这里的原因是应为后面的函数引用必须要先建立然后存，不然找不到该函数地址。

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    
    file_name = env['PATH_INFO']
    # file_name = "/index.py"

    try:
		return g_url_route[file_name]()
	except Exception as ret:
		return "%s" % ret

```

## 四、利用装饰器实现自动添加路由与函数引用

&nbsp;&nbsp;&nbsp;&nbsp;如果每次都是自己手动添加路由会导致工作量繁多，并且也适得其反，那么我们就可以利用装饰器的特性，自动将该函数的引用与url对应起来即可

-   创建装饰器

```python
def route(url):
	def set_func(func):
		g_url_route[url] = func
		
		def call_func(*args, **kwargs):
			return func(*args, **kwargs)
		
		return call_func
	
	return set_func
```

上面的装饰器是一个带参数的装饰器，该装饰器首先执行最外层的函数，然后将最外层函数的返回值作为一个装饰器进行装饰。具体做法如下：

```python
import re

g_url_route = dict()


def route(url):
	def set_func(func):
		g_url_route[url] = func
		
		def call_func(*args, **kwargs):
			return func(*args, **kwargs)
		
		return call_func
	
	return set_func


@route("/index.html")
def index():
	with open("./templates/index.html") as f:
		content = f.read()
	
	my_stock_info = "哈哈哈哈 这是你的本月名称....."
	
	content = re.sub(r"\{%content%\}", my_stock_info, content)
	
	return content


@route("/center.html")
def center():
	with open("./templates/center.html") as f:
		content = f.read()
	
	my_stock_info = "这里是从mysql查询出来的数据。。。"
	
	content = re.sub(r"\{%content%\}", my_stock_info, content)
	
	return content


def application(env, start_response):
	start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
	
	file_name = env['PATH_INFO']
	# file_name = "/index.html"
	
	try:
		return g_url_route[file_name]()
	except Exception as ret:
		return "%s" % ret

```

并且该路由已经自动遵循了伪静态了。具体的在上一篇讲过，简单来说就是为了方便记忆然后使得url更加适配SEO。

## 五、实现能正则匹配的路由

在后续的开发中，一定会出现如下的情况:`http://127.0.0.1:7890/add/0000001.html`那么如果不使用正则将会出现有多少个东西就需要重复写多少个函数，实现非常庞大的代码冗余。其实正则匹配也很简单，只需要在装饰器传入的函数中做一下手脚然后在application函数中作一些调整即可。

```python
import re

g_url_route = dict()


def route(url):
	def set_func(func):
		g_url_route[url] = func
		
		def call_func(*args, **kwargs):
			return func(*args, **kwargs)
		
		return call_func
	
	return set_func


@route("/index.html")
def index():
	with open("./templates/index.html") as f:
		content = f.read()
	
	my_stock_info = "哈哈哈哈 这是你的本月名称....."
	
	content = re.sub(r"\{%content%\}", my_stock_info, content)
	
	return content


@route("/center.html")
def center():
	with open("./templates/center.html") as f:
		content = f.read()
	
	my_stock_info = "这里是从mysql查询出来的数据。。。"
	
	content = re.sub(r"\{%content%\}", my_stock_info, content)
	
	return content


@route(r"/update/(\d*)\.html")
def update(file_name, url):
    """显示 更新页面的内容"""
    pass


def application(env, start_response):
	start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
	
	file_name = env['PATH_INFO']
	# file_name = "/index.html"
	
	try:
        # func = URL_FUNC_DICT[file_name]
        # return func()
        # return URL_FUNC_DICT[file_name]()
        for url, func in URL_FUNC_DICT.items():
            # {
            #   r"/index.html":index,
            #   r"/center.html":center,
            #   r"/add/\d+\.html":add_focus
            # }
            ret = re.match(url, file_name)
            if ret:
                return func()
        else:
            return "请求的url(%s)没有对应的函数...." % file_name


    except Exception as ret:
        return "产生了异常：%s" % str(ret)

```



