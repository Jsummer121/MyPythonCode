# -*- coding: utf-8 -*-
import copy

a = [11, 22]
b = (a, )
c = [b]
d = copy.copy(c)
e = copy.deepcopy(c)
print(id(a))
print(id(b))
print(id(c))
print(id(c[0]))
print(id(d))
print(id(d[0]))
print(id(e))
print(id(e[0]))

