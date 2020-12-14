#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/28 22:26


# 多层装饰
def outer_0(func):
    def inner(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        print("end")
    return inner


def outer(func):
    def inner(*args, **kwargs):
        print("在原函数前增加新功能")
        func(*args, **kwargs)
        print("在原函数后增加新功能")
    return inner


@outer_0
@outer  # 表示：1.执行outer函数，并将其下方的函数名作为参数赋值给了out函数2.将outer函数的返回值重新赋值给了下方的函数
def f1():
    print("原功能块")


f1()
