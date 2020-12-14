# 一、datetime

是python处理时间和日期的标准库

有四个类：

date:年月日

time：时分秒毫秒

datetime：年月日时分秒毫秒

timedelta(时间间隔)

```
datetime.data(2019,8,0)->2019-8-1
类型为日期对象：class'datatime.date'

datetime.time(8,05,20,1)->08:05:20.000001

datetime.datetime.now()#打印当前时间

应为datetime其他类不怎么用所以导入时，直接导入from datetime import datetime

now = datetime.now()
now.time()
now.date()

常用方法：
1.获取当前日期时间：datetime.now()
2.日期转化为时间戳（从格林威治时间：70.1.1 0:0:0开始到现在所经过的秒数）：时间日期对象.timestamp()
now.timestamp()
时间戳转化为日期时间：datetime.fromtimestamp()

转化为中文strftime(format)
常用格式：
年 %Y/%y 2019/19
月 %m
日 %d
时 %H/%h 24h/12h
分 %M
秒 %s
now.strftime('%Y年%m月%d日 %H:%M:%s')

字符串转日期时间对象strptime
s = '01 Aug 2019 21:28:32'
datatime.strptime(s,'%d %b（月） %Y %H:%M%s GMT')
```

```
#timedelta
import datetime
now = datetime.datetime.now()
res = datetime.datetime.fromtimestamp(1412412515.124125)
t = now-res
t=0:01:14.2142141
type(time) datetime.timedelta

#主要作用，时差处理
td = datetime.timedelta(hours=3, minutes=16,seconds=26)
print(now+td)
```

# 二、logging

日志模块，开发者可以清楚地了解发生了哪些事件，包括出现了哪些错误。

```python
import logging
from datetime import datetime

now = datetime.now()
logging.info(now) 无
logging.warning(now) #WARNING:root:time

#logging可以把输出的信息分成多个级别
#设置级别，不然只能后面三个输出
logging.basicConfig(level=logging.DEBUG)#注意不要小写，level里面设置的是最低等级，高于这个等级就可以打印。

logging.debug(now)#最低级别
logging.info(now)
logging.warning(now)
logging.error(now)
logging.critical(now)#最高级别

等级作用：
DEBUG：
调试信息，通常在诊断问题时用得着
INFO：
普通信息，确认程序按照预期进行
WARNING：
警告信息，表示发生意想不到的事情，或者指示接下来，可能会出现一些问题，但是程序还是继续运行
ERROR：
错误信息，程序运行中出现一些问题，程序某些功能不能执行
CRITICAL：
危险信息，一个严重的错误，导致程序无法继续运行

Formatter格式
%(asctime)s 日志事件发生的事件
%(levelname)s 该日志记录的日志级别
%(message)s 日志记录的文本内容
%(name)s 所使用的的日志器名称，默认'root'
%(pathname)s 调用日志记录函数的文件的全路径
%(filename)s 条调用日志记录函数的文件
%(funcName)s 调用日志记录函数的函数名
%(lineno)d 调用日志记录函数的代码所在的行号

应用1：调试
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
a = 2 + 3
logging.debug(a)
b = a - 1
logging.debug(b)
c = b / 2
logging.debug(c)
d = c * 8
logging.debug(d)
e = d ** 2
print(e)

应用2：格式
注：如果有两个basicConfig只有第一次生效，第二次无效。
import logging
logging.basicConfig(filename='my.log'(将这些记录存到文件内),filemode='a'(追加默认）w（覆盖）,level=logging.DEBUG, fromat='时间：%(asctime)s 文件名：%(filename)s 行号：%(lineno)s')
a = 8 + 6
logging.debug(a)
```

## 模块化组件（了解）

loggers（日志记录器） 提供程序直接使用的接口

handlers（日志处理器）将记录的日志发送到指定位置

filters（日志过滤器） 用于过滤特定的日志记录

formatters（日志格式器） 用于控制日志信息的输出格式

```
import logging
#1.日志记录器(只需要1个)
my_logger = logging.Logger('第一个日志处理器')

#设置第一个handler
#2.日志处理器
fh = logging.FileHandler('you.log')
#3.设置级别+格式
fh.setLevel(logging.INFO)
fmt = logging.Fromatter('time:%(asctime)s - content:%(message)s') #日志各时器，给自己看的保存到文件里
fh.setFormatter(fmt)
#4.定义完毕，把handler添加到logger里面去
my_logger.addHandler(fh)

#设置第二个handler
sh = logging.StreamHandler()#定义
sh.setLevel(logging.DEBUG)#设置日志级别
fmt2 = logging.Formatter('time:%(asctime)s - content:%(message)s')#简单的东西给别人看的
sh.setFormatter(fmt2)
my_logger.addHandler(sh)

#设置完毕，开始使用
my_logger.info('我是ad发放')
```

