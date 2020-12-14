# python基础知识总结

## 一、数字

### 1.将八进制转化为十进制

**int(0o12)**
**10**（其他类推）

### 2.字符串转化为数字

**int('89')**
**89**

### 3.用int将字符串数字强转进制位

**int('100',8)=64  int('40',8)=64,int('100000',2)=64**

#**int('0o40',16)=64**#

### 4.查看十进制转二进制后的长度

```python
L = 92
L.bit_length()  #7
```

### 5.整除与除

**x//y&x/y**

```
L = (5/2),(5/2.0),(5/-2.0),(5/-2)
M = (5//2),(5//2.0),(5//-2.0),(5//-2)
N = (9/3),(9.0/3),(9//3),(9//3.0)
####
L=(2.5, 2.5, -2.5, -2.5)
M=(2, 2.0, -3.0, -3)
N=(3.0, 3.0, 3, 3.0)
```

### 6.math函数的简单运用

```
import math
L = math.trunc(5/-2)  #-2（类似于取整）
M = math.floor(-2.9)  #-3（类似于取他左边的整数）
N = math.pi,math.e    #3.141592653589793,2.718281828459045
O = math.sin(2*math.pi/180) #0.03489949670250097
R = math.sqrt(2)            #1.4142135623730951
S = pow(2,4),2**4,2.0**4.0  #(16, 16, 16.0)
T = abs(-2),sum((1,2,3))     #(2, 6)
U = min(1,2,3),max(2,3,5,2,15,3,1)#(1, 15)
round(x,y) round函数将x进行四舍五入，并舍弃小数。y为要精确到哪一个数。
```

### 7.运算符

```
# 算术运算符：+，-，*，/，%，**，//
# 比较运算符：==，!=，>，<，>=，<=
# 赋值运算符：=，+=，-=，*=，/=，%=， **=，//=
# 逻辑运算符：and，or，not
# 成员运算符：in，not in
```

### 8.按位操作

```
1<<2  #1的二进制为0001，2表示向左移2位 0100 为4
   1|2                  1|1
0001|0010            0001|0001
  0011=3			   0001=1
```

```
   1&2                  1&1
0001&0010            0001&0001
0000 = 0             0001 = 1
```

```
x ^ y    异或
```

### 9.产生随机数

```
import random
a = random.random()   #产生0-1随机数
b = random.randint(1,10) #产生1-10随机整数
c = random.choice([1,2,3,4]) #随机选择一个数字
d = [1,2,3,4,5,6]
random.shuffle(d)    #将d顺序打乱
```

### 10.分数

```
from fractions import Fraction
a = Fraction(1,3)    #1/3
b = Fraction(2,6)    #1/3
c = Fraction('0.25') #1/4
f=2.5
z=Fraction(*f.as_integer_ratio()) #Fraction(5,2)
x = Fraction.from_float(2.5)   #5/2 
```

### 11.分数形式转化小数

```
import decimal
decimal.getcontext().prec = x
decimal.Decimal(1) / decimal.Decimal(3)
#按照第三行计算 取x为小数

```

### 12.小数转分数

```
2.5.as_integer_ratio()   #(5, 2)
```

### 13.格式化输出小数

```
x = '{:,.2f}'.format(64.23535) #64.24
b = "%.2f" %64.24235325       #64.24
```

# 二、字符串-书本 217

​         s    p    a    n
​         **0    1    2    3**
​        -4   -3   -2   -1

### 1.s='span'

```
  s[1:3]
  =pa
```

### 2.s[:3]=spa

### 3. s.find('an') 2

### 4.s.find('na')

-1

### 5.s+'nihao'

   spannihao

### 注意——字符串不可变，s[1]=w(是错的)

### 6.查看X的ASCII码

ord(X)

### 7.用dir函数查看定义的东西它所包含的函数

### 8.字符串对的包含关系：

可以包含在单引号和双引号中
当使用三个双引号时，内部的换行符也会被打印出来并且所有字符串变为一行

### 9.切片逆序输出

### **s[::-1]**

### 10.排序

**a.sort()**
**或者sorted()**

### 11.格式化

**'{0：o}'.format(64)**
**'100'**
**上面：前面的数字代表format里面的位置 ：代表分隔符 o代表转化所需的进制 或者在数字里面可进行小数表示**

### 12.转义字符串若不想执行可在‘’前面加一个r或者在原来的\后面再加个\

### 13.去除空白

```
s = 'hello.TZ'
# 移除空白strip() left right
# S.strip([chars]) -> str
s1 = " hello,TZ "
s = 'hello.TZ'
print(s)
print(s1)
print(s1.strip())    # 移除两端空格
print(s1.lstrip())   # 移除左端空格
print(s1.rstrip())   # 移除右端空格
print(s.strip("Z"))  # 移除两端指定的字符
```

### 14.小写变大写

**upper()**

### 15.将列表转化为字符串

**'*'.join(X*)**
***内为间隔内的东西
X*为要结合的东西**

### 16.print输出

**若要用for语句打印字符串 正常情况下是竖排的 可以在print（）内加入，end=‘’等‘’内部可以添加人空格等喜欢的东西**

**若不想有转义字符，或者单独想输出“\”可以进行print（r“”）或者在\后面再加一个\。**



### 17.字符串转化为列表

**list(s)**

### 18.分割split

```python
# S.split(sep=None, maxsplit=-1) -> list of strings
s = 'hello,TZ'
print(s.split(','))  # ['hello', 'TZ']
print(s.split())    # ['hello,TZ']
print(s.split("l", 1))    # ['he', 'lo,TZ']
print(s.split("l", 2))    # ['he', '', 'o,TZ']
```

# 三、列表

**L=[123,'span',1.23]**
**L+[1,2,3]**
**L=[123,'span',1.23,1,2,3]**

### 1.添加元素

```楷体
L = [1,2,3,4]
L.extend([5])
L.append(6)
L.insert(6,7) #【可以在任何地方加】
```

### 2.删除元素

```
L.pop(2)   	  #删除第n个
L.clear()     #清除
del L[3]      #删除第3个元素
del L[1:2]    #删除第1:2的片段
L[1:2] = []   #删除第1:2的片段
L.remove('1') #删除最左边的x
```

### 3.索引

**L.index(x) #查找**

### 4.计算

**可以在[]内进行加减乘除等运算。**

### 5.如果列表是二维的 要输出地2列

**[row[1] for row in L]**

### 6.正向排序

**L.sort()**

### 7.反转

**L.reverse()**

### 8.把列表L根据‘’进行化为字符串

**''.join(L)**

### 9.1 生成(0,4）的整数

**range（4）**

### 9.2 range(x,y,z)

**从x到y-1 以z为公差的等差数列。**

### 10.求和

**sum(L) #函数可以求列表内的和。**

### 11.map

**map函数可以生成一个新的列表.**
**m=[[1,2,3],[4,5,6],[7,8,9]]**
**map(sum(m))=[6,15,24]**

### 12.列表转化为元组

**L=[1,2,3]**
**S=tuple(L)**
**S==(1,2,3)**

# 四、元组

#### 定义：tuple元组是有序的不可变的元素集合

### 1.空元组 a = （）

```
a = ()  # 空元组
b = (1, False, 'ab', [], ())
print('a的类型是：', type(a))    # a的类型是： <class 'tuple'>
print('b的类型是：', type(b))    # a的类型是： <class 'tuple'>
```

```
# 注意：单元素元组要注意，带上‘，’
f = ('hello')
g = ('hell0',)
print('f的类型是：', type(f))    # f的类型是： <class 'str'>
print('g的类型是：', type(g))    # g的类型是： <class 'tuple'>
```

### 2.索引

```
T = ('a', 'b', 'c')
print(T[1])  # 通过索引去取值

# T.index(value, [start, [stop]]) -> integer
print(T.index('b'))  # 通过值去获取索引

# T.count(value) -> integer
print(T.count('b'))
```

### 3.长度

len(a)

### 4.切片

```
T[1:]
T[-2:]
```

### 5.包含

```
T = ('a', 'b', 'c')
a = 'c'
b = 'w'

print(a in T)
print(b in T)
```

# 五、字典

**{key:value}**

### 1.各种输入方法

#### ①d={'name':'jxx','age':20}

#### ②d=dict(name='jxx',age=20)

#### ③d=dict（zip(['name','age'],['jxx',20])）



### 2.嵌套

**ID={'name' :{'first':'jiang','last':'xinxin'},'like':['football','tabletenns']}**
**ID['name']**
**={'first':'jiang','last':'xinxin'}**
**ID['like'][-1]**
**='tabletenns'**

**'name' in ID**
**true**

**'first' in ID**
**False**

### 3.查找

D.get('name')

```
D={'a':1,'c':3,'b':2}
for key in sorted(D):
    print(key,'->',D[key])
a -> 1
b -> 2
c -> 3
```

```
for c in 'spam':
    print(c.upper())
S
P
A
M
```



### 4.字典视图

```
D = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3',
}

# D1 = {}
# L = [1, 2, 3]
# print(D1.fromkeys(L))
# print(D1.fromkeys(L, 'v'))
# 长度len()
print(len(D))

# 键、值、键值对
print(D.items())    # dict_items([('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3')])
print(D.keys())    # dict_keys(['k1', 'k2', 'k3'])
print(D.values())    # dict_values(['v1', 'v2', 'v3'])
```

### 5.例子

```
#2.新建一个字典
d = {}
#用3种方法往字典里面插入值
d = dict(lname = 'x',age = '20')
d.setdefault("like")
d['2name']='j'
#用 4 种方法取出values
print(d['lname'])
print(d.get('2name'))
print(list(d.values()))
print(d.setdefault("age"))
#用2种方法取出key
print(list(d.keys()))
z = [key for(key,value) in d.items()]
```

# 六、文件

```
# 1.r和w：只读和只写

# r只读

# w只写,文件已经存在会覆盖写入，不存在则创建文件写入

# 2.rb和wb：只读和只写，非文本的读取和写入

# 3.a追加：在文件末尾增加，文件不存在创建新的文件

# 4.r+,w+,a+

"""
r+:读写，指针在文件开头
w+:读写，文件已经存在会覆盖写入，不存在则创建文件写入
a+:读写，文件存在则在文件末尾追加，文件不存在创建新的文件
"""
```



### 1.write和writelines的区别

1.write()传入的是字符串
2.writelines()传入既可以是字符串也可以是字符序列，注意不能是数字序列



### 2.with函数

可以不用写close（）函数

```python
with open("demo.txt", "w", encoding="utf-8") as f:
    f.writelines(["你好世界\n", "你好潭州\n", "5"])


with open("demo.txt", "r", encoding="utf-8") as f:
    print(f.read())
```



### 3.tell()和seek()函数

tell()函数可以告诉你光标所在的位置

seek()可有把光标移动到你想要的位置

__注：因为中文在python的utf—8的编码为3字节，所以当你把光标移动到不是3的倍数是，读出来的数据会报错

### 4.read()读取文件(从指针所在的位置到文件结束为止)，字符串对象

注：line.strip()清除字符串两行的空白字符

```python
with open("static/demo.txt", "r", encoding="utf-8")as f:
    file = f.read()
    print(file.strip())
    print(type(file)) #<class 'list'>
```

### 5.readline():每次出一行内容，所以，读取占用内存小，适合大文件，字符串对象

```python
with open("static/demo.txt", "r", encoding="utf-8")as f:
    line = f.readline()
    print(type(line))   # <class 'str'>
    while line:
        print(line.strip())
        line = f.readline()
```

### 6.readlines():读取整个问价所有行，保存在一个列表里，每行作为一个元素，读取大文件比较占内存

```python
with open("static/demo.txt", "r", encoding="utf-8")as f:
    lines = f.readlines()
    print(type(lines))  # <class 'list'>
    for line in lines:
        print(line.strip())
```

### 7.with为什么可以实现文件自动打开和关闭呢？—上下文管理器

```python
class RunTime:
    def __enter__(self):
        print("进来了")
        self.start_time = datetime.now()
        print(self.start_time)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = datetime.now()
        print(self.end_time)
        print("出去了")
        print("运行时间：{}".format(self.end_time - self.start_time))


run = RunTime()

with run as a:  # 上下文管理器
    print("我是type")
    for i in range(100000):
        type("hello")
```

# 七、编码

### 1.字符串编码

```
计算机其实是只认识0和1的，我们编写的代码，要让计算机认识，中间涉及到字符转换为数字0和1的过程，这个过程实际就是一个字符如何对应一个特定的数字的标准，这个标准就称之为字符编码

0/1 = 1bit
1byte = 8bit    # 计算机的最小存储单位 0-255的数值

字符编码的发展史00000000
第一个阶段：
考虑英文ASCII（英文字符/键盘上的所有字符）
ASCII码用一个字节代表一个字符

第二个阶段：
各个国家纷纷定制了自己的字符编码
GBK使用两个字节（2bytes）代表一个字符 2**16-1 65535

第三个阶段：
unicode兼容万国语言 使用两个字节（2bytes）代表一个字符

第四个阶段：
utf-8：对英文字符1byte表示，中文3bytes
```



```
# 总结：
1.为了处理英文字符，产生了ASCII码
2.为了处理中文字符，产生了GBK
3.为了处理各国字符，产生了Unicode
4.为了提高存储和传输性能，产生了utf-8
```



```
# 重点：python3下字符编码使用情况

unicode：简单粗暴，所有字符都是2bytes，优点字符--》数字的转换速度快，缺点占用空间大
utf-8：精准，对不同的字符用不同的长度表示，优点：节省空间，缺点：字符--》数字的转换速度慢

python3中字符编码实际类型使用
1.内存中使用的就是unicode，用空间换时间
2.硬盘中或者网络传输用utf-8，尽可能节省带宽，保证数据传输的稳定性
```



```
# 编码（encode）和解码（decode）

# 编码（encode）：将unicode转换为其他指定的编码

# 解码（decode）：将原编码转换为unicode编码
```



### 2.赋值深浅复制

1.字符串（数字）：在内存中是一次性创建的，不能直接修改，如需修改，需要重新创建
2.列表等可修改的数据类型：在内存中创建时是以链表的形式创建
3.字符串、数字：赋值、深浅拷贝都没有意义，因为其永远指向同一个内存地址
4.列表、元组、字典

```python
# 赋值:只是创建一个变量，该变量指向原来的内存地址
n1 = {"k1": 'fei', "k2": 123, "k3": ["fly", 18]}
# 赋值
n2 = n1

n1["k1"] = "李波奇"
print(n1)
print(n2)

n1["k3"][0] = "溪日流水"
print(n1)
print(n2)

# 浅复制:在内存中只额外的创建第一层数据（若嵌套，只赋值嵌套最外面那层）
import copy
n3 = copy.copy(n1)

n1["k1"] = "二月兰"
print(n1)
print(n3)

n1["k3"][0] = "托马斯"
print(n1)
print(n3)

# 深拷贝 取所有值得最深层东西（最后面）
n4 = copy.deepcopy(n1)

n1["k1"] = "勿忘我"
print(n1)
print(n4)

n1["k3"][0] = "李贤滂"
print(n1)
print(n4)
```

### 3.bytes和bytearray(字符串，列表）

```python
print(type("ffff"))
print(type(b"ffff"))
# bytes是byte的序列，字符串是字符的序列
# str---》bytes
s1 = "中"
b1 = s1.encode('utf-8')
print(b1)
# bytes--->str
s2 = b1.decode("utf-8")
print(s2)

# 拓展
# str---》bytes
s = '托马斯'
b1 = bytes(s, encoding='utf-8')
b2 = bytes(s, encoding='GBK')
print(b1)
print(b2)

# bytes--->str
s1 = str(b1, encoding='utf-8')
s2 = str(b2, encoding='gbk')
print(s1)
print(s2)

# bytearray
s1 = "你好，朦胧"
b1 = bytearray(s1.encode('utf-8'))
print(b1)
print(type(b1))

print(b1.decode('utf-8'))

b1[:6] = bytearray("美丽", encoding="utf-8")
print(b1)
print(b1.decode('utf-8'))
```

# 八、函数

### 1.函数基础

```
1.函数定义：函数头、函数接口、函数体、函数返回值
2.函数调用：函数名（）
3.函数参数：形参，必须参数，默认参数，动态参数（*args，**kwargs）；实参，位置参数，关键字参数
```

#### 1.函数定义

![1561121236729](E:/python-summer-1/函数/1561121236729.png)

##### 1.1.解释器是怎么处理定义函数：

![1561121542832](E:/python-summer-1/函数/1561121542832.png)



#### 2.函数的调用

函数名（参数1，参数2.。。。。。。）

只要函数在内存已经存在，那么在程序的任何位置都是可以调用的

### 2.函数参数

```
def sum(y, a, b, c=666):   # a, b, c形式参数，简称形参，函数没有调用时，它没有任何意义，调用时，它必须传入参数，所以也叫必须参数。
    result = a + b + c
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print(result)


"""
def sum(a, b, c=666):   # c=666默认参数，不传入实参时，形参默认为666，但是，你如果传入实参，它也能接收
# 注意：默认参数一定要写在必须参数的后面，语法规则
"""

# sum(11, 22)
sum(25, b=11, c=22, a=33)  # 11, 22, 33实际参数，简称实参，按照位置，与形参一一对应，所以它也叫位置参数

"""
sum(b=11, c=22, a=33)   # b=11, c=22, a=33关键字参数，函数参数会通过关键字去找，不需要一一对应
# 注意：关键字参数和位置参数一起使用时，关键字参数必须要写在位置参数的后面，这是语法
"""
```

```
# 动态参数。
# def f1(*args, **kwargs):
"""
*args, **kwargs
星号是关键字
args，kwargs是变量名，规范
调用函数时，所有传入的 多余的 位置参数都会被args接收生成一个元组
调用函数时，所有传入的 多余的 关键字参数都会被kwargs接收生成一个字典
"""
```

### 3.内置函数（见附件--07-python3内置函数大全 (1).html）

### 4.匿名函数

```
f = lambda 变量名：返回值
f()
```

### 5.函数作用域

```
1.函数内部定义的变量是局部变量，函数外无法调用--局部作用域
2.函数外定义的变量是全局变量
```

```
# 总结：
"""
1.函数内部定义的为局部变量，其作用域是局部作用域，函数外无法调用的
2.函数外定义的为全局变量，其作用域是全局作用域，如果在函数内想要进行修改，需要global
3.外层函数的变量，如果想要在内层函数进行修改，需要nonlocal
"""
```

### 6.闭包

1. 函数嵌套流程图![1561383958219](E:/python-summer-1/函数/1561383958219.png)
2. 注意：函数名（）----》函数调用，不带括号，函数名可以看做是一个变量
3. 闭包的流程图![1561384765091](E:/python-summer-1/函数/1561384765091.png)

### 7.递归函数![1561386666886](E:/python-summer-1/函数/1561386666886.png)



# 九、函数继承和魔术方法

定义：重用代码，方便代码的管理和修改

### 1.访问方法

1.类。若果找不到，转到其父类中查找

2.直接基类。如果再找不到，转到父类的父类中查找

3.简介基类。

### 2.多继承的优先级

子类先查前面的父类若第一个父类有父类在以此进行检查

### 3.super函数可以调用父类的方法

```python
class A:
    def run(self):
        print("happy")


class B:
    def eat(self):
        print("miaomiaomiao")


class C(B,A):
    def run(self):
        super().run()   # super函数可以调用父类的方法，
        print("fly")


c = C()
c.run()
```

### 4.魔术方法

##### 1.运算符

```python
class Test:
    """这是一个测试类"""
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        res = self.num + other.num
        print(res)
        # return res


a = Test(66)
b = Test(88)

a + b
```

上面的__add__可以换成其他的运算符

##### 2.str和repr

作用：在交互模式下输出交互信息与直接print有些不同

```python
class A:
    def __str__(self):
        return "你好"

    def __repr__(self):
        return "hello"


a = A()
print(a)    # <__main__.A object at 0x000001733935B978>
```

在python中，str和repr方法在处理对象的时候，分别调用的是对象的__str__和__repr__方法
print也是如此，调用str函数来处理输出的对象，如果对象没有定义__str__方法，则调用repr处理
在 shell 模式下，展示对象 __repr__ 的返回值

##### 3.类的直接调用

__call__函数

```python
class B:
    """这是一个测试类"""
    def __init__(self, num):
        self.num = num
        self.eat = "food"
        self.run = "happy"

    def __call__(self, *args, **kwargs):
        print("ok")


b = B(66)
b()  # 直接调用会报错，想要直接调用，加上__call__
```

##### 4.其他魔术方法

1.__class__查看类名

2.__base__查看继承的父类

3.__bases__查看继承的全部父类

4.__dict__查看全部属性，返回属性值

5.__doc__查看对象文件

6.__dir__查看全部属性和方法

# 十、循环



# 十一、类



### 1.类的定义

```
# 面向过程编程：程序按照流程一步步往下走
tu = ('fei', 18, 160)
di = {'name': 'sophia', 'age': 20, 'height': 165}

print(dict(zip(di.keys(), tu)))  # {'name': 'fei', 'age': 18, 'height': 160}
print(tuple(di.values()))   # ('sophia', 20, 165)


# 面向函数编程：将不同的功能设置成不同的函数，在需要的时候随时调用
def func(tu, di):
    return dict(zip(di.keys(), tu)), tuple(di.values())


x, y = func(tu, di)
print(x)
print(y)

# 面向对象编程：类
# 一切事物皆为对象
# 面向对象最重要的概念是类（class）和实例（instance）
```

![1561466649829](E:/python-summer-1/类/1561466649829.png)

​	**类的定义**

```
class Cat:
    """这是一个猫类"""

# class 关键字
# Cat 类名 大驼峰命名法
# """这是一个猫类""" 解释类的用途
```

**实例化对象**

```
orange = Cat()
```

### 2.类属性

```
# 实例属性
# 类属性
# 私有属性
# 初始化
# __   __
# __init__, 实例化之后自动被调用,完成实例的初始化


class Cat:
    """这是一个猫类"""
    def __init__(self, color, eat):
        self.color = color  # 实例属性：记录是具体对象的特征
        self.eat = eat
        print("内部调用：", self.color)   # 内部调用：需要加上self


kitty = Cat('white', 'milk')    # kitty, 'white', 'milk'
print(kitty.color)

orange = Cat('orange', 'food')  # orange, 'orange', 'food'
print(orange.eat)   # 外部调用：实例名.属性


# 类属性：记录与类相关的特征
# 在__init__外初始化的
class Cat:
    """这是一个猫类"""
    count = 0   # 类属性

    def __init__(self, color, eat):
        self.color = color  # 实例属性：记录是具体对象的特征
        self.eat = eat
        # 计数
        Cat.count += 1  # 内部调用：类名.类属性名


# 实例化对象
kitty = Cat('white', 'milk')
orange = Cat('orange', 'food')
hua = Cat('hua', 'fish')

# 输出创建对象的个数
print("现在创建了{}只猫".format(Cat.count))    # 外部调用：类名.类属性名
print(kitty.count)  # 外部调用：实例名.类属性名


# 总结
"""
实例可以访问实例属性，实例可以访问类属性
类只能访问类属性
"""

# 3.私有属性
# a.单下划线开头：只是告诉别人这是私有属性，外部依然可以访问更改
# b.双下划线开头：外部不能通过实例名(instancename).属性名(propetyname)来访问或者更改


class Cat:
    def __init__(self, color, eat):
        self._color = color
        self.__eat = eat


kitty = Cat('white', 'milk')
print(kitty._color)
# print(kitty.__eat)
```

### 3.类方法

```
# 类和函数
class Cat:
    """这是一个猫类"""
    def __init__(self, color, age):
        self.color = color
        self.age = age


kitty = Cat("white", 2)
hua = Cat("hua", 1)

# 以上部分，我们实现了：1.创建了Cat类 2.实例化了两个对象kitty&hua


# 接下来，我们来创建一个函数,实现上面两只猫猫的年龄求和后的新属性，给第三只猫
def add_cat(name, c1, c2):
    cat = Cat(name, c1.age + c2.age)
    return cat


yellow = add_cat("yellow", kitty, hua)
print(yellow.age)

red = add_cat("red", kitty, yellow)
print(red.age)


# 方法：和某个特定的类相关联的函数
# 函数--->方法：只需要将函数的定义移动到类的定义中即可
class Cat:
    """这是一个猫类"""
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def print_cat(self):
        print("{}-{}".format(self.color, self.age))


kitty = Cat("white", 2)
hua = Cat("hua", 1)

# print_cat调用
Cat.print_cat(kitty)

kitty.print_cat()

# 封装：self指向对象，在对象中封装数据，对类进行优化的方法，就叫封装


class Cat:
    """这是一个猫类"""
    count = 0   # 类属性

    def __init__(self, name, color, eat, age):
        self.eat = eat
        self.name = name    # 实例属性
        self._color = color  # 外部可访问私有属性
        self.__age = age    # 外部不可访问私有属性
        Cat.count += 1  # 内部调用：类名.类属性名

    def print_cat(self):
        print("{}-{}-{}".format(self._color, self.__age, self.name))

    def __get_none(self):
        # 私有方法，不可以被实例和类直接调用
        return "我是私有方法"

    def test(self):
        self.__get_none()


kitty = Cat('kitty', 'white', 'milk', 2)
print(kitty.eat)
print(Cat.count)
print(kitty.count)

kitty.print_cat()
# kitty.__get_none()
```



### 5.类是一个独立存放 变量的空间

##### 注：每个实例都是一个独立的变量空间。不同实例之间的空间互不可见

运算符“.”—用于进行变量空间的计算

```
class Person:
	pass
p1 = Person()
p2 = Person()
p1.var = '在实例中封装的变量'
print(p1.var)
print(Person.var)  #类中找不到，不回去找实例中的
print(p2.var)   #p2也没有，去找Person也没有
```



### 6.类与实例之间的关系

类：是实物的抽象，不是真实存在的，描绘了该类事物的共性。如：动物、植物

实例：某类实物的具体个体，是该类实物及具体表现，他是真实存在的。如：小明，小红

### 7.实例方法表示的是实例的行为

##### 调用过程

​	通常，将默认会传入的那个参数命名为self，用来表示调用这个方法的实例对象本身。

​	方法总是定义在类中，但是却叫"实例方法"，因为它表示该类所有实例所共有的行为。

### 8.--init__

它会在实例化之后自动被调用，以完成实例的初始化。

orange = cat()

这时已经将orange进行初始化

# 十二、装饰器

### 1.__new__单例模式

如果不想把实例弄在两个不同的空间，可以使用new来改变

```python
class Earth:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):  # 如果我的类没有实例对象，那我就去new一个实例对象
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.name = 'earth'


e = Earth()
print(e)
a = Earth()
print(a)
```

### 2.定制属性（增删改查）

#### 1.增

```python
one.num = 1
#（据点法）
#魔术方法给了我们一个自定义的接口，函数的执行底层其实就是去调用了魔术方法。
setattr(one.num.txt,2)#设置属性
one.__setattr(num.txt,3)
```

#### 2.查

```python
print(hasattr(one, 'num'))  # 是否有该属性，返回布尔值
print(getattr(one, 'num'))  # 获取属性值
print(one.__getattribute__("num"))  # 获取属性值
```

#### 3.改

```python
setattr(one, 'num1', 66)    # 无则增
setattr(one, num.txt, 88)    # 有则改
one.__setattr__("num2", 55)  # 无则增,有则改
one.__setattr__(num.txt, 66)
print(one.num)
print(one.num2)
```

#### 4.删

```python
del one.num
delattr(one, "num2")
one.__delattr__("num2")
```

#### 5.自定义

```python
class Rectangle:    # 矩形类：正方形、长方形
    def __init__(self, length, width):  # __init__实例化对象时自动调用
        self.length = length
        self.width = width

    def __getattr__(self, item):
        return "no attribute"   # 当属性不存在时，调用此方法，如果没有定义此方法报错

    def area(self):
        areas = self.length * self.width
        return "面积是：{}".format(areas)


a = Rectangle(66, 88)
a.num = 1 #如果没有定义将调用__getattr方法
print("有属性：", a.length)
print(a.num)
```

### 3.描述符

上一个实例对象拿来做这一个类的类熟悉，这就是描述符

类里面实例化另一个类，对这个实例做访问的时候，需要定义__get__,__set__,__delete__方法来实现属性的增删改查

#### ①.查

会去第一个类里面执行__get方法

#### ②.改

会去第一个类里面执行__set方法

#### ③.删除

会去第一个类里面执行__delete方法

### 4.装饰器

闭包：函数里面嵌套函数，外层函数返回内层函数的函数名
装饰器：本质就是闭包。
不修改原函数的前提下，方便的增加函数功能

用@+想调用的函数名

### 5.内置装饰器

#### 1.property

可以直接使用，但是又不能随意修改。

#### 2.staticmethod

方法边静态，没有参数绑定无需再方法后面的括号内加self，解绑，无需实例化就可以调用方法，执行效率高。

#### 3.classmethod

方法边类方法

```python
class Cat:
    """这是一个猫类"""
    name = '猫'

    def __init__(self, color, eat):
        self.color = color
        self.eat = eat

    @property
    def print_cat(self):
        print("{}-{}".format(self.color, self.eat))

    @staticmethod   # 方法变静态方法，没有参数绑定
    def func():
        print("我来测试静态方法")
        print("我不需要self参数也能运行")
        print("我不需要实例化也能运行")

    @classmethod    # 类方法
    def func1(cls):  # cls代表类本身
    # def func1(self, cls):  # cls代表类本身
        print("="*50)
        print("我是来测试类方法的")
        print(cls)
        print(cls.name)


Cat.func()  # 解绑，不用实例化就可以调用方法。执行效率高
kitty = Cat('white', 'food')
print(kitty.color)
kitty.color = "hua"
print(kitty.color)
# kitty.print_cat()   # 调用类内方法的方式

# 1.property装饰器：方法变属性
# class、instance、property
# 使用起来方便，但是又不能随意去修改
kitty.print_cat

# 2.staticmethod装饰器：方法变静态方法，没有参数绑定
# 只在类本身生效
kitty.func()
Cat.func()

# 3.classmethod装饰器：方法变类方法
kitty.func1()
print("以下是类名.类方法")
Cat.func1()
# 属性：实例是可以调用实例属性、类属性，类只能调用类属性
# 方法：实例是可以调用类内方法、类方法，类只能调用类方法
# Cat.func1(kitty)
```

### 6.类作装饰器

```python
class Test:
    """这是一个用来做装饰器的类"""
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("前增加")
        self.func(*args, **kwargs) #这里必须为self.func()
        print("后增")
```

# 十三、迭代器生成器

### 1.迭代器

#### 1.1 可迭代对象的判断

```
# 1.for
# 2.'__iter__'
li = [1, 2, 3, 4, 5]
print(dir(li))  # '__iter__'
```

#### 1.2 迭代器：容器，将可迭代对象通过iter包起来

```
li = [1, 2, 3]    # 可迭代对象
a = iter(li)    # 迭代器
print(a)    # <list_iterator object at 0x00000278AE9AB080>
# 迭代器如何取值
print(next(a))  # 每next一次，取一个值，注意取值次数不能超过可迭代对象的数量，超出报StopIteration错
print(next(a))
print(next(a))
# print(next(a))  # StopIteration
```

#### 1.3 迭代器特定

```
1.仅仅只需在迭代到某个元素时才计算该元素，而在这之前或者之后，元素可以不存在或者被销毁，适合于遍历一些巨大的或者无限的集合
2.不能回退
3.不能随机访问值
```

```
li = [1, 2, 3]    # 可迭代对象
a = iter(li)    # 迭代器

print(dir(li))  # 有"__iter__", 可迭代对象
print(dir(a))   # 有"__iter__"和"__next__"， 迭代器
```

#### 1.4 for循环如何实现迭代

```
li = [1, 2, 3]    # 可迭代对象
for i in li:
    print(i)

# for实现迭代原理
li = [1, 2, 3]    # 可迭代对象
itr = iter(li)  # 迭代器

print("==="*15)
try:
    while True:
        b = next(itr)
        print(b)
except StopIteration:
    pass

# Python将关键字in后的对象调用iter函数获取迭代器，然后通过调用迭代器的next方法获取元素，直到抛出StopIteration异常。
```

#### 1.5 自定义可迭代对象 `__iter__`

```
class Mylist:
    # pass
    def __iter__(self):
        return iter([1, 2, 3])


a = Mylist()    # 实例化对象，可迭代对象？
# for i in a:
#     print(i)
print(dir(a))
```

### 2.生成器：

```
更加优雅的自定义可迭代对象的方法：生成器
```

#### 2.1生成器定义

```
# 1.回忆函数
def func():
    pass


func()


# 2.生成器定义,容器
def func():
    yield 1
    yield 3
    yield 8


g = func()
print(g)    # 生成器对象<generator object func at 0x0000019591F4C1A8>
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))  # StopIteration
```

#### 2.2 暂停和恢复

```
def func():
    print("1前")
    yield 1
    print("3前")
    yield 3
    print("8前")
    yield 8


g = func()

# 执行
ret = next(g)   # 执行函数，到yield中止
print("返回值1：", ret)
ret = next(g)   # 执行函数，到yield中止
print("返回值2：", ret)
ret = g.__next__()   # 执行函数，到yield中止
print("返回值3：", ret)
```

#### 2.3生成器的应用：

```
def func(elem, n):
    count = 0
    while True:
        if count < n:
            yield elem  # 函数内有yield，这个函数就是生成器函数
            count += 1
        else:
            break


man = func("刘若英，我爱你", 100)
# print(next(man))
#
# for i in man:
#     print(i)
# 生成器的本质还是一个迭代器。
```

### 3.推到表达式

```
# a = [1, 3, 5]
# for i in range(10):
#     print(i)
a = [i for i in range(1, 11)]
print(a)    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [i for i in range(1, 11, 2)]
print(a)    # [1, 3, 5, 7, 9]
a = [i for i in range(1, 11, 2) if i > 5]
print(a)    # [7, 9]
```

### 4.模块

#### 4.1模块路径

```
import sys

for i in sys.path:
    print(i)    # 模块搜索路径

"""
F:\class49\lesson16  # 当前目录
F:\class49
D:\software\python\python36.zip
D:\software\python\DLLs
D:\software\python\lib    # 内置模块存放处
D:\software\python
D:\software\python\lib\site-packages    # 第三方模块存放处
C:\Program Files\JetBrains\PyCharm 2018.3.3\helpers\pycharm_matplotlib_backend
"""
```

#### 4.2 模块的导入

```
# 1.内置模块：
import keyword
# print(keyword.kwlist)

# 2.第三方模块：
# 安装方法：
"""
pip install tornado
py -2/3 -m pip install django
"""
import tornado.web

# 3.自建模块
# 第一种导入方式：直接导入需要的函数
from lib.index import register

register()

# 第二种导入方式：导入py文件
from lib import index

index.register()
index.login()

# 第三种导入方式：导入py文件,但使用另一个名字代替，方便代码开发
from lib import index as dd
dd.login()
```

#### 4.3 其他目录下模块的导入

```
import sys
sys.path.append("E:")
import fei
fei.f()

# for i in sys.path:
#     print(i)
```

### 5.包

```
对于自建模块，当开发项目时，在project文件夹下创建lib文件夹专门存放（编程规范）
模块是什么？模块是py文件，那包呢，就是包含了很多模块的文件夹，比如上面的lib文件夹。
```

# 十四、异常

### 1.认识异常

```
# 异常就是报错
# 异常处理
# 常见的报错信息
# a + 1   # NameError: name 'a' is not defined 变量未定义
# for i in range(5)：# SyntaxError: invalid character in identifier 语法错误
# 5 - "b"  # TypeError: unsupported operand type(s) for -: 'int' and 'str' 类型错误

# 自查和解决报错的能力
# 问题描述清楚的能力，掌握如何去提问

```

### 2.异常处理

```
#   1.一旦发生异常，程序终止
# print("one")
# aaa
# print("two")

# 2.处理
print("one")
try:
    aaa
except:
    print("three")
print("two")

# try和except与if和else相似，但if和else可以不要else，try和except必须成对出现
# 基本用法：
"""
先执行try里面的代码，try不满足条件，捕获异常，执行except里面的代码
先执行try里面的代码，try满足条件，直接执行try里面的代码，不再执行except里面的代码
"""

# 巩固
# f = open("haha.py", "r")    # 当文件不存在时，会报错FileNotFoundError: [Errno 2] No such file or directory: 'haha.py'

try:
    f = open("haha.py", "r")
except:
    print('发生了异常')

# 1/0  # ZeroDivisionError: division by zero
try:
    1 / 0
except:
    print("发生了异常")

# 拓展：捕获具体的异常

try:
    # f = open("haha.py", "r")
    aaa
except ZeroDivisionError:
    print("分母为零了")
except FileNotFoundError:
    print('文件不存在')
except Exception as e:
    print(e)    # name 'aaa' is not defined

try:
    1 / 0
except ZeroDivisionError:
    print("分母为零了")

# 捕获具体异常：让你捕获你想要捕获的异常


# 自动抛出异常
# raise
# def func(name):
#     if name == '胡涛':
#         raise TypeError("黑名单用户，拒绝访问")
#
#
# func("胡涛")

try:
    # raise TypeError("主动抛出的类型错误")    # 自制异常
    a = 5
except ZeroDivisionError:
    print("分母为零了")
except FileNotFoundError:
    print('文件不存在')
except Exception as e:
    print(e)
else:
    print("try里的代码无异常，正常执行后执行else")
finally:
    print("代码不管是否正常执行，最后都会执行finally")

```

# 十五、正则表达式

### 1.概念

```
正则表达式是一个工具，用来匹配或者提取字符串，用re库来实现，所有的正则表达式的语法都是一样的
```

```
爬虫和web
爬虫：按指定的格式提取信息
web：12345@qq.com 
```

```
怎么学？正则本身不难，但是正则的内容多，要去做笔记，要去用，去敲：笔记一定要记好，多练习。
```

```
re.findall():将符合规则的字符串，以列表的形式，全部返回。
```

### 2.元字符

```
正则表达式由普通字符和元字符组成。普通字符包括大小写的字母和数字，而元字符则具有特殊含义。
```

```
常用元字符：.  ^  $  {}  *  +  ? |  []
```

### 3.预定义字符类

| **预定义字符类** | **说明**           | **对等字符类**  |
| ---------------- | ------------------ | --------------- |
| \d               | 任一数字字符       | [0-9]           |
| \D               | 任一非数字字符     | [^0-9]          |
| \s               | 任一空白符         | [\t\n\x0B\f\r]  |
| \S               | 任意非空白符       | [^\t\n\x0B\f\r] |
| \w               | 任一字母数字字符   | [a-zA-Z0-9]     |
| \W               | 任一非字母数字字符 | [^a-zA-Z0-9]    |

### 4.分组元字符

# 十六、压缩解压

### **1.zip/unzip**

```
zip命令可以用来解压缩文件，或者对文件进行打包操作
unzip命令用于解压缩由zip命令压缩的“.zip”压缩包

这两个不是Linux自带的，需要安装
sudo apt-get install zip
sudo apt-get install unzip
```

选项

```
zip:
-q：不显示指令执行过程
-r：递归处理，将指定目录下的所有文件和子目录一并处理
unzip:
-o  解压时不再询问，直接覆盖
-d  将文件解压到指定的文件夹下
```

```
zip -q -r ~/test.zip test	# 指定路径压缩
unzip test.zip -d ~/tmp/a	# 指定路径解压
```

### **2.gzip/gunzip**

```
gzip命令用来压缩文件。gzip是个使用广泛的压缩程序，文件经它压缩过后，其名称后面会多处.gz扩展名。

gunzip命令用来解压缩文件。gunzip是个使用广泛的解压缩程序，它用于解开被gzip压缩过的文件，这些压缩文件预设最后的扩展名为.gz。事实上gunzip就是gzip的硬连接，因此不论是压缩或解压缩，都可通过gzip指令单独完成。
```

选项

```
gzip:
-d 对压缩的文件进行解压
-r 递归式压缩指定目录以及子目录下的所有文件
-l 显示压缩文件的压缩信息
-c 保留源文件
gunzip：
-c 把解压后的文件输出到标准输出设备
-f 强行解开压缩文件
-q 不显示警告信息
-r 递归处理
-v 显示命令执行过程
```

```
gzip a.py
gzip -c b.py > b.py.gz	# 保留源文件
```

```
gzip -d a.py.gz	# 解压 
```

### **3.bzip2/bunzip2**

```
bzip2命令用于创建和管理（包括解压缩）.bz2格式的压缩包,它是Linux下的一款压缩软件，比传统的gzip或zip的压缩效率更高，但是它的压缩速度较慢。

bunzip2命令解压缩由bzip2指令创建的.bz2压缩包
```

选项

```
-c  将压缩与解压缩结果送到标准输出
-d  执行解压缩
-f  文件同名时，预设不会覆盖现有文件,使用这个会覆盖
-k  bizp2 在压缩或解压缩后，会删除原始文件，使用这个不会删除
-s  降低程序执行时内存的使用量
-v  压缩或解压缩文件时，显示详细的信息
```

```
bzip2 a.py
bzip2 -c b.py > b.py.bz2 # 保留源文件
bzip2 -d a.py.bz2	# 解压
```

### 二.文件打包

```
tar命令用于将文件打包或解包，扩展名一般为.tar,指定特定参数可以调用gzip或bzip2制作压缩包或解开压缩包
```

选项

```
-c 建立新的压缩包
-x 解压压缩包
-f 使用压缩包的名字，f参数之后不能再加参数
-i 忽略存档中的0字块
-v 处理过程中输出相关信息
-z 调用gzip来压缩归档文件，与-x联用时调用gzip完成解压缩
-j 调用bzip2压缩或解压
-p 使用源文件的原来属性
find -name '*.py' >> ~/a.list
tar -T a.list -zcvf a.tar.gz
tar -zcvf a.tar.gz a.list
```

### 三.链接命令

```
ln命令用来为文件创件链接，链接类型分为硬链接和符号链接两种，默认的链接类型是硬链接。如果要创建符号链接必须使用-s选项

注意：符号链接文件不是一个独立的文件，它的许多属性依赖于源文件，所以给符号链接文件设置存取权限是没有意义的

软链接只会在目的位置生成一个文件的链接文件，实际不会占用磁盘空间，相当于Windows中的快捷方式。硬链接会在目的位置上生成一个和源文件大小相同的文件。无论软链接和硬链接，文件保持同步变化。
```

选项

```
-i 覆盖既有文件之前先询问用户
-s 创建符号(软)链接而不是硬链接
```

```
如果修改文件内容，那么链接会随着一起变化
如果删除源文件，硬链接可以继续使用，软链接失效
```







