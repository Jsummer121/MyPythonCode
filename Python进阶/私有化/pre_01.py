# -*- coding: utf-8 -*-


class Student:
    def __init__(self, name):
        self.name = name

    def show_person(self):
        print(self.name)


if __name__ == '__main__':
    s1 = Student("summer")
    print(s1.name)
    s1.show_person()
