#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/21 22:10

# li = dir(__builtins__)
# li = li[li.index('abs'):]
#
# for i in range(len(li)):
#     print("#{}.{}()".format(i + 1, li[i]))

li = [9, 2, 5, 8]
print(len(li))
print(min(li))
print(max(li))
print(sum(li))
print(sorted(li))
print(list(reversed(li)))

# 进制转换函数
print(bin(10))  # 0b1010
print(oct(10))  # 0o12
print(hex(10))  # 0xa

# enumerate # 返回一个可以遍历的对象
print(enumerate(li))    # <enumerate object at 0x000001FD47172CF0>

for i in enumerate(li):
    print(i)

print(dict(enumerate(li)))

# eval()    # 识别表达式，返回值
b = '1 + 2 + 3'
print(eval(b))

# exec()  # 识别赋值语句，没有返回值
b = 'x + y + z'
x = 1
y = 2
z = 3
print(eval(b))

s = """
z = 10
b = x + y + z
print(b)
print("ok")
"""
# x = 1
# y = 2
# exec(s)
# exec(s, {'x': 1, 'y': 2})
exec(s, {'x': 1, 'y': 2}, {'x': 5, 'y': 6})

# filter() 过滤器
# i = filter(函数，可迭代对象)
# 过滤，每个可迭代对象去执行函数，符合条件的留下，不符合的删去


def test(x):
    return x > 5


l1 = [10, 2, 5, 15, 8]
print(filter(test, l1))  # <filter object at 0x000001AE08A2B7F0>
print(list(filter(test, l1)))


# map :每个可迭代对象去执行函数,是对数据的处理，将结果返回
def func(num):
    return num * 10


l2 = [1, 2, 3]
print(map(func, l2))    # <map object at 0x000001848837B908>
print(list(map(func, l2)))    # [10, 20, 30]

# zip：将对象逐一的配对
l3 = ['k1', 'k2', 'k3']
l4 = ['v1', 'v2', 'v3']
print(zip(l3, l4))  # <zip object at 0x000002047F7AB408>
print(dict(zip(l3, l4)))    # {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

