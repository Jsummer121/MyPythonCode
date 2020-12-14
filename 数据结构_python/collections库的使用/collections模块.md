#  Collections模块

​		在Python中，有一个很神奇的库存在：Collections，它提供了一些额外的数据结构，比如：

- Counter：计数器，用于统计元素的数量
- OrderedDict：有序字典
- defaultdict：带有默认类型的字典
- ChainMap：创建多个可迭代对象的集合。类字典类型
- namedtuple：可命名元组，通过名字来访问元组元素
- deque：双向队列，队列头尾都可以放，也都可以取（与单向队列对比，单向队列只能一头放，另一头取）



## 1.`__init__.py`

```python
'''This module implements specialized container datatypes providing
alternatives to Python's general purpose built-in containers, dict,
list, set, and tuple.

* namedtuple   factory function for creating tuple subclasses with named fields
* deque        list-like container with fast appends and pops on either end
* ChainMap     dict-like class for creating a single view of multiple mappings
* Counter      dict subclass for counting hashable objects
* OrderedDict  dict subclass that remembers the order entries were added
* defaultdict  dict subclass that calls a factory function to supply missing values
* UserDict     wrapper around dictionary objects for easier dict subclassing
* UserList     wrapper around list objects for easier list subclassing
* UserString   wrapper around string objects for easier string subclassing

'''

__all__ = ['deque', 'defaultdict', 'namedtuple', 'UserDict', 'UserList',
            'UserString', 'Counter', 'OrderedDict', 'ChainMap']
```



## 2.Counter

​		**计数器，用于统计对象中每个元素出现的个数**

```python
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


```



## 3.OrderedDict

​		**OrderedDict**在迭代操作的时候会保持元素被插入时的顺序，OrderedDict内部维护着一个根据键插入顺序排序的**双向链表**。每次当一个新的元素插入进来的时候，它会被放到链表的尾部。**对于一个已经存在的键的重复赋值不会改变键的顺序。**

​		需要注意的是，一个OrderedDict的大小是一个普通字典的**两倍**，因为它内部维护着另外一个链表。 所以如果你要构建一个需要大量OrderedDict 实例的数据结构的时候(比如读取100,000行CSV数据到一个 OrderedDict 列表中去)，那么你就得仔细权衡一下是否使用 OrderedDict带来的好处要大过额外内存消耗的影响。

​		在3.6版本之前，python自带的是字典类型是无序的（即dict内部存放的顺序与key放入的顺序无关），到了3.6之后，dict也是有序的，那么还需要OrderedDict干啥呢？其实这个对于OrderedDict来说，他基本能实现dict的功能，但部分功能做了升级，例如：popitem()。OrderedDict可以设置last参数，last默认为True即删除最后一个键值对，把last改为False，则以FIFO（先进先出）的原则来删除元素。另外OrderDict增加了一个move_to_end的方法。

```python
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
```



## 4.defaultdict

​		带有默认值的字典。父类为Python内置的dict

​		字典带默认值有啥好处？举个栗子，在使用dict时，如果调用的key是不存在的，则会抛出keyerror错误，但是如果是用defaultdiet创建的话，它自动会生成一个默认值，同时使用defalutdict创建的对象也是dict类型

```python
# -*- coding: utf-8 -*-
from collections import defaultdict

a = {}
print(a["key"])  # KeyError

b = defaultdict(list)
print(b["key"])  # []

c = defaultdict(lambda: "NO KEY")
print(c["key"])  # NO KEY

d = defaultdict(set)  # set()
print(d["key"])

print(isinstance(d,dict))  # True
```



## 5.ChainMap

​		一个 ChainMap 接受多个字典并将它们在逻辑上变为一个字典。然后，这些字典并不是真的合并在一起了，ChainMap 类只是在内部创建了一个容纳这些字典的列表并重新定义了一些常见的字典操作来遍历这个列表。大部分字典操作都是可以正常使用的，比如：

```python
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
```

​		作为ChainMap的替代，你可能会考虑使用 update() 方法将两个字典合并。这样也能行得通，但是它需要你创建一个完全不同的字典对象(或者是破坏现有字典结构)。同时，如果原字典做了更新，这种改变不会反应到新的合并字典中去。

```python
a = {'x': 1, 'y': 2}
b = {'y': 6, 'z': 3}
merge = dict(b)
print(merge)  # {'y': 6, 'z': 3}
merge.update(a)
print(merge)  # {'y': 2, 'z': 3, 'x': 1}
print(merge['x'], merge['y'], merge['z'])  # 1 2 3
a['x'] = 11
print(merge['x'])  # 1
```



## 6.namedtuple

​		可命名元组，给元组每个元素起一个名字，这样就可以通过名字来访问元组里的元素，增强了可读性；尤其对于坐标，html标签的长宽等，使用名字可读性更强；有点类似于字典了

​		用途：创建命名字段的元组。工厂函数

```python
# -*- coding: utf-8 -*-
from collections import namedtuple

circle_model = namedtuple("Circle", ["x", "y", "r"])

c1 = circle_model(1, 2, 3)
c2 = circle_model(2, 3, 4)
print(c1)  # Circle(x=1, y=2, r=3)
print(c2.x, c2.y, c2.r, sep="  |  ")  # 2  |  3  |  4
print(c2.__doc__)  # Circle(x, y, r)
```

​		接下来还有更加实用的：

```python
users_message = [
    ("summer",20,"www.123@qq.com"),
    ("july",20,"www.12@qq.com"),
    ("lixi",20,"www.1251@qq.com")
]

page_info = namedtuple("user_messages",["name","age","email"])
for User in users_message:
    user = page_info(*User)  # *User是解包
    print(user)
# user_messages(name='summer', age=20, email='www.123@qq.com')
# user_messages(name='july', age=20, email='www.12@qq.com')
# user_messages(name='lixi', age=20, email='www.1251@qq.com')
```

​		<font color="red">注意：nametuple是函数而不是类，因此下面的情况是错误的</font>

```python
namedtuple("winter",["first","last"])
year1 = winter(9,12)
print(year1)  # NameError: name 'winter' is not defined
```



## 7.deque

​		deque其实是 double-ended queue 的缩写，双向队列说到队列就要说到队列和栈了；队列是FIFO，栈是FILO

​		队列又分为：单向队列（只能从一边放，从另外一边取）；双向队列（两头都可以放，也都可以取）

​		Python中单向队列就是queue.Queue

​		用途：双端队列，头部和尾部都能以O(1)时间复杂度插入和删除元素。类似于列表的容器。这里需要注意一点，在python中，如果在列表的头部插入一个值，则它的时间复杂度为O(n)，因为在内存地址中，往第一个添加元素，后面的内存地址需要逐个往后移动一个。因此，如果遇到经常需要操作列表头的场景，还是使用队列较好。

下面是一些常用的方法：

```python
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
```



参考文案：

https://www.imooc.com/article/265193

https://www.cnblogs.com/deeper/p/8073412.html

