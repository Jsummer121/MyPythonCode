#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/20 20:57

# while循环
# a = 8
# if a > 5:
#     print('aaa')
# a = 8
# while a > 5:
#     print('aaa')

# 打印1到10所有数字
# i = 1
# print(i)
# i += 1
# print(i)
# i += 1
# print(i)
# i += 1
# print(i)
# i += 1
# print(i)

i = 1
while i <= 10:
    print(i)
    i += 1  # 没有i += 1就死循环

"""
while 条件：
    条件满足的时候执行的事情
    
先判断，再执行，执行完后再回到判断，直到判断条件不成立，运行结束    
"""

li = [1, 3, 5, 7, 9, 11, 2, 8]
# i = 0
# print(li[i])
# i += 1
# print(li[i])
# i += 1
# print(li[i])
# i += 1
# print(li[i])
print("="*20)
i = 0
# while i < len(li):
#     if li[i] > 5:
#         print(li[i])
#     else:
#         print(False)
#     i += 1

while i < len(li):
    print(li[i]) if li[i] > 5 else print(False)
    i += 1

a = ['hello', 'world', '!']
print(a[0], a[1], a[2])
print('----1----', end='**')
print('----2----', end='**')
print('----3----', end='**')
