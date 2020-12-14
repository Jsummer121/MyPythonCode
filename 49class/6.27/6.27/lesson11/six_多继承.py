#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/27 21:41


# class A:
#     def run(self):
#         print("happy")
#
#
# class D:
#     def run(self):
#         print("happy")
#
#
# class B:
#     def eat(self):
#         print("miaomiaomiao")
#
#
# class C(D, B):
#     def run(self):
#         D.run(self)
#         print("fly")
#
#
# c = C()
# c.run()

class A(object):
    def run(self):
        print("happy")


class B:
    def eat(self):
        print("miaomiaomiao")


class C(A, B):
    def run(self):
        super().run()   # super函数可以调用父类的方法，
        print("fly")


c = C()
c.run()
print(C.mro())  # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]获取全部的继承关系
print(C.__bases__)  # (<class '__main__.A'>, <class '__main__.B'>) 查看继承的全部父类
print(C.__base__)  # <class '__main__.A'> 查看继承的第一个父类



