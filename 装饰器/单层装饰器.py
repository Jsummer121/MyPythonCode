#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/28 21:54


# 装饰器
# 闭包：函数里面嵌套函数，外层函数返回内层函数的函数名
# 装饰器：本质就是闭包。
# 不修改原函数的前提下，方便的增加函数功能
def outer(func):
    def inner(*args, **kwargs):
        print("在原函数前增加新功能")
        func(*args, **kwargs)
        print("在原函数后增加新功能")
    return inner


@outer  # 表示：1.执行outer函数，并将其下方的函数名作为参数赋值给了out函数2.将outer函数的返回值重新赋值给了下方的函数
def f1():
    print("原功能块")


# f1 = outer(f1)
f1()


# 为了方便接收不同个数的参数，我们使用动态参数
@outer
def f2(a):
    print("功能2")
    print(a)


f2(5)


@outer
def f3(a, b):
    print("功能3")
    print(a, ",", b)


f3(6, 7)


@outer
def f100(a, b, c):
    print("功能100")
    print(a, ",", b, ",", c)


f100(7, 8, 9)
