# -*- coding: utf-8 -*-
from numpy import *
#男女比例最终走向
# P1 = mat([[0.419,0.581,0],[0.312,0.688,0],[0.314,0.686,0]])
# a1 = mat([0.338,0.662,0])
# while not (a1==a1*P1).all():
#     a1 = a1*P1
#     print(a1)
# print(a1)

#人数的增长率最终走向
P2 = mat([[0.7183908,0],[0.14381271,0]])
a2 = mat([0.3128655,0])
while not (a2==a2*P2).all():
    a2 = a2*P2
    print(a2)
print(a2)