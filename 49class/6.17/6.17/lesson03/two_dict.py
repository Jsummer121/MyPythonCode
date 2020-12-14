#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/17 20:34

D = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3',
}
# dict
print(D.items())    # dict_items([('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3')])
print(D.keys())     # dict_keys(['k1', 'k2', 'k3'])
print(D.values())   # dict_values(['v1', 'v2', 'v3'])

# 获取值
# 第一种方法：通过key值去取value值
print(D['k1'])

D = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3',
}
# 第二种D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
# 通过给定的key查找对应的value值，如果给定的key在字典中，返回对应的value，如果不在，则默认返回None（如果设置了d，则返回d）
print("="*20)
print(D.get('k3'))
print(D.get('k4'))
print(D)
print(D.get('k4', 'false'))

# 第三种D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
# 通过给定的key查找对应的value值，如果给定的key在字典中，返回对应的value，如果不在,返回默认值，同时，在字典中增加了key：默认值的键值对（默认为None，如果设置了d，则使用d）
print("="*20)
print(D.setdefault("k3"))
print(D.setdefault("k4"))
print(D)
print(D.setdefault("k5", "v5"))
print(D)

# 增
# 第一种:通过key，key有则改，无则增
D = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3',
}
print("="*20)
print(D['k1'])
D['k1'] = 'w'
print(D['k1'])
D['k4'] = 'v4'
print(D)

# 第二种：setdefault(k[,d])
# key有获取，无则新增
print(D.setdefault("k3"))
print(D.setdefault("k5", "v5"))
print(D)

# 删
D = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3',
}
# pop:(获取并删除指定key值项)
# D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
# If key is not found, d is returned if given, otherwise KeyError is raised
a = D.pop('k2')
print(a)
print(D)

# popitem:获取并在字典中移除最后一项
b = D.popitem()
print(b)
print(D)

# clear(清空)
D.clear()
print(D)    # {}

