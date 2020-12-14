#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/18 21:43

# 赋值:只是创建一个变量，该变量指向原来的内存地址
n1 = {"k1": 'fei', "k2": 123, "k3": ["fly", 18]}
# 赋值
n2 = n1

n1["k1"] = "李波奇"
print(n1)
print(n2)

n1["k3"][0] = "溪日流水"
print(n1)
print(n2)

# 浅复制:在内存中只额外的创建第一层数据（若嵌套，只赋值嵌套最外面那层）
import copy
n3 = copy.copy(n1)

n1["k1"] = "二月兰"
print(n1)
print(n3)

n1["k3"][0] = "托马斯"
print(n1)
print(n3)

# 深拷贝 取所有值得最深层东西（最后面）
n4 = copy.deepcopy(n1)

n1["k1"] = "勿忘我"
print(n1)
print(n4)

n1["k3"][0] = "李贤滂"
print(n1)
print(n4)