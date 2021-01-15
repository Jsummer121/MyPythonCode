# 一、datetime

datetime是python处理时间和日期的标准库，有四个类：

-   date:年月日
-   time：时分秒毫秒
-   datetime：年月日时分秒毫秒
-   timedelta(时间间隔)

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

# 