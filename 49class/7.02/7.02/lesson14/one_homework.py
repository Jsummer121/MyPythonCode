#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/2 19:53


# 测试type和isinstance两个函数，哪个速度更加的快(类装饰器）
# 1.r，rb：只读；w，wb:只写；a：追加；
# 2.r+，w+，a+：读写
from datetime import datetime


class RunTime:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = datetime.now()
        print('开始时间是：{}'.format(start_time))
        self.func(*args, **kwargs)
        end_time = datetime.now()
        print('结束时间是：{}'.format(end_time))
        total_time = end_time - start_time
        print('总共花费的时间是:{}'.format(total_time))
        return total_time


@RunTime    # 1.RunTime(func1)2.func1--->RunTime(func1)
def func1(a):
    for i in range(10000000):
        type(a)


@RunTime
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


class Cat:
    def __call__(self, *args, **kwargs):
        print("我是call方法，我可以实现类的实例对象的可调用")


kitty = Cat()
kitty()  # TypeError: 'Cat' object is not callable

