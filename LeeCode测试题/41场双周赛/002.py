# -*- coding: utf-8 -*-
import time


def getSumAbsoluteDifferences(nums):
    N = len(nums)
    if N == 0:
        return 0
    ans = []
    Sum = []
    lsum,rsum = 0,0
    for i in range(N):
        if nums[i] == nums[i-1]:
            ans.append(ans[-1])
            continue
        if i == 0:
            for j in nums:
                Sum.append(j-nums[i])
            ans.append(sum(Sum))
        else:
            if not lsum:
                lsum = sum(Sum[:i])
                rsum = sum(Sum[i+1:])
            a = abs(lsum-(nums[i]-nums[0])*(i-1) + (nums[i]-nums[0])*(N-2-i) - rsum)
            lsum += nums[i]
            if i != N-1:
                rsum -= nums[i+1]
            ans.append(a)
    return ans

# def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
#     n, sums, pre, ans = len(nums), sum(nums), 0, []
#     for i in range(n):
#         ans.append((nums[i] * i - pre) + (sums - pre - nums[i]) - nums[i] * (n - i - 1))
#         pre += nums[i]
#     return ans


if __name__ == '__main__':
    print(getSumAbsoluteDifferences([1,4,6,8,10]))
