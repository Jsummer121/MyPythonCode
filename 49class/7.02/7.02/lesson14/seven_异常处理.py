#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/2 22:02

#   1.一旦发生异常，程序终止
# print("one")
# aaa
# print("two")

# 2.处理
print("one")
try:
    aaa
except:
    print("three")
print("two")

# try和except与if和else相似，但if和else可以不要else，try和except必须成对出现
# 基本用法：
"""
先执行try里面的代码，try不满足条件，捕获异常，执行except里面的代码
先执行try里面的代码，try满足条件，直接执行try里面的代码，不再执行except里面的代码
"""

# 巩固
# f = open("haha.py", "r")    # 当文件不存在时，会报错FileNotFoundError: [Errno 2] No such file or directory: 'haha.py'

try:
    f = open("haha.py", "r")
except:
    print('发生了异常')

# 1/0  # ZeroDivisionError: division by zero
try:
    1 / 0
except:
    print("发生了异常")

# 拓展：捕获具体的异常

try:
    # f = open("haha.py", "r")
    aaa
except ZeroDivisionError:
    print("分母为零了")
except FileNotFoundError:
    print('文件不存在')
except Exception as e:
    print(e)    # name 'aaa' is not defined

try:
    1 / 0
except ZeroDivisionError:
    print("分母为零了")

# 捕获具体异常：让你捕获你想要捕获的异常


# 自动抛出异常
# raise
# def func(name):
#     if name == '胡涛':
#         raise TypeError("黑名单用户，拒绝访问")
#
#
# func("胡涛")

try:
    # raise TypeError("主动抛出的类型错误")    # 自制异常
    a = 5
except ZeroDivisionError:
    print("分母为零了")
except FileNotFoundError:
    print('文件不存在')
except Exception as e:
    print(e)
else:
    print("try里的代码无异常，正常执行后执行else")
finally:
    print("代码不管是否正常执行，最后都会执行finally")

