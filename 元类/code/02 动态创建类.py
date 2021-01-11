# -*- coding: utf-8 -*-
# @Author  : summer


def choose_class(name):
	if name == "foo":
		class Foo:
			pass
		return Foo
	else:
		class Bar:
			pass
		return Bar


MyClass = choose_class("foo")
print(MyClass)  # <class '__main__.choose_class.<locals>.Foo'>
print(MyClass())  # <__main__.choose_class.<locals>.Foo object at 0x01C88D10>

print(type(1))  # <class 'int'>
print(type("1"))  # <class 'str'>
print(type(MyClass()))  # <class '__main__.choose_class.<locals>.Foo'>
print(type(MyClass))  # <class 'type'>
