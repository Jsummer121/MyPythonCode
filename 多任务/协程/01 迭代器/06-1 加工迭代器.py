# -*- coding: utf-8 -*-
class MyList(object):
    """自定义的一个可迭代对象"""
    def __init__(self):
        self.items = []
        self.current = 0

    def add(self, val):
        self.items.append(val)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.items):
            item = self.items[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration


if __name__ == '__main__':
    mylist = MyList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.add(4)
    mylist.add(5)
    for num in mylist:
        print(num)