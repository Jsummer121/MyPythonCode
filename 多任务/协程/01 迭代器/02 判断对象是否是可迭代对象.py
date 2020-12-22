# -*- coding: utf-8 -*-
from collections import Iterable


# 判断列表是否是可迭代对象
print(isinstance([], Iterable))

# 判断字符串是否是可迭代对象
print(isinstance("", Iterable))


# 判断自己写的类创建的对象是否是可迭代对象
class MyList():
    def __init__(self):
        self.container = list()

    def add(self, val):
        self.container.append(val)


mylist = MyList()
print(isinstance(mylist, Iterable))

# 判断数字是否是可迭代对象
print(isinstance(100, Iterable))