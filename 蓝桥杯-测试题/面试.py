# -*- coding: utf-8 -*-

Max = 0
N = int(input())
List1 = list(map(int, input().split()))
List2 = list(map(int, input().split()))


def f(l, r):
    global Max
    list1_num = 0
    list2_num = 0
    for i in range(l, r + 1):
        list1_num |= List1[i]
        list2_num |= List2[i]
    MAX = list1_num + list2_num
    if (MAX > Max):
        Max = MAX


for i in range(N):
    for j in range(i + 1, N):
        f(i, j)

print("{}\n".format(Max))
