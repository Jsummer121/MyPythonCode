# -*- coding: utf-8 -*-


def choose_sort(alist):
    n = len(alist)
    for i in range(n):
        index = i
        for j in range(i + 1, n):
            if alist[index] > alist[j]:
                alist[index], alist[j] = alist[j], alist[index]
    return alist


if __name__ == '__main__':
    li = [1, 2, 4, 67, 4, 2, 4, 67, 9, 5, 2, 4, 8, 9, 5, 3]
    print(choose_sort(li))
