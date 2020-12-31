# -*- coding: utf-8 -*-


class Student:
    def __init__(self, name):
        self._name = name

    def show_person(self):
        print(self._name)

    def _show_person2(self):
        print(self._name)


if __name__ == '__main__':
    s1 = Student("summer")
    print(s1._name)
    s1.show_person()
