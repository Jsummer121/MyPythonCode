# -*- coding: utf-8 -*-
# @Author  : summer

# type可以接受一个类的描述作为参数，然后返回一个类。（要知道，根据传入参数的不同，同一个函数拥有两种完全不同的用法是一件很傻的事情，但这在Python中是为了保持向后兼容性）
# type(类名, 由父类名称组成的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)

class Test1:
	pass


Test2 = type("Test3", (), {})
print(Test1)  # <class '__main__.Test1'>
print(Test2)  # <class '__main__.Test3'>
print(help(Test1))
"""
Help on class Test1 in module __main__:

class Test1(builtins.object)
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)

None
"""
print((help(Test2)))
"""
Help on class Test3 in module __main__:

class Test3(builtins.object)
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)

None

Process finished with exit code 0

"""
