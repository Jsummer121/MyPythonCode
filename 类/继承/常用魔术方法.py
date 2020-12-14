#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/27 22:03


# 魔术方法：
# 1.运算方法
class Test:
    """这是一个测试类"""
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        res = self.num + other.num
        print(res)
        # return res


a = Test(66)
b = Test(88)

a + b
# res = a + b #此时res的值为None
# print(res)


# 2.__str__和__repr__
class A:
    def __str__(self):
        return "你好"

    def __repr__(self):
        return "hello"


a = A()
print(a)    # <__main__.A object at 0x000001733935B978>


# 对象地址--->__str__--->__repr__


# __call__:让实例能够直接被调用
class B:
    """这是一个测试类"""
    def __init__(self, num):
        self.num = num
        self.eat = "food"
        self.run = "happy"

    def __call__(self, *args, **kwargs):
        print("ok")


b = B(66)
b()  # 直接调用会报错，想要直接调用，加上__call__

print(b.__class__)  # <class '__main__.B'> 查看类名
print(b.__dict__)   # {'num': 66}   查看全部的属性（属性和属性值的键值对）
print(b.__doc__)    # 这是一个测试类, 查看对象文档即类的注释部分


