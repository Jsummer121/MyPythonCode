# -*- coding: utf-8 -*-
list = ['__x86_64__','__ATOMIC_HLE_ACQUIRE','__ATOMIC_HLE_RELEASE']

with open('test.c', 'r', encoding='UTF-8') as f:
    test = f.readlines()

for i in test:
    for j in list:
        if i == "#if defind({})\n".format(j):
            print("ok")