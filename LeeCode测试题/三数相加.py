# -*- coding: utf-8 -*-


def threeSum(nums):
    n = len(nums)
    res = []
    nums.sort()
    if n < 3:
        return res
    for i in range(n - 2):
        if sum(nums[i:i + 3]) > 0:
            return res
        if nums[i] + sum(nums[-1:-3:-1]) < 0:
            continue
        left, right = i + 1, n - 1
        while left < right:
            count = nums[i] + nums[left] + nums[right]
            if count < 0:
                left += 1
            elif count > 0:
                right -= 1
            else:
                middle = [nums[i], nums[left], nums[right]]
                if middle not in res:
                    res.append(middle)
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return res
