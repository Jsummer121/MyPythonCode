# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCircleLinkList(object):
    """单向循环链表"""
    """
    is_empty():判空
    length():链表的长度
    travel():遍历整个表
    add(item):表头添加元素
    append(item):表尾添加元素
    insert(pos,item):指定位置添加元素
    remove(item):删除节点
    search(item):查找节点是否存在
    """

    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表的长度"""
        if self.is_empty():
            return 0
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        # 退出循环，cur指向尾节点，但尾节点为打印
        print(cur.elem)
        print("")

    def add(self, item):
        """表头添加元素,头插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        cur = self.__head
        while cur.next != node.next:
            cur = cur.next
        node.next = self.__head
        self.__head = node
        cur.next = node

    def append(self, item):
        """表尾添加元素，尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始索引
        """
        if pos < 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < pos-1:
                count += 1
                pre = pre.next
            # 当循环退出后，pre指向pos结点的前一位
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        pre = None
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                # 判断当前节点是否是头节点
                if cur == self.__head:
                    # 头节点的情况，找尾结点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        if cur.elem == item:
            if cur == self.__head:
                # 只有一个节点
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            return True
        return False


if __name__ == '__main__':
    lcl = SingleCircleLinkList()
    print(lcl.is_empty())
    print(lcl.length())
    lcl.append(1)
    print(lcl.is_empty())
    print(lcl.length())
    lcl.append(2)
    lcl.append(3)
    lcl.append(4)
    lcl.append(5)
    lcl.travel()
    print(lcl.remove(4))
    lcl.travel()
