# -*- coding: utf-8 -*-


def merge_sort(alist):
    # 判断传入的数组长度是否小于1，如果是返回该数组
    if len(alist) < 2:
        return alist

    mid = len(alist) // 2  # 获取中间值

    # left_li,right_li:采用归并排序后形成的新的有序的列表
    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])

    # 下面是将两个数组合并成一个新的数组
    left_pointer = 0
    right_pointer = 0
    result = []
    # 如果左指针小于左列表长度并且右指针小于右列表的长度
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        # 如果左列表下的左指针所指向的值小于右边的，则把该值放入新列表
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            # 不然就把右边的值放入新列表指针加一
            result.append(right_li[right_pointer])
            right_pointer += 1
    # 当结束上层循环说明，某个指针已经达到了该列表的长度，另一个列表还有多余的值需要全部传入
    if left_pointer < len(left_li):
        # 也可以使用extend方法而不能使用append。
        # extend是将传入的列表挨个值放入列表，但是append是将整个放入
        result += left_li[left_pointer:]
    if right_pointer < len(right_li):
        result += right_li[right_pointer:]
    return result


if __name__ == '__main__':
    li = [1, 3, 65, 6, 4, 23, 65, 87, 5, 3, 3, 7, 7, 4, 3, 237, 9, 9865, 3, 2, 57]
    print(merge_sort(li))
