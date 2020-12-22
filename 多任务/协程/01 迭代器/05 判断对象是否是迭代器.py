# -*- coding: utf-8 -*-
from collections import Iterator

# 判断list是否是迭代器
print(isinstance([], Iterator))

print(isinstance(iter([]), Iterator))

print(isinstance(iter("abc"), Iterator))
