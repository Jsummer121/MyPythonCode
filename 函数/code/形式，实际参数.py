#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/21 21:02


def sum(y, a, b, c=666):   # a, b, c形式参数，简称形参，函数没有调用时，它没有任何意义，调用时，它必须传入参数，所以也叫必须参数。
    result = y + a + b + c
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print(result)


"""
def sum(a, b, c=666):   # c=666默认参数，不传入实参时，形参默认为666，但是，你如果传入实参，它也能接收
# 注意：默认参数一定要写在必须参数的后面，语法规则
"""

sum(1,11,22)
sum(25, b=11, c=22, a=33)  # 11, 22, 33实际参数，简称实参，按照位置，与形参一一对应，所以它也叫位置参数

"""
sum(b=11, c=22, a=33)   # b=11, c=22, a=33关键字参数，函数参数会通过关键字去找，不需要一一对应
# 注意：关键字参数和位置参数一起使用时，关键字参数必须要写在位置参数的后面，这是语法
"""


