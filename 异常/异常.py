#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/2 21:44

# 异常就是报错
# 异常处理
# 常见的报错信息
# a + 1   # NameError: name 'a' is not defined 变量未定义
# for i in range(5)：# SyntaxError: invalid character in identifier 语法错误
# 5 - "b"  # TypeError: unsupported operand type(s) for -: 'int' and 'str' 类型错误

# 自查和解决报错的能力
# 问题描述清楚的能力，掌握如何去提问


def a():
    aaa = 1


def b():
    a()


def c():
    b()


c()



