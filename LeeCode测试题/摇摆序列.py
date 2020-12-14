# -*- coding: utf-8 -*-


def wiggleMaxLength(nums):
    up, down = 1, 1
    if len(nums) < 2:
        return len(nums)
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            up = down + 1
        if nums[i] < nums[i - 1]:
            down = up + 1
    return max(up, down)


if __name__ == '__main__':
    print(wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
