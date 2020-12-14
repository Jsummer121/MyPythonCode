# -*- coding: utf-8 -*-
from collections import deque

raw = [1, 2, 3]
d = deque(raw)
print(d)  # 结果deque([1, 2, 3])

# 右增
d.append(4)
print(d)  # 结果deque([1, 2, 3, 4])
# 左增
d.appendleft(0)
print(d)  # 结果deque([0, 1, 2, 3, 4])

# 右扩展
d.extend([5, 6, 7])
print(d)  # 结果deque([0, 1, 2, 3, 4, 5, 6, 7])
# 左扩展
d.extendleft([-3, -2, -1])
print(d)  # 结果deque([-1, -2, -3, 0, 1, 2, 3, 4, 5, 6, 7])

# 右弹出
r_pop = d.pop()
print(r_pop)  # 结果7
print(d)  # 结果deque([-1, -2, -3, 0, 1, 2, 3, 4, 5, 6])
# 左弹出
l_pop = d.popleft()
print(l_pop)  # 结果-1
print(d)  # 结果deque([-2, -3, 0, 1, 2, 3, 4, 5, 6])

# 将右边n个元素值取出加入到左边
print(d)  # 原队列deque([-2, -3, 0, 1, 2, 3, 4, 5, 6])
d.rotate(3)
print(d)  # rotate以后为deque([4, 5, 6, -2, -3, 0, 1, 2, 3])
