# -*- coding: utf-8 -*-
# @Author  : summer

# 元类的主要目的就是为了当创建类时能够自动地改变类。
def upper_attr(class_name, class_parents, class_attr):
	# 遍历属性字典，把不是__开头的属性名字变为大写
	new_attr = {}
	for name, value in class_attr.items():
		if not name.startswith("__"):
			new_attr[name.upper()] = value
	
	# 调用type来创建一个类
	return type(class_name, class_parents, new_attr)


class Foo(object, metaclass=upper_attr):
	bar = 'bip'


print(hasattr(Foo, 'bar'))  # False
print(hasattr(Foo, 'BAR'))  # True

f = Foo()
print(f.BAR)  # bip
