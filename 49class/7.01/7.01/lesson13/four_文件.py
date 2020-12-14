#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/1 21:34

# 桌面上文件操作流程：打开，读，关闭
# 电脑上文件操作流程：打开，读，关闭
# f = open(r"C:\Users\JiaNeng\Desktop\demo.txt", 'r', encoding='utf-8') # 绝对地址
f = open("demo.txt", 'r', encoding='utf-8')  # 相对地址
print(f.read())
f.close()

# 文件的基本操作：写入
f = open("demo.txt", "w", encoding="utf-8")
# f.write("hello,world")
f.writelines(["hello,TZ\n", "2", "3"])
f.close()
"""
write和writelines区别
1.write()传入的是字符串
2.writelines()传入既可以是字符串也可以是字符序列，注意不能是数字序列
"""

f = open("demo.txt", 'r', encoding='utf-8')
print(f.read())

# 刷新缓冲区，保存内容
# f.flush()
# 关闭文件
f.close()

# with语句
