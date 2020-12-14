# -*- coding: utf-8 -*-

def maxArea(height):
    ans = 0
    N = len(height)
    left, right = 0, N - 1
    while left < right:
        low = min(height[left], height[right])
        ans = max(ans, low * (right - left))
        if height[left] == low:
            left += 1
        else:
            right -= 1
    return ans


if __name__ == '__main__':
    a = [1,2,3,4,5,6,4,2,7]
    print(maxArea(a))
