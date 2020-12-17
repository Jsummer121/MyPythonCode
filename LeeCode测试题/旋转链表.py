# -*- coding: utf-8 -*-
# leetcode:61. 旋转链表https://leetcode-cn.com/problems/rotate-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 预处理
        if not head:
            return None
        if not head.next:
            return head

        # 将整个链表变成首尾相连的环，并且记录整个链表长度
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        # 查找需要断开的结点(n - k % n - 1)th node
        # 且下一个结点即为新的头结点(n - k % n)th node
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # 找到头结点后即可解开环，然后返回新的头结点
        new_tail.next = None

        return new_head
