#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/8/2 22:18

from threading import Thread, current_thread
from queue import Queue
import time
from multiprocessing.pool import ThreadPool

# class ThreadPool(object):
#     def __init__(self, n):  # 参数n是可重复使用的线程数
#         # 生成一个队列，里面放任务
#         self.q = Queue(n)
#         # 生成线程
#         for i in range(n):
#             Thread(target=self.worker, daemon=True).start()
#
#     def worker(self):
#         """实现从队列里取任务完成"""
#         while True:  # 死循环，这样线程才会一直不结束，一直使用下去
#             func, args, kwargs = self.q.get()   # 从队列去取任务
#             func(*args, **kwargs)   # 运行刚得到的任务
#             self.q.task_done()  # 执行完，通知队列
#
#     def put_q(self, func, args=(), kwargs={}):
#         """实现往队列里放任务"""
#         self.q.put((func, args, kwargs))
#
#     def join_q(self):
#         self.q.join()   # 阻塞，等待完成


def task1():
    print('我是线程{}我正在执行task1'.format(current_thread().name))
    time.sleep(3)
    print('我是线程{}我执行task1完毕'.format(current_thread().name))


def task2(*args, **kwargs):
    print('我是线程{}我正在执行task2'.format(current_thread().name))
    print("我接收的参数是", args, kwargs)
    time.sleep(3)
    print('我是线程{}我执行task2完毕'.format(current_thread().name))


if __name__ == '__main__':
    pool = ThreadPool(2)
    # pool.put_q(task1)
    # pool.put_q(task2, args=(1, 2), kwargs={'a': 1, 'b': 2})
    pool.apply_async(task1)
    pool.apply_async(task2, args=(1, 2), kwds={'a': 1, 'b': 2})
    print('任务提交完成')
    # pool.terminate()    # 终止线程池，终止所有的任务
    pool.close()
    pool.join()
    # pool.join_q()
    print('所有任务完成')
