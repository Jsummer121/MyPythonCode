# -*- coding: utf-8 -*-
from collections import Iterable


class MyList(object):
    def __init__(self):
        self.contant = list()

    def add(self, val):
        self.contant.append(val)

    def __iter__(self):
        """返回一个迭代器"""
        # 暂时这里我们先不写，即我们暂时忽略如何构造一个迭代器对象
        pass


mylist = MyList()
print(isinstance(mylist, Iterable))
# 这回测试发现添加了__iter__方法的mylist对象已经是一个可迭代对象了
