# -*- coding: utf-8 -*-


def count(val):
    while True:
        print("yield生成前")
        yield val
        print("yield生成后")
        val -= 1


n = count(10)
print("----1----")
print(next(n))
print("----2----")
print(next(n))
print("----3----")
print(next(n))
