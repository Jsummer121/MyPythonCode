#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/27 20:57


class A:
    pass
    # def f(self):
    #     print("A")


class B:
    def f(self):
        print("B")


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


e = E()  # 此时类中的self始终指向的是e，所有方法选择的优先级始终从E开始判断的
e.f()   # E无--->C,C无--->A,A无--->D,D无--->B




