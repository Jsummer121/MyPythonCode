# -*- coding: utf-8 -*-
import collections

# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

class Solution:
    def levelOrder(self, root):
        d = collections.defaultdict(list)
        def f(r, i):
            if r:
                d[i].append(r.val)
                f(r.left, i + 1)
                f(r.right, i + 1)
        f(root, 0)
        return [*d.values()]
# [3,9,20,null,null,15,7]

# defaultdict(<class 'list'>, {})
# defaultdict(<class 'list'>, {0: [3]})
# defaultdict(<class 'list'>, {0: [3], 1: [9]})
# defaultdict(<class 'list'>, {0: [3], 1: [9]})
# defaultdict(<class 'list'>, {0: [3], 1: [9]})
# defaultdict(<class 'list'>, {0: [3], 1: [9, 20]})
# defaultdict(<class 'list'>, {0: [3], 1: [9, 20], 2: [15]})
# defaultdict(<class 'list'>, {0: [3], 1: [9, 20], 2: [15]})
# defaultdict(<class 'list'>, {0: [3], 1: [9, 20], 2: [15]})
# defaultdict(<class 'list'>, {0: [3], 1: [9, 20], 2: [15, 7]})
# defaultdict(<class 'list'>, {0: [3], 1: [9, 20], 2: [15, 7]})