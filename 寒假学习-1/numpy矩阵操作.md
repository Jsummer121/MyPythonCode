# numpy矩阵操作

## numpy矩阵库（Matrix）

- numpy包含了一个举证库numpy.matlib，该模块中的函数返回的是一个矩阵，二不是ndarry对象
- 一个有MxN的矩阵是一个由m行和n列元素排列而成的矩阵阵列
- 矩阵里的元素可以是数字，符号或数学公式，
- numpy和Matlab不一样，对于多维数组的运算，缺省情况下并不知道使用矩阵运算，如果希望加快运算，可以调用ndarry对象相应的函数

## numpy矩阵的生成方式

### 常规生成

```
x = np.matrix([[1,2,3],[4,5,6]])
y = np.matrix([1,2,3,4,5,6])

# x[0,0]返回行下标和列下标都为0的数
# 注，对于矩阵x来说，x[0,0]和x[0][0]含义不一样
print(x,y,x[0,0],sep='\n\n')
>>>[[1 2 3]
 [4 5 6]]

[[1 2 3 4 5 6]]

1
```

### matlib.empty()

```
numpy.matlib.empty(shape, dtype, order)
```

shape:定义新矩阵的形状的整数或整数元组

dtype：数据类型

order：C 行优先，F列优先

```
import numpy.matlib
import numpy as np

print(np.matlib.empty(2,2)) #创造一个2*2的矩阵，内部参数随机
```

还有其他的

### numpy.matlib.zeros() 

 创建以0为填充的矩阵

### numpy.matlib.ones() 

创建以1位填充的矩阵

```
import numpy.matlib
import numpy as np

print(np.matlib.zeros((2,2)))
>>>[[0. 0.]
 [0. 0.]]
print(np.matlib.ones((2,2)))
>>>[[1. 1.]
 [1. 1.]]
```

### numpy.matlib.eye()

函数返回一个矩阵，对角线元素为1，其他位置为0

```
numpy.matlib.eye(n, M, k, dtype)
```

- n：返回矩阵行数
- M：返回矩阵列数，默认为n
- k：对角线的索引
- dtype：数据类型

```
print(np.matlib.eye(n = 3, M = 4, k = 0, dtype = int))
>>>[[1 0 0 0]
 [0 1 0 0]
 [0 0 1 0]]
```

### numpy.matlib.inentity()

返回给定大小的单位矩阵

单位矩阵是个方阵，从左上角到右下角的对角线（主对角线）上的元素均为1，除此之外为0

```
print(np.matlib.identity(4,dtype = int))
>>>[[1 0 0 0]
 [0 1 0 0]
 [0 0 1 0]
 [0 0 0 1]]
```

### numpy.matlib.rand()

创建一个给定大小的矩阵，数据是随机数

```
print(np.matlib.rand(4,4))
```

## 常用操作

### 矩阵与二维数组相互转化

矩阵总是二维的，二ndarry是一个nn维数组，两个对象是可以互换的

```
i = np.matrix('1,2;3,4')
print(i)
>>>matrix([[1, 2],
        [3, 4]])
j = np.asarray(i)
print(j)
>>>array([[1, 2],
       [3, 4]])
k = np.asmatrix(j)
print(k)
>>>matrix([[1, 2],
        [3, 4]])
```

### 矩阵的转置

```
x = np.matrix([[1,2,3],[4,5,6]])
y = np.matrix([1,2,3,4,5,6])
print(x.T,y.T,sep='\n\n')
>>>[[1 4]
 [2 5]
 [3 6]]

[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]
print(x,y,sep='\n\n')
>>>[[1 2 3]
 [4 5 6]]

[[1 2 3 4 5 6]]
```

### 矩阵乘法

```
x = np.matrix([[1,2,3],[4,5,6]])
y = np.matrix([[1,2],[3,4],[5,6]])
print(x*y)
>>>matrix([[22, 28],
        [49, 64]])
```

## 矩阵运算

- numpy.linalg中有一组标准的矩阵分解运算以及诸如求逆和行列式之类的东西
- 它们根MATLAB和R语言所使用的的是相应行业标准级Fortran库

| 函数  | 说明                                                         |
| ----- | ------------------------------------------------------------ |
| diag  | 以以为数组的形式返回放在的对角线元素，或将一位数组转化为方阵 |
| dot   | 矩阵乘法                                                     |
| trace | 计算对角线元素的和                                           |
| det   | 计算矩阵行列式                                               |
| eig   | 计算方阵的特征值和特征向量                                   |
| inv   | 计算方阵的逆                                                 |
| avd   | 计算奇异值分解（SVD）                                        |
| solve | 解线性方程组Ax=b，其中A为一个方阵                            |
| lstsq | 计算Ax=b的最小二乘解                                         |

### numpy.dot():两个组的点积，即元素对应相乘

- 对于两个一位数组，计算的是这两个数组对应下标元素的乘积和（数学上称之为内积）；
- 对于二维数组，计算的是两个数组的矩阵乘积
- 对于多维数组，它的通用计算公式如下，即结果数组中的每个元素都是：数组a的最后一维上的所有元素与数组b的倒数第二位上的所有元素的乘积和

```
doc(a,b)[i,j,m] = sum(a[i,j:]*b[k,:,m]
```

```
numpy.doc(a, b, out=None)
```

a:ndarray数组

b:ndarray数组

out：ndarray。可选。用来保存dot（）的计算结果

```
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
print(np.dot(a,b))
>>>array([[37, 40],
       [85, 92]])
```

方法：

```
[[1*11+2*13,1*12+2*14],[3*11+4*13,3*12+4*14]]
```

### numpy.vdot():返回两个向量的点积

如果第一个参数是复数，那么他的共轭复数会用于计算。如果参数是多维数组，他会被展开

```
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])

print(np.vdot(a,b))
>>> 130
```

计算过程：

```
1*11+2*12+3*13+4*14=130
```

### numpy.linalg.inv():计算逆矩阵

逆矩阵：设a是数域上的一个n阶矩阵，若在相同的数域上存在另一个n阶矩阵b，使得AB=BA=E，则我们称B是A的逆矩阵，而A则被称为可逆矩阵，注：E为单位矩阵

```
x = np.array([[1,2],[3,4]])
y = np.linalg.inv(x)
print(x,y,np.dot(x,y),sep='\n\n')
>>>[[1 2]
 [3 4]]

[[-2.   1. ]
 [ 1.5 -0.5]]

[[1.0000000e+00 0.0000000e+00]
 [8.8817842e-16 1.0000000e+00]]
```

### numpy.linalg.solve():线性方程组的解

```
a = np.array([[1,1,1],[0,2,5],[2,5,-1]])
b = np.array([6,-4,27])
x = np.linalg.solve(a,b)
print(x)
>>>array([ 5.,  3., -2.])
print(np.dot(a,x))
>>>array([ 6., -4., 27.])
```