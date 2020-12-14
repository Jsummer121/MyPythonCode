#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/3 20:04


# 十进制：逢十进一
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
# 二进制：逢二进一
# 0, 1, 10, 11, 100, 101, 110, 111, 1001
# 八进制：逢八进一
# 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20

# 1.题目：分析已知条件，需要实现的功能
# 2.找到对应的方法，去把功能实现
from datetime import datetime

start = datetime.now()
print(type("hello"))
end = datetime.now()

start1 = datetime.now()
print(isinstance("hello", str))
end1 = datetime.now()

if end-start > end1-start1:
    print("type慢")
else:
    print("isinstance慢")


# 函数：代码复用
def func1():
    start = datetime.now()
    print(type("hello"))
    end = datetime.now()
    total = end - start
    return total


def func2():
    start1 = datetime.now()
    print(isinstance("hello", str))
    end1 = datetime.now()
    total = end1 - start1
    return total


if __name__ == '__main__':
    res1 = func1()
    res2 = func2()
    if res1 > res2:
        print("type慢")
    else:
        print("isinstance慢")


import time


# 类:
class Test:
    def fun1(self):
        self.start = datetime.now()
        time.sleep(5)

    def fun2(self):
        self.end = datetime.now()
        total = self.end - self.start
        print(total)



# res = fun1()
# fun2(res)   # 0:00:05.000609

