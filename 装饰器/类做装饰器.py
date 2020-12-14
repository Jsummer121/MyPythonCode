#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/1 21:09


# def outer(func):
#     def inner(*args, **kwargs):
#         print("前增加")
#         func(*args, **kwargs)
#         print("后增")
#
#     return inner

class Test:
    """这是一个用来做装饰器的类"""
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("前增加")
        self.func(*args, **kwargs)
        print("后增")


# 类做装饰
@Test   # 实例化对象，Test(f)--->把下方函数作为参数传入
def f():
    print("你好")
# 1.把下方的函数名作为参数传入我们装饰器函数
# 2.把装饰器函数的内层函数名返回出来给下方的函数

# 1.Test(f)把下方的函数名作为参数传入我们装饰器类
# 2.把Test(f)---->f,此时f指向的是实例对象，实例对象的调用就是去调用call方法


f()


