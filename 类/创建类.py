#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/25 20:55


class Cat:
    """这是一个猫类"""
    pass


kitty = Cat()
# 句点法给实例赋值属性
kitty.color = 'white'
kitty.eat = 'milk'

print(kitty)
print(kitty.color)  # kitty.color:找到kitty所应用的对象，并获取color属性值

orange = Cat()
# __   __
# __init__, 实例化之后自动被调用,完成实例的初始化


class Cat:
    """这是一个猫类"""
    def __init__(self, color, eat):
        self.color = color  # 实例属性：记录是具体对象的特征
        self.eat = eat
        print("内部调用：", self.color)   # 内部调用：需要加上self


kitty = Cat('white', 'milk')    # kitty, 'white', 'milk'
print(kitty.color)

orange = Cat('orange', 'food')  # orange, 'orange', 'food'
print(orange.eat)   # 外部调用：实例名.属性


# 类属性：记录与类相关的特征
# 在__init__外初始化的
class Cat:
    """这是一个猫类"""
    count = 0   # 类属性

    def __init__(self, color, eat):
        self.color = color  # 实例属性：记录是具体对象的特征
        self.eat = eat
        # 计数
        Cat.count += 1  # 内部调用：类名.类属性名


# 实例化对象
kitty = Cat('white', 'milk')
orange = Cat('orange', 'food')
hua = Cat('hua', 'fish')

# 输出创建对象的个数
print("现在创建了{}只猫".format(Cat.count))    # 外部调用：类名.类属性名
print(kitty.count)  # 外部调用：实例名.类属性名


# 总结
"""
实例可以访问实例属性，实例可以访问类属性
类只能访问类属性
"""

# 3.私有属性
# a.单下划线开头：只是告诉别人这是私有属性，外部依然可以访问更改
# b.双下划线开头：外部不能通过实例名(instancename).属性名(propetyname)来访问或者更改


class Cat:
    def __init__(self, color, eat):
        self._color = color
        self.__eat = eat


kitty = Cat('white', 'milk')
print(kitty._color)
# print(kitty.__eat)


