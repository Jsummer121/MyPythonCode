# -*- coding: utf-8 -*-
# @Author  : summer


class Foo:
	bar = True
	
	
# 添加实例方法
def echo_bar(self):
	print(self.bar)


FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
# 让FooChild类中的echo_bar属性，指向了上面定义的函数
print(hasattr(Foo, 'echo_bar'))  # 判断Foo类中 是否有echo_bar这个属性
# False
print(hasattr(FooChild, 'echo_bar'))  # 判断FooChild类中是否有echo_bar这个属性
# True
my_foo = FooChild()
my_foo.echo_bar()
# True


# 添加静态方法
@staticmethod
def test_static():
	print("static_method..")


Foochild = type('Foochild', (Foo,), {"echo_bar": echo_bar, "test_static": test_static})
fooclid = Foochild()
print(fooclid.test_static)
# <function test_static at 0x01E3D540>
fooclid.test_static()
# static_method..
fooclid.echo_bar()
# True


# 添加类方法
@classmethod
def test_class(cls):
	print(cls.bar)
	

Foochild = type('Foochild', (Foo,), {"echo_bar":echo_bar, "test_static": test_static, "test_class": test_class})
fooclid = Foochild()
fooclid.test_class()
# True
