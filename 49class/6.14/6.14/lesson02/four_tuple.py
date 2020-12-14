#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/14 21:48

# tuple元组是有序的不可变的元素集合 。
# 变量初始化：元素可以是任何类型的数据
a = ()  # 空元组
b = (1, False, 'ab', [], ())
print('a的类型是：', type(a))    # a的类型是： <class 'tuple'>
print('b的类型是：', type(b))    # a的类型是： <class 'tuple'>

# 注意：单元素元组要注意，带上‘，’
f = ('hello')
g = ('hell0',)
print('f的类型是：', type(f))    # f的类型是： <class 'str'>
print('g的类型是：', type(g))    # g的类型是： <class 'tuple'>

# 索引
T = ('a', 'b', 'c')
print(T[1])  # 通过索引去取值

# T.index(value, [start, [stop]]) -> integer
print(T.index('b'))  # 通过值去获取索引

# T.count(value) -> integer
print(T.count('b'))

# 长度len()
print(len(T))

# 切片
print(T[1:])
print(T[-2:])

# 包含
T = ('a', 'b', 'c')
a = 'c'
b = 'w'

print(a in T)
print(b in T)


