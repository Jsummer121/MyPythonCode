#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/17 21:02

# 一个包含唯一元素的可变和无序的集合数据类型
# 变量初始化,同列表类似，元素可以是任何数据类型(排除列表)
a = set()
print("a的数据类型是：", type(a))  # a的数据类型是： <class 'set'>
# 注 a = {} 是空字典
b = {1, 'a', ()}
print("b的数据类型是：", type(b))

# 添加（add、update）
SE = {1, 2, 3, 4, 5, 7, 8}
SE.add('hello')
print(SE)

# update:把要传入的元素拆分，作为个体传入到集合中
SE.update('hello')
print(SE)

# 删(remove/pop/discard)：
# remove:如果有，直接删除,如果无，报错
# pop:随机删除一个集合中的元素,如果集合没有元素报错
# discard：如果有，直接删除,如果无，不做任何操作
se = {1, 2, 3, 4, 5, 7, 8}
se.remove(4)
# se.remove(6)
print(se)

# pop
se.pop()
print(se)
# s1 = set()
# s1.pop()
# print(s1)

# discard
se = {1, 2, 3, 4, 5, 7, 8}
se.discard(4)
print(se)
se.discard(9)
print(se)

# 交集（&）
S1 = {1, 2, 5, 8, 10}
S2 = {2, 5, 10, 11, 15}

S3 = S1 & S2
print(S3)   # {2, 10, 5}

# 并集 |
S1 = {1, 2, 5, 8, 10}
S2 = {2, 5, 10, 11, 15}
# S3 = {1, 2, 5, 8, 10, 11, 15}
S4 = S1 | S2
print(S4)   # {1, 2, 5, 8, 10, 11, 15}

# 差集 -
S1 = {1, 2, 5, 8, 10}
S2 = {2, 5, 10, 11, 15}
S5 = S1 - S2    # {1, 8}
print(S5)

# 相对差集^
S1 = {1, 2, 5, 8, 10}
S2 = {2, 5, 10, 11, 15}
S6 = S1 ^ S2
print(S6)   # {1, 8, 11, 15}

# 去重
L = [1, 2, 3, 4, 5, 5, 4, 6, 3, 8, 9, 7]
T = (1, 2, 3, 4, 5, 5, 4, 6, 3, 8, 9, 7)
S1 = set(L)
print(S1)
L = list(S1)
print(L)
S2 = set(T)
print(tuple(S2))
