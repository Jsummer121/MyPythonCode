# -*- coding: utf-8 -*-
# @Author  : summer

class UpperAttrMetaClass(type):
	# __new__ 是在__init__之前被调用的特殊方法
	# __new__是用来创建对象并返回之的方法
	# 而__init__只是用来将传入的参数初始化给对象
	# 你很少用到__new__，除非你希望能够控制对象的创建
	# 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
	# 如果你希望的话，你也可以在__init__中做些事情
	# 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
	def __new__(cls, class_name, class_parents, class_attr):
		# 遍历属性字典，把不是__开头的属性名字变为大写
		new_attr = {}
		for name, value in class_attr.items():
			if not name.startswith("__"):
				new_attr[name.upper()] = value
		
		# 方法1：通过'type'来做类对象的创建
		return type(class_name, class_parents, new_attr)
		
		# 方法2：复用type.__new__方法  # 这就是基本的OOP编程，没什么魔法  # return type.__new__(cls, class_name, class_parents, new_attr)


# python3的用法
class Foo(object, metaclass=UpperAttrMetaClass):
	bar = 'bip'


print(hasattr(Foo, 'bar'))
# 输出: False
print(hasattr(Foo, 'BAR'))
# 输出:True

f = Foo()
print(f.BAR)  # 输出:'bip'
