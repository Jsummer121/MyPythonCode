#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/14 21:04

# 列表list
# 变量的初始化
a = []  # 空列表
b = [1, True, 'abc', []]
print('a的类型是：', type(a))    # a的类型是： <class 'list'>
print('b的类型是：', type(b))    # a的类型是： <class 'list'>

# 索引
L = ['a', 'b', 'c']
print(L[0])
print(L[-3])
# 列表是有序的可变的元素集合 。
L[0] = 'w'
print(L[0])
print(L)
print("="*20)
S = 'abc'
# print(S[0])
# S[0] = 'w'
# print(S[0])
# print(S)

# 长度len()
print(len(L))

# 切片
L = ['a', 'b', 'c']
print(L[:2])
print(L[-3:-1])

# 排序sort
# L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
L = ['a', 'c', 'b']
L.sort()
print("正序1：", L)
L.sort(reverse=True)    # 逆序
print("2:", L)
L.reverse()
print("3:", L)
print("="*20)
# 增删改查
# 增
L = ['a', 'b', 'c']
# 追加：append、
# 批量追加：extend
# 插入：insert
L.append('d')
print(L)

L2 = [1, 2, 3]
L.extend(L2)
print(L)

L.insert(1, 'w')
print(L)

# 删除
# 删一个尾巴,并且该尾巴可以赋值给另一个变量：pop
# 移除左边起第一个指定的元素：remove
# 删除指定索引元素：del
# 清空：clear
a = L.pop()
print(a)
print(L)

L.append('w')
print(L)
L.remove('w')
print(L)

del(L[1])
print(L)

L.clear()
print(L)

# 包含in
L = ['a', 'b', 'c']
a = 'c'
b = 'd'

print(a in L)   # True
print(b in L)   # False


