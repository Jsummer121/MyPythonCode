# -*- coding: utf-8 -*-
# 设计一个小程序，让用户输入一个整数X，判断0 —— X 这个数之间有多少个数是5的倍数？
# 并把所有5的倍数用保存到一个列表里面，打印出来。

x = int(input("请输入一个大于0整数："))
a=[]
for i in range(1,x+1):
    if i%5 == 0:
        a.append(i)
print(a)