#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/8/2 21:59

from threading import Thread
from queue import Queue
from random import randint

my_queue = Queue(10)    # 创建队列对象，指定队列长度


def my_put(my_queue):
    """往队列塞东西"""
    for x in range(10):
        num = randint(0, 1000)
        my_queue.put(num)


def my_get(my_queue):
    """往队列拿东西"""
    for y in range(3):
        num = my_queue.get()
        print(num)


p = Thread(target=my_put, args=(my_queue,))
g = Thread(target=my_get, args=(my_queue,))
p.start()
g.start()
p.join()
g.join()

