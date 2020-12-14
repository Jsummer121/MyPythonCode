# -*- coding: utf-8 -*-
"""
1   2   3   4   5   6   7   8   9   10  11
1   2   0   4   5   0   7   8   0   10  11  3
0   13      14  0       16  17      0   19  3
    20      0           22  23          0   2
    25                  26  0               1
    28                  29
    0
"""
N = int(input())#原来的人数
a = {}
j = 1
for i in range(1,N+1):
    a[i] = 0
def die(a,j):
    b = list(a.keys())
    for i in b:
        if j == 3:
            j = 1
            a.pop(i)
            continue
        a[i] = j
        j += 1
    return a,j

while True:
    a,j = die(a,j)
    if len(a) <= 2:
        print(list(a.keys())[-1])
        break