#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/1 20:01

# 测试type和isinstance两个函数，哪个速度更加的快
# 测试type
# 测试isinstance
# 哪个速度更加的快
# 1.回忆
"""
type():查看数据类型
isinstance():判断数据类型
"""
# 2.使用
# print(type("hello"))
# print(isinstance("hello", str))

# 3.转函数
# a = "hello"


# def func1(a):
#     print(type(a))
#
#
# def func2(a):
#     print(isinstance(a, str))


# func1(a)
# func2(a)

# 4.调用装饰器，完成速度测试
from datetime import datetime


# 装饰器
def run_time(func):
    def new_func(*args, **kwargs):
        start_time = datetime.now()
        print('开始时间是：{}'.format(start_time))
        func(*args, **kwargs)
        end_time = datetime.now()
        print('结束时间是：{}'.format(end_time))
        total_time = end_time - start_time
        print('总共花费的时间是:{}'.format(total_time))
        return total_time
    return new_func


@run_time
def func1(a):
    for i in range(10000000):
        type(a)


@run_time
def func2(a):
    for i in range(10000000):
        isinstance(a, str)


if __name__ == '__main__':
    a = "hello"
    type_time = func1(a)
    is_time = func2(a)
    if type_time > is_time:
        print("isinstance 快")
    else:
        print("type 快")



