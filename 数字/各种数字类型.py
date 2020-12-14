#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/13 21:10

# 浮点数float
a = 0.0
print('a的类型是：', type(a))

b = 75.
print('b的类型是：', type(b))

c = -3.1415926
print('c的类型是：', type(c))

d = 9.8e-2
print('d的类型是：', type(d))

s = 0.1 + 0.2
print(s)    # 0.30000000000000004
print('s的类型是：', type(s))

# decimal 3.141592696532441*1.23456789
import decimal

a = decimal.Decimal(3.141592696532441)
b = decimal.Decimal(1.23456789)
decimal.getcontext().prec = 20  # 精确位数
print(a * b)    # 3.8785094665974659284

# 复数complex
a = 12.3 + 4j
print('a的数据类型是：', type(a))
print(a.real)
print(a.imag)
print('='*20)
# int、float、complex的相互转化
# 初始化数字类型
a = 2
b = 3.14
c = '2'     # 数字类型的字符串
print('a的类型是：', type(a))    # int
print('b的类型是：', type(b))    # float
print('c的类型是：', type(c))    # str

# 转换为整数
d = int(b)
e = int(c)
print(d)
print('d的类型是：', type(d))    # int
print(e)
print('e的类型是：', type(e))    # int

# 转换为浮点数
f = float(a)
g = float(c)
print(f)
print(g)

# 转换复数
a = 2
b = 3.14
c = '2'     # 数字类型的字符串

h = complex(a, b)   # 两个参数时，前后都不允许有字符串，否则报错
i = complex(b, a)
j = complex(c)  # 只有单个参数时，才可以使用字符串类型的数字
print(h)    # (2+3.14j)
print(i)    # (3.14+2j)
print(j)    # (2+0j)
print(type(h))

