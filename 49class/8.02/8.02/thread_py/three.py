#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/8/2 21:35
from threading import Thread

a = 5


def f():
    print('我是子线程，我要修改全局的变量值')
    global a
    a = 2


if __name__ == '__main__':
    print('我是主线程，变量a的值是{}'.format(a))
    t = Thread(target=f)
    t.start()
    t.join()
    print('我是主线程，变量a的值是{}'.format(a))

# 全局变量被所有子线程共享的。资源竞争


