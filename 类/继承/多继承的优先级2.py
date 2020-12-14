#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/27 21:09


class F1:
    # pass
    def f(self):
        print("F1")
class F2:
    # pass
    def f(self):
        print("F2")

class A(F1):
    pass
    # def f(self):
    #     print("A")


class B(F2):
    pass
    # def f(self):
    #     print("B")


class C(A):
    pass
    # def f(self):
    #     print("C")


class D(B):
    pass
    # def f(self):
    #     print("D")


class E(C, D):
    pass
    # def f(self):
    #     print("E")


e = E()
e.f()   # E无--->C,C无--->A,A无--->D,D无--->B,B无--->F
