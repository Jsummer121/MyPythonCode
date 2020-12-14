#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/8/2 20:49
from threading import Thread
import time


def f1(people):
    print("hello，{}".format(people))
    time.sleep(3)
    print("bye")


def f2():
    print("hi")
    time.sleep(3)
    print("goodbye")


if __name__ == '__main__':
    # 正常调用，是有先后顺序，主线程
    # f1()
    # f2()
    # 线程操作
    f1_thread = Thread(target=f1, args=("胡歌",), name='hello')  # 创建了一个线程实例
    f2_thread = Thread(target=f2, name='hi')   # 实例对象时，函数并未执行

    f1_thread.setName("dai")
    f1_thread.setName("hu")

    print("f1 name:", f1_thread.getName())
    print("f2 name:", f2_thread.getName())

    # f1_thread.setDaemon(True)
    # f2_thread.setDaemon(True)

    # f1_thread.start()   # 调用start方法才开始执行
    # f2_thread.start()

    # f1_thread.join()  # 阻塞调用，主线程进行等待
    # f2_thread.join()

    print("主线程执行完毕")

"""
主线程执行完毕了，但是子线程依然没有关闭，程序一直无法关闭
守护线程：主线程执行完毕后，程序就关闭
"""

