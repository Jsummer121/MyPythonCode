# -*- coding: utf-8 -*-
start = 0
end = 0

# 打开文件，读取test.c文件内的内容
with open('test.c', 'r', encoding='UTF-8') as f:
    test = f.readlines()

list = ['__x86_64__', '__ATOMIC_HLE_ACQUIRE', '__ATOMIC_HLE_RELEASE', '__DECIMAL_BID_FORMAT__', '__FXSR__',
        '__GCC_ASM_FLAG_OUTPUTS__', '__MMX__', '__SEG_FS', '__SEG_GS', '__SIZEOF_FLOAT128__', '__SIZEOF_FLOAT80__',
        '__SSE2_MATH__', '__SSE2__', '__SSE_MATH__', '__SSE__', '__amd64', '__amd64__', '__code_model_small__', '__k8',
        '__k8__', '__x86_64', '__x86_64__', 'i386', '__i386__', '__X86__', '_X86_']
num = 1  # 确定行数
type_ = 0  # 第几种情况0为不存在x86的情况（默认）
do = 0
for i in test:
    for j in list:
        # 第一种情况：只存在#if defind(__x86_64__)的情况下
        if i == "#if defined({})\n".format(j) or i == "#ifdef {}\n".format(j):
            type_ = 1
            start = num + 1
            end = num + 1
        if type_ == 1 and i == "#endif\n":
            end = num - 1
            type_ = 4
            do = 1
            print("起始行为{}，结束行为{}。".format(start, end))
        # 第二种情况：第一个if为#if !defind(__x86_64__)，第二个为else的情况
        if i == "#if !defined({})\n".format(j) or i == "#ifndef {}\n".format(j):
            type_ = 2
        if type_ == 2 and i == "#else\n":
            type_ = 3
            start = num + 1
            end = num + 1
        if type_ == 3 and i == "#endif\n":
            end = num - 1
            type_ = 4
            do = 1
            print("起始行为{}，结束行为{}。".format(start, end))
    num += 1

if type_ == 2 and do == 0:
    print("NULL")
