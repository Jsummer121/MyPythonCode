class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.

从给定的对象创建一个新的字符串对象。如果指定了编码或错误，则对象必须公开一个数据缓冲区，该缓冲区将使用给定的编码和错误处理程序进行解码。否则，返回对象的str类型或者repr类型， 默认编码为sys.getdefaultencoding().，默认错误为'strict'

 |  Methods defined here:
 |  __add__(self, value, /)
 |      Return self+value.

 |  __contains__(self, key, /)
 |      Return key in self.

 |  __eq__(self, value, /)
 |      Return self==value.

 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.

 |  __ge__(self, value, /)
 |      Return self>=value.

 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).

 |  __getitem__(self, key, /)
 |      Return self[key].

 |  __getnewargs__(...)

 |  __gt__(self, value, /)
 |      Return self>value.

 |  __hash__(self, /)
 |      Return hash(self).

 |  __iter__(self, /)
 |      Implement iter(self).

 |  __le__(self, value, /)
 |      Return self<=value.

 |  __len__(self, /)
 |      Return len(self).

 |  __lt__(self, value, /)
 |      Return self<value.

 |  __mod__(self, value, /)
 |      Return self%value.

 |  __mul__(self, value, /)
 |      Return self*value.*

 |  __ne__(self, value, /)
 |      Return self!=value.

 |  __repr__(self, /)
 |      Return repr(self).

 |  __rmod__(self, value, /)
 |      Return value%self.

 |  __rmul__(self, value, /)
 |      Return value*self.*
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.

 |  __str__(self, /)
 |      Return str(self).

# 以下为字符串的自带函数

 |  **capitalize(self, /)**
 |      Return a capitalized version of the string.

 |      More specifically, make the first character have upper case and the rest lower case.

​	**将字符串开头字母大写**

```
>>> a = 'abc'
>>> a.capitalize()
'Abc'
```

 |  **casefold(self, /)**
 |      Return a version of the string suitable for caseless comparisons.

​	**将字符串全变成小写**

```
>>> a = 'ABcd'
>>> a.casefold()
'abcd'
```

 |  **center(self, width, fillchar=' ', /)**
 |      Return a centered string of length width.
 |      Padding is done using the specified fill character (default is a space).

​	**将字符串居中，fillchar传入需要填充的字符串，默认是空格**

```
>>> a = 'ABcd'
>>> a.center(20,' ')
'        ABcd        '
>>> a.center(20,'+')
'++++++++ABcd++++++++'
```

 |  **count(...)**
 |      S.count(sub[, start[, end]]) -> int
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.

​	**返回字符串在S里面出现的次数**

```
>>> a = '1244'
>>> a.count('1')
1
>>> a.count('4')
2
```

 |  **encode(self, /, encoding='utf-8', errors='strict')**
 |      Encode the string using the codec registered for encoding.
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
	**对字符串进行编码,encoding传入编码的格式，默认为utf—8，error，用于编码错误的处理方法，包括（'ignore', 'replace' ,'xmlcharrefreplace'以及在编码器中注册的任何可能的其他名称）**

```
a = '1244'
>>> a.encode()
b'1244'
>>> a = '开开心心'
>>> a.encode()
b'\xe5\xbc\x80\xe5\xbc\x80\xe5\xbf\x83\xe5\xbf\x83'
```

 |  **endswith(...)**
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
**查看字符串的结尾是否是给定的字符串结尾，如果是返回True，如果不是则返回False**

```
a = '开开心心'
>>> a.endswith('心心')
True
>>> a.endswith('心')
True
>>> a.endswith('开')
False
```

 |  **expandtabs(self, /, tabsize=8)**
 |      Return a copy where all tab characters are expanded using spaces.
 |      If tabsize is not given, a tab size of 8 characters is assumed.
**返回用空格代替tab的字符串，一个tab默认转化为8个空格，可以根据tabsize来控制转化**

```
>>> a = '	awdf'
>>> a.expandtabs()
'        awdf'
>>> a
'\tawdf'
>>> b = a.expandtabs()
>>> b
'        awdf'
>>> b = a.expandtabs(tabsize=4)
>>> b
'    awdf'
```

 |  **find(...)**
 |      S.find(sub[, start[, end]]) -> int
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      Return -1 on failure.
**查找，从左到右查找需要查找的字符串，如果发现，就查看第一个遇见的下标，如果查找的元素在字符串内不存在，则返回-1**

```
>>> a = '12415'
>>> a.find('1')
0
>>> a.find('6')
-1
```

 |  **format(...)**
 |      S.format(*args, **kwargs) -> str
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
格式化输出：

```
s = 'Hello world'
print('{}'.format(s))
>>>'Hello world'
```

 |  **index(...)**
 |      S.index(sub[, start[, end]]) -> int
 |      Return the lowest index in S where substring sub is found, 
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      Raises ValueError when the substring is not found.
**索引，查看该字符串在字符串的下标位置，如果没有则返回ValueError。同样的如果存在两个要索引的对象，返回最左边的下标**

```
>>> a = 'abcdefg'
>>> a.index('c')
2
>>> a.index('h')
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.index('h')
ValueError: substring not found
>>> a = 'abcdefga'
>>> a.index(a)
0
```

 |  **isalnum(self, /)**
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
**如果字符串是字母-数字字符串（字符串里面只有数字和字母，没有其他），则返回True，如果不是返回False**

```
a = 'abcdefg'
>>> a.isalnum()
True
>>> a = '1245'
>>> a.isalnum()
True
>>> a = '\tas'
>>> a.isalnum()
False
>>> a = '21asfaf'
>>> a.isalnum()
True
>>> a = '21as  f'
>>> a.isalnum()
False
```

 |  **isalpha(self, /)**
 |      Return True if the string is an alphabetic string, False otherwise.
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.

**如果字符串是字母字符串，则返回true，否则返回false**

```
>>> a = '124'
>>> a.isalpha()
False
>>> a = 'abcdefg'
>>> a.isalpha()
True
>>> a = '124asd'
>>> a.isalpha()
False
```

 |  **isascii(self, /)**
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.

**如果字符串中的所有字符串都是ascii码，则返回true，如果是空字符串，也是属于ascii的**

```
>>> a = '1245'
>>> a.isascii()
True
>>> a = '你好'
>>> a.isascii()
False
>>> a = ''
>>> a.isascii()
True
```

 |  **isdecimal(self, /)**
 |      Return True if the string is a decimal string, False otherwise.
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.

**如果字符串是十进制字符串则返回True，否则为False**

```
>>> a = '12'
>>> a.isdecimal()
True
>>> a = '0b001'
>>> a.isdecimal()
False
```

 |  **isdigit(self, /)**
 |      Return True if the string is a digit string, False otherwise.
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
如果字符串是数字字符串则返回True，否则为false

```
>>> a = '12'
>>> a.isdigit()
True
>>> a = '0b001'
>>> a.isdigit()
False
```

 |  **isidentifier(self, /)**
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      Use keyword.iskeyword() to test for reserved identifiers such as "def" and
 |      "class".
**如果字符串是有效的python保留字，返回True否则返回fasle**

```
>>> a = 'def'
>>> a.isidentifier()
True
>>> a = '123'
>>> a.isidentifier()
False
```

 |  **islower(self, /)**
 |      Return True if the string is a lowercase string, False otherwise.
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
**如果字符串都是小写字母，返回True否则为False**

```
a = 'abc'
>>> a.islower()
True
>>> a = 'ABa'
>>> a.islower()
False
```

 |  **isnumeric(self, /)**
 |      Return True if the string is a numeric string, False otherwise.
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
**如果字符串是数字字符串，返回true**

```
>>> a.isnumeric()
True
>>> a = 'asf'
>>> a.isnumeric()
False
```

 |  **isprintable(self, /)**
 |      Return True if the string is printable, False otherwise.
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
**如果字符串可以打印，返回true**

 |  **isspace(self, /)**
 |      Return True if the string is a whitespace string, False otherwise.
 |      A string is whitespace if all characters in the string are whitespace and there is at least one character in the string.
**如果字符串空白字符串，返回True**

```
>>> a = ''
>>> a.isspace()
False
>>> a = ' '
>>> a.isspace()
True
>>> a = 'asfa'
>>> a.isspace()
False
```

 |  **istitle(self, /)**
 |      Return True if the string is a title-cased string, False otherwise.
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
如果字符串是大小写混合模式并且大写在前面，返回true，否则为False

```
>>> a = 'asdfAD'
>>> a.istitle()
False
>>> a = 'Abc'
>>> a.istitle()
True
```

 |  **isupper(self, /)**
 |      Return True if the string is an uppercase string, False otherwise.
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
**如果字符串都是大写字符串，则返回true**

```
>>> a = 'ABD'
>>> a.isupper()
True
>>> a = 'abA'
>>> a.isupper()
False
>>> a = 'Abc'
>>> a.isupper()
False
```

 |  **join(self, iterable, /)**
 |      Concatenate any number of strings.
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
**将列表转化为字符串，根据前面的字符串进行分割，并且列表内的所有值都得是字符串格式**

```
>>> a = [1,2,3,4]
>>> ''.join(a)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    ''.join(a)
TypeError: sequence item 0: expected str instance, int found
>>> a = ['1','2','3']
>>> ''.join(a)
'123'
```

 |  **ljust(self, width, fillchar=' ', /)**
 |      Return a left-justified string of length width.
 |      Padding is done using the specified fill character (default is a space).

**返回一个靠左对其的填充型字符串，默认为空格填充**

```
>>> a = '124'
>>> a.ljust(20,' ')
'124                 '
>>> a.ljust(20,'+')
'124+++++++++++++++++'
>>> a.ljust(20)
'124                 '
```

 |  **lower(self, /)**
 |      Return a copy of the string converted to lowercase.

**返回字符串所有的小写格式**

```
>>> a = 'abd'
>>> a.lower()
'abd'
>>> a = 'ABC'
>>> a.lower()
'abc'
>>> a = '123'
>>> a.lower()
'123'
```

 |  **lstrip(self, chars=None, /)**
 |      Return a copy of the string with leading whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
**返回一个从左边切割的字符串，默认为空格**

```
>>> a = '1241251'
>>> a.lstrip('1')
'241251'
>>> a = '     12'
>>> a.lstrip()
'12'
>>> a.lstrip('')
'     12'
>>> a.lstrip(' ')
'12'
```

 |  **partition(self, sep, /)**
 |      Partition the string into three parts using the given separator.
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
**将字符串根据所给定的字符串分为三部分，给定的字符串左边一部分，自己一部分和右边一部分，如果找不到，则返回整个字符串一部分，其他两部分都为空字符串**

```
>>> a = '1231241251'
>>> a.partition('1')
('', '1', '231241251')
>>> a.partition('c')
('1231241251', '', '')
```

 |  **replace(self, old, new, count=-1, /)**
 |      Return a copy with all occurrences of substring old replaced by new.
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
**替换，传入新的和就得值进行替换，count传入最大的替换次数，默认为-1**

```
>>> a = '12151241512512'
>>> a.replace('1','a')
'a2a5a24a5a25a2'
>>> a
'12151241512512'
>>> a.replace('1','a',2)
'a2a51241512512'
```

 |  **rfind(...)**
 |      S.rfind(sub[, start[, end]]) -> int
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      Return -1 on failure.
**做查找，从字符串右边开始查找，有的话就返回下标，没有就返回-1**

```
>>> a = 'qwraf12341'
>>> a.rfind('1')
9
>>> a.rfind('z')
-1
```

 |  **rindex(...)**
 |      S.rindex(sub[, start[, end]]) -> int
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      Raises ValueError when the substring is not found.
**从字符串右边进行索引，找到就返回下标，没有则返回ValueError**

```
>>> a = '12415asfafag'
>>> a.rindex('a')
10
>>> a.rindex('b')
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    a.rindex('b')
ValueError: substring not found
```

 |  **rjust(self, width, fillchar=' ', /)**
 |      Return a right-justified string of length width.
 |      Padding is done using the specified fill character (default is a space).
**将字符串进行右填充，默认为空格**

```
>>> a = '123'
>>> a.rjust(20)
'                 123'
>>> a.rjust(20,'+')
'+++++++++++++++++123'
```

 |  **rpartition(self, sep, /)**
 |      Partition the string into three parts using the given separator.
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
**从右边开始查找的将字符串分为3部分，如果没有找到字符串，则前两个个为空字符串，后面为整个字符串**

```
>>> a = '1241eagtwt1'
>>> a.rpartition('1')
('1241eagtwt', '1', '')
>>> a.rpartition('z')
('', '', '1241eagtwt1')
```

 |  **rsplit(self, /, sep=None, maxsplit=-1)**
 |      Return a list of the words in the string, using sep as the delimiter string.
 |        sep
 |          The delimiter according which to split the string.
 |          None (the default value) means split according to any whitespace,
 |          and discard empty strings from the result.
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      Splits are done starting at the end of the string and working to the front.

**从右边进行查找并分片，maxsplit为最大分几次**

```
>>> a = '1241eagtwt1'
>>> a.rsplit('t')
['1241eag', 'w', '1']
>>> a.rsplit('t',2)
['1241eag', 'w', '1']
>>> a.rsplit('t',1)
['1241eagtw', '1']
```

 |  **rstrip(self, chars=None, /)**
 |      Return a copy of the string with trailing whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
**删除右边的想要删除的字符串**

```
>>> a = '12211112'
>>> a.rstrip('2')
'1221111'
>>> a.rstrip('3')
'12211112'
```

 |  **split(self, /, sep=None, maxsplit=-1)**
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      sep
 |        The delimiter according which to split the string.
 |        None (the default value) means split according to any whitespace,
 |        and discard empty strings from the result.
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
**分片，左右两边同时分片，一般用来进行input输入时的操作**

```
>>> a = '   23    '
>>> a.strip()
'23'
>>> a = '   2'
>>> a.strip()
'2'
```

 |  **splitlines(self, /, keepends=False)**
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
**返回字符串中用换行分割的字符组成列表**

```
>>> a = '124  124 125 12512 512 '
>>> a.splitlines()
['124  124 125 12512 512 ']
>>> a = 'afraw\nwaf'
>>> a.splitlines()
['afraw', 'waf']
```

 |  **startswith(...)**
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 **如果字符串是以输入的字符开头，返回true**

```
>>> a = '124141'
>>> a.startswith('12')
True
>>> a.startswith('2')
False
```

 |  **strip(self, chars=None, /)**
 |      Return a copy of the string with leading and trailing whitespace remove.
 |      If chars is given and not None, remove characters in chars instead.

**分割，根据所给的字符串进行分割**

```
>>> a = '12121224214'
>>> a.split('2')
['1', '1', '1', '', '4', '14']
>>> a.split('1')
['', '2', '2', '2242', '4']
```

 |  **swapcase(self, /)**
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
**大小写交换**

```
>>> a = 'asqarAasfAFA'
>>> a.swapcase()
'ASQARaASFafa'
```

 |  **title(self, /)**
 |      Return a version of the string where each word is titlecased.
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
**将字符串进行标题化输出**

```
>>> a = 'hello world'
>>> a.title()
'Hello World'
```

 |  **translate(self, table, /)**
 |      Replace each character in the string using the given translation table.
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
**根据table来将字符串进行翻译**

 |  **upper(self, /)**
 |      Return a copy of the string converted to uppercase.
**将字符串所有字符进行大写**

```
>>> a = 'wraf'
>>> a.upper()
'WRAF'
```

 |  **zfill(self, width, /)**
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      The string is never truncated.
**给定一个长度，左边全部用0填充**

```
>>> a = '2141'
>>> a.zfill(20)
'00000000000000002141'
```

 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.