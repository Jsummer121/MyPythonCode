# -*- coding: utf-8 -*-
# @Author  : summer

Foo = type('Foo', (), {'bar': True})
# 上面类似于：class Foo: bar = True

# 可以将Foo当作普通类使用
print(Foo)  # <class '__main__.Foo'>
print(Foo.bar)  # True
f = Foo()
print(f)  # <__main__.Foo object at 0x012070B0>
print(f.bar)  # True


# 继承类
class NextFoo(Foo):
	pass


print(NextFoo)  # <class '__main__.NextFoo'>
print(NextFoo.bar)  # True

# 使用type继承
FooChild = type('FooChild', (Foo,), {})
print(FooChild)  # <class '__main__.FooChild'>
print(FooChild.bar)  # True
