#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/25 21:48


# 类和函数
class Cat:
    """这是一个猫类"""
    def __init__(self, color, age):
        self.color = color
        self.age = age


kitty = Cat("white", 2)
hua = Cat("hua", 1)

# 以上部分，我们实现了：1.创建了Cat类 2.实例化了两个对象kitty&hua


# 接下来，我们来创建一个函数,实现上面两只猫猫的年龄求和后的新属性，给第三只猫
def add_cat(name, c1, c2):
    cat = Cat(name, c1.age + c2.age)
    return cat


yellow = add_cat("yellow", kitty, hua)
print(yellow.age)

red = add_cat("red", kitty, yellow)
print(red.age)


# 方法：和某个特定的类相关联的函数
# 函数--->方法：只需要将函数的定义移动到类的定义中即可
class Cat:
    """这是一个猫类"""
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def print_cat(self):
        print("{}-{}".format(self.color, self.age))


kitty = Cat("white", 2)
hua = Cat("hua", 1)

# print_cat调用
Cat.print_cat(kitty)

kitty.print_cat()

# 封装：self指向对象，在对象中封装数据，对类进行优化的方法，就叫封装


class Cat:
    """这是一个猫类"""
    count = 0   # 类属性

    def __init__(self, name, color, eat, age):
        self.eat = eat
        self.name = name    # 实例属性
        self._color = color  # 外部可访问私有属性
        self.__age = age    # 外部不可访问私有属性
        Cat.count += 1  # 内部调用：类名.类属性名

    def print_cat(self):
        print("{}-{}-{}".format(self._color, self.__age, self.name))

    def __get_none(self):
        # 私有方法，不可以被实例和类直接调用
        return "我是私有方法"

    def test(self):
        self.__get_none()


kitty = Cat('kitty', 'white', 'milk', 2)
print(kitty.eat)
print(Cat.count)
print(kitty.count)

kitty.print_cat()
# kitty.__get_none()



