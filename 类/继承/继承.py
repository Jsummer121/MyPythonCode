#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/27 20:24


class Animal:
    def __init__(self, name, color, eat):
        self.name = name
        self.color = color
        self.eat = eat


class Owner:
    def run(self):
        print("happy")


class Dog(Animal):  # 单继承：子类只继承一个父类
    pass


class Cat(Owner, Animal):   # 多继承：子类继承多个父类
    pass


kitty = Cat("kitty", "white", "milk")
print(kitty.name)
kitty.run()






