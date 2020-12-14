# -*- coding: utf-8 -*-
from datetime import datetime


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