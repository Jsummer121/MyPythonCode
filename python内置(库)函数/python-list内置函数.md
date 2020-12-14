# list内置函数

class list(object)
 |  list(iterable=(), /)
 |  Built-in mutable sequence.
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.

**列表，内置可变序列，如果没有给出可变参数，则创建一个空列表，如果指定了，则这个参数必须是可迭代的。**

 |  Methods defined here:
 | ` __add__`(self, value, /)
 |      Return self+value.
 |  `__contains__`(self, key, /)
 |      Return key in self.
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
 |  `__iadd__`(self, value, /)
 |      Implement self+=value.
 |  `__imul__`(self, value, /)
 |      Implement self*=value.
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 | ` __iter__`(self, /)
 |      Implement iter(self).
 |  `__le__`(self, value, /)
 |      Return self<=value.
 |  `__len__`(self, /)
 |      Return len(self).
 |  `__lt__`(self, value, /)
 |      Return self<value.
 |  `__mul__`(self, value, /)
 |      Return self*value.
 |  `__ne__`(self, value, /)
 |      Return self!=value.
 |  `__repr__`(self, /)
 |      Return repr(self).
 |  `__reversed__`(self, /)
 |      Return a reverse iterator over the list.
 |  `__rmul__`(self, value, /)
 |      Return value*self.
 |  `__setitem__`(self, key, value, /)
 |      Set self[key] to value.
 |  `__sizeof__`(self, /)
 |      Return the size of the list in memory, in bytes.

**以下为list内置函数**
 |  **append(self, object, /)**
 |      Append object to the end of the list.
**在当前列表的后面增加object**

```
>>> a = [1,2,3]
>>> a.append('4')
>>> a
[1, 2, 3, '4']
>>> a.append([1,2,3])
>>> a
[1, 2, 3, '4', [1, 2, 3]]
```

 |  **clear(self, /)**
 |      Remove all items from list.
**清除，将列表内的所有元素都清除**

```
>>> a = [1,2,3]
>>> a.clear()
>>> a
[]
```

 |  **copy(self, /)**
 |      Return a shallow copy of the list.
**复制出一个同样的列表，因为列表使用赋值号时，这两个指针同时指向一块内存，当一个指针修改后，另一个指针也会随着被动修改**

```
>>> a = [1,2,3]
>>> b = a
>>> a.append('1')
>>> a
[1, 2, 3, '1']
>>> b
[1, 2, 3, '1']
>>> c = a.copy()
>>> c
[1, 2, 3, '1']
>>> a.append([1,2,3])
>>> a
[1, 2, 3, '1', [1, 2, 3]]
>>> b
[1, 2, 3, '1', [1, 2, 3]]
>>> c
[1, 2, 3, '1']
```

 |  **count(self, value, /)**
 |      Return number of occurrences of value.
**计算value在列表中出现的次数并返回**

```
>>> a = [1,1,1,1,2,3,4,3,2,22,2,2]
>>> a.count(2)
4
>>> a.count(1)
4
```

 |  **extend(self, iterable, /)**
 |      Extend list by appending elements from the iterable.

**往列表后面延伸一块列表，类似于使用两个列表相加**

```
>>> a.extend([1,2,3])
>>> a
[1, 2, 3, 4, 5, 1, 2, 3]
>>> b = [1,2,3]
>>> a+b
[1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 3]
```

 |  **index(self, value, start=0, stop=2147483647, /)**
 |      Return first index of value.
 |      Raises ValueError if the value is not present.

**索引，从0到2147483647位开始索引，如果找到了则返回下标，如果没有则报错**如果列表长度大于2147483647，则需要重新传入stop值

```
>>> a = [1,2,3,4]
>>> a.index(2)
1
>>> a.index(5)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.index(5)
ValueError: 5 is not in list
```

 |  **insert(self, index, object, /)**
 |      Insert object before index.
**插入，在index位置前方插入一个object，并且如果index超出了列表的长度，并不会报错，只是在列表的最后面加上这个object**

```
>>> a = [1,2,3,4]
>>> a.insert(2,[1,2,3])
>>> a
[1, 2, [1, 2, 3], 3, 4]
>>> a.insert(6,[222,22,2])
>>> a
[1, 2, [1, 2, 3], 3, 4, [222, 22, 2]]
>>> a.insert(100,[00])
>>> a
[1, 2, [1, 2, 3], 3, 4, [222, 22, 2], [0]]
>>> a.append(1)
>>> a
[1, 2, [1, 2, 3], 3, 4, [222, 22, 2], [0], 1]
```

 |  **pop(self, index=-1, /)**
 |      Remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.

**删除，默认为删除最后一个元素也可以自己传入一个索引值，并且返回这个元素**

```
>>> a = [1,2,3,4,5]
>>> a.pop()
5
>>> a
[1, 2, 3, 4]
>>> b = a.pop()
>>> b
4
>>> a.pop(2)
3
>>> a
[1, 2]
```

 |  **remove(self, value, /)**
 |      Remove first occurrence of value.
 |      Raises ValueError if the value is not present.

**移除，从左往右，移除第一次出现value的值，如果不存在则报错**

```
>>> a = [1,2,3,4,3,3,]
>>> a.remove(3)
>>> a
[1, 2, 4, 3, 3]
>>> a.remove(3)
>>> a
[1, 2, 4, 3]
>>> a.remove(5)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.remove(5)
ValueError: list.remove(x): x not in list
```

 |  **reverse(self, /)**
 |      Reverse *IN PLACE*.
**将列表进行反向排序，并没有返回值，因此这里离不能使用复制号**

```
>>> a = [1,2,3,4]
>>> a.reverse()
>>> a
[4, 3, 2, 1]
```

 |  **sort(self, /, *, key=None, reverse=False)**
 |      Stable sort *IN PLACE*.
**正向排序，如果reverse默认为F，如果为T，则为反向排序**

```
>>> a = [1,2,3,4]
>>> a.sort()
>>> a
[1, 2, 3, 4]
>>> a.sort(reverse=True)
>>> a
[4, 3, 2, 1]
```

 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None