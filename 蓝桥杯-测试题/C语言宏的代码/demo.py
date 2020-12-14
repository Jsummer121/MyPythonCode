# -*- coding: utf-8 -*-
start = 0
end = 0

# 打开文件，读取test.c文件内的内容
with open('test.c', 'r', encoding='UTF-8') as f:
    test = f.readlines()

num = 1  # 确定行数
type_ = 0  # 第几种情况0为不存在x86的情况（默认）
do = 0
for i in test:
    # 第一种情况：只存在#if defind(__x86_64__)的情况下
    if i == "#if defined(__x86_64__)\n" or i == "#ifdef __x86_64__\n":
        type_ = 1
        start = num + 1
        end = num + 1
    if type_ == 1 and i == "#endif\n":
        end = num - 1
        type_ = 4
        do = 1
        print("起始行为{}，结束行为{}。".format(start, end))
    # 第二种情况：第一个if为#if !defind(__x86_64__)，第二个为else的情况
    if i == "#if !defined(__x86_64__)\n" or i == "#ifndef __x86_64__\n":
        type_ = 2
    if type_ == 2 and i == "#else\n":
        type_ = 3
        start = num + 1
        end = num+1
    if type_ == 3 and i == "#endif\n":
        end = num - 1
        type_ = 4
        do = 1
        print("起始行为{}，结束行为{}。".format(start, end))
    num += 1

if type_ == 2 and do == 0:
    print("NULL")
