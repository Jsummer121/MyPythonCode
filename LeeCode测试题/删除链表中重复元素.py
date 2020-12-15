# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, val = 0):
        self.val = val
        self.next = None


def deleteduplicates(head):
    dummy_head = ListNode(0)  # 获取一个空结点
    dummy_head.next = head  # 将空节点的next指向头结点
    pre, cur = dummy_head, head  # 设计双指针，第一个用来判断是否需要进行跳帧，第二个用来判断元素是否重复
    while cur:
        while cur.next and cur.val == cur.next.val:  # 如果2指针的下一个结点存在，并且该结点的值与下一个结点的值相同
            cur = cur.next  # 将2结点跳转到下一个结点，重复此操作，直至不同为止
        if pre.next == cur:  # 如果1指针的下一个结点就是2结点，说明并不存在相同节点，则1结点可以直接往下移动一格
            pre = pre.next
        else:  # 注意题目，说的是删除全部重复的，因此如果存在重复，那么就应当1结点直接跳过相同的元素，直接到达相同元素最后一个的下一个结点
            pre.next = cur.next
        cur = cur.next  # 将2结点往后移一位
    return dummy_head.next


if __name__ == '__main__':
    s = [1, 2, 3, 3, 4, 4, 5]
    link = ListNode()
    pre = link
    for i in s:
        node = ListNode(i)
        pre.next = node
        pre = pre.next
    r = link
    a = deleteduplicates(r)
    a = a.next
    while a:
        print(a.val)
        a = a.next
