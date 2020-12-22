# -*- coding: utf-8 -*-


L = [i for i in range(10)]
print(L)

G = (x*2 for x in range(5))
print(G)  # <generator object <genexpr> at 0x0031F930>

# 方法一，使用next方法
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
# print(next(G))  # StopIteration

# 方法二、用for循环依次获取
for i in G:
    print(i)

# 方法三、用list方法获取
print(list(G))
