栈

​		栈是一种容器，可以存入数据元素、访问元素、删除元素，它的特点在于只能允许在容器的一端进行加入数据和输出数据的运算，没有了位置的概念，保证任何时候可以访问、删除的元素都是此前后存入的那个元素，确定了一种默认的访问顺序。

​		由于栈数据结构只允许在一端进行操作，因而按照后进先出的原则运作。

```python
# -*- coding: utf-8 -*-


class Stack(object):
    """栈"""
    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        if self.__list:
            return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.pop())
    s.push(3)


```

## 队列

队列是只允许在一端进行插入操作，而在另一端进行删除操作的线性表

```python
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

```

