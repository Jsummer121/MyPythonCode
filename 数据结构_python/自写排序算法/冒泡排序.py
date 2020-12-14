# -*- coding: utf-8 -*-


def bubble_sort(alist):
    n = len(alist)
    for i in range(n):
        for j in range(i + 1, n):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
    return alist


if __name__ == '__main__':
    li = [1, 2, 4, 7, 54, 8, 5, 3, 5, 9, 5, 3]
    print(bubble_sort(li))
