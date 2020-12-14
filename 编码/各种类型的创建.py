#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/17 22:13

# list/tuple/dict/set
# list:有序、可变、允许重复的
# tuple:有序、不可变、允许重复的
# dict:无序、可变、key必须是唯一
# set:无序、重要的应用去重

# 数据类型的创建
# 1.int
n = 122
n = int('122')
print(type(n))

# id:查看变量的内存地址
print(id(n))    # 1964884832
# 为了优化内存，对于-5--257范围内值，不同变量是共用一个内存地址的

n = 122
n1 = int(122)
n2 = 122
print(id(n))
print(id(n1))
print(id(n2))

# str
# 创建方法
s = ""
s = str()
s = "fei"
s = str('fei')

print(type(s))

# 补充：
# 1.取消转义
print('after\\noon')
print(r'after\noon')
print('\n')
# 2.+
s1 = "a"
s2 = "b"
s3 = s1 + s2
print(s3)
print("1:" + s3)
print("1:", s3)

print("="*20)

# list
# 创建
li = []
li = list()
li = [1, 2, 3, 4]
li = list([1, 2, 3, 4])

# 转换
name = '托马斯'
l1 = list(name)
print(l1)

# tuple
# 创建
t = ()
t = tuple()
t = tuple([1, 2])

t = (11, 22, ['fei', {'k1': 'v1'}])
print(type(t))

# dict
# 创建方法
a = {}
a = dict(k1=123, k2=456, k3='v3')
print(a)

# 集合
s = set()
s = {1, 2, 3}
l = list(s)
print(l)

