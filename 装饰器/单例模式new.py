#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/28 20:37


# __new__
class Earth:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):  # 如果我的类没有实例对象，那我就去new一个实例对象
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.name = 'earth'


e = Earth()
print(e)
a = Earth()
print(a)

# 类每次实例化时都会新建一个对象，并在内存里划出一块存放对象
# 通过__new__可以实现不管实例多少次，始终都是同一个对象
# __new__方法是在__init__之前执行的
# 单例模式
# 1.适用情况：当所有实例中封装的数据都相同时(可视为同一个实例),此时可以考虑单例模式
# 2.案例：数据库连接池


