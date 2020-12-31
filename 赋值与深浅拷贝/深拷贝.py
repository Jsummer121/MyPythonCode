# -*- coding: utf-8 -*-
import copy

a = [11, 22]
b = [33, 44]
c = [a, b]
print(id(a))
print(id(b))
print(id(c))
print(id(c[0]))
print(id(c[1]))
d = copy.deepcopy(c)
print(id(d))
print(id(d[0]))
print(id(d[1]))
