# -*- coding: utf-8 -*-


def shell_sort(alist):
    n = len(alist)
    gap = 4
    while gap > 0:
        for i in range(gap, n):
            tmp = alist[i]
            j = i
            while j >= gap and alist[j - gap] > tmp:
                alist[j] = alist[j - gap]
                j -= gap
            alist[j] = tmp
        gap -= 1


# 新的思路，即不指定gap的大小，而是由n决定，根据1,4,13来一次一次的改变，
def Knuth_shell_sort(alist):
    # h=1 h=3*h+1 ...
    n = len(alist)
    h = 1
    while h < n/3:
        h = 3*h+1
    gap = h
    while gap > 0:
        for i in range(gap, n):
            temp = alist[i]
            j = i
            while j >= gap and alist[j - gap] > temp:
                alist[j] = alist[j - gap]
                j -= gap
            alist[j] = temp
        gap = int((gap-1)/3)


if __name__ == '__main__':
    li = [1, 3, 6, 5, 4, 43, 7, 9, 7, 54, 3, 6, 9, 7, 5, 3, 6, 9, 65, 3, 43, 7, 4, 3, 5, 87, 54, 4, 7, 96]
    shell_sort(li)
    print("普通希尔排序：")
    print(li)
    li = [1, 3, 6, 5, 4, 43, 7, 9, 7, 54, 3, 6, 9, 7, 5, 3, 6, 9, 65, 3, 43, 7, 4, 3, 5, 87, 54, 4, 7, 96]
    Knuth_shell_sort(li)
    print("Knuth希尔排序：")
    print(li)
