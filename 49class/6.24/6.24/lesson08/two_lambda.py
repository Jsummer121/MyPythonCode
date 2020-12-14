#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/24 20:32


# 简单函数
# def f1(): # 不带参数
#     return 1213

# 等同于
f1 = lambda: 12123


res = f1()
print(res)


# def f2(a1, a2):   # 带参数
#     return a1 + a2

# 等同于
f2 = lambda a1, a2: a1 + a2


res = f2(5, 6)
print(res)

# filter(func, li)
li = [3, 15, 10, 5, 9, 8]


# def f1(x):
#     return x > 8
# f1 = lambda x: x > 8

print(list(filter(lambda x: x > 8, li)))


# 强化
# def test(a, b):
#     result = a + b
#     return result

test = lambda a, b: a + b


num = test(5, 6)
print(num)


def test(a, b, func):
    res = func(a, b)
    return res


num = test(5, 6, lambda a, b: a + b)
print("加法：", num)
num = test(5, 6, lambda a, b: a - b)
print("减法：", num)

# 实现匿名函数的输入
# func = input("请输入一个匿名函数：")
# print(func)
# print(type(func))
# eval:返回值/exec：没有返回值
# func = eval(func)
# num = test(11, 22, func)
# print(num)

# 实现输入函数循环执行
while True:
    flag = input("继续吗？如果继续请输入y，其他结束")
    if flag.lower() == 'y':
        func = input("请输入一个匿名函数：")
        func = eval(func)
        num = test(11, 22, func)
        print(num)
    else:
        print("结束运行")
        break
