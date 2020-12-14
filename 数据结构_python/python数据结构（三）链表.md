# 链表

**为什么需要链表？**

​		顺序表的构建需要预先知道数据大小来申请存储空间，而在进行扩充时有需要进行数据的迁移，所以使用起来并不是很灵活。

​		链表结构可以充分利用计算机内存空间，实现灵活的内存动态管理。

**链表的定义**

​		链表是一种常见的基础数据结构，是一种线型表，但不像顺序表一样连续存储数据，而是在每一个结点例存放下一个结点的位置信息（即地址）。

## 一、单向链表

​		单向链表也叫单链表，是链表中最简单的一种形式，它的每个节点包含两个域，一个信息域，一个链接域，这个链接指向下一个节点，而最后一个结点的链接域指向一个空值。

### 1.1结点实现

```python
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None
```

### 1.2单链表的操作

- is_empty():判空
- length():链表的长度
- travel():遍历整个表
- add(item):表头添加元素
- append(item):表尾添加元素
- insert(pos,item):指定位置添加元素
- remove(item):删除节点
- search(item):查找节点是否存在

```python
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表"""
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

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表的长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """表头添加元素,头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """表尾添加元素，尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

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
        pre = None
        cur = self.__head
        count = 0
        while cur != None:
            if cur.elem == item:
                # 判断当前节点是否是头节点
                # 头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                return count
            else:
                count += 1
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.travel()
    print(ll.remove(4))
    ll.travel()

```

### 1.3 链表与顺序表的对比

​		链表失去了顺序表随机读取的优点，同时变脸由于增加了结点的指针域，空间开销跟那个大，但对于存储空间的使用要相对灵活。

​		链表与顺序表的各种操作复杂度如下：

|        操作         | 链表 | 顺序表 |
| :-----------------: | :--: | :----: |
|      访问元素       | O(n) |  O(1)  |
| 在头部插入/删除元素 | O(1) |  O(n)  |
| 在尾部插入/删除元素 | O(n) |  O(1)  |
| 在中间插入/删除元素 | O(n) |  O(n)  |

​		注意，虽然表面看起来复杂度都是O（n），但是链表和顺序表在插入和删除时金星秀的是完全不同的操作，链表的主要耗时操作是遍历查找，删除和插入操作本身的复杂度是O（1）。顺序表查找很快，主要耗时的操作是拷贝覆盖，因为除了目标元素在尾部的特殊情况，顺序表进行插入和删除时需要对操作点之后的所有元素进行前后移位操作只能通过拷贝和覆盖的方法进行。

## 二、单向循环链表

​		单链表的一个变形是单向循环链表，链表的最后一个节点的next不在是None，而是指向链表的头节点

### 2.1操作

- is_empty():判空
- length():链表的长度
- travel():遍历整个表
- add(item):表头添加元素
- append(item):表尾添加元素
- insert(pos,item):指定位置添加元素
- remove(item):删除节点
- search(item):查找节点是否存在

```python
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

```

## 三、双向链表

​		一种更加复杂的链表是“双向链表”，每个节点有两个链接：一个海子乡前一个节点，当此结点为第一个节点时，指向空，而另一个指向下一个结点，当此结点为最后一个结点时，指向空。

### 3.1操作

- is_empty():判空
- length():链表的长度
- travel():遍历整个表
- add(item):表头添加元素
- append(item):表尾添加元素
- insert(pos,item):指定位置添加元素
- remove(item):删除节点
- search(item):查找节点是否存在

```python
# -*- coding: utf-8 -*-


class Node(object):
    # 构建节点
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None

        
class DoubleLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表的长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """表头添加元素,头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head.prev = node
        self.__head = node
        # node.next.prev = node

    def append(self, item):
        """表尾添加元素，尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始索引
        """
        if pos < 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < pos-1:
                count += 1
                cur = cur.next
            # 当循环退出后，pre指向pos位置
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                # 判断当前节点是否是头节点
                # 头节点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        # 判断链表是否只有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
    
    
if __name__ == '__main__':
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())
    dll.append(1)
    print(dll.is_empty())
    print(dll.length())
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.travel()
    print(dll.remove(4))
    dll.travel()

```

