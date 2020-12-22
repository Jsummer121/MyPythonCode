# -*- coding: utf-8 -*-
import math
import copy

n, m = input().split()
a = list(map(int, input().split()))
b = list(map(int, input().split()))


for j in b:
    List = copy.deepcopy(a)
    for i in range(len(List)):
        List[i] += j

    print(min(List))
