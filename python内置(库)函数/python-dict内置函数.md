# 字典内置函数

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(`**kwargs`) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  Methods defined here:
 |  `__contains__`(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |  `__delitem__`(self, key, /)
 |      Delete self[key].
 |  `__eq__`(self, value, /)
 |      Return self==value.
 |  `__ge__`(self, value, /)
 |      Return self>=value.
 |  `__getattribute__`(self, name, /)
 |      Return getattr(self, name).
 |  `__getitem__`(...)
 |      x.__getitem__(y) <==> x[y]
 |  `__gt__`(self, value, /)
 |      Return self>value.
 |  `__init__`(self, /, `*args`, `**kwargs`)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  `__iter__`(self, /)
 |      Implement iter(self).
 |  `__le__`(self, value, /)
 |      Return self<=value.
 |  `__len__`(self, /)
 |      Return len(self).
 |  `__lt__`(self, value, /)
 |      Return self<value.
 |  `__ne__`(self, value, /)
 |      Return self!=value.
 |  `__repr__`(self, /)
 |      Return repr(self).
 |  `__setitem__`(self, key, value, /)
 |      Set self[key] to value.
 |  `__sizeof__`(...)
 |      D.`__sizeof__`() -> size of D in memory, in bytes
 **以下为字典的内置函数**
 |  **clear(...)**
 |      D.clear() -> None.  Remove all items from D.
**清除，将字典内所有元素都删光**

```
>>> a = {1:'2'}
>>> a.clear()
>>> a
{}
```

 |  **copy(...)**
 |      D.copy() -> a shallow copy of D
**将字典进行拷贝**

```
>>> a = {1:1}
>>> b = a.copy()
>>> a
{1: 1}
>>> b
{1: 1}
```

 |  **get(self, key, default=None, /)**
 |      Return the value for key if key is in the dictionary, else default.
**根据所给的key来查找字典内的所对应的值，如果没有，则返回default所给定的值，默认为None**

```
>>> a = {1:'1'}
>>> a.get(1)
'1'
>>> a.get(2,'no 2')
'no 2'
```

 |  **items(...)**
 |      D.items() -> a set-like object providing a view on D's items
**以字典独有的一种dict_items类型将字典内所有键值对按照元组的方式返回**

```
>>> a = {1:1,2:2,3:3}
>>> a.items()
dict_items([(1, 1), (2, 2), (3, 3)])
>>> type(a.items())
<class 'dict_items'>
```

 |  **keys(...)**
 |      D.keys() -> a set-like object providing a view on D's keys
**以字典独有的dict_keys返回字典内所有的键**

```
>>> a = {1:1,2:2,3:3}
>>> a = a.keys()
>>> a
dict_keys([1, 2, 3])
>>> type(a)
<class 'dict_keys'>
```

 |  **pop(...)**
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
**删除给定的键并且返回键所对应的值，如果键不存在，但是给了一个默认值，则返回默认值，如果没有默认值则报错**

```
>>> a = {1:1,2:2,3:3}
>>> a.pop(1)
1
>>> a
{2: 2, 3: 3}
>>> a.pop(4)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.pop(4)
KeyError: 4
>>> a.pop(4,'no 4')
'no 4'
```

 |  **popitem(...)**
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.

**删除字典最后一组键值对，并且返回这个键值对，如果字典为空，则报错**

```
>>> a = {1:1,2:2,3:3}
>>> a.popitem()
(3, 3)
>>> a
{1: 1, 2: 2}
>>> a.popitem()
(2, 2)
>>> a.popitem()
(1, 1)
>>> a.popitem()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.popitem()
KeyError: 'popitem(): dictionary is empty'
```

 |  **setdefault(self, key, default=None, /)**
 |      Insert key with a value of default if key is not in the dictionary.
 |      Return the value for key if key is in the dictionary, else default.

**根据所给的key查找字典中是否存在这个值，如果存在则返回key所以对应的值，如果不存在则按照所给的键和默认值插入字典，如果没给默认值也不存在该键，则创建一个值为None的键值对**

```
>>> a = {1:1,2:2,3:3}
>>> a.setdefault(2)
2
>>> a
{1: 1, 2: 2, 3: 3}
>>> a.setdefault(2,20)
2
>>> a
{1: 1, 2: 2, 3: 3}
>>> a.setdefault(20,20)
20
>>> a
{1: 1, 2: 2, 3: 3, 20: 20}
>>> a.setdefault(21)
>>> a
{1: 1, 2: 2, 3: 3, 20: 20, 21: None}
```

 |  **update(...)**
 |      D.update([E, ]`**F`) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]

**跟新，根据所给的字典进行查找，如果相应的键，则进行修改值，如果不存在则创建该键值对**

```
>>> a = {1:1,2:2,3:3}
>>> a.update({5:5})
>>> a
{1: 1, 2: 2, 3: 3, 5: 5}
>>> a.update({1:5})
>>> a
{1: 5, 2: 2, 3: 3, 5: 5}
```

 |  **values(...)**
 |      D.values() -> an object providing a view on D's values
**以字典独有的dict_values返回字典内所有的键**

```
>>> a = {1:1,2:2,3:3}
>>> a = a.values()
>>> a
dict_values([1, 2, 3])
>>> type(a)
<class 'dict_values'>
```

 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  `__new__`(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  `__hash__ `= None