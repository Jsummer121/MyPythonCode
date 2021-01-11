# -*- coding: utf-8 -*-
# @Author  : summer

class ObjectCreator(object):
	pass


my_object = ObjectCreator()
print(my_object)  # <__main__.ObjectCreator object at 0x017B1F50>


def echo(o):
	print(o)
	
	
echo(ObjectCreator)  # 你可以将类做为参数传给函数 <class '__main__.ObjectCreator'>
print(hasattr(ObjectCreator, 'new_attribute'))  # False
ObjectCreator.new_attribute = 'foo'  # 你可以为类增加属性
print(hasattr(ObjectCreator, 'new_attribute'))  # True
print(ObjectCreator.new_attribute)  # foo
ObjectCreatorMirror = ObjectCreator  # 你可以将类赋值给一个变量
print(ObjectCreatorMirror())  # <__main__.ObjectCreator object at 0x020D2110>
