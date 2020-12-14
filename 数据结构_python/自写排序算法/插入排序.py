# -*- coding: utf-8 -*-


def init_sort(alist):
    n = len(alist)
    for i in range(n):
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
    return alist


if __name__ == '__main__':
    li = [12, 5, 3, 2, 5, 78, 4, 3, 2, 4, 7, 8, 5, 4, 212, 6]
    print(init_sort(li))
