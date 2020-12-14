#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/20 20:30

# 程序三大执行流程：1.顺序执行 2.选择执行 3.循环执行
# 控制流程
print('----1-----')
print('----2-----')
print('----3-----')

# 2.选择执行
a = 5
if a > 3:
    print('a > 3')
elif a == 3:
    print('a == 3')
else:
    print('a < 3')
print('ok')

"""
if 条件1：
    条件1成立，需要做的事情
elif 条件2：
    条件2成立，需要做的事情   
elif 条件3：
    条件3成立，需要做的事情 
...
else:
    以上条件都不满足时，需要做的事情         
"""
age = 19

if age > 18:
    print("----0----")
    print("----1----")
    print("----2----")
    print("----3----")
    print("----4----")
    print("----5----")
print('----6----')

# 缩进代表的就是包含关系

# 拓展
# a = int(input('请输入你的年龄：'))   # input进来一定是一个字符串
# print(type(a))  # <class 'str'>
# if a <= 18:
#     print("少先队员")
# elif 40 > a > 18:
#     print('青少年')
# else:
#     print("成熟人士")

# 2.三目运算
a = 6
if a > 5:
    print(True)
else:
    print(False)

# 语法糖：三目运算、装饰器、lambda

a = 6
print(True) if a > 5 else print(False)
# 成立执行值1 if 判断语句 else 不成立执行值2
# 简单的判断，写几行太麻烦，就可以使用三目运算写成一行

