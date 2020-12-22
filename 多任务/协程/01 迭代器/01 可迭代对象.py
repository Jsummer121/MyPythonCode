# -*- coding: utf-8 -*-


class MyList():
    def __init__(self):
        self.container = list()

    def add(self, val):
        self.container.append(val)


if __name__ == '__main__':
    mylist = MyList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)

    for i in mylist:
        print(i)
    # 由此可知，虽然MyList类中放置了list是可迭代的，但是整个类并不能迭代
