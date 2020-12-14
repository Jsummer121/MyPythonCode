#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/5 22:15
import re

# 字符组[]
# 预定义字符组
# \d == [0-9]
s = "<a href='asdf'>9874516846579845789456</a>"

r = re.findall("\d", s)
print(r)

r = re.findall("\d.*\d", s)
print(r)
# \D == [^0-9]
r = re.findall("\D", s)
print(r)

# \s:匹配任意的空白符:空格、换行（\n)、制表符（tab）
s = "j0ohqngkadij*+-/你 好\t\n_ajgoaenoigjarif"
r = re.findall('\s', s)
print(r)    # [' ', '\t', '\n']

# \w:匹配字母数字下划线汉字
s = "j0ohqngkadij*+-/你 好\t\n_ajgoaenoigjarif"
r = re.findall('\w', s)
print(r)

s = "email:123456@qq.com"
r = re.findall("\d+@\w+\.com$", s)
print(r)
