# -*- coding: utf-8 -*-

a1 = [1, 2, 3, 4, 5, 6, 7, 8]
b1 = set(a1)
c1 = list(b1)
print(a1)
print(b1)
print(c1)
print(a1 == c1)
a2 = [1, 5, 2, 7, 5, 2, 5, 9, 7, 4, 2, 4, 7, 9, 6, 4, 32]
b2 = set(a2)
c2 = list(b2)
print(a2)
print(b2)
print(c2)
print(a2 == c2)
a3 = {1, 6, 3, 21, 3, 84, 2, 23, 8, 8545, 3, 1, 3, 427, 344, 23, 13, 125}
b3 = list(a3)
c3 = set(b3)
print(a3)
print(b3)
print(c3)
print(a3 == c3)
a4 = {1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9, 9, 1, 2, 3, 4, 5, 6}
b4 = list(a4)
c4 = set(b4)
print(a4)
print(b4)
print(c4)
print(a4 == c4)
