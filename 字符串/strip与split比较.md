# strip

strip(self, chars=None, /)
    Return a copy of the string with leading and trailing whitespace remove.
If chars is given and not None, remove characters in chars instead

**将字符串按所给的值进行切割，并以字符串的形式返回，当不传入值时，char默认为空，与之对应的有`rstrip`和`lstrip`,左切割与右切割。**

```
>>> s = '     22    '
>>> s.strip()
'22'
>>> s.rstrip()
'     22'
>>> s.lstrip()
'22    '
```

**当传入的值不在两端时，则不进行切割，返回整个值**

```
>>> s = '1112421421512435124121'
>>> s.strip()
'1112421421512435124121'
>>> s.strip('1')
'242142151243512412'
>>> s.rstrip('2')
'1112421421512435124121'
>>> s.rstrip('1')
'111242142151243512412'
>>> s.lstrip('1')
'2421421512435124121'
```

# split

split(self, /, sep=None, maxsplit=-1)
    Return a list of the words in the string, using sep as the delimiter string.

sep
  The delimiter according which to split the string.
  None (the default value) means split according to any whitespace,
  and discard empty strings from the result.
maxsplit
  Maximum number of splits to do.
  -1 (the default value) means no limit.

**将字符串按照所给的值进行切片，并以列表值返回。如果什么都没传入，则默认为空字符。maxsplit是最多切几次，同样相似的函数有`rsplit`和`lsplit`。**

```
s = '1241221122124125121'
>>> s.split('1')
['', '24', '22', '', '22', '24', '25', '2', '']
>>> s.split('2')
['1', '41', '', '11', '', '1', '41', '51', '1']
>>> s.split('1',2)
['', '24', '221122124125121']
>>> s = '    125 11   '
>>> s.strip()
'125 11'
>>> s.split()
['125', '11']
```

