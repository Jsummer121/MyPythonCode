#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/8/1 20:36

# import datetime
#
# res = datetime.date(2019, 8, 1)
# print(res)  # 年月日
# print(type(res))    # <class 'datetime.date'>   日期对象
#
# res = datetime.time(8, 43, 55, 1)   # 时分秒毫秒
# print(res)  # 08:43:55.000001
# print(type(res))    # <class 'datetime.time'> 时间对象
#
# res = datetime.datetime.now()
# print(res)  # 2019-08-01 20:45:22.283372

from datetime import datetime

# 通常用法
now = datetime.now()    # 对象
print(now)
print(now.date())   # 2019-08-01
print(now.time())   # 20:51:13.033755

# 时间戳：格林威治时间70.1.1 0:0:0
res = now.timestamp()
print(res)  # 1564664260.634484

# 时间戳转换为日期时间
res = datetime.fromtimestamp(res)
print(res)  # 2019-08-01 20:57:40.634484

# 2019年08月01日 21:02
# strftime(format)
res = now.strftime("%Y年%m月%d日 %H:%M:%S")    # Y:2019;y:19;H:24小时;I:12小时;
print(res)  # 2019年08月01日 21:07:40

# 字符串转日期时间对象strptime
s = '01 Aug 2019 21:28:32 GMT'
t = datetime.strptime(s, '%d %b %Y %H:%M:%S GMT')
print(t)    # 2019-08-01 21:28:32

# timedelta
import datetime

now = datetime.datetime.now()
res = datetime.datetime.fromtimestamp(1564666398.565904)

t = now - res
print(t)    # 0:03:13.798104
print(type(t))  # <class 'datetime.timedelta'>

now = datetime.datetime.now()
td = datetime.timedelta(hours=3, minutes=56, seconds=26)
print(now - td)     # 2019-08-01 17:42:54.113623
print(now + td)     # 2019-08-02 01:35:46.113623

