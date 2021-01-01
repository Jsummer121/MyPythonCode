# -*- coding: utf-8 -*-
class Foo(object):
    def __init__(self, name):
        self.name = name

    def ord_func(self):
        """ 定义实例方法，至少有一个self参数 """
        # print(self.name)
        print('实例方法')

    @classmethod
    def class_func(cls):
        """ 定义类方法，至少有一个cls参数 """
        print('类方法')

    @staticmethod
    def static_func():
        """ 定义静态方法 ，无默认参数"""
        print('静态方法')


f = Foo("中国")
# 调用实例方法
f.ord_func()

# 调用类方法
Foo.class_func()

# 调用静态方法
Foo.static_func()
