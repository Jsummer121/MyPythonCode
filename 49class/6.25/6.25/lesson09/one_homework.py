#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/25 19:40

# 定义一个函数，能够输入字典和元组。函数返回一个字典和元组，字典的value值和元组的值交换
"""
eg:
tu = ('fei', 18, 160)
di = {'name': 'sophia', 'age': 20, 'height': 165}
"""
# 变量初始化
tu = ('fei', 18, 160)
di = {'name': 'sophia', 'age': 20, 'height': 165}
# ====》
# tu = ('sophia', 20, 165)
# di = {'name': 'fei', 'age': 18, 'height': 160}
# 面向过程编程：
# zip
l1 = ["k1", "k2", "k3"]
l2 = ["v1", "v2", "v3"]
print(dict(zip(l1, l2)))    # {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
print(dict(zip(di.keys(), tu)))  # {'name': 'fei', 'age': 18, 'height': 160}
print(tuple(di.values()))   # ('sophia', 20, 165)


# 函数式编程
def func(tu, di):
    # print(dict(zip(di.keys(), tu)))  # {'name': 'fei', 'age': 18, 'height': 160}
    # print(tuple(di.values()))  # ('sophia', 20, 165)
    return dict(zip(di.keys(), tu)), tuple(di.values())


x, y = func(tu, di)
print(x)
print(y)


