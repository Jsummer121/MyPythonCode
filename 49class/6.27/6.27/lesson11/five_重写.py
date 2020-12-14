#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/27 21:20


class Animal:
    def __init__(self):
        print("A构造方法")


class Owner:
    def __init__(self):
        print("C构造方法")


class Cat(Owner, Animal):
    def __init__(self):
        print("B构造方法")


kitty = Cat()   #
