# -*- coding: utf-8 -*-


# 归并排序，一个数组的前半部分和后半部分都已经排序完成的情况下，将前半部分和后半部分分别看待，重新获取一个列表，两个指针分别指向第一个，并判断他们的大小，小的则压如新数组，指针加一重复以上操作。操作完以后，如果发现还有剩下的，则将剩下的全部压入新数组
arr = [1, 3, 9, 12, 5, 7, 12]


# 马士兵版 核心
def mergesort(arr):
    mid = int(len(arr) / 2)
    tmp = []
    i = 0
    j = mid + 1
    while i <= mid and j < len(arr):
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    if i <= mid:
        # tmp.append(arr[i:])用while
        tmp.extend(arr[i:])
    if j < len(arr):
        # tmp.append(arr[j:])
        tmp.extend(arr[j:])
    print(tmp)


# 先递归分解数组，再合并数组。
def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2

    # left_li,right_li:采用归并排序后形成的新的有序的列表
    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])

    # 将两个有序的子序列合并为一个新的整体
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    if left_pointer < len(left_li):
        result += left_li[left_pointer:]
    if right_pointer < len(right_li):
        result += right_li[right_pointer:]
    return result


if __name__ == '__main__':
    li = [1, 2, 6, 4, 2, 5, 8, 6, 3, 67, 3, 3, 2, 9, 4, 2]
    print(merge_sort(li))
