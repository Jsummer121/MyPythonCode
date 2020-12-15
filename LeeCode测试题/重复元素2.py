# -*- coding: utf-8 -*-


def containsNearbyDuplicate(nums, k):
    # 1.滑动窗口,list版
    # k += 1
    # def check(win):
    #     return len(win) != len(set(win))
    #
    # window = nums[:k]
    # if check(window):  # 判断第一个窗口是否符合要求
    #     return True
    # for i in range(k, len(nums)):
    #     window.append(nums[i])
    #     window = window[1:]
    #     if check(window):
    #         return True
    # return False

    # 1.2 滑动窗口，用set取代list（主要作用，降低pop时的时间复杂度）
    # window = set()
    # for i in range(len(nums)):
    #     if nums[i] in window:
    #         return True
    #     window.add(nums[i])
    #     if len(window) > k:
    #         window.remove(nums[i - k])
    # return False

    # 3.dict版
    hash_map = {}
    for i in range(len(nums)):
        num = nums[i]
        if num in hash_map and i - hash_map[num] <= k:
            return True
        else:
            hash_map[num] = i
    return False


if __name__ == '__main__':
    print(containsNearbyDuplicate([1,2,3,1,2,3], 2))
