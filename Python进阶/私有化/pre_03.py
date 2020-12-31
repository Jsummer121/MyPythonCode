# -*- coding: utf-8 -*-


class Student:
    def __init__(self, name):
        self.__name = name

    def show_person(self):
        print(self.__name)


if __name__ == '__main__':
    s1 = Student("summer")
    s1.show_person()
    # print(s1.__name)
    print(s1.__dict__)
    print(s1._Student__name)
