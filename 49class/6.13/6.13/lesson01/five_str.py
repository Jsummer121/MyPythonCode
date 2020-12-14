#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/13 21:58

# 字符串str
# 变量初始化
a = '你好'
b = "hello,world"
c = '''hello,TZ'''
d = """hello,FF"""
e = """
    红豆生南国，
    春来发几枝？
    愿君多采撷，
    此物最相思。
    """
f = '''
    床前明月光，
    疑是地上霜。
    举头望明月，
    低头思故乡。
    '''

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)
print("f:", f)
print('a的数据类型：', type(a))
print(b.capitalize())
print(a.center(20, '*'))
# S.count(sub[, start[, end]]) -> int
b = "hello,world"
print(b.count("l"))     # 3
print(b.count('l', 3))  # 2
print(b.count('l', 3, 8))   # 1
