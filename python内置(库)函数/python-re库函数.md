# 正则表达式

## 1.概念

**正则表达式是一个工具，用来匹配或者提取字符串，用re库来实现，所有的正则表达式的语法都是一样的**

应用的地方：爬虫和web

格式：`re.findall()`:将符合规则的字符串，以列表的形式，全部返回。

正则表达式由普通字符和元字符组成。普通字符包括大小写的字母和数字，而元字符则具有特殊含义。

## 2.普通字符

将符合普通字符的字符串通过列表进行返回,大小写敏感。

```
import re
s1 = 'Tseting'
s2 = 'testing'
r1 = re.findall('test', s1) #['test'] 
r2 = re.findall('test', s2) #[]
# 忽略大小写re.I
r3 = re.findall('test', s2, re.I) #['Test']
```

## 3.元字符

**常用元字符**:`.  ^  $  {}  *  +  ? |  []`

### 3.1通配符（.）

匹配除换行符"\n"以外的单个字符

```
s1 = 'testing'
s2 = 'Testing\n'
r1 = re.findall('.', s1) #['t', 'e', 's', 't', 'i', 'n', 'g']
r2 = re.findall('.', s2) #['t', 'e', 's', 't', 'i', 'n', 'g']
# 同时也要识别换行符
r3 = re.findall('.', s2,re.S) #['t', 'e', 's', 't', 'i', 'n', 'g', '\n']
```

### 3.2 脱字符（^）

匹配输入字符串的开始位置

```
s = 'testing\nTesting\ntest'
r1 = re.findall("^test", s) #['test']
# 实现多行匹配
r2 = re.findall("^test", s, re.M) #['test','test']
# 实现多行匹配与忽略大小写
r3 = re.findall("^test", s, re.M | re.I) #['test','Test','test']
```

### 3.3 （$）

匹配输入字符串的结束位置

```
s = 'testing\nTesting\ntest'
r1 = re.findall("testing$", s) #[]
r2 = re.findall("testing$", s, re.M) #['testing']
r3 = re.findall("testing$", s, re.M | re.I) #['testing','Testing']
```

### 3.4 （* + ?）

匹配前面的子表达式的次数

| 符号 |    作用     |
| :--: | :---------: |
|  *   |   任意次    |
|  +   | 大于等于1次 |
|  ？  |   0或1次    |

```
s = 'z\nzo\nzoo'
r1 = re.findall('zo*', s) #['z','zo','zoo']
r2 = re.findall('zo+', s) #['zo','zoo']
r3 = re.findall('zo?', s) #['z','zo','zo']
```

### 3.5重复元字符（{}）

控制匹配子表达式的次数

```
s = 'z\nzo\nzoo'
r1 = re.findall('zo*', s) #['z','zo','zoo']
r2 = re.findall('zo{0,}', s) #['z','zo','zoo']
######################################
r3 = re.findall('zo+', s) #['zo','zoo']
r4 = re.findall('zo{1,}', s) #['z','zo','zoo']
######################################
r5 = re.findall('zo?', s) #['z','zo','zo']
r6 = re.findall('zo{0,1}', s) #['z','zo','zo']
```

### 3.6 字符组（[]）

大括号代表次数，中括号代表内容，匹配单个内容

```
s = 'test\ntesting\nTesting\nzoo'
r1 = re.findall('[e]',s)#['e', 'e', 'e']
r2 = re.findall('[es]',s)#['e', 's', 'e', 's', 'e', 's']
r3 = re.findall('[e-o]',s)#['e', 'e', 'i', 'n', 'g', 'e', 'i', 'n', 'g', 'o', 'o']
r4 = re.findall('^[e-o]',s，re.M)#[]
r5 = re.findall('[^e-o]',s)#['t', 's', 't', '\n', 't', 's', 't', '\n', 'T', 's', 't', '\n', 'z'] 这个表示排除这些字符
```

**注：如果存在换行符，则内部的n也是会被匹配的到的**

```
s = 'test\ntesting\nTesting\nzoo'
r1 = re.findall('[n]',s)#['n', 'n']
r2 = re.findall('[n]',s,re.s)#['n', 'n']
r3 = re.findall('[e-o]',s)#['e', 'e', 'i', 'n', 'g', 'e', 'i', 'n', 'g', 'o', 'o']
```

### 3.7 选择元字符（|）

```
s = 'z\nzood\nfood'
r1 = re.findall('z|food',s)#['z', 'z', 'food']
r2 = re.findall('[z|f]ood',s)#['zood','food']
```

### 3.8 分组元字符（()）

匹配表达式的字符，保存到临时区域，返回（）内的内容

```
s = 'z\nzood\nfood'
r1 = re.findall('[z|f]o*',s)#['z',zoo','foo']
r2 = re.findall('[z|f](o*)',s)#['', 'oo', 'oo']
```

### 3.9 取消字符串转义

在前面加r或者在加一个/

```
s = r'z\nzoo\nzooo'
s = 'z\\nzoo\\nzooo'
```

### 3.10 取消正则语法转义

在前面加\

```
s = 'www.123.com'
r1 = re.findall('.',s) #['w', 'w', 'w', '.', '1', '2', '3', '.', 'c', 'o', 'm']
r2 = re,findall('\.',s)#['.']
```

### 3.11 贪婪模式和非贪婪模式（记牢）

贪婪模式：`.*`或`.+`尽可能多的匹配字符

```
s = 'abcdasafaf'
r1 = re.findall(r'ab.*f',s) #['abcdasafaf']
r2 = re.findall(r'ab.+f',s) #['abcdasafaf']
```

非贪婪模式：`.*?`尽可能少的匹配字符

```
s = 'abcfdasafafafafafaf'
r1 = re.findall(r'ab.*f',s)		#['abcfdasafafafafafaf']
r2 = re.findall(r'ab.*?f',s)	#['abcf']
```

爬虫常用非贪婪

```
s = "<a href=#>2151216125612511251</a>"
r1 = re.findall(r'>(.*?)<',s)#['2151216125612511251']
```

## 4.预定义字符类

| **预定义字符类** | **说明**           | **对等字符类**  |
| ---------------- | ------------------ | --------------- |
| \d               | 任一数字字符       | [0-9]           |
| \D               | 任一非数字字符     | [^0-9]          |
| \s               | 任一空白符         | [\t\n\x0B\f\r]  |
| \S               | 任意非空白符       | [^\t\n\x0B\f\r] |
| \w               | 任一字母数字字符   | [a-zA-Z0-9]     |
| \W               | 任一非字母数字字符 | [^a-zA-Z0-9]    |

### 4.1 \d

```
s = "<a href=#>2151216125612511251</a>"
r1 = re.findall('\d',s)#['2', '1', '5', '1', '2', '1', '6', '1', '2', '5', '6', '1', '2', '5', '1', '1', '2', '5', '1']
r2 = re.findall('\d.*\d',s)#['2151216125612511251']
```

### 4.2 \D

```
s = "<a href=#>2151216125612511251</a>"
r1 = re.findall('\D',s)#['<', 'a', ' ', 'h', 'r', 'e', 'f', '=', '#', '>', '<', '/', 'a', '>']
```

### 4.3 \s

匹配任意空白符：空格、换行、制表符

```
s = 'awaio21rhq3qh5hwha  h你好\t\n\b'
r1 = re.findall('\s',s)#[' ', ' ', '\t', '\n']
```

### 4.4\S

```
s = 'awaio21rhq3qh5hwha  h你好\t\n\b'
r1 = re.findall('\S',s)#['a', 'w', 'a', 'i', 'o', '2', '1', 'r', 'h', 'q', '3', 'q', 'h', '5', 'h', 'w', 'h', 'a', 'h', '你', '好', '\x08']
```

### 4.5 \w

```
s = 'awaio21rhq3qh5hwha  h你好\t\n\b'
r1 = re.findall('\w',s)#['a', 'w', 'a', 'i', 'o', '2', '1', 'r', 'h', 'q', '3', 'q', 'h', '5', 'h', 'w', 'h', 'a', 'h', '你', '好']
```

### 4.6 \W

```
s = 'awaio21rhq3qh5hwha  h你好\t\n\b'
r1 = re.findall('\W',s)#[' ', ' ', '\t', '\n', '\x08']
```

### 实例

```
s = 'email:1245@qq.com'
r1 = re.findall('\d.*@\w+\.com')#['1245@qq.com']
```

## 5.修饰符

| 符号 |                          作用                          |
| :--: | :----------------------------------------------------: |
| re.I |                  忽略字符中的小大小写                  |
| re.S |                  使字符可以识别换行符                  |
| re.M | 实现多行匹配(一般不用，当用到$或^后需要考虑使用该符号) |

## 6.正则常用函数

### 1:re.findall(pattern, string, flags=0)

将匹配的全部内容放入一个列表中

```
s = 'Cats are Cat'
r1 = re.findall('C\w+',s)		#['Cats','Cat']
r2 = re.findall('(C\w+)',s)		#['Cats','Cat']
r3 = re.findall('C(\w)',s)		#['ats','at']
r4 = re.findall('(C)(\w),s')	#[('C', 'a'), ('C', 'a')]
```

### 2:re.math(pattern, string, flags=0)

从头匹配（只匹配字符串的开始，如果字符串快开始不符合正则表达式，则匹配失败返回None）

```python
s = 'Cats are Cat'
r1 = re.match('C\w+',s)		#<re.Match object; span=(0, 4), match='Cats'>
print(r1.group())			#'Cats'
r2 = r4 = re.match('(C)(\w),s')
print(r2.group())			#'Cats'
print(r2.groups())			#('C', 'ats')
s = 'cats are Cat'
re.match('C\w+',s)			#None
```

### 3:re.search(pattern, string, flags=0)

浏览全部字符串，匹配符合规则的第一个字符串

```
s = 'Cats are Cat'
r1 = re.search('C\w+',s)
print(re.group())		#'Cats'
s = 'cats are Cat'
r2 = re.search('C\w+',s)	
print(r2.group())		#'Cat'
r3 = re.search('(C)(\w+)',s)
print(r3.group())		#Cat
print(r3.groups())		#('C', 'at')
```

