# -*- coding: utf-8 -*-
from collections import ChainMap


# 合并多个字典和映射
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
# 现在假设你必须在两个字典中执行查找操作
# (比如先从 a 中找，如果找不到再在 b 中找)。
# 一个非常简单的解决方案就是使用collections模块中的ChainMap类
c = ChainMap(a, b)
print(c)  # ChainMap({'x': 1, 'z': 3}, {'y': 2, 'z': 4})
a['x'] = 11  # 使用ChainMap时，原字典做了更新，这种更新会合并到新的字典中去
print(c)  # 按顺序合并两个字典 ChainMap({'x': 11, 'z': 3}, {'y': 2, 'z': 4})
print(c['x'])  # 11
print(c['y'])  # 2
print(c['z'])  # 3

# 对于字典的更新或删除操作影响的总是列中的第一个字典。
c['z'] = 10
c['w'] = 40
del c['x']
print(a)   # {'z': 10, 'w': 40}
# del c['y']  # 将出现报错:KeyError: "Key not found in the first mapping: 'y'"

# ChainMap对于编程语言中的作用范围变量（比如globals,locals等）
# 是非常有用的。事实上，有一些方法可以使它变得简单：
values = ChainMap()  # 默认会创建一个空字典
print('\t', values)  # 	 ChainMap({})
values['x'] = 1
values = values.new_child()  # 添加一个空字典
values['x'] = 2
values = values.new_child()
values['x'] = 30
#  values = values.new_child()  # ChainMap({}, {'x': 30}, {'x': 2}, {'x': 1}) 30
print(values, values['x'])  # values['x']输出最后一次添加的值  ChainMap({'x': 30}, {'x': 2}, {'x': 1}) 30
values = values.parents  # 删除上一次添加的字典
print(values['x'])  # 2
values = values.parents
print(values)  # ChainMap({'x': 1})

a = {'x': 1, 'y': 2}
b = {'y': 6, 'z': 3}
merge = dict(b)
print(merge)
merge.update(a)
print(merge)  # {'y': 2, 'z': 3, 'x': 1}
print(merge['x'], merge['y'], merge['z'])  # 1 2 3
a['x'] = 11
print(merge['x'])  # 1

