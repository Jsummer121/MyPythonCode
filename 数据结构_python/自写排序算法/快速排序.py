# -*- coding: utf-8 -*-


def fast_sort(alist, first, last):
    # 判断该函数是否结束
    if first >= last:
        return
    mid_val = alist[first]
    low = first
    high = last
    while low < high:
        # 如果开始指针小于结束指针并且结束指针指向的值大于等于中间值
        while low < high and alist[high] >= mid_val:
            # 结束指针往左移动一位
            high -= 1
        # 当上层循环结束时，说明开始指针等于结束指针或者结束指针小于中间值
        # 则需要将结束指针指向的值放到开始指针指向的位置
        alist[low] = alist[high]
        # 接下来由开始指针进行判断，如果开始指针小于结束指针并且开始指针指向的值小于中间值
        while low < high and alist[low] < mid_val:
            # 开始指针往右移动一位
            low += 1
        # 当上层循环结束时，说明开始指针等于结束指针或者开始指针大于中间值
        # 则需要将开始指针指向的值放到结束指针指向的位置
        alist[high] = alist[low]
    # 如果上层循环结束，说明开始指针和结束指针指向同一个位置，则把中间值放到开始指针所指位置（也可以是结束指针）
    alist[low] = mid_val

    # 结束以上的工作，说明该数组在first到end之间，已经分出了三部分（即中间值，中间值的左半部分和中间值的右半部分），接下来即可将左半部分和右半部分放入函数进行重新递归。
    fast_sort(alist, first, low - 1)
    fast_sort(alist, low + 1, last)


if __name__ == '__main__':
    li = [1, 2, 4, 6, 4, 3, 65, 7, 4, 2, 5, 7, 8, 54, 3, 2, 76, 6, 43, 2, 8]
    fast_sort(li, 0, len(li)-1)
    print(li)
