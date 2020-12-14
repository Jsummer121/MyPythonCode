#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/1 22:14

# 1.r和w：只读和只写
# r只读
with open("demo.txt", "r", encoding="utf-8") as f:
    print(f.tell())
    print(f.read())

# w只写,文件已经存在会覆盖写入，不存在则创建文件写入
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("hahaha")

with open("demo1.txt", "w", encoding="utf-8") as f:
    f.write("hello")


# 2.rb和wb：只读和只写，非文本的读取和写入
s = ""
with open("联系方式.png", "rb")as f:
    print(f.tell())
    s = f.read()

with open("test.png", "wb")as f:
    f.write(s)
print("="*50)
# 3.a追加：在文件末尾增加，文件不存在创建新的文件
with open("demo.txt", "r", encoding="utf-8") as f:
    print(f.tell())
    print(f.read())

with open("demo.txt", "a", encoding="utf-8") as f:
    print(f.tell())
    f.write("托马斯")

with open("demo.txt", "r", encoding="utf-8") as f:
    print(f.tell())
    print(f.read())

with open("demo2.txt", "a", encoding="utf-8") as f:
    print(f.tell())
    f.write("托马斯")

# 4.r+,w+,a+
"""
r+:读写，指针在文件开头
w+:读写，文件已经存在会覆盖写入，不存在则创建文件写入
a+:读写，文件存在则在文件末尾追加，文件不存在创建新的文件
"""
with open("demo.txt", "r+", encoding="utf-8")as f:
    print(f.tell())
    print(f.read())
    f.write("nihao")
with open("demo.txt", "w+", encoding="utf-8")as f:
    f.read()
    f.write("=====")
with open("demo.txt", "a+", encoding="utf-8")as f:
    f.read()
    f.write("=====")
