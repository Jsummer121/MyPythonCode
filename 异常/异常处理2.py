#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/3 20:43

try:
    # 1/0
    aaa
except ZeroDivisionError:
    print("分母不能为零哦")
except Exception as e:
    print("其他普通异常")
    print(e)
else:
    print("try里能够正常执行，才会执行else")
finally:
    print("最终都会执行此部分")


# 自定义异常类型
class ZiDingYiError(Exception):  # 普通异常的父类是Exception
    pass


def func(name):
    if name == '胡涛':
        print("允许登录")
    else:
        raise ZiDingYiError("你不是胡涛，不许登录！！！")


try:
    func("托马斯成")
except ZiDingYiError as e:
    print(e)

# 断言assert:自动抛错
a = 1
b = 2

print(a > b)    # False
print(b > a)    # True

# assert a > b    # 条件不满足抛出AssertionError
assert b > a    # 条件满足，正常往后执行代码


# 和raise比较
def func(name):
    if name == "张博文":
        raise TypeError("黑名单用户，拒绝访问")


func("薛乃毅")


# assert
def func1(name):
    assert name != "张博文"


func1("薛乃毅")


# print("ok")   #用来检查错误
# exit()