#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/18 21:59

print(type("ffff"))
print(type(b"ffff"))
# bytes是byte的序列，字符串是字符的序列
# str---》bytes
s1 = "中"
b1 = s1.encode('utf-8')
print(b1)
# bytes--->str
s2 = b1.decode("utf-8")
print(s2)

# 拓展
# str---》bytes
s = '托马斯'
b1 = bytes(s, encoding='utf-8')
b2 = bytes(s, encoding='GBK')
print(b1)
print(b2)

# bytes--->str
s1 = str(b1, encoding='utf-8')
s2 = str(b2, encoding='gbk')
print(s1)
print(s2)

# bytearray
s1 = "你好，朦胧"
b1 = bytearray(s1.encode('utf-8'))
print(b1)
print(type(b1))

print(b1.decode('utf-8'))

b1[:6] = bytearray("美丽", encoding="utf-8")
print(b1)
print(b1.decode('utf-8'))

