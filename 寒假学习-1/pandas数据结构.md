# Pandas

## 引言

- Pandas是基于Numpy的一种工具，该工具是为了解决数据分析任务二创建的。
- Pandas纳入了大量库和一些标准的数据模型，提供了高效的操作大学数据及所需的工具
- Pandas提供了大量能使我们快速便捷梳理数据的函数和方法
- Pandas是Python的一个数据分析包，最初于2008年4月开发，2009年底开源
- Pandas最初被作为进入数据分析工具而开发出来，也未试驾序列分析提供了很好的支持。

## Pandas库介绍：

- pandas是python的第三方库，提供高性能易用数据类型和分析工具

- pandas基于numpy实现，鲳鱼numpy与matplotlib一同使用

- pandas中有两大核心数据结构：Series（一维数据）和DataFrame（多特征数据，既有行索引，又有列索引）
- Series
  - 一位数组，与numpy中的一维array类似
  - Series，numpy中的一维array与python基本的数据结构list也很接近，其区别是：list中的元素可以是不同的数据类型，二array和Series中则只允许存储相同的数据类型
  - Series可以更有效的使用内存，提高运行效率
- Time-Series:以时间为索引的Series
- DataFrame：带标签且大小可变的二维表格数据结构，可以将DataFrame理解为Series的容器
- Panel：三维数组，可以理解为DataFrame的容器

## Series

- series是一种类似于一位数组的对象，他有一位数组（各种numpy数据类型）以及一组与之相关的标签（索引）组成

### Series创建函数

```
pandas.Series(data, index, dtype, copy)
```

| 参数  | 描述                                                         |
| ----- | ------------------------------------------------------------ |
| data  | 数据采取各种形式，如：ndarray,list,constants                 |
| index | 索引值必须是唯一的和散列的，与数据的长度相应。默认np.arange(n)如果没有被索引被传递 |
| dtype | dtype用于数据类型 如没有，将腿短数据类型                     |
| copy  | 复制数据，默认为false                                        |

#### Series的创建

- 使用python数组创建
- 使用numpy的数组创建
- 使用python的字典创建

注：与字典不同的是：Series允许索引重复

```
import pandas as pd
import numpy as np
print(pd.Series([11,12],index=["金华","宁波"]))
>>>金华    11
宁波    12
dtype: int64
print(pd.Series(np.arange(2,6)))
>>>0    2
1    3
2    4
3    5
dtype: int32
print(pd.Series({"金华":11,"宁波":12,"杭州":13}))
>>>金华    11
宁波    12
杭州    13
dtype: int64
```

- Series的字符串表现形式为：索引在左边，值在右边
- 如果没有微数据指定索引，则自动创建一个0-N-1的整数型索引
- 可以通过Series的values和index属性获取其数据表示形式和索引对象
- 与普通numpy数组相比，可以通过索引的方式选取series中的单个或一组值

```
obj = pd.Series([4,7,-5,3])
print(obj.values)
>>>[ 4  7 -5  3]
print(obj.index)
>>>RangeIndex(start=0, stop=4, step=1)
print(obj[2])
>>>5
obj[1] = 8
print(obj[[0,1,3]])
>>>0    4
1    8
3    3
dtype: int64
```

通常我们希望所创建的Series带有一个可以对各个数据点进行标记的索引。

与普通numpy数组相比，可以通过索引的方式选取Series中的单个或一组值

```python
obj2 = pd.Series([14,2,-5,3],index=['a','b','c','d'])
print(obj2)
>>>a    14
b     2
c    -5
d     3
dtype: int64
print(obj2['a'])
>>>14
obj2['d'] = 6
print(obj2)
>>>a    14
b     2
c    -5
d     6
dtype: int64
print(obj2[['a','c','d']])
>>>a    14
c    -5
d     6
dtype: int64
```

**Series还有一个很重要的功能，是它会在算数运算中自动对齐不同索引的数据**

```
obj2 = pd.Series({'summer':123,'july':456,'april':678,'hello':123})
obj3 = pd.Series({'july':261,'summer':373,'april':123,'april':456})
print(obj2+obj3)
>>>april     1134.0
hello        NaN
july       717.0
summer     496.0
dtype: float64
```

Series对象本身及其索引都有一个name属性

Series的索引可以通过赋值的方式就地修改

```
obj = pd.Series([1,2,3])
obj.name = 'summer'
obj.index.name = 'july'
print(obj)
>>>
july
0    1
1    2
2    3
Name: summer, dtype: int64
obj2 = pd.Series([4,7,-1.3])
obj2.index = ['summer','july','april']
print(obj2)
>>>
summer    4.0
july      7.0
april    -1.3
dtype: float64
```



## DataFrame

- DataFrame是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数字，字符串，布尔值）
- DataFrame既有行索引，也有列索引，它可以被看做由Series组成的字典（共同用一个索引）
- 根其他类似的数据结构相比，DataFrame中面向行和面向列的操作基本上是平衡的
- DataFrame中的数据是以一个或多个二维块存放的（而不是列表，字典或别的以为数据结构）

### DataFrame特点

- 潜在的列式不同类型
- 大小可变
- 标记轴（行和列）
- 可以对行和列执行计算术运算

### DataFrame构造函数

```
pandas.DataFrame(data, index, columns, dtype, copy)
```

data：数据采取各种形式，如nadrray,series,map,lists,dict,constant和另一个DataFrame

index：对于行标签，要用于结果帧的索引是科员缺省值np.arrange(n),如果没有传递索引值

columns：对于列标签，可选的默认语法是np.arrange(n),这只有在没有索引传递的情况下

dtype：每列的数据类型

copy：如果默认值为False，则此命令用于赋值数值

### 创建一个空的FataFrame

函数不指定参数，返回一个空的DataFrame

```
df = pd.DataFrame()
print(df)
>>>
Empty DataFrame
Columns: []
Index: []
```

### 从列表创建DataFrame

```python
data = [1,2,3,4]
df = pd.DataFrame(data)
print(df)
>>>
   0
0  1
1  2
2  3
3  4
# 从嵌套列表创建DataFrame，并指定数据类型
data = [['summer',20],['april',21],['july',21]]
df = pd.DataFrame(data,columns=['Nmae','age'],dtype=float)
print(df)
>>>
     Nmae   age
0  summer  20.0
1   april  21.0
2    july  21.0
```

由等长列表或numpy数组组成的字典创建DataFrame

DataFrame结果会自动加上索引（根Series一样），且全部会被有序排列

```
data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],'year':[2000,2001,2002,2001,2002],'pop':[1.1,1.2,3,5,8.0]}
frame = pd.DataFrame(data)
print(frame)
>>>
    state  year  pop
0    Ohio  2000  1.1
1    Ohio  2001  1.2
2    Ohio  2002  3.0
3  Nevada  2001  5.0
4  Nevada  2002  8.0
```

如果指定了列的顺序，DataFrame的列就会按照指定顺序进行排列

根原Series一样，如果传入的列在数据中找不到，就会产生NAN值

```
pd.DataFrame(data,columns=['year','state','pop'])
>>>
   year   state  pop
0  2000    Ohio  1.1
1  2001    Ohio  1.2
2  2002    Ohio  3.0
3  2001  Nevada  5.0
4  2002  Nevada  8.0

frame2 = pd.DataFrame(data,columns=['year','state','pop','det'],index=['1','2','3','4','5'])
print(frame2)
>>>
   year   state  pop  det
1  2000    Ohio  1.1  NaN
2  2001    Ohio  1.2  NaN
3  2002    Ohio  3.0  NaN
4  2001  Nevada  5.0  NaN
5  2002  Nevada  8.0  NaN
print(frame2.columns)
>>>
Index(['years', 'states', 'pop', 'det'], dtype='object')
```

通过类似字典标记的方式或属性的方式，可以将DataFrame的列获取为一个Series

返回的Series拥有原DataFrame相同的索引，且其他name属性也已经被相应的设置好了

```
print(frame2['year'])
>>>
1    2000
2    2001
3    2002
4    2001
5    2002
Name: year, dtype: int64
```

- 列也可以通过赋值的方式进行修改

```
frame2['det'] = 12
print(frame2)
>>>
   year   state  pop  det
1  2000    Ohio  1.1   12
2  2001    Ohio  1.2   12
3  2002    Ohio  3.0   12
4  2001  Nevada  5.0   12
5  2002  Nevada  8.0   12
frame2['det'] = np.arange(5)
print(frame2)
>>>
   year   state  pop  det
1  2000    Ohio  1.1    0
2  2001    Ohio  1.2    1
3  2002    Ohio  3.0    2
4  2001  Nevada  5.0    3
5  2002  Nevada  8.0    4
```

将列表或数组复值给某个列时，其长度必须跟DataFrame的长度相匹配

如果赋值的是一个Series，就会精确匹配DataFrame的索引，所有空位都将被填上空缺值。

```
val = pd.Series([1,2,3],index=['3','5','4'])
frame2['det']=val
print(frame2)
>>>
   year   state  pop  det
1  2000    Ohio  1.1  NaN
2  2001    Ohio  1.2  NaN
3  2002    Ohio  3.0  1.0
4  2001  Nevada  5.0  3.0
5  2002  Nevada  8.0  2.0
```

为不存在的列赋值会创建出一个新列

关键字del用于删除列

```
frame2['esaterm'] = frame2.state == 'Ohio'
print(frame2)
>>>
   year   state  pop  det  esaterm
1  2000    Ohio  1.1  NaN     True
2  2001    Ohio  1.2  NaN     True
3  2002    Ohio  3.0  1.0     True
4  2001  Nevada  5.0  3.0    False
5  2002  Nevada  8.0  2.0    False
del frame2['esaterm']
print(frame2.columns)
>>>
Index(['year', 'state', 'pop', 'det'], dtype='object')
```

也可以将嵌套字典传给DataFrame，它就会被截石位：外层字典的键为列，内层字典的键为行索引

**也可以进行转置**

```
pop = {'Nevada':{2001:2,2002:3},'Ohio':{2000:1,2004:5}}
frame3 = pd.DataFrame(pop)
print(frame3)
>>>
      Nevada  Ohio
2001     2.0   NaN
2002     3.0   NaN
2000     NaN   1.0
2004     NaN   5.0
print(frame3.T)
>>>
        2001  2002  2000  2004
Nevada   2.0   3.0   NaN   NaN
Ohio     NaN   NaN   1.0   5.0
```

如果设置了DataFrame的index和columns的name属性，这些信息也会显示出来

```
frame3.index.name = 'year'
frame3.columns.name = 'state'
print(frame3)
>>>
state  Nevada  Ohio
year               
2001      2.0   NaN
2002      3.0   NaN
2000      NaN   1.0
2004      NaN   5.0
```

跟Series一样，values属性也会以二维ndarray的形式返回DataFrame中的数据

如果DataFrame各列数据类型不同，则数组的数据类型就会选用能兼容所有列的数类型

```
print(frame3.values)
>>>
array([[ 2., nan],
       [ 3., nan],
       [nan,  1.],
       [nan,  5.]])
```


