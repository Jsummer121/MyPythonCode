# -*- coding: utf-8 -*-


def add():
    a = 1
    yield a
    a += 1
    print(a,'======')
    yield a



b = add()

print(next(b))#激活生成器

print(next(b))


# 1
# 2 ======
# 2