# Django

## 一、简介

Django是一个web应用框架

2.web应用框架：

互联网：传送 数据 信息

电网： 传送 电

3.web应用：

发电厂 ——》 服务器程序（nginx，apache）

web应用的本质—程序—服务器程序+应用程序

4.应用程序—电器 

5.WSGI—电源模块

6.web框架

web应用—造电器

web框架—基本原理

7.电器有不同的品牌，web框架也是如此

- Django，全能型web框架
- web.py 小巧的web框架
- flask.py 一个轻量级优秀的web框架
- tornado 一个异步web框架

**源文档**

url：https://docs.djangoproject.com/en/2.1/topics/http/urls/

内置模板标签和过滤器：https://docs.djangoproject.com/en/2.1/ref/templates/builtins/

自定义模板标签和过滤器：https://docs.djangoproject.com/en/2.1/howto/custom-template-tags/

## 二、设计模式

### MTV

-m：models 模型：负责业务数据对象和数据库对象

-t ： template模板：负责吧页面展示给用户（HTML）

-v ：view 视图：模型和模板的桥梁

### MVC

-m ：models 模型：负责业务数据对象和数据库对象

-v   :   view 视图：与用户交互的页面

-c  ： controller 控制器：接受用户的输入，去调用模型和视图完成用户的请求，模型和视图的桥梁

## 三、Django框架的介绍

目前主流的pythonweb框架

## 四、环境搭建

1.查看当前有哪些虚拟环境：workon 

2.创建新的虚拟环境：

mkvirtualenv /p /usr/bin/python3 diangoApp

3.退出虚拟环境：deactivate

4.删除虚拟环境：rmvituralenv djangoApp

## 五、项目创建

(因为刚刚开始，pycharm的设置不一样，导致Terminal里的文字不尽人意，可以在setting里面的SSH Terminal里面进行配置编码语言)

1.mkvituralenv -p /usr/bin/python diangoApp

2.pip install django==2.1.7

3.创建项目空间

​	cd 项目文件存放的文件夹名。

4.选择和并集齐版本无关的通用方式来创建项目--》命令：django-admin startproject CRM(项目名)

5.运行：
python manage.py runserver 0:8000

需要看到manage.py才可以运行

**ctrl+c 关闭服务**

## 六、配置pycharm的远程同步

1.pycharm在本地创建一个空的而新项目

2.配置远程解释器（注意：与项目解释器一致）

3.修改文件映射路径（本地项目文件夹对应虚拟机下的项目文件夹）

4.设置自动同步

## 七、pycharm运行

工具里面的 start ssh就可以开始运行虚拟机

workon djangoApp

## 八、端口映射

端口

22：shh远程登录协议规定的默认监听端口

8000：Django运行命令默认监听端口

3306：mysql

6379：redis

## 九、pycharm启动项目

设置setting里的：ALLOWD_HOST = ['*']

注意：路径映射html：///必须是三个/。

## 十、应用创建

打开ssh 

然后输入workon djangoApp

cd djangoProject/CRM

python manage.py startapp teacher(应用名)

## 十一、url配置

https://www,sougo.com/web?query=

协议  域名（ip地址和端口）路径 参数

### 自制项目

1.为了后期的导入包适用，将标记目录为来源根。

**2.环境不等于虚拟机**。在一个环境创建一个文件夹再另一个环境下也可以看到这个文件夹。环境只是不同的解释器

A项目 cd两个模块  --》解释器 --》A 虚拟环境

B项目 de模块         --》解释器 --》B 虚拟环境

3.**关闭进程**

Ps-ef|grep 8000

​		Kill 进程号

4.只要动过crm项目下的url配置的 127.0.0.1:8000就不能再进去了。

```
现在CRM新建一个 views.py的文件
from django.http import HttpResponse

#下面的index为项目名可以改
def index(request):
    return HttpResponse("hello world")
    
然后在urls的目录下
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]
此时网页搜索127.0.0.1:8000/index/就可以看到所需要的视图。
```

### 1.路由系统（url.py）

URL配置 URLconf python模块  —》是URL路径到视图函数的一个映射

### 2.path（route，view,kwargs=None,name=None）

- Route字符串，URL的路径
- View：视图
- Kwargs：额外参数，必须为字典
- Name：

### 3.传参<>通过捕获参数

```
def detail(request, id):
    return HttpResponse("{}号学生详情".format(id))
path('index/<id>/', views.index),
```

但这个时候，你输入任何值都会显示要用路径转换器

### 4.路径转换器

<转换器：参数名>

- str:匹配除了"/"以外的非空字符串
- int:匹配整数
- uuid:格式化字符串，有破折号小写字母和数字。

```
def detail(request, id,year,month):
    return HttpResponse("{}号学生详情".format(id))
path('detail/<id>-<int:year>-<int:month>/', views.index)
```

**应为需要保证输入的数字位数，需要正则来控制输入**

**命名正则表达式分组的语法(?p<组名>正则表达式)**

```
from django.urls import re_path
def detail(request, id,year,month):
    return HttpResponse("{}年{}月{}号学生详情".format(year,month,id))
re_path(r'detail/(?P<year>\d{4})/(?P<month>[0-9]|1[0-2])/(?P<id>\d+)/', views.detail)
]
```

### 5.kwargs：额外参数

当我们的kwargs中的key与url捕获的key一致的时候，以kwargs为准。

```
def student(request,name):
    return HttpResponse("学生:{}".format(name))
path('student/<name>/', views.student,kwargs={'name':'summer'}),
```

### 6.url命名：name

```
from django.shortcuts import redirect
def test1(request):
    return redirect('https://www.baidu.com')
    
def login(request):
    return redirect('/index/')#硬编码
    return redirect('index')#通过name来寻找相应的路径。
    
    
path('test1/', views.test1),
path('login/', views.login),
path('index/guanngtouqiang', views.index, name='index'),
```

### 7.包含其他的URL：include

实际开发中，我们的视图都在app中，这时怎么访问app中的views呢？

传值也可以使用固定参数。

```
from django.urls import path,re_path,include
path('teacher/', include('teacher.urls'), kwargs={'name':'summer'}),
传参会传递到include下面包含的每一条路劲中，要谨慎使用。


def students(request,name):
    return HttpResponse('学生姓名：{}'.format(name))
def detail(request,name='summer'):
    return HttpResponse('{}:成功'.format(name))
    

path('<name>/students/', views.students),
```

总结：

1.当一个请求过来时，Django会查找我们的根URL配置，再找路由匹配规则。从上往下找，一直找到为止

2.如果路由规则对应的是include，去找这个include包含的urlp配置

3.访问的url由路由规则来决定。

### 8.补充 App_name

因为有许多的app，因此有许多的app同时存在index或者login，

在app的urls应用下添加app_name = 'app的name'

如果不设置其他的name那么在login搜索时，只搜索根目录下的index并且如果不命名index将会报错。解决必须加上app_name

```
def login(request):
    return redirect('student:index')
```

## 十二、模板变量和路径映射

1.硬编码

```
def test1(request):
	return HttpResponse('<h1 style='color:red'>我是前端代码</h1>')
```

**html文件写到模板文件中，**

**1.模板放到app目录下templates文件夹下（得自己创建在相应的app目录下）**

**2.集中的放到一个目录（templates）中：在公共的CRM目录下创建templates的文件夹，把所有app的页面都放在里面。**

### 1.创建模板

#### 1.在总目录下创建tempaltes

- 模板要放到特定的文件夹中，在项目根目录下（和manage.py同级）去创建一个文件夹。

- settings.py里的TEMPLATES的DIRS=[]里面设置路径os.path.join(BASE_DIR,'templates')

- 在templates的目录下创建对应名称的app文件夹，用来存放模板文件。

- 在相应的app文件夹下写入html文件

- 再回到对应的视图文件下

- ```
  from django.template.loader import get_template#先导入这个模板
  def test1(request):
  	t = get_template('student/test.html')
  	html = t.render()
  	return HttpResponse(html)
  	### 实际
  	return render(request,'student/test.html')
  ```

#### 2.在模板app下创建templates

- 在app下创建templates的文件夹
- 在CRM的setting.py文件下寻找INSTALLED_APPS的代码下加入student这个代码

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'student',
    'teacher',
]
在student的views里设置相应的代码
def test2(request):
    return render(request,'test3.html')
```

#### 3.总结

- 模板有两种存放方式：1.在app目录下创建一个templates去存放。2.根目录下定义一个目录集中存放。
- 如何选择：1.一般情况下，我们会选择集中存放。2.如果我们要编写可重复使用的app时。
- 为什么我们要在templates文件夹下创建以app名字命名的文件夹？

不同应用会有同名的模板，所以为了区分不同应用的模板，所以要这样。

### 2.模板变量

1.静态页面、动态页面

2.模板变量的语法：{{	变量名	}}

- 变量的命名规则：与其他的命名规则相同。

### 3.模板过滤器

可以让我们在模板文件上直接对模板变量进行在处理

- 常用的过滤器ppt中有第11页

data：日期时间格式

time：时间格式

add：相加，add如果是数字型的字符串会先转为整数如果是其他字符串，会给空值

safe:跨域脚本攻击(xss)

```
<p>{{ js|safe }}</p>
如果不加safe则只能显示这行代码
如果加了safe那么这段代码将执行
```

1.反射型

2.存储型

**模板的例子：**

```
def test4(request):
    now = datetime.now()  #获取当前时间
    # now = now.strftime('%Y年%m月%d日 %H：%M： %S')
    date_format = "Y年m月d日 H：i：s"
    lt = [4,5,6]
    dt = {"name":'summer',"age":18,"height":182}
    st = 'hello world'
    js = "<script>alert('1')</script>"
    lt:lt
    dt:dt
    st:st
    date_format:date_format
    js:js
    return render(request, 'student/test4.html',context={'now':now,'lt':lt,'dt':dt,'st':st,'date_format':date_format,'js':js})

<p>现在时间是：{{ now|date:"Y年m月d日 H：i：s" }}</p>
<p>我是一个列表：{{ lt }}</p>
<p>我是一个列表的一个值：{{ lt.1 }}</p>
<p>我是一个列表的一个值相加：{{ lt.1|add:'8' }}</p>
<p>我是一个列表的一个值相加：{{ lt.1|add:'a' }}</p>{#会失败#}
<p>我是一个列表的第一个值：{{ lt|first}}</p>
<p>我是一个列表的最后一个值：{{ lt|last}}</p>
<p>我是一个列表的切片：{{ lt|slice:':::-1'}}</p>
<p>我是一个列表的拼接：{{ lt|join:'//'}}</p>
<p>我是一个列表的拼接：{{ lt|join:'//'}}</p>
<p>我是英文字符串：{{ st }}</p>
<p>我是英文字符串：{{ st|capfirst }}</p>
<p>我是英文字符串：{{ st|upper }}</p>
<p>我是一个字典：{{ dt }}</p>
```

### 4.总结

- **模板过滤器的语法**

{{ name|过滤器 }}

{{ name|过滤器：字符串参数 }}

字符串参数可以是字符串也可以使模板变量

- **设置模板变量的步骤**

  1.进行变量赋值。2.变量的声明3.进行变量的传参

- **注意事项**

模板里面不能空格--》冒号前后不能空格

一个变量可以过滤多次

### 5.静态文件的导入（css,js,html）

1.公共目录

2.app下

- 统一放在项目根目录下，static的文件夹
- static文件夹下创建好app同名的文件夹
- 配置：并且在setting里STATIC下面一行设置

```
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
```

不推荐直接从根目录下的static文件导入css等文件。解决方法

在网页的第一行加上{% load static %}

然后设置：这样可以不随static_url的改变而重新改变整个文档

```
<link rel="stylesheet" href="{% static 'student/css/index.css' %}">
```

### 6.bootstrap

<https://v4.bootcss.com/docs/4.3/examples/>

去这个网站寻找实例

首先拿到源代码，然后在static文件的相应的文件夹下创建各自的html和css文件。导入的css也需要重新放进去。

在views里设置相应的视图并且在urls里设置相应的路由，注意！在HTML的文件里一定要在第一行加上{% load static%}然后link里的href放{% static '放路径'%}**这样可以保证STATIC_URL改变的情况下也能拿到相应的文件。**

### 7.模板标签

一般;

```
<table>
    <tr>
        <th>序号</th>
        <th>姓名</th>
        <th>年龄</th>
        <th>升高</th>
        <th>性别</th>
    </tr>

    <tr>
        <td>1</td>
        <td>{{ students.0.name }}</td>
        <td>{{ students.0.age }}</td>
        <td>{{ students.0.height }}</td>
        <td>{{ students.0.sex }}</td>
    </tr>
</table>
```

#### 1.常用标签

{% load static%}

{% 标签%}{% 结束标签%}

![1568014263030](assets\1568014263030.png)

**url的使用**

```
<a href="{% url 'student:detail' student.name%}">{{ forloop.counter }}</a>
```

**for循环的使用**

```
{% for student in students %}
<tr>
    <td><a href="{% url 'student:detail' student.name%}">{{ forloop.counter }}</a></td>
    <td>{{ student.name }}</td>
    <td>{{ student.age }}</td>
    <td>{{ student.height }}</td>
    <td>{{ student.sex }}</td>
</tr>
{% endfor %}
```

**if语句的使用**

```
{% if student.sex == '女' %}style="color: red" {% endif %}
```

**with语句的使用**

```
{% with stu_name=student.name %}
{% endwith %}
```

#### 2.模板的继承和引用

- 引用include

Django模板通过模板标签实现一个模板，再其特点定的位置引入另一个模板

```
<div id="ad">
    {% include 'student/ad.html' %}
</div>
```

#### 3.继承extends+block

bootstarp

- 放在第一行

```
{% extends 'teacher/base.html' %}
```

- block

- ```
  {% block 名字 %}
  {% endblock %}
  ```

- 一个放在头部和尾部的中间部分

- 另一个放在需要放入的部分

```
    <link href="{% static 'teacher/css/base.css' %}" rel="stylesheet">
      {% block link %}
      {% endblock %}
    
    
    {% block link %}
<link rel="stylesheet" href="{% static 'student/css/index.css' %}">
    {% endblock %}
```

### 8.自定义过滤器

1.设置数据是，通常并不会直接使用男女；而是使用数字来表示（女：0，男：1）

2.但是显示在页面上时，需要显示男和女

3.代码布局

- 某个app特有

- 根目录，多个app公用

  **常用设置是**：设置app特有

步骤：

1.创建一个叫templatetags的包（‘__init__.py')

2.app必须要在setting的INSTALL_APPS里配置好

3.重启服务

4.写自动以过滤器函数

```
def to_sex(value,arg='zh'):
    change={
        'zh':('女','男'),
        'en':('Female','Male')
    }
    return change[arg][value]
```

5.注册

```
from django import template

register = template.Library()#变量名必须是register

def to_sex(value,arg='zh'):
    change={
        'zh':('女','男'),
        'en':('Female','Male')
    }
    return change[arg][value]

register.filter('sex',to_sex)#前面可以取名字，
register.filter(to_sex)#如果不起名字，函数名就是过滤器名
```

注：因为使用的是元组，并且使用查找。所以在设置1和0的时候必须要将1和0设置为数字类型，如果为str类型，会报错。

6.在需要的地方把函数名进行过滤器的放置。因为有一个默认参数，如果需要改变这个默认参数，可以在函数名后面进行传值:to_sex:'en'。

第二种：装饰器

```
from django import template

register = template.Library()#变量名必须是register

@register.filter(name='sex1')
def to_sex(value,arg='zh'):
    change={
        'zh':('女','男'),
        'en':('Female','Male')
    }
    return change[arg][value]
```

### 9.自定义模板标签--可以干任何事情

在app内创建一个名字为templatetags的包

在INSTALLED_APPS里配置好路径

#### 1.简单标签

{% url 'app_name:name' stu.name %}

```
1.创建函数
from datetime import datetime


def current_time(format_str):
    now = datetime.now().strftime(format_str)
    return now
2.导入
{% load customer_tags %}
3.注册
<p>我是通过自定义模板标签现实的时间:{% current_time '%Y年%m月%d日 %H：%M： %S'}</p>
3.使用
4.上下文管理
在视图函数里创建：
format_str = '%Y年%m月%d日 %H：%M： %S'

在函数里写：
@register.simple_tag(takes_context=True)#这个可以接受路由里的全部的值
def current_time(context):
    return datetime.now().strftime(context['format_str'])
```

#### 2.包含标签：一个模板通过渲染另一个模板来展示数据

前提：

- 表格内多行内容显示<td>{{ student.course }}</td>

- 通过for循环<td>{% for course in student.course %}{{ course }}{% endfor %}</td>

- 通过无序列表和for循环;

  ```
  <td>
      <ul>
          {% for course in student.course %}
              <li>{{ course }}</li>
          {% endfor %}
      </ul>
  </td>
  ```

这个方法在很多地方都会用到,choices为需要迭代的对象

```
<ul>
	{% for i in choices %}
	<li>{{i}}</li>
	{% endfor%}
</ul>
```

- 利用模板+自定义标签来实现

1.创建文件

```
def show_list_as_ul(value): #定义一个函数接受一个模板变量
    return {'u_list':value} #'u_list'由模板决定

t = get_template('student/show_list_as_ul.html')#模板渲染
register.inclusion_tag(t)(show_list_as_ul)
```

2.注册

```
<td>{% show_list_as_ul student.course%}</td>
```

3.使用

4.优化



#### 3简析：标签

对于**简单标签**，return什么东西就会在网页上显示什么。

对于**包含标签**，先接受变量，然后在register的模板里去渲染一遍然后return出来，



### 10.数据库的连接配置

db.sqlite3是django默认的数据库：有自己的一套语法

在项目中需要一套可伸缩的数据库。

python提供了api可以连接数据库

#### 1.需要配置

1.数据接口

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

2.配置MySQL数据库：同数据库阶段

- workon到相应的环境下安装pymysql（API）

- 创建数据库

  - root账户不允许远程登录，可以远程访问对的数据库用户

  - 创建数据库

    ```
    1.进入mysql的命令：mysql -uroot -pqwe123
    2.展示所有的数据库：show databases;
    3.创建数据库：create database CRM charset=utf-8;#指定字符编码格式
    4.创建用户并且授权
    grant all privileges on CRM.* to 'summer'@'%(允许远程)' identified by 'summer'
    5.flush privileges;(刷新权限)
    6.可以直接mysql -usummer -psummer -A CRM (直接进入库)
    7.settings里修改配置：
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'CRM',#数据库的名字
            'USER':'summer',
            'PASSWORD':'summer',
            'HOST':'127.0.0.1',
            'PORT':3306,
        }
    }
    ```

  - 导入pymysql

  在项目目录下有一个__init__文件

  ```
  import pymysql
  pymysql.install_as_MySQLdb()
  ```

  

## 十三、ORM

概念：对象关系映射

本质:用面向对象的方式，去描述数据库，操作数据库，达到不用编写sql语句对数据库进行增删改查。

优势：不用直接编写SQL代码，只需像操作对象一样从数据库操作数据

类—》表

类属性—》字段

实例—》数据

所有的代码写在moudles里面

### 1.模型的创建与映射

#### 1.模型文件：student/models.py

#### 2.创建模型：

- varchar—》models.CharField(max_length) 字符串 max_length设置长度


- int—》SmallIntegerField（IntegerField)数字


- models.DateTimeField(auto_now_add=True) 时间（自动填充当前时间）
- models.DateField 日期
- longtext—》models.TextField 文本

```
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    sex = models.SmallIntegerField(default=1)  #设置默认值
    qq = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    # c_time = models.DateTimeField(verbose_name='数据创建时间',auto_now_add=True)#auto_now_add 自动填充当前时间
    c_time = models.DateTimeField('数据创建时间',auto_now_add=True)#名字必须放在第一位
```

#### 3.激活模型

- 1.检查app是否被注册（settintg里的installed_app)
- 2.迁移

python manage.py makemigrations teacher#指定app迁移

python manage.py makemigrations #迁移全部模型

```
(djangoApp) pyvip@VIP:~$ workon djangoApp
(djangoApp) pyvip@VIP:~$ ls
config  djangoProject  install.sh  py_case  snap  summer-2  公共的  模板  视频  图片  文档  下载  音乐  桌面
(djangoApp) pyvip@VIP:~$ cd djangoProject/CRM
(djangoApp) pyvip@VIP:~/djangoProject/CRM$ python manage.py makemigrations

python manage.py qslmigrate student 0001 #查看原生sql语句
```

以上操作完成，保存更改，但是操作还没生效。

- 迁移生效

```
python manage.py migrate
```

- 重点：注意

  迁移功能非常强大，允许我们在开发项目是对模型随时更改，不需要删除数据库或者创建新的表----实时去升级数据库而不丢失数据。

#### 4.总结，模型修改三部曲

1.修改模型（创建模型）

2.运行 python manage.py makemigrations  创建迁移

3.运行 python manage.py migrate 迁移生效

### 2.模型数据的增删改查

进入交互式python shell中

```
pip install ipython
python manage.py shell
```

1.增

```
from student.models import Student  #导入模型
#第一种方式,需要将创建的对象保存
s = Student(name='summer',age=20,qq='12345') 
s.save()

#第二种方式#创建空实力，在属性赋值，对象要保存
s1 = Student()
s1.name = 'july'
s1.age = 18

#第三种方式#create，不用保存
Student.objects.create(name='april',age = 19) 
#第四种方式#有就取值，没有就创建记录
s = Student.objects.get_or_create(name = 'blue') 
```

2.查

```
#查所有
In [15]: res = Student.objects.all()                                                          

In [16]: res                                                                                  
Out[16]: <QuerySet [<Student: Student object (1)>, <Student: Student object (2)>, <Student: Student object (3)>, <Student: Student object (4)>]>

In [18]: print(res.query)                                                                     
SELECT `student_student`.`id`, `student_student`.`name`, `student_student`.`age`, `student_student`.`sex`, `student_student`.`qq`, `student_student`.`phone`, `student_student`.`c_time` FROM `student_student`

#查单条，只能返回一个对象，同时符合条件的有多个会报错
Student.objects.get(pk=1)  #逐渐不一定会命名为id，

2 Student.objects.filter(age=18)  

3 res = Student.objects.filter(age=18)   print(res.query) 
```

3.改

```
 s = Student.objects.get(id = 4) 
 s                               <Student: blue>
 s.phone = '1254135'             
 s.save()
 
 
 
 第二种，一次修改多条数据
 Student.objects.filter(sex = 1).update(sex=0) 
```

4.删

```
s = Student.objects.get(pk = 3) 

s.delete()  

批量删除
Student.objects.filter(age=18).delete() 
Student.objects.all().delete() 
```

### 3.字段类型+属性

#### Field常用参数

primary_key:  指定是否为主键。
unique:  指定是否唯一。
null:  指定是否为空，默认为False。
blank: 等于True时form表单验证时可以为空，默认为False。
default:  设置默认值。
DateField.auto_now:  每次修改都会将当前时间更新进去，只有调用，QuerySet.update方法将不会调用。这个参数只是Date和DateTime以及TimModel.save()方法才会调用e类才有的。
DateField.auto_now_add:  第一次添加进去，都会将当前时间设置进去。以后修改，不会修改这个值

**如果你在最起初的时候去设置primary_key和unique，必须在刚刚开始是就去加上，如果一定要在后面加上就要删除全部的数据库，并且在mysql里删除有关app的一切**

### 4.查询方法

首先在环境下进入python编写页面

```
python manage.py shell
from teacher.modles import Student
#然后插入数据
#get all filter

#all
1.
In [7]: Student.objects.all()                             
Out[7]: <QuerySet [<Student: summer>, <Student: july>, <Student: april>, <Student: hah>]>


#filter
2.
In [10]: Student.objects.filter(name='summer')            
Out[10]: <QuerySet [<Student: summer>]>



3.
res = In [12]: res = Student.objects.filter(name='july')        

In [13]: print(res.query)                                 
SELECT `student_student`.`num`, `student_student`.`name`, `student_student`.`age`, `student_student`.`sex`, `student_student`.`qq`, `student_student`.`phone`, `student_student`.`c_time`, `student_student`.`x_time` FROM `student_student` WHERE `student_student`.`name` = july


#get
Student.objects.get(name='april')
```

共同点：

1.都是通过objects去实现——》objects：每一个django模型类，都有一个默认管理器，objects

#### 其他

```
1.
In [15]: Student.objects.first() #查询第一条数据                         
Out[15]: <Student: summer>#返回一个对象

2.
In [16]: Student.objects.last() #查询最后一条数据                          
Out[16]: <Student: hah>#返回一个对象

3.
In [17]: Student.objects.exclude(name='summer')    #与filter用法相同，作用相反，排除       
Out[17]: <QuerySet [<Student: july>, <Student: april>, <Student: hah>]>

In [18]: Student.objects.filter(name='summer')            
Out[18]: <QuerySet [<Student: summer>]>


4.指定字段查询
In [19]: Student.objects.values('name')                   
Out[19]: <QuerySet [{'name': 'summer'}, {'name': 'july'}, {'name': 'april'}, {'name': 'hah'}]>#返回字典

In [23]: res = Student.objects.values('name')             
#他可以查指定字段的东西，但是其余的东西却不能找到
In [24]: res[2]['name']                                   
Out[24]: 'april'

#如果要拿全部的东西，需要用到only

In [27]: res = Student.objects.only('name')               

In [28]: res                                              
Out[28]: <QuerySet [<Student: summer>, <Student: july>, <Student: april>, <Student: hah>]>
In [30]: res[2]                                           
Out[30]: <Student: april>

In [31]: res[2].name                                      
Out[31]: 'april'

In [32]: res[2].sex                                       
Out[32]: 0


#和only相反的defer（排除）
#####排序
#order_by:根据指定字段排序
In [37]: res = Student.objects.order_by('age')            

In [38]: print(res.query)  
SELECT `student_student`.`num`, `student_student`.`name`, `student_student`.`age`, `student_student`.`sex`, `student_student`.`qq`, `student_student`.`phone`, `student_student`.`c_time`, `student_student`.`x_time` FROM `student_student` ORDER BY `student_student`.`age` ASC
ASC表示正序

In [40]: res = Student.objects.order_by('-age')            

In [41]: print(res.query)                                  
SELECT `student_student`.`num`, `student_student`.`name`, `student_student`.`age`, `student_student`.`sex`, `student_student`.`qq`, `student_student`.`phone`, `student_student`.`c_time`, `student_student`.`x_time` FROM `student_student` ORDER BY `student_student`.`age` DESC
DESC表示反序


##切片
In [43]: Student.objects.all()[:2]                         
Out[43]: <QuerySet [<Student: summer>, <Student: july>]>


##查询
#单条件
In [47]: Student.objects.filter(age=20,sex=0)              
Out[47]: <QuerySet [<Student: summer>, <Student: april>]>

#多条件查询，需要导入Q库
In [48]: from django.db.models import Q                    

In [49]: Student.objects.filter(Q(sex=0),Q(age=20)|Q(age=19
    ...: ))                                                
Out[49]: <QuerySet [<Student: summer>, <Student: april>]>
```

### 5.查询条件

```
#exatc 准确匹配
 WHERE `student_student`.`name` = summer


#iexatc 不区分大小写匹配
WHERE `student_student`.`name` LIKE summer

#contains 包含匹配
WHERE `student_student`.`name` LIKE BINARY %s%

#icontains 不匹配大小写的包含匹配
 WHERE `student_student`.`name` LIKE %s%
# in
In [63]: Student.objects.filter(pk__in=[1,2])              
Out[63]: <QuerySet [<Student: summer>, <Student: july>]>

In [65]: Student.objects.filter(sex__in='01')              
Out[65]: <QuerySet [<Student: summer>, <Student: july>, <Student: april>, <Student: hah>]>

#子查询
res = Student.objects.filter(name__icontains='s'). only('name') 
res1 = Student.objects.filter(pk__in=res).only('name')                  print(res1.query)                                 
SELECT `student_student`.`num`, `student_student`.`name` FROM `student_student` WHERE `student_student`.`num` IN (SELECT U0.`num` FROM `student_student` U0 WHERE U0.`name` LIKE %s%)

#gt大于 gte大于等于 lt小于 lte小于等于
In [71]: Student.objects.filter(pk__gt=2)                  
Out[71]: <QuerySet [<Student: april>, <Student: hah>]>

#range，范围查找
In [74]: Student.objects.filter(age__range=(0,21))         
Out[74]: <QuerySet [<Student: summer>, <Student: july>, <Student: april>, <Student: hah>]>

#聚合分组annotate
In [76]: from django.db.models import Count,Avg,Max,Sum    

In [77]: res = Student.objects.values('sex').annotate(ren=C
    ...: ount('sex'))                                      

In [78]: print(res.query)                                  
SELECT `student_student`.`sex`, COUNT(`student_student`.`sex`) AS `ren` FROM `student_student` GROUP BY `student_student`.`sex` ORDER BY NULL
```

### 6.表关系的实现

一对一，一对多，多对多

#### 1.表关系

一个班级-----多个学生

问：foreignkey放在哪？

​		一个班级找一个学生

​		一个学生找一个班级

所以foreignkey放在学生表

```
from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField('学生姓名',max_length=20)
    age = models.SmallIntegerField('年龄',null=True)
    sex = models.SmallIntegerField('性别',null=True)
    qq = models.CharField('QQ',max_length=20,unique=True)
    phone = models.CharField('电话',max_length=20,unique=True)
    c_time = models.DateTimeField('创建时间',auto_now_add=True)
    # detail = models.OneToOneField('TeacherDetail',on_delete=models.SET_NULL,null=True)
    grade = models.ForeignKey('Grade',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return"{}-{}".format(self.name,self.age)



class TeacherDetail(models.Model):
    college = models.CharField('学院',max_length=20)
    teacher = models.OneToOneField('Teacher',on_delete=models.CASCADE)


class Grade(models.Model):
    name = models.CharField("班级名称",max_length=20)
    num = models.CharField('班期',max_length=20)


class Coures(models.Model):
    name = models.CharField("课程名称",max_length=20)
    teachers = models.ManyToManyField('Teacher')
```

#### 2.回滚

```
python manage.py migrate teacher 0001
注意回滚后必须把最后一次记录删了
```

#### 3.中间表自己创建

```
前面需要在一个表上加上through：
class Coures(models.Model):
    name = models.CharField("课程名称",max_length=20)
    teachers = models.ManyToManyField('Teacher',through='Enroll')#在关联的表上面添加through，这样可以不按照他给你的teacher_coures创建中间表，而是按照自己的表格来创建

#中间表
class Enroll(models.Model):
    teacher = models.ForeignKey('Teacher',on_delete=models.CASCADE)
    course = models.ForeignKey('Coures',on_delete=models.CASCADE)
    pay = models.FloatField('缴费金额',default=0)
    c_time = models.DateTimeField('报名时间',auto_now_add=True)
```

### 4.OneToMany(正向/反向增删改查)

```
正向：一个模型有外键字段，通过这个模型对外键进行操作就叫正向
反向：一个模型如果被另一个模型外键关联，通过这个模型对关联他的模型进行操作
class Student(models.Model):
	....
	grade = models.ForeignKey('Grade',on_delete=models.SET_NULL,null=True)
```

```
#增：通过属性赋值
In [12]: s1 = Teacher(name='summer',age=20,sex=1,qq='123',
    ...: phone='456',grade = g1)                          
In [13]: s1.save() 
#增：主键方式
s3 = Teacher(name='april',age=18,sex=0,qq='1357',phone='2468')  
s3.grade_id = g3.id               s3.save()  

#查
In [22]: s1                                                    
Out[22]: <Teacher: summer-20>

In [23]: s2.grade.name                                         
Out[23]: '爬虫班'

In [25]: Teacher.objects.filter(grade__name='django框架') 

Out[25]: <QuerySet [<Teacher: summer-20>]>

#删：删除两个之间的关联关系
In [26]: s1.grade = None                                       
In [27]: s1.save()                                             
In [28]: s1.grade  

```

反向的管理器：如果一个模型（Teacher）有一个ForeignKey（grade），那么这一个外建模型的实例为g1将可以返回一个teacher模型的所有市里的管理器（teacher_set)(teacher是模型名,小写)

```
#增
#1.通过teacher_set管理器
new_s = g2.teacher_set.create(name='fat',age=20,sex=1,qq='12367',phone='12537')  
#2.一次多个数据
In [32]: s1,s2,s3 = Teacher.objects.filter(id__lte=3);         

In [33]: g1.teacher_set.add(s1,s2,s3) 

#改
g2.teacher_set.set([s2,s3])  

#删
g2.teacher_set.remove(s2,s3) 

g2.teacher_set.clear() 

#查：和objects一样使用
g1.teacher_set.all() 

In [44]: g1.teacher_set.filter(age=18)                         
Out[44]: <QuerySet []>
```

### 5.ManyToMany

```
class Course(models.Model):
	...
	teachers = models.ManyToManyField('Tracher',through='Enroll')
反向模型管理器：Course_set
替换模型名：related_name--可以通过这个来指定属性替代course_set
teachers = models.ManyToManyField('Teacher',through='Enroll',related_name = 'course')
```

因为改了数据，因此需要重新迁移数据。

```
python manage.py makemigrations
python manage,py migrate
#再次导入ipython
python manage.py shell
就可以再次进行编写
```

```
In [1]: from teacher.models import Teacher,TeacherDetail,Coures,Enroll,Grade  
#增
c1 = Course.objects.create(name='python')  
s1 = Teacher.objects.first() 
#关联
In [7]: e = Enroll()             
In [8]: e.course = c1             
In [9]: e.teacher = s1 
In [14]: e.save() 

#查
#正向查找
In [21]: c1.teachers.all()       
Out[21]: <QuerySet [<Teacher: summer-20>]>
#反向查找
In [19]: s1.course.all()         
Out[19]: <QuerySet [<Course: Course object (1)>]>
```

### 6.OneToOne

正向：foreignkey在哪个字段下面就是通过这个字段去找关联的东西。

```
正向：一对一字段所载的模型，通过这个模型去访问关联的模型
In [23]: d1 = TeacherDetail(college='宁夏理工学院')                  
In [24]: d1.teacher = s1         
In [25]: d1.save()
#查
In [26]: TeacherDetail.objects.values('college','teacher__name','teacher__qq')               
Out[26]: <QuerySet [{'college': '宁夏理工学院', 'teacher__name': 'sum'teacher__qq': '123'}]>
反向：前面的反向都是通过管理器，泽丽反向类似正向
In [28]: s = Teacher(name='yl',age=19,sex=0,qq='151551',phone='357337')    #原始模型的小写名  
In [29]: s.studentdetail = d1     
In [30]: s.save()  
#查
Teacher.objects.values('name','qq','teacherdetail__college')
```

### 7.跨表查询

```
#如果我想要跨越关系，只需要使用跨模型的向相关字段的字段名以双下划线隔开，知道达到想要的结果为止。
#男老师的课程
In [56]: Course.objects.filter(teachers__sex=1)          
Out[56]: <QuerySet [<Course: Course object (1)>]>
#报名python课程的老师
Teacher.objects.filter(course__name='python') 
####contions模糊查询
#及报名python也是django11期学员
Teacher.objects.filter(course__name='python',grade__num__contains='11') 

#查缴费小于3000的老师
In [71]: e = Enroll()  
In [72]: e.course = c2 
In [73]: e.teacher = s5 
In [74]: e.pay = 1000 
In [75]: e.save()  
In [68]: Teacher.objects.filter(enroll__pay__lt=3000)       
Out[68]: <QuerySet [<Teacher: summer-20>, <Teacher: july-19>, <Teacher: april-18>, <Teacher: fat-20>]>
#查询学员报名课程的班级有哪些
In [5]: Grade.objects.filter(teacher__course__name='python') 
Out[5]: <QuerySet [<Grade: django框架>, <Grade: django框架>, <Grade: 基础班>]>
#去重
In [6]: Grade.objects.filter(teacher__course__name='python').distinct()   
Out[6]: <QuerySet [<Grade: django框架>, <Grade: 基础班>]>
```

## 十四、请求与响应

Django框架是一个web应用框架

请求和响应的流程：

输入网址，请求页面(**GET请求**)，通过路径找到对应的视图函数。

django创建的HttpRequest对象，该对象包含关于请求的源数据

经过处理，视图return一个HttpResponse对象

查找 ：先找根目录的url配置，然后一层一层往下找。

#### 1.get

debug模式，先关闭原来的crm，然后打断点，然后点小虫子。运行到断点就暂停。

**1.并且运行调试工具的时候，必须使用的是恢复程序执行，不能一次一次点，不然会特别麻烦。**

```
 action="{% url 'teacher:form' %}" 
 2.对于这个代码，teacher后面的网页必须经过命名才可以使用。不然会报错哟
```

3.在网页上赋值的时候，使用http://127.0.0.1:8000/teacher/form/?username=summer&password=123&hoppy=basketball&hoppy=football

4.此时在获取参数时如果使用request.GET.get('hoppy')将得到最后一个值。如果要多个赋值，那需要使用getlist

#### 2.post

get在请求一个网页的时候是可以看到网页后面的参数的，但是使用post却可以让别人看不到。

**注：**

**因为django自带一个安全措施csrf所以当你需要请求网页时，回进行报错。因此需要在<form action="" method="post">的下面加上{% csrf_token %}。在页面上他会自己生产一些东西。**

简单的登录代码。

```
def form(request):
    # return render(request, 'teacher/form.html')
    if request.method == 'GET':
        return render(request, 'teacher/form.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'summer' and password == '123':
            return redirect('teacher:login')
        else:
            return render(request,'teacher/form.html')
```

优化：

```
if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'summer' and password == '123':
        return redirect('teacher:login')
    else:
        return render(request,'teacher/form.html')
return render(request, 'teacher/form.html')
```

#### 总结：

- get从服务器获取数据，不回去更改服务器的数据。

- post：携带数据发送给服务器，一般会更爱服务器的数据。

- get在url中携带参数发送给数据库。post不会在url中看到参数。

### 1.文件上传存储路径的设置

**因为文件信息不同于get和post所以在debug的时候，需要有单独的请求代码。request.FILES.get('file')**

1.创建：一般放在ststic文件夹下。在项目根目录下static文件夹中创建media文件夹。

2.配置：在setting文件下的最后一行创建一行命令：MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')

3.创建提交表单

```
<form action="" method="post" enctype="multipart/form-data">{#文件上传必须使用enctype#}
    {% csrf_token %}
    <input type="file" name="file">
    <input type="submit" value="上传">
</form>
```

4.修改视图函数

```
from datetime import datetime
import os
from CRM.settings import MEDIA_ROOT


def form(request):
    if request.method == 'POST':
        file = request.FILES.get('file')

        #每天的文件放到每天的文件夹里面
        day_dir = datetime.now().strftime('%Y%m%d')
        dir_path = os.path.join(MEDIA_ROOT, day_dir)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)


        filename = os.path.join(dir_path,file.name)#路径拼接
        with open(filename,'wb') as f:
            for line in file.chunks():#将上传文件过大时进行分块
                f.write(line)
```

**注：如果需要多个文件上传，则需要在input为file的属性名添加一个mutiple。同时file=request.FILES.getlist('file')并且之前是以此添加文件，这边加个循环就可以使整个文件都上传。for file in flies:下面的和之前一个文档的内容一样**

### 2.HttpRequest对象

```
In [5]: response = HttpResponse("上传成功")               
In [6]: response.content 
Out[6]: b'\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x88\x90\xe5\x8a\x9f'

In [7]: response.content.decode("utf-8") 
Out[7]: '上传成功'

In [8]: response  
Out[8]: <HttpResponse status_code=200, "text/html; charset=utf-8">
```

同时也支持先创建然后写入

```
In [11]: response = HttpResponse()  
In [12]: response.write("你好") 
In [14]: response.write("<h1>你好世界</h1>")              

In [15]: response.content                                 
Out[15]: b'\xe4\xbd\xa0\xe5\xa5\xbd\xe6\x88\x91\xe5\xa5\xbd<h1>\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xb8\x96\xe7\x95\x8c</h1>'

In [16]: response.content.decode("utf-8")
Out[16]: '你好我好<h1>你好世界</h1>'
```

render：渲染

redirect：重定向，跳转另一个网页

**JsonResponse**

```
from teacher.models import Teacher
def test_json(request):
    sex = request.GET.get("sex")
    rex = Teacher.objects.values('name','age','sex').filter(sex=sex)
    res = list(rex)
    data = {'result' : res}
    # return HttpResponse("ok")
    return JsonResponse(data)
```

### 3.cookie

客户端访问服务器时（发送请求时）服务器在http协议里加上请求头，通过响应，传送到客户端，并保存在客户端，当客户端再次访问时，将携带这个cookie去访问，这样服务器才能区分不同的客户端。

注：+=必须左右两边同时为int不然会报错。

```
num = request.COOKIES.get('num')
if num:
    num = int(num) + 1
else:
    num = 1
```

```
response = render(request, 'student/test4.html',context={
    'num':num,
    'now':now,
    'lt':lt,
    'students':sts,
    'st':st,
    'date_format':date_format,
    'js':js,
    'dr':dr,
    'format_str':format_str})
response.set_cookie('num',num,max_age=5)#后面的max_age可以设置cookie的有效值，5秒后重置。
return response
```

## 十五、分页

### 1.准备工作

实现分页，需要几个关键数据

1.数据总量

2.每页数据条数

3.当前页码

```
#导入
from django.core.paginator import Paginator 

#第一个是objects，第二个是每页显示几个数据
p = Paginator(Student.objects.all().order_by('c_time'),3) 

#输出几个总数
p.count 

#查看显示的页数
p.num_pages 

#查看页面的范围
p.page_range 

#查看当前页现实的数据
In [10]: page1  = p.page(1)

In [11]: page1.object_list
Out[11]: <QuerySet [<Student: summer-20>, <Student: july-19>, <Student: april-18>]>
    #或者
In [16]: sts = p.get_page(1)     
In [17]: for student in sts: 
    ...:     print(student) 
    ...:                         
summer-20
july-19
april-18


#查看是否有上下页
In [14]: page1.has_previous()
Out[14]: False

In [15]: page1.has_next() 
Out[15]: True

#查看当前页的下一页
page1.next_page_number() 
```

### 2.简单分页

```
    sts = sts.order_by('-c_time')#排序

    #实现分页

    #数据总量
    total_num = sts.count()

    #每页条数
    per_page = request.GET.get('per_page',10)#后面的为默认值


    #当前页码
    page = request.GET.get('page',1)
    pageinator = Paginator(sts,per_page)
    sts = pageinator.get_page(page)
```

## 十六、session

```
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')
        if username == 'summer' and password == 'summer':
            request.session['name'] = username
            request.session.set_expiry(10)#设置过期时间，10秒
            return redirect('test1:index')


    return render(request,'test1/login.html')


def index(request):
    name = request.session.get('name','游客')#后面的为默认值，因为点击退出会显示none
    return render(request,'test1/index.html',context={
        'name':name,
    })

def logout(request):
    request.session.flush()
    return redirect('test1:index')
```

**login.html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录</title>
</head>
<body>
<form action="" method="post">
    {% csrf_token %}
    <p><input type="text" placeholder="请输入用户名" name="username"></p>
    <p><input type="password" placeholder="请输入密码" name="password"></p>
    <input type="submit" value="登录">
</form>
</body>
</html>
```

**index.html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
恭喜{{ name }}访问

{% if request.session.name %}
<a href="{% url 'test1:logout' %}">退出</a>
{% else %}
<a href="{% url 'test1:login' %}">登录</a>
{% endif %}
</body>
</html>
```

## 十七、模型表单

### 1.简单表单

本质上：表单--》类

app目录下，创建一个forms.py的模块

创建的表单默认为test类型，如果需要修改，则应该在widget后面进行修改，并且可以再atters里面进行其他属性的操作。

并且视图函数默认是在一行的，这里存在as_p,as_table,as_ul三个大小放在洞内

```
{{ form.as_p }}
```

### 2.并且form表单的标签和提交按钮需要自己写

自定义校验实现密码不一致时的提示。

```
def clean(self): #多字段
    cleaned_data = super().clean() #继承父类

    #增加提示信息
    password = cleaned_data.get('password')
    password_repeat = cleaned_data.get('password_repeat')

    if password != password_repeat:
        msg = '密码不一致'
        self.add_error('password_repeat',msg)



def clean_uesrname(self):  #单字段
    pass
```

### 3.模型表单forms.ModelForm

```
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student   #模型
        fields = '__all__' #字段，指定展示在前台的数据


class StudentDetailForm(forms.ModelForm):
    class Meta:
        model = StudentDetail   #模型
        fields = '__all__'
```

**views.py**

```
def detail_form(request,pk):
    student = Student.objects.get(pk=pk)
    form = StudentForm(instance=student)

    return render(request,'test1/detail_form.html',context={
        'form':form,
    })
```

## 十八、中间件

```
中间价文件可以放在项目路径下的任何位置。雷诗雨视图函数，接受response

# test/middleware.py

激活中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'test1.middleware.simple_middleware',
]

3.如果有多个中间件，他会像装饰器一样【【【】】】从上往下走，然后最后一个慢慢往外走
```

## 十九、上下文管理器

解决多余的context代码冗余

同样是一个python函数

context传递变量到模板

如果所有页面需要某些特定的变量

上下文处理====python函数

案例：假如说都需要一个name变量

```
# teacher/customer_context_processor.py

#注册 配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'test1.customer_context_processor',
            ],
        },
    },
]

在html里可以直接使用{{name}}

相同的key，context生效
如果视图里也设置了name，这是公共变量，它将使用context来生效。
```

## 二十、admin

1.在CRM里面创建超级用户

python manage.py createsuperuser

Username (leave blank to use 'pyvip'): summer
Email address: 1789572985@qq.com
Password: summer
Password (again): summer

2.因为刚刚开始真个页面都是一样的，需要转化为中文的话，去setting里面的

```
LANGUAGE_CODE = 'en-us'
```

把它变为zh-hans

3.app下的admin.py中注册要管理的模型

```
from django.contrib import admin
from .models import Student,StudentDetail
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','sex','qq','phone']
    list_display_links = ['name','sex']
    list_filter = ['sex']
    search_fields = ['name','qq','phone']
    list_per_page = 5

    #详情页面
    # fields = ['age','sex']
    fieldsets = [  #分组设置
        (None,{'fields':['name','sex']}),#分组名字,分组信息
        ('详细信息',{'fields':['qq','phone','grade']}),
        ('设置',{'fields':['is_delete']}),
    ]

admin.site.register(Student, StudentAdmin)
admin.site.register(StudentDetail)
```

## 二十一、auth系统

```
django自带的用户身份验证系统
1.用户验证：登录的账号是否是真正的用户
2.授权：允许用户做什么
```

### 一、用户验证

#### 1.1、实现登录

```
1.view.py里面
def login_view(request):
    # user = request.user
    #判断是否登录
    if request.user.is_authenticated: #匿名用户返回false
        return redirect('test1:student_list')

    if request.method == 'POST':
        #获取用户名和密码
        username = request.POST.get('username')
        password = request.POST.get['password']
        #校验码用户名和密码
        user = authenticate(username=username, password=password)  #正确返回user对象，错误返回none
        if user is not None:
            # 用户信息存放到session并登录。
            login(request,user)
            return redirect('test1:student_list')


    return render(request,'test1/login.html')
2.index.html里面
恭喜{{ user.username|default:'游客' }}访问

{% if user.is_authenticated %}
<a href="{% url 'test1:logout' %}">退出</a>
{% else %}
<a href="{% url 'test1:login' %}">登录</a>
{% endif %}
```

#### 1.2、实现退出

```
def logout_view(request):
    logout(request)
    return redirect('text1:index')
```

#### 1.3、实现限制

在student_list里面添加

```
#限制登录
if not request.user.is_authenticated:  #未登录用户访问，返回登录页面
    return redirect('test1:login')
```

#### 1.4、限制优化

```
#登录优化一：实际开发过程中间，如果我要访问某个页面，而这个页面需要登录权限，我们登录后自动转回此前我想访问的页面。

#处理方法，把当前的路径当做参数传入
保留/拼接路径：request.path.path_info

#return redirect(reverse('test1:login')+'?next={}'.format(request.path.path_info))
#登录优化二：多个视图都要这个功能，需要每个视图加上向他的内容会出现代码冗余，处理方式：装饰器
from django.contrib.auth.decorators import login_required
删除原来的限制登录代码，在def上面加上装饰器：@login_required

@login_required
def student_list(request):
    #限制登录
    # if not request.user.is_authenticated:  #未登录用户访问，返回登录页面
    #     return redirect(reverse('test1:login')+'?next={}'.format(request.path.path_info))
        #student/login/?next=test/test1/student_list
# settings.py

from django.urls import reverse, reverse_lazy

LOGIN_URL = reverse_lazy('test1:login')
```

### 二、授权

添加权限：从左边的框里面搜索相应的权限，然后全选，点击下卖弄的全选就可以添加到右边的方框里面。

在manage.py里面查看

```
from django.contrib.auth.models import User, Group , Permission  
```

u1.groups#分组

u1.user_permission#权限



查看有无权限

user = User.objects.last()  

user.has_perm('student.add_grade')   

**对某个app.权限_某个表**

1.权限验证

```
1.view.py
from django.contrib.auth.decorators import login_required,permission_required

@permission_required('student.view_student',raise_exception=True)
@login_required
def student_list(request):

    #确认是否有权限
    # if not request.user.has_perm('student.view_student'):
    #     return HttpResponse('你无权查看')
```

## 二十二、类视图

一般命名规则：

函数：下划线

类：大驼峰

前端：小驼峰 

路径自动找函数，需要把请求和相关参数发送给函数，但是发送不了给类。

类函数的路径：path('my_oh/',views.MyView.as_view(),name='my_oh'),

### 1.类视图使用表单

```
class Register(View):
    def get(self,request):
        form = RegisterForm()
        return render(request, 'test1/register.html', context={
                    'form':form,
                })


    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():#进行字段校验，校验成功返回true
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            if password == password_repeat:
                return HttpResponse('注册成功')
        return render(request, 'test1/register.html', context={'form': form,})
```

### 2.通用视图

#### 2.1 ListView

注意：自己app下的视图必须使用自己app下的models的数据库，不然会报错。

```
# 案例：学生列表修改成listview
```

```
class StudentListView(ListView):
    section = '学生列表'
    template_name = 'test1/student_list.html'
    model = Student
    context_object_name = 'students' #正常为object_list 这里可以改名

    paginate_by = 3#每页展示条数


    #第一步优化：过滤+搜索

    section = '学生列表'

    #查询功能
    def get_queryset(self): #过滤
        search = self.request.GET.get('search','').strip()#最后的是去除两边的空格
        per_page = self.request.GET.get('per_page', 10)
        self.paginate_by = int(per_page)
        if search:
            if search.isdigit():#如果是数字查看是qq还是电话
                sts = Student.objects.filter(Q(qq=search)|Q(phone=search), is_delete=False)
            else:
                sts=Student.objects.filter(name=search)
        else:#如果没有查询内容，返回全部
            sts = Student.objects.filter(is_delete=False)

        students = sts.order_by('-c_time')  # 排序
        self.students = students

        return students

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) #注意继承父类
        context['section'] = self.section
        context['per_page'] = self.paginate_by
        context['total_page'] = math.ceil(self.students.count()/int(context['per_page']))
        context['page'] = self.request.GET.get('page',1)
        return context
```

#### 2.2 detailView

展示具体某个对象

```
#学生详情修改成datailView
```

```
class StudentDetailView(DetailView):
    section = '学生详情'
    template_name = 'test1/student_detail.html'
    model = Student #模型

    context_object_name = 'student' #改名

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) #注意继承父类
        context['section'] = self.section
        return context
```

#### 2.3.类装饰器

##### 1.直接在url配置部分

```
    # path('student_list/', views.StudentListView.as_view(),name = 'student_list'),
    path('student_list/', login_required(views.StudentListView.as_view()),name = 'student_list'),      
```

##### 2.装饰类

    from django.utils.decorators import method_decorator
    from django.contrib.auth.decorators import login_required
    
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( *args, **kwargs)
##### 3：直接

```
@method_decorator(login_required, name='dispatch')
class StudentListView(ListView):
	······
```