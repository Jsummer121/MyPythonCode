# Pandas常用方法

## 数据读取写入

Pandas支持常用的文本格式数据（json，csv，jtml，剪切板）、二进制数据，SQL数据等

一般情况下，读取文件的方法以pd.read_ 开头，而写入的方法以pd.to_开头

| 数据类型 | 描述符 | 读方法         | 写方法       |
| -------- | ------ | -------------- | ------------ |
| text     | CSV    | read_csv       | to_csv       |
| text     | JSON   | read_json      | to_json      |
| text     | HTML   | read_csv       | to_csv       |
| text     | 剪切板 | read_clipboard | to_clipboard |
| 二进制   | Excel  | raed_excel     | to_excel     |
| 二进制   | HDF5   | read_hdf       | to_hdf       |
| 二进制   | PKL    | read_pickle    | to_pickle    |
| SQL      | SQL    | read_sql       | to_sql       |

### 读入剪切板数据，写入csv转化为json，html，excel等格式

```
import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# 从剪切板读取数据
df1 = pd.read_clipboard()
# 把数据放入到剪切板中，数据可以直接粘贴到excel文件中
df1.to_clipboard()
# 读写csv文件，可以取消index
de1.to_csv('df1.csv')
df1.to_csv('df1_noIndex.csv',index = False)
# 转化为Json数据
df1.to_json('df1.json')
# 转化为html格式
df1.to_html('df1.html')
# 转化为excel格式
df1.to_excel('df1.xlsx')
```

### 数据读取函数read_csv()

自定义索引：可以指定csv文件中的一列来使用index_col定制索引

dtype：数据类型转化

skiprows：跳过指定行数

```
df = pd.read_csv('temp.csv')
print(df)

df = pd.read_csv('temp.csv',dtype={'Salary':np.float64})
print(df)
print(df.dtypes)

df = pd.read_csv('temp.csv',index_col=['S.No'])
print(df)


df = pd.read_csv('temp.csv',names=['a','b','c','d','e'])
print(df)
# 如果多的列没有值，下面会自动填充NAN，如果列名设置少了，会从后往前给

df = pd.read_csv('temp.csv',skiprow=2)
print(df)
```

## 描述性统计方法

pandas提供了几个统计和描述性方法，方便从宏观的角度去了解数据集，例如count（）用于统计非空数据的数量。

除了统计类方法，Pandas还提供了很多计算类的方法，比如sum（）等

| 函数      | 描述             |
| --------- | ---------------- |
| count()   | 非空观测数量     |
| sum()     | 所有值之和       |
| mean()    | 所以值的平均值   |
| median()  | 所以值的中位数   |
| std()     | 值的标准偏差     |
| min()     | 所有值中的最小值 |
| max()     | 所有值中的最大值 |
| abs()     | 绝对值           |
| prod()    | 数组元素的乘积   |
| cumsum()  | 累计总和         |
| cumprod() | 累计乘积         |

```
import pandas as pd
import numpy as np

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack','Lee','David','Grasper','Betina','Andres']),'Age':pd.Series([25,14,15,26,23,32,18,12,23,25,24,10]),'Rating':pd.Series([4.23,5.213,1.42,4.241,2.421,4.12,3.12,5.124,6.124,4.124,5.14,3.15])}

df = pd.DataFrame(d)
print(df,'\n')
print(df.sum(),'\n') # 列求和 默认axis=0
print(df.sum(1),'\n') # 行求和 axis=1
print(df.mean(),'\n') # 求均值
print(df.std(),'\n')  # 标准差

>>>
       Name  Age  Rating
0       Tom   25   4.230
1     James   14   5.213
2     Ricky   15   1.420
3       Vin   26   4.241
4     Steve   23   2.421
5     Minsu   32   4.120
6      Jack   18   3.120
7       Lee   12   5.124
8     David   23   6.124
9   Grasper   25   4.124
10   Betina   24   5.140
11   Andres   10   3.150 

Name      TomJamesRickyVinSteveMinsuJackLeeDavidGrasperB...
Age                                                     247
Rating                                               48.427
dtype: object 

0     29.230
1     19.213
2     16.420
3     30.241
4     25.421
5     36.120
6     21.120
7     17.124
8     29.124
9     29.124
10    29.140
11    13.150
dtype: float64 

Age       20.583333
Rating     4.035583
dtype: float64 

Age       6.666856
Rating    1.325204
dtype: float64 
```

include参数是用于传递关于什么列需要考虑用于总结的必要信息的参数，获取列值表，默认情况下是‘数字值’‘

object-汇总字符串列，number-汇总数字列，all-将所有列汇总在一起（不应该将其作为列表值传递）

```
print(df.describe(include=['number']))
>>>
Age     Rating
count  12.000000  12.000000
mean   20.583333   4.035583
std     6.666856   1.325204
min    10.000000   1.420000
25%    14.750000   3.142500
50%    23.000000   4.177000
75%    25.000000   5.128000
max    32.000000   6.124000
```

## 迭代与遍历

pandas对象之间的基本迭代的行为取决于类型，当跌迭代一个系列时，他被视为数组式，基本迭代产生这些值，其他数据结构如：DataFrame遵循类似管理迭代对象的键。

简言之，基本迭代（对于i在对象中）产生：

- Series-值
- DataFrame-列标签

要遍历数据帧（DataFrame）中的行，可以使用一下的函数：

- iteritems（） -迭代（key，value）对
- iterrows（） -将行迭代为（索引，系列）对
- itertuples（） -以namedtuples的形式迭代行

```
# 迭代DataFrame
import pandas as pd
import numpy as np

N = 5

df = pd.DataFrame({
    'D':pd.date_range(start='2020-01-01',periods=N,freq='M'),
    'x':np.linspace(0,stop=N-1,num=N),
    'y':np.random.rand(N),
    'z':np.random.choice(['Low','Medium','High'],N).tolist(),
    })

print(df,'\n')
for col in df:
    print(col)
>>>
           D    x         y       z
0 2020-01-31  0.0  0.626911  Medium
1 2020-02-29  1.0  0.530151    High
2 2020-03-31  2.0  0.328737    High
3 2020-04-30  3.0  0.572256  Medium
4 2020-05-31  4.0  0.405204  Medium 

D
x
y
z
```

遍历iteritems（）将么一个列作为名称，将索引和值作为键和罗列值迭代为Series对象

```
df = pd.DataFrame(
    np.random.rand(4,3),columns=['col1','col2','col3'])

print(df,'\n')
for key,value in df.iteritems():
    print(key,value,'\n')

>>>
       col1      col2      col3
0  0.168234  0.189750  0.591156
1  0.806730  0.889839  0.263811
2  0.156040  0.333223  0.648128
3  0.710578  0.166591  0.254272 

col1 0    0.168234
1    0.806730
2    0.156040
3    0.710578
Name: col1, dtype: float64 

col2 0    0.189750
1    0.889839
2    0.333223
3    0.166591
Name: col2, dtype: float64 

col3 0    0.591156
1    0.263811
2    0.648128
3    0.254272
Name: col3, dtype: float64 
```

iterrows（）返回迭代器，产生每个索引值以及包含每行数据的序列

```
df = pd.DataFrame(
    np.random.rand(4,3),columns=['col1','col2','col3'])

print(df,'\n')
for row_index,row in df.iterrows():
    print(row_index,row,'\n')
>>>
       col1      col2      col3
0  0.881504  0.902464  0.957250
1  0.477801  0.480380  0.819103
2  0.353978  0.842091  0.717807
3  0.801734  0.729330  0.348971 

0 col1    0.881504
col2    0.902464
col3    0.957250
Name: 0, dtype: float64 

1 col1    0.477801
col2    0.480380
col3    0.819103
Name: 1, dtype: float64 

2 col1    0.353978
col2    0.842091
col3    0.717807
Name: 2, dtype: float64 

3 col1    0.801734
col2    0.729330
col3    0.348971
Name: 3, dtype: float64 
```

itertuples（）方法将DataFrame中的每一行返回产生一个命名元组的迭代器，元组的第一个元素将是行的相应索引值，二剩余的值时行值。

```
df = pd.DataFrame(
    np.random.rand(4,3),columns=['col1','col2','col3'])

print(df,'\n')
for row in df.itertuples():
    print(row,'\n')
>>>
       col1      col2      col3
0  0.558386  0.004099  0.611956
1  0.356145  0.662296  0.398654
2  0.630491  0.046594  0.288967
3  0.715079  0.863405  0.964175 

Pandas(Index=0, col1=0.5583855700015643, col2=0.0040987862486008275, col3=0.6119559578039486) 

Pandas(Index=1, col1=0.35614533567980367, col2=0.662296433360181, col3=0.3986540692192757) 

Pandas(Index=2, col1=0.6304909132237632, col2=0.046594240964178635, col3=0.2889668591348905) 

Pandas(Index=3, col1=0.7150789226259381, col2=0.8634050945203743, col3=0.9641752322377131) 
```

## 排序

按索引排序：使用sort_index（）方法，通过传递axis参数和排序顺序，可以对DataFrame进行排序。默认情况下，按照圣墟对行标签进行排序。

**按数值排序**：sort_values()是按值排序方法。它接受一个by参数，它将使用要与其排序值的DataFrame的列名称

**排序顺序**：通过将布尔值传递给升序参数ascending可以控制排序顺序

**按行或列排序**：通过设置axis参数为0或1，为0时逐行排序，为1时逐列排序，默认为0

```
unsorted_df = pd.DataFrame(np.random.rand(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['A','B'])
print(unsorted_df,'\n')

sorted_df = unsorted_df.sort_index(ascending = True)
print(sorted_df,'\n') #按索引排序

sorted_df = unsorted_df.sort_values(by='B')
print(sorted_df,'\n') # 按'B'列的值进行排序
>>>
          A         B
1  0.961256  0.302314
4  0.820918  0.270748
6  0.016357  0.578068
2  0.101770  0.617789
3  0.479742  0.457839
5  0.738100  0.227945
9  0.545030  0.966452
8  0.262354  0.821287
0  0.886291  0.169482
7  0.977245  0.707497 

          A         B
0  0.886291  0.169482
1  0.961256  0.302314
2  0.101770  0.617789
3  0.479742  0.457839
4  0.820918  0.270748
5  0.738100  0.227945
6  0.016357  0.578068
7  0.977245  0.707497
8  0.262354  0.821287
9  0.545030  0.966452 

          A         B
0  0.886291  0.169482
5  0.738100  0.227945
4  0.820918  0.270748
1  0.961256  0.302314
3  0.479742  0.457839
6  0.016357  0.578068
2  0.101770  0.617789
7  0.977245  0.707497
8  0.262354  0.821287
9  0.545030  0.966452 
```

## 缺失值处理

缺失值主要是指数据丢失的现象，也就是数据集中的某一块数据不存在

除了原始数据集就已经存在缺失值以外，当我们用到索引对其（reindex（），选择等）方法时，也容易认为导致缺失值的产生

缺失值处理包括：

- 缺失值标记
- 缺失值填充
- 缺失值插值

Pandas为了更方便的检测缺失值，将不同类型数据的缺失值均采用NAN标记。这里的NaN代表Not a Numer，它仅仅是作为一个标记。 



**Pandas中用于标记缺失值主要用到两个方法，分别是：isnull（）和notnull（），顾名思义就是【是缺失值】和【不是缺失值】。默认会返回布尔值用于判断**

```
df = pd.DataFrame(np.random.rand(4,3),index=['a','c','e','f'],columns=['one','two','three'])
df = df.reindex(['a','b','c','d','e','f','g'])
print(df,'\n')

print(df['one'].isnull,'\n')
print(df['one'].notnull,'\n')
>>>
        one       two     three
a  0.632097  0.550568  0.790110
b       NaN       NaN       NaN
c  0.283101  0.398604  0.703860
d       NaN       NaN       NaN
e  0.421465  0.512418  0.893076
f  0.278658  0.843139  0.685803
g       NaN       NaN       NaN 

<bound method Series.isnull of a    0.632097
b         NaN
c    0.283101
d         NaN
e    0.421465
f    0.278658
g         NaN
Name: one, dtype: float64> 

<bound method Series.notnull of a    0.632097
b         NaN
c    0.283101
d         NaN
e    0.421465
f    0.278658
g         NaN
Name: one, dtype: float64> 
```

**Pandas提供了个职工方法老赖清除缺失的值。fillna（）函数可以通过集中方法用非空数据‘填充’NaN值。**

- 用标量值替换NaN

  print(df.dillna(0))

- 向前填充：pad/fill

- 向后填充：bfill/backfill

print(df.fillna(method='pad'))

print(df.fillna(method='backfill'))



**丢弃缺少的值**：如过只想排除缺少的值，则使用dropna函数和axis参数。默认情况下，axis=0，如果行内的任何值是NaN，那么整行被删除

- 丢弃NaN值的行

print(df.dropna())

- 丢弃含NaNDE列

print(df.dropna(axis=1))



**替换缺失值**：用一些具体的值取代一个通用的值或缺失值。用标量替换NaN和使用fillna（）函数等效。

```
df = pd.DataFrame({'one':[10,20,30,40,50,2000]},'two':[1000,0,30,40,50,60])
print(df,'\n')
print(df.replace({1000:10,2000:60}))
```





