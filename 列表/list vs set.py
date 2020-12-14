# -*- coding: utf-8 -*-
import time
import random

l = [random.randrange(0, 1000000) for x in range(0, 1000000)]
s = {x for x in range(0, 1000000)}

print('set size=', len(s))
# 测试 list，搜索 1000次，看花费时间
start_time = time.time()
for i in range(0, 1000):
    x = random.randrange(0, 1000000)
    b = x in l
print('list index of time:', time.time() - start_time)

# 测试 list，搜索 1000次，看花费时间
start_time = time.time()
for i in range(0, 1000):
    x = random.randrange(0, 1000000)
    b = x in s
print('set index of time:', time.time() - start_time)
