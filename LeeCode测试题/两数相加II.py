# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = 0, 0
        while l1:
            num1 *= 10
            num1 += l1.val
            l1 = l1.next
        while l2:
            num2 *= 10
            num2 += l2.val
            l2 = l2.next
        num = str(num1 + num2)
        pre = ListNode(0)
        r = pre
        for i in num:
            node = ListNode(int(i))
            r.next = node
            r = r.next
        return pre.next