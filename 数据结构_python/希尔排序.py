# -*- coding: utf-8 -*-


# 给一个列表，给定一个间隔，然后在列表上根据间隔的个数先排列，然后循环直到该间隔全部排完。
# 缩小间隔继续上面操作 最好的时间复杂度O(n**1.3)
arr = [9, 6, 11, 3, 5, 12, 8, 7, 10, 15, 14, 4, 1, 13, 2]


# 版本1
def shellSort1(arr):
    for gap in range(4, 0, -1):
        for i in range(gap, len(arr)):
            for j in range(i, gap-1, -gap):
                if arr[j] < arr[j-gap]:
                    arr[j], arr[j-gap] = arr[j-gap], arr[j]


# 版本2
def shellSort2(arr):
    n = len(arr)
    gap = int(n / 2)
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = int(gap / 2)


# 版本3 Knuth序列
def shellSort3(arr):
    # h=1 h=3*h+1 ...
    n = len(arr)
    h = 1
    while h < n/3:
        h = 3*h+1
    gap = h
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = int((gap-1)/3)


shellSort3(arr)
print(arr)
