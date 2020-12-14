#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/8/2 22:09

from queue import Queue

my_queue = Queue(3)

if __name__ == '__main__':
    my_queue.put(1)
    print(my_queue.qsize())
    my_queue.get()
    print(my_queue.qsize())
    print(my_queue.empty())
    my_queue.put(1)
    my_queue.put(1)
    my_queue.put(1)
    print(my_queue.full())
    my_queue.task_done()    # 任务结束
    my_queue.task_done()    # 任务结束
    my_queue.task_done()    # 任务结束
    my_queue.task_done()    # 任务结束
    my_queue.join()  # 等待完成，用来判断task_done的次数是否和put的次数一致
    print("任务结束")
