# -*- coding: utf-8 -*-


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_message(self):
        print("%s的年龄为%d" % (self.name, self.age))


class Student(People):
    pass


if __name__ == '__main__':
    s1 = Student("summer", 20)
    s1.show_message()
