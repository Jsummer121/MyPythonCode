# -*- coding: utf-8 -*-


def gen(val):
    i = 0
    while i < val:
        temp = yield i
        print(temp)
        i += 1


f = gen(5)
while True:
    print(f.__next__())