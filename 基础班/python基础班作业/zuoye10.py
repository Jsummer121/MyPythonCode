# -*- coding: utf-8 -*-

# 在之前的基础上，定义正方形类。实现类实例的可调用，调用时打印边长；同时，直接打印类实例时能够打印出实例的面积
class Rectangle:
    def __init__(self, length, width):  # __init__实例化对象时自动调用
        self.length = length
        self.width = width

    def area(self):
        areas = self.length * self.width
        return "面积是：{}".format(areas)


class Square(Rectangle):
    def __init__(self, width):
        self.width = width
        self.length = width

    def __call__(self, *args, **kwargs): #实现类的调用
        print('正方形的边长是：{}'.format(self.width))

    def __str__(self):
        return self.area()


zheng = Square(4)
zheng()
print(zheng)




