#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/1 20:35


# 类的定义和使用
class Cat:
    """这是一个猫类"""
    name = '猫'

    def __init__(self, color, eat):
        self.color = color
        self.eat = eat

    @property
    def print_cat(self):
        print("{}-{}".format(self.color, self.eat))

    @staticmethod   # 方法变静态方法，没有参数绑定
    def func():
        print("我来测试静态方法")
        print("我不需要self参数也能运行")
        print("我不需要实例化也能运行")

    @classmethod    # 类方法
    def func1(cls):  # cls代表类本身
    # def func1(self, cls):  # cls代表类本身
        print("="*50)
        print("我是来测试类方法的")
        print(cls)
        print(cls.name)


Cat.func()  # 解绑，不用实例化就可以调用方法。执行效率高
kitty = Cat('white', 'food')
print(kitty.color)
kitty.color = "hua"
print(kitty.color)
# kitty.print_cat()   # 调用类内方法的方式

# 1.property装饰器：方法变属性
# class、instance、property
# 使用起来方便，但是又不能随意去修改
kitty.print_cat

# 2.staticmethod装饰器：方法变静态方法，没有参数绑定
# 只在类本身生效
kitty.func()
Cat.func()

# 3.classmethod装饰器：方法变类方法
kitty.func1()
print("以下是类名.类方法")
Cat.func1()
# 属性：实例是可以调用实例属性、类属性，类只能调用类属性
# 方法：实例是可以调用类内方法、类方法，类只能调用类方法
# Cat.func1(kitty)

