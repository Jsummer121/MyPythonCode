#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/25 20:33

# 面向过程编程：程序按照流程一步步往下走
tu = ('fei', 18, 160)
di = {'name': 'sophia', 'age': 20, 'height': 165}

print(dict(zip(di.keys(), tu)))  # {'name': 'fei', 'age': 18, 'height': 160}
print(tuple(di.values()))   # ('sophia', 20, 165)


# 面向函数编程：将不同的功能设置成不同的函数，在需要的时候随时调用
def func(tu, di):
    return dict(zip(di.keys(), tu)), tuple(di.values())


x, y = func(tu, di)
print(x)
print(y)

# 面向对象编程：类
# 一切事物皆为对象
# 面向对象最重要的概念是类（class）和实例（instance）


class Cat:
    """这是一个猫类"""

# class 关键字
# Cat 类名 大驼峰命名法
# """这是一个猫类""" 解释类的用途


# 实例化对象
orange = Cat()

# 总结
"""
python中一切皆对象
新建一个对象的过程就叫做实例化。而对象是这个类的实例
"""

