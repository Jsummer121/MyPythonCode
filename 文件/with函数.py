#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/1 21:56

# f = open("demo.txt", "w", encoding="utf-8")
# f.writelines(["hello,world\n", "hello,TZ\n", "5"])
# f.close()
#
# f = open("demo.txt", "r", encoding="utf-8")
# print(f.read())
# f.close()

with open("demo.txt", "w", encoding="utf-8") as f:
    f.writelines(["你好世界\n", "你好潭州\n", "5"])


with open("demo.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 总结一下：
# 1.open打开方式我们用到了"r"读，"w"写两种方式
# 2.读用到了read，写用到了write还有writelines

# 光标
# tell() 以bytes为单位，从文件头到当前指针所在位置
# seek() 以bytes为单位，光标的偏移量
print("你好世界".encode("utf-8"))   # b'\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xb8\x96\xe7\x95\x8c'
with open("demo.txt", "r", encoding="utf-8") as f:
    print("1:", f.tell())
    print(f.read())
    print("2:", f.tell())
    f.seek(0)
    print("3:", f.tell())
    f.seek(2)
    print("4:", f.tell())
    print(f.read())  # 一个中文字符在python3里是3个字节，移动两个字节，中文被你拆开了。


