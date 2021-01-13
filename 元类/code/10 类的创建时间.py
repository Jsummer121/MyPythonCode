# -*- coding: utf-8 -*-
# @Author  : summer

def a():
	print("Test——0")


def test(class_name, class_parents, class_attr):
	print("Test类——2")
	return type(class_name, class_parents, class_attr)


class Test(metaclass=test):
	print("Test类——1")
	pass


print("Test——3")

a()
t1 = Test()
t2 = Test()
print(id(t1))
print(id(t2))

# 执行结果
# -------
# Test类——1
# Test类——2
# Test——3
# Test——0
# 27402096
# 27402192
# -------
# 由上面代码可知，我们的函数是先定义，然后等调用的时候去创建，而我们的类却是先创建，然后等你调用，并且只创建一次，
# 如果由需要调用的时候，就分出一块地址然后让变量去引用。
