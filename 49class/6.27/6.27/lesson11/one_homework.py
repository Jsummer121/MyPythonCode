#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/27 19:52


# 定义个矩形类，有长和宽两个实例属性，还有一个计算面积的方法.
class Rectangle:
    def __init__(self, length, width):  # __init__实例化对象时自动调用
        self.length = length
        self.width = width

    def __test(self):
        print("私有方法")

    def area(self):
        areas = self.length * self.width
        self.__test()
        return areas
        # print(areas)


one = Rectangle(5, 6)
res = one.area()
# res += 1
# print(res)


