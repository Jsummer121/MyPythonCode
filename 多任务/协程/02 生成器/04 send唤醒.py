# -*- coding: utf-8 -*-


def gen(val):
    i = 0
    while i < val:
        temp = yield i
        print("====temp====>", temp)
        i += 1


# 使用send
print("使用send方法")
g = gen(5)
print(next(g))
print(g.send("summer"))
print(next(g))
print(g.send("haha"))

# 使用next
print("-------使用next方法-----")
f = gen(5)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))  # None StopIteration
