# -*- coding: utf-8 -*-
from collections import Counter


# 计数器，用于统计对象中每个元素出现的个数
# 通过字典形式统计每个元素重复的次数传
res = Counter('abcdabcaba')
print(res)  # 结果Counter({'a': 4, 'b': 3, 'c': 2, 'd': 1})

# dict的子类，所以也可以以字典的形式取得键值对
for k in res:
    print(k, res[k], end='  |  ')  # 结果 a 4  |  b 3  |  c 2  |  d 1  |
for k, v in res.items():
    print(k, v, end='  |  ')  # 结果 a 4  |  b 3  |  c 2  |  d 1  |

# 通过most_common(n)，返回前n个重复次数最多的键值对
print(res.most_common())  # 结果None
print(res.most_common(2))  # 结果[('a', 4), ('b', 3)]

# 通过update来增加元素的重复次数，通过subtract来减少元素重复的次数
a = Counter('abcde')
res.update(a)
print(res)  # 结果Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})，比原来的res增加了重复次数

b = Counter('aaafff')
res.subtract(b)
print(res)  # 结果Counter({'b': 4, 'c': 3, 'a': 2, 'd': 2, 'e': 1, 'f': -3})，还有负值，要注意

