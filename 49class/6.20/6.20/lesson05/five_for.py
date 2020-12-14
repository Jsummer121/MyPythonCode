#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/20 21:52

# 遍历
# for主要应用在遍历
# 列表的遍历
li = [1, 3, 5, 7, 9]
for i in li:
    print(i)

print("="*20)
# 元组的遍历
tu = (1, 3, 5, 7, 9)
for i in tu:
    print(i)

print("="*20)
# 集合
se = {'k1', 'k2', 'k3'}
for i in se:
    print(i)

# 字典
dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
for k, v in dic.items():
    print(k, v)

print("="*20)
li = [1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1]
for i in li:
    # li.append(i)
    print(i)
# 如果是可变对象，一定不要再循环的往里面插入东西

# 怎么判断一个对象是不是可迭代对象：1.直接放到for里面2.如果一个对象有'__iter__'方法，它就是可迭代的

print(dir(li))
"""
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

"""

# range()
# li.append("a")
# del(li[2])
#    range(stop) -> range object
#    range(start, stop[, step]) -> range object
# 表示的是一个范围

print(list(range(5)))   # [0, 1, 2, 3, 4]
print(list(range(1, 5)))   # [1, 2, 3, 4]
print(list(range(1, 5, 2)))   # [1, 3]

# for i in range(1, 21):
#     print(i)

# 跳出循环
for i in range(1, 21):
    if i % 5 == 0:
        break   # 跳出整个循环，程序终止
        # continue    # 跳出当前循环，进入下一次循环
    print(i)
else:
    print("----end----")

# for break/continue/else 同while
