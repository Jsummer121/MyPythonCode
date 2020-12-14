# -*- coding: utf-8 -*-
from collections import Counter


def a(nums, limit):
    number = []
    for i in range(len(nums) // 2):
        li = [nums[i], nums[len(nums) - i - 1]]
        number.append(sum(li))
    new_map = Counter(number)  # 用计数器获取每个值
    if (len(new_map) == 1):
        return 0
    else:
        # 获取最多个数的
        max_i = 0
        max_j = 0
        for i, j in new_map.items():
            if j > max_j:
                max_i = i
                max_j = j
        max_num = len(nums) // 2 - new_map[max_i]
        new_map.pop(max_i)
        for i, j in new_map.items():
            if i > 2*limit:
                max_num += 1
        return max_num




print(a([1, 2, 3, 3, 3, 3, 3, 3, 2, 1], 5))
