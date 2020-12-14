#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/24 19:57

# 函数， 排序， 参数决定正序还是反序
# 1.列表方法：li.sort(reverse=)/li.reverse(),修改列表本身
# 2.内置函数：sorted(reverse=)/reversed()，返回一个新的列表

li = [1, 8, 2, 5, 3]
a = sorted(li, reverse=False)  # 正序
b = sorted(li, reverse=True)    # 逆序

print(a, b)


# def my_sorted(*args, reversed):
#     a = sorted(*args, reverse=reversed)
#     print("a:", a)
#
#
# my_sorted([1, 8, 2, 5, 3], reversed=False)

def my_sorted(*args, reversed=0):  # 不传或者输入0表示正序，如果为1逆序
    if reversed == 0:
        a = sorted(*args, reverse=False)
        print("a:", a)
    elif reversed == 1:
        b = sorted(*args, reverse=True)
        print("b:", b)
    else:
        print('输入有误！')


my_sorted([1, 8, 2, 5, 3], reversed=0)
my_sorted([1, 8, 2, 5, 3], reversed=1)

li = input("请输入用逗号隔开的数字：")
print(li)
li = li.split(",")
print(li)

