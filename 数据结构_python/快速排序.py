# -*- coding: utf-8 -*-


# 必须掌握！！！
# 设置两个指正，分别从头和尾开始，找一个中间值（前指针指的值），从后指针开始，如果比中间值大则指针往前移，否则把后指针的位置放到前指针的位置。然后移动前指针与后指针相同，当后指针小于等于钱指针时，把中间值放入前指针当前所在位置。现在分为前半部分，中间值，后半部分，然后把这两部分分别再次递归循环。
def quick_sort(alist, first, last):
    """快速排序"""
    # 进行结束判断
    if first >= last:
        return
    mid_val = alist[first]
    low = first
    high = last
    while low < high:
        while low < high and alist[high] >= mid_val:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid_val:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_val

    # 对low左边的进行快速排序
    quick_sort(alist, first, low - 1)
    # 对low右边的进行快速排序
    quick_sort(alist, low + 1, last)


if __name__ == '__main__':
    li = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    quick_sort(li, 0, len(li) - 1)
    print(li)
