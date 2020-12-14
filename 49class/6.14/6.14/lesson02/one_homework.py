#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/14 20:05

# 1.定义讲过的每种数字类型并实现相互之间的转换
# 初始化变量
a = 5
b = 2.3
c = 4 + 3j
d = '5'

# 转换成整数int
e = int(b)
# print(c.real)
# print(c.imag)
f = int(d)

# 转换成浮点数float
g = float(a)
h = float(d)

# 转换成复数complex
complex(a)
complex(b)
complex(d)
complex(a, b)
complex(b, a)

# 2.有一个时间形式(eg: 20180929),要求从这个格式中得到年、月、日
s = '20190614'
year = s[0:4]
mon = s[4:6]
day = s[6:]

s1 = s[:2]
