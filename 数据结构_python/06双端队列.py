# -*- coding: utf-8 -*-


class Deque(object):
    """双端队列"""
    def __init__(self):
        self.__item = []

    def is_empty(self):
        return self.__item == []

    def size(self):
        return len(self.__item)

    def add_front(self, item):
        self.__item.insert(0,item)

    def add_rear(self, item):
        self.__item.append(item)

    def remove_front(self):
        if self.__item:
            return self.__item.pop(0)
        else:
            return None

    def remove_rear(self):
        if self.__item:
            return self.__item.pop(-1)
        else:
            return None


if __name__ == '__main__':
    dq = Deque()
    dq.add_front(1)
    dq.add_front(2)
    dq.add_rear(3)
    dq.add_rear(4)
    print(dq.remove_front())
    print(dq.remove_front())
    print(dq.remove_rear())
    print(dq.remove_rear())

