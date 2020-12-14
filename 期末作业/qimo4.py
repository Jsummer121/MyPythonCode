# -*- coding: utf-8 -*-
# 4.面向对象：定义一个Person类，这个类有名字，年纪，职业，并且有至少三个方法。
# 这个类的实例之间，可以通过 + 进行互动。
# 并且实例可以直接被调用，调用的时候会去使用类的其中一个方法。


class Person:
    def __init__(self,name,age,work,food):
        self.name = name
        self.age = age
        self.work = work
        self.food = food

    def __call__(self, *args, **kwargs):
        Person.eat(self)

    def __add__(self, other):
        all_age = self.age +other.age
        print("他们的年龄之和为:"+str(all_age))

    def eat(self):
        print("{}喜欢吃{}".format(self.name, self.food))


wang = Person("小王",15,"football","蔬菜")
liu = Person("小刘",20,"basketball","水果")
wang + liu
wang()
