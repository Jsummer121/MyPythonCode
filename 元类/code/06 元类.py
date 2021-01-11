# -*- coding: utf-8 -*-
# @Author  : summer

a = 100
print(a.__class__)  # <class 'int'>
name = "summer"
print(name.__class__)  # <class 'str'>


def foo():
	pass


print(foo.__class__)  # <class 'function'>


class Bar:
	pass


b = Bar()
print(b.__class__)  # <class '__main__.Bar'>

print(a.__class__.__class__)  # <class 'type'>
print(name.__class__.__class__)  # <class 'type'>
print(foo.__class__.__class__)  # <class 'type'>
print(b.__class__.__class__)  # <class 'type'>
