# -*- coding: utf-8 -*-
# @Author  : summer


a = 100


def b():
	pass


class C:
	pass


g = globals()
# print(g)
print(g["__builtins__"].__dict__)