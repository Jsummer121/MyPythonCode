#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/13 22:24

# 索引取值
s = 'hello,TZ'
print(s[0])

# 长度len()
print(len(s))

# 切片
# 切片：变量[头下标：尾下标]，不包含尾下标（包头不包尾）
print(s[0:2])
print(s[1:4])
print('这里是：', s[4:1])   # 不能交叉取值
