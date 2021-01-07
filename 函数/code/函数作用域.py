#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/24 21:05

# 函数作用域
# 作用域？变量作用的范围
num = 100   # 全局变量


# global：在函数内部定义全局变量
def f():
    global num  # 定义全局变量，
    # num = 200
    num += 1
    print("1:", num)


print("2:", num)
f()
print("3:", num)


# nonlocal:函数嵌套时，作用在内层函数的变量，可以修改外层函数的变量
def f1():
    num = 66

    def f2():
        # num = 88
        nonlocal num
        num += 1
        print("1:", num)

    f2()
    print("2:", num)


f1()

# 总结：
"""
1.函数内部定义的为局部变量，其作用域是局部作用域，函数外无法调用的
2.函数外定义的为全局变量，其作用域是全局作用域，如果在函数内想要进行修改，需要global
3.外层函数的变量，如果想要在内层函数进行修改，需要nonlocal
"""