# -*- coding: utf-8 -*-


class Queue(object):
    """队列"""
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """往队列尾部添加元素"""
        self.__list.append(item)

    def dequeue(self):
        """从队列头部删除元素"""
        if self.is_empty():
            return None
        else:
            return self.__list.pop(0)

    def is_empty(self):
        """判断队列是否为空"""
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
