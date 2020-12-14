#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/14 20:32

# 字符串
s = 'hello.TZ'
print(s[2:5])
print(s[-6:-3])  # 从头往后切
print(s[5:2])   # 不能交叉取值
print(s[0])
print(s[-8])

print(s[0:5:1])
print(s[0:5:2])

print(s[::-1])
print(s[::-2])

# 移除空白strip() left right
# S.strip([chars]) -> str
s1 = " hello,TZ "
s = 'hello.TZ'
print(s)
print(s1)
print(s1.strip())   # 移除两端空格
print(s1.lstrip())   # 移除左端空格
print(s1.rstrip())   # 移除右端空格
print(s.strip("Z"))  # 移除两端指定的字符

# 分割split
# S.split(sep=None, maxsplit=-1) -> list of strings
s = 'hello,TZ'
print(s.split(','))  # ['hello', 'TZ']
print(s.split())    # ['hello,TZ']
print(s.split("l", 1))    # ['he', 'lo,TZ']
print(s.split("l", 2))    # ['he', '', 'o,TZ']

# eval()    # 识别表达式，返回值
b = '1 + 2 + 3'
print(eval(b))

# exec()  # 识别赋值语句，没有返回值
b = 'x + y + z'
x = 1
y = 2
z = 3
print(eval(b))

s = """
z = 10
b = x + y + z
print(b)
print("ok")
"""
# x = 1
# y = 2
# exec(s)
# exec(s, {'x': 1, 'y': 2})
exec(s, {'x': 1, 'y': 2}, {'x': 5, 'y': 6})

# filter() 过滤器
# i = filter(函数，可迭代对象)
# 过滤，每个可迭代对象去执行函数，符合条件的留下，不符合的删去

