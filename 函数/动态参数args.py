#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/21 21:33

# 动态参数。
# def f1(*args, **kwargs):
"""
*args, **kwargs
星号是关键字
args，kwargs是变量名，规范
调用函数时，所有传入的 多余的 位置参数都会被args接收生成一个元组
调用函数时，所有传入的 多余的 关键字参数都会被kwargs接收生成一个字典
"""


def sum(a, *args):
    print(a)
    # result = 0
    print(args)
    print(type(args))   # <class 'tuple'>
    # for i in args:
    #     print(i)
    #     result += i
    # print("result:", result)
    # return result


# sum(5, 6, 7, 8, 9)

def sum1(f, **kwargs):
    print(f)
    print(kwargs)
    print(type(kwargs))


sum1(a=5, c=6, b=7, f=8, g=9)


# 第一种：
def f1(*args):
    print(args, type(args))


f1(123, 456)


# 第二种
def f2(**kwargs):
    print(kwargs, type(kwargs))


f2(k1=123, k2=456)


# 混合使用：
def f3(p, *args, **kwargs):
    print(p, type(p))
    print(args, type(args))
    print(kwargs, type(kwargs))


f3(11, 22, 33, k1=123, k2=456)


# 为动态参数传入列表、字典、元组
# 列表
def f1(*args):
    print(args, type(args))


li = [11, 22, 33]
f1(li, 233)  # ([11, 22, 33], 233) <class 'tuple'>
f1(*li, 233)  # (11, 22, 33, 233) <class 'tuple'>


def f2(**kwargs):
    print(kwargs, type(kwargs))  # {'k1': 123, 'k2': 456} <class 'dict'>


dic = {'k1': 123, 'k2': 456}
# f2(dic=dic)
f2(**dic)

# 形参，必须参数，默认参数，*args，**kwargs。实参，位置参数，关键字参数。

