#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/28 21:31


# 描述符
class Test1:
    """这是一个测试类"""
    def __get__(self, instance, owner):
        return "__get__"

    def __set__(self, instance, value):
        print("__set__")

    def __delete__(self, instance):
        print("___delete__")
# a = Test1()


# 定义第二个类，在第二个类里实例化第一个类
class Test2:
    def __init__(self):
        self.name = "小薛"    # 实例属性

    girl = Test1()  # 上一个类的实例对象我拿来做了这一个类的类属性，这就是描述符


c = Test2()
print(c.name)
# 查
print(c.girl)  # 获取对象属性，会去第一个类里面执行__get__方法
c.girl = 'true'  # 改，会去第一个类里面执行__set__方法
del c.girl  # 删除，会去第一个类里面执行__delete__方法

# 类里面实例化另一个类，对这个实例做访问的时候，需要定义__get__,__set__,__delete__方法来实现属性的增删改查

