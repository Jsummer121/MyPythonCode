#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/8/2 21:15
from threading import Thread
import time


# class MyThread(Thread):
#     def run(self):
#         print('hello')
#         time.sleep(3)
#         print('bye')
#
#
# my_thread = MyThread()  # 创建一个线程实例
# my_thread.start()

# 重写了类中run方法，通过start方法自动去调用类中的run方法

class MyThread(Thread):
    def __init__(self, people, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.people = people

    def run(self):
        print('hello，{}'.format(self.people))
        time.sleep(3)
        print('bye')


my_thread = MyThread("齐时久", name="hello")  # 创建一个线程实例
print(my_thread.getName())
my_thread.start()


