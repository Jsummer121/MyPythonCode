#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/14 22:09

# dict字典是由键值对构成（key、value）的无序集合
# （不像字符串、列表和元祖那样有固定的位置）。
# 1，"a", ['ab', 2, 'c'], ('ab', 2, 'c')
# 姓名：xf， 密码：123456，。。。。。。。。。。。。。。
# {key: value}

# int/float/complex/bool/str/list/tuple/dict
# 初始化变量
# 字典key一般使用数字或者字符串，也可以使用元组， value可以使用任何类型的数据类型
a = {}  # 空字典
print('a的数据类型是：', type(a))  # a的数据类型是： <class 'dict'>
b = {
    1: 2,   # key:数字，value：数字
    'k1': 'v1',  # key:字符串， value：字符串
    False: True,
    'k2': [1, 2, 3],  # value:列表
    (1, 2, 3): (1, 2, 3),   # key: 元组， value：元组
    'k3': {                 # value: 字典
        'k2': 'v2',
        'k4': 'v9',
        'k5': {}
    },
}
print('b的数据类型是：', type(b))

# 常用功能
D = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3',
}

# D1 = {}
# L = [1, 2, 3]
# print(D1.fromkeys(L))
# print(D1.fromkeys(L, 'v'))
# 长度len()
print(len(D))

# 键、值、键值对
print(D.items())    # dict_items([('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3')])
print(D.keys())    # dict_keys(['k1', 'k2', 'k3'])
print(D.values())    # dict_values(['v1', 'v2', 'v3'])

