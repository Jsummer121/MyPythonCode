#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/17 20:01

# 1.自定义一个字符串（eg：a = “hello,world!”），用切片的方式进行逆序
s = 'hello,world!'
print(s[2:5])
print(s[-10:-7])
# 索引、反向索引
# 切片从前往后切，不能交叉取值
# 逆序
print("逆序：", s[::-1])
# 逆序切片从后往前切，不能交叉取值
print("1:", s[4:1:-1])
print("2:", s[-8:-11:-1])

# 2.用多种方法往列表中增加值
L = ['a', 'b', 'c']

# append():追加
# extend():批量追加
L.append('d')
print(L)

L2 = ['q', 'w', 'e']
L.extend(L2)
print(L)

# 列表相加
L3 = L + L2
print(L3)

# insert：插入
L.insert(1, 'hello')
print(L)

