# -*- coding: utf-8 -*-

def containsNearbyAlmostDuplicate(nums, k, t):
    # set
    window = set()
    for i in range(len(nums)):
        num = nums[i]
        if num in window or i > k and len(window) < k:
            return True
        for j in window:
            if num - t <= j <= num + t:
                return True
        window.add(num)
        if len(window) > k:
            window.remove(nums[i - k])
    return False


if __name__ == '__main__':
    nums = []
    k = 2
    t = 3
    print(containsNearbyAlmostDuplicate(nums, k, t))
