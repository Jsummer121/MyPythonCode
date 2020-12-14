#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/28 20:55


# 定制属性访问(增删改查）
# 1.属性访问
class Rectangle:    # 矩形类：正方形、长方形
    def __init__(self, length, width):  # __init__实例化对象时自动调用
        self.length = length
        self.width = width

    def area(self):
        areas = self.length * self.width
        return "面积是：{}".format(areas)


one = Rectangle(66, 88)

# 对象属性的增删改查
# 增
# one.num = 1
# setattr(one, "num", 2)
# 魔术方法给了我们一个自定义的接口，函数的执行底层其实就是去调用了魔术方法。
one.__setattr__("num", 3)
print(one.num)

# 查
print(hasattr(one, 'num'))  # 是否有该属性，返回布尔值
print(getattr(one, 'num'))  # 获取属性值
print(one.__getattribute__("num"))  # 获取属性值

# 改
# setattr(one, 'num1', 66)    # 无则增
# setattr(one, 'num', 88)    # 有则改
one.__setattr__("num2", 55)  # 无则增,有则改
one.__setattr__("num", 66)
print(one.num)
print(one.num2)

# 删
print(hasattr(one, "num2"))
# del one.num
# delattr(one, "num2")
one.__delattr__("num2")
print(hasattr(one, "num2"))


# 2.自定义
class Rectangle:    # 矩形类：正方形、长方形
    def __init__(self, length, width):  # __init__实例化对象时自动调用
        self.length = length
        self.width = width

    def __getattr__(self, item):
        return "no attribute"   # 当属性不存在时，调用此方法，如果没有定义此方法报错

    def area(self):
        areas = self.length * self.width
        return "面积是：{}".format(areas)


a = Rectangle(66, 88)
print("有属性：", a.length)
print(a.num)
