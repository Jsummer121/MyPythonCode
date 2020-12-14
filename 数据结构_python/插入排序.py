# -*- coding: utf-8 -*-

# 类似于从第一个元素开始遍历，然后该元素从前冒泡排序
arr = [9, 6, 11, 3, 5, 12, 8, 7, 10, 15, 14, 4, 1, 13, 2]
for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]

for i in arr:
    print(i)
