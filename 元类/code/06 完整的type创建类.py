# -*- coding: utf-8 -*-
# @Author  : summer


class A(object):
    num = 100


def print_b(self):
    print(self.num)


@staticmethod
def print_static():
    print("----haha-----")


@classmethod
def print_class(cls):
    print(cls.num)


B = type("B", (A,), {"print_b": print_b, "print_static": print_static, "print_class": print_class})
b = B()
b.print_b()  # 100
b.print_static()  # ----haha----
b.print_class()  # 100
