#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/2 20:32

# 1.read():读取文件（从指针所在的位置到文件结束为止）,字符串对象
with open("demo.txt", "r", encoding="utf-8")as f:
    file = f.read()
    print(file.strip())
    print(type(file))   # <class 'str'>

# 2.readline():每次读出一行内容，所以，读取占用内存小，适合大文件，字符串对象
with open("demo.txt", "r", encoding="utf-8")as f:
    line = f.readline()
    print(type(line))   # <class 'str'>
    while line:
        print(line.strip())
        line = f.readline()

# 3.readlines():读取整个文件所有行,保存在一个列表里，每行作为一个元素，读取大文件比较占内存
with open("demo.txt", "r", encoding="utf-8")as f:
    lines = f.readlines()
    print(type(lines))  # <class 'list'>
    for line in lines:
        print(line.strip())

