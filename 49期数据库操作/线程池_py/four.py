#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/8/2 21:42

from threading import Thread, Lock

data = 0


def add_1():
    global data
    lock.acquire()
    for i in range(1000000):
        data += 1
    lock.release()


def red_1():
    global data
    lock.acquire()
    for i in range(1000000):
        data -= 1
    lock.release()


if __name__ == '__main__':
    # 正常执行，结果为0
    # add_1()
    # red_1()
    # print(data)
    lock = Lock()
    # 线程操作
    t1 = Thread(target=add_1)
    t2 = Thread(target=red_1)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(data)

"""
data += 1
x = data + 1
data = x

data = 0
t1: x1 = data + 1 # x1 = 0 + 1 = 1
t2: x2 = data - 1 # x2 = 0 - 1 = -1
t1: data = x1 = 1
t2: data = x2 = -1

结果：data = -1
"""