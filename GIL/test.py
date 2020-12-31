﻿from ctypes import *
from threading import Thread

# 加载动态库
lib = cdll.LoadLibrary("./loop.so")

# 创建一个子线程，让其执行c语言编写的函数，此函数是一个死循环
t = Thread(target=lib.test)
t.start()

# 主线程
while True:
    pass