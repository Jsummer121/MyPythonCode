#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/28 22:47

# type():查看数据类型
# isinstance():判断数据类型
a = "hello"
# 运行前时间
print(type(a))
# 运行后的时间

# 运行前时间
print(isinstance(a, str))
# 运行后的时间

# 获取当前时间
from datetime import datetime
time = datetime.now()
print(time)

