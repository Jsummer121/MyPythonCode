#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/2 20:53
from datetime import datetime


# with ---->__enter__和__exit__
class RunTime:
    def __enter__(self):
        print("进来了")
        self.start_time = datetime.now()
        print(self.start_time)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = datetime.now()
        print(self.end_time)
        print("出去了")
        print("运行时间：{}".format(self.end_time - self.start_time))


run = RunTime()

with run as a:  # 上下文管理器
    print("我是type")
    for i in range(100000):
        type("hello")
