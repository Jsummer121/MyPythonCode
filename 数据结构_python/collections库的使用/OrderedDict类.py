# -*- coding:utf-8 -*-
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# d['bar'] = 22 #对于一个已经存在的键，重复赋值不会改变键的顺序
for key in d:
    print(key, d[key])

print(d)  # OrderedDict([('foo', 1), ('bar', 2), ('spam', 3), ('grok', 4)])

# 创建一个有序字典
dic = OrderedDict()
dic['name'] = 'winter'
dic['age'] = 18
dic['gender'] = 'male'

print(dic)  # 结果OrderedDict([('name', 'winter'), ('age', 18), ('gender', 'male')])

# 将一个键值对放入最后
dic.move_to_end('name')
print(dic)  # 结果OrderedDict([('age', 18), ('gender', 'male'), ('name', 'winter')])
