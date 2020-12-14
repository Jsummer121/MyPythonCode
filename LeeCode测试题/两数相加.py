# -*- coding: utf-8 -*-
import time


s = [7777 for i in range(500000)]+[3,4]
print("start")
start = time.time()
def twoSum(nums, target):
    Len = len(nums)
    a = 0
    for i in nums:
        a += 1
        try:
            return [a - 1, nums.index(target - i, a, Len)]
        except:
            pass
    return []
print(twoSum(s,7))
end = time.time()
print("indexTime:",end-start)



