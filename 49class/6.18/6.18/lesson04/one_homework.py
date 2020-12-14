#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/18 19:48

# 1.找出两个列表中相同的元素
L1 = [1, 2, 3, 4]
L2 = [3, 4, 5, 6]
print(list(set(L1) & set(L2)))
# 2.新建一个字典，用3种方法往字典里面插入值；用 4 种方法取出values，用2种方法取出key
D = {
    'name': "托马斯",
    'age': 18
}
# 往字典里面插入值
D.setdefault('height', 180)  # 有则查，无则增
print(D)

D['qq'] = 123456
print(D)

D.update({"addr": "TZ"})
print(D)

# 用 4 种方法取出values
print(D['name'])
print(D.setdefault("age"))
print(D.get("addr"))
print(list(D.values())[0])
print(list(D.items())[0][1])

# 用2种方法取出key
print(list(D.keys())[0])
print(list(D.items())[0][0])

# 3.定义我们学过的每种数据类型，并且注明，哪些是可变，哪些是不可变的
"""
1.数字数据类型：不可变
2.字符串：不可变
3.列表：有序，可变，允许重复
4.元组：有序，不可变，允许重复
5.字典：无序，可修改，key唯一，value可以重复
6.集合：无序，可修改，不允许重复
"""
# 4.列表[‘hello’,‘python’,‘!’] 拼接并输出'hello python !' （至少两种以上的方法）
print("+"*20)
L = ['hello', 'python', '!']
print(L[0] + " " + L[1] + " " + L[2])

s = " ".join(L)
print(s)

print("%s %s %s" % (L[0], L[1], L[2]))
print("{} {} {}".format(L[0], L[1], L[2]))
print("{} {} {}".format(*L))



print("+"*20)
L = ['a', 'b', 'c', 'd']
# 索引和反向索引
print(L[0])
print(L[-4])

print(L[1:3])
print(L[-3:-1])
# 逆序
print(L[::-1])
# 逆序切片
print(L[2:0:-1])
print(L[-2:-4:-1])
