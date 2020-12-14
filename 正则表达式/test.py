#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/6 20:30
import re
# 正则的常用函数
# 1.re.findall(pattern, string, flags=0):将匹配的全部内容放入一个列表中
s = 'Cats are Cat'

r1 = re.findall("C\w+", s)
r2 = re.findall("(C\w+)", s)
r3 = re.findall("C(\w+)", s)
r4 = re.findall("(C)(\w+)", s)
print(r1)   # ['Cats', 'Cat']
print(r2)   # ['Cats', 'Cat']
print(r3)   # ['ats', 'at']
print(r4)   # [('C', 'ats'), ('C', 'at')]

# 2.re.match(pattern, string, flags=0):从头匹配（只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败返回None）
s = 'Cats are Cat'

r = re.match("C\w+", s)
# print(r)    # None
print(r.group())    # Cats

r1 = re.match("(C)(\w+)", s)
print(r1.group())    # Cats获取匹配到的结果
print(r1.groups())    # ('C', 'ats') 获取匹配到的分组结果

# 3.re.search(pattern, string, flags=0):浏览全部字符串，匹配第一个符合规则的字符串
s = 'Cats are Cat'

r = re.search("C\w+", s)
print(r.group())    # Cats

s1 = 'cats are Cat Cats Catt'
r1 = re.search("C\w+", s1)
print(r1.group())   # Cat

r2 = re.search("(C)(\w+)", s1)
print(r2.group())   # Cat
print(r2.groups())  # ('C', 'at')
