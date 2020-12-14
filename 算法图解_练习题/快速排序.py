# -*- coding: utf-8 -*-


# 选取第一个元素作为基准值,根据基准值，可以将一个数组分为三部分，即小于基准值的部分，基准值和大于基准值的部分，然后再次递归，将剩余两个继续利用该方法排序。
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))
