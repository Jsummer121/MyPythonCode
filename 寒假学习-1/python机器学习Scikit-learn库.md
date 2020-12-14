# Scikit-learn库

## 概述

​	1.Scikit-learn库最早由数据科学家David Cournapeau在2007年发起，使用需要Numpy和Scipy等其他库的支持，是Python中专门针对机器学习应用而发展起来的一款开源扩展库。

​	2.和其他众多的开源项目一样，Scikit-learn目前主要有社区成员自发进行维护

​	3.Scikit-learn相比其他开源项目显得更为保守，主要提为：一是Scikit-learn从来不做除计算机学习领域之外的其他扩展。二是Scikit-learn从来不采用未经广泛验证的算法

​	4.网址：https://scikit-learn.org/stable/index.html

## Scikit-learn库数据集

在机器学习中，经常需要使用各种各样的数据集，Scikit-learn库提供了一些常用的数据集：

| 序号 | 数据集名称       | 调用方式             | 数据描述                         |
| ---- | ---------------- | -------------------- | -------------------------------- |
| 1    | 鸢尾花数据集     | Load_iris()          | 用于多分类任务的数据集           |
| 2    | 波士顿房价数据集 | Load_boston()        | 用于回归任务的经典数据集         |
| 3    | 糖尿病数据集     | Load_diabetes()      | 用于回归任务的经典数据集         |
| 4    | 手写数字数据集   | Load_digits()        | 用于多分类任务的数据集           |
| 5    | 乳腺癌数据集     | Load_breast_cancer() | 经典的用于二分类任务的数据集     |
| 6    | 体能训练数据集   | Load_linnerud()      | 经典的用于多变量回归任务的数据集 |

## 功能

### 1.分类：

​	分类是指识别给定对象的所属类别，属于监督学习的范畴，最常见的应用场景包括垃圾邮件检测和图像识别等	

​	目前Scikit-learn已经实现的算法包括：支持向量机（SVM），最近邻，逻辑回归，随机森林，决策树以及多层感知器（MLP）神经网络。

### 2.回归

​	回归是指预测与指定对象相关联的连续值属性，最常见的应用场景包括预测药物反应和预测股票价格等。

​	目前Scikit-learn以及实现的算法包括：支持向量回归（SVR），脊回归，Lasso回归，弹性网络（Elastic Net），最小角回归（LSRS），贝叶斯回归以及各种不同的鲁棒回归算法。

​	回归算法几乎涵盖了所有开发者的需求范围，而且更重要的是，Scikit-learn还针对每种算法都提供了简单明了的用例参考。

### 3.聚类

​	聚类是指自动识别具有相似属性的给定对象，并将其分组为集合，属于无监督学习的范畴

​	最常见的应用场景包括顾客细分和实验结果分组。目前Scikit-learn已经实现的算法包括：K-均值聚类，谱聚类，均值偏移，分层聚类，DBSCAN聚类等。

### 4.数据降维

​	数据降维是指使用主成分分析（PCA）、非负矩阵分析（NMF）或特征选择等降维技术来减少要考虑的随机变量的个数，其主要应用场景包括可视化处理和效提升。

### 5.模型选择

​	模型选择是指对于给定参数和模型的比较、验证和选择，其主要目的是通过参数来调整提升精度。目前Scikit-learn实现的模块包括：个点搜索、交叉验证和各种针对预测误差评估的度量函数。

### 6.数据预处理

​	数据预处理是指数据的特征提取和归一化，是机器学习过程中的第一个也是最重要的一个环节。

​	归一化是指将输入数据转化为具有零均值和单位全房差的新变量，但因为大多数时候都做不到精确度等于零，因此会设置一个可接受的范围，一般都要求落在0-1之间

​	特征提取是指将文本或图像数据转化为可用于及其新学习的数字变量。

## Sklearn库分类算法

### 1.K近邻分类器(KNN)

​	**KNN**:通过计算待分类数据点，与已有数据及中所有数据点的距离。取距离最小的前K个点，根据“少数服从多数”的原则，将这个点划分为出现次数最多的那个类别。

#### 1.1 Sklearn的k近邻分类器：

在sklearn库中，可以使用sklearn.neighbors.KNeighborsClassifier创建一个K近邻分类器，主要参数有：

- n_neighbors：用于指定分类器中K的大小（默认为5）（最大值为给定的值的个数）
- Weights：设置选中的K个点分别对分类结果影响的权重（默认值为平均权重“uniform”，可以选择“distance”代表跃进的点权重越高，或者传入自己编写的以距离为参数的权重计算函数）。
- algorithm：设置用于计算邻近点的方法（选择中有ball_tree，kd_tree和brute，分别代表不同的寻找邻近的优化算法，默认为auto，根据训练数据自动选择）

#### 1.2 Sklearn的k邻分类器 示例

```
from sklearn.neighbors import KNeighborsClassifier

# 创建一组数据X和它对于的标签y
X = [[0],[1],[2],[3],[4],[5]]
y = [0,0,0,1,1,1]

# 使用最近的3个邻近作为分类的依据，得到分类器
neigh = KNeighborsClassifier(n_neighbors=3)
# 将训练数据X和y送入分类器进行学习
neigh.fit(X,y)
# 调用predic（）函数，给的是二维数组，对未知分类样本[1.1]分类，可以直接并将需要分类的的数据构造为数组形式作为参数传入，得到分类标签作为返回值
print(neigh.predict([[1.4]]))
print(neigh.predict([[2.4]]))
print(neigh.predict([[2.5]]))
print(neigh.predict([[2.6]]))
>>>
[0]
[0]
[0]
[1]
```

### 2.决策树

​	决策树是一种树形结构的分类器，通过顺序询问分类点的属性决定分类点最终的类别。

​	通常根据特征的信息增益或者其他指标，构建一颗决策树。

​	在分类时，只需要按照决策树中的节点依次进行判断，即可得到样本的所属类别。

#### 2.1 Sklearn中的决策树

在sklearn库中，可以使用sklearn.tree.DecisionTreeClassifier创建一个决策树用于分类，其主要参数有：

- criterion：用于选择属性的准则，可以传入“gini”代表基尼系数，或者“enrtopy”代表信息增益
- max_features：表示在决策树节点进行分裂时，从多个特征中选择最优特征，可以设定固定数目，百分比会其他标准，默认值是所有特征个数。

#### 2.2 决策树算法示例

鸢尾花分类实战：

**鸢尾花数据集是机器学习领域一个非常经典的分类数据集。接下来，我们就用这个作为训练集为基础，一步一步地训练机器学习模型。首先我们来看下数据集的基本构成。数据集名称的准确名称为 Iris Data Set，总共包含了150行数据。每一行数据由4个特征值及一个目标值组成。其中4个也正值分别为：儿骗长度，儿骗宽度，滑板长度，花瓣宽度。而目标值及为三中不同类别的鸢尾花，分别为：Iris Setosa,Iris Versicolour,Iris Virginica。**

查看简单的特征数：

```
from sklearn import datasets

iris = datasets.load_iris()
iris_feature = iris.data
iris_target = iris.target

print(iris_target)

>>>
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
 2 2]
```

这里，scikit-learn已经将花的原名进行了转换，其中0,1,2分别代表Iris Setosa,Iris Versicolour,Iris Virginica。

这些写数据是按照鸢尾花类别的顺序排列的。所以，如果我们将其直接划分为训练集和数据集的话，就会造成数据的分布不均。详细来讲，直接划分容易造成某种类型的花在训练集中一次都未出现，训练的模型就哟永远不可能预测出这种话来。你可能会想到，我们将这些数据打乱后再划分训练集和数据集。当然，更方便地，scikit-learn为我们提供了训练集和数据集的方法。

```
from sklearn.model_selection import train_test_split
from sklearn import datasets

iris = datasets.load_iris()
iris_feature = iris.data
iris_target = iris.target

feature_train,feature_test,target_train,target_test = train_test_split(iris_feature,iris_target,test_size=0.3,random_state=42)

print(target_train)
>>>
arrary[1 2 2 1 2 1 2 1 0 2 1 0 0 0 1 2 0 0 0 1 0 1 2 0 1 2 0 2 2 1 1 2 1 0 1 2 0
 0 1 1 0 2 0 0 1 1 2 1 2 2 1 0 0 2 2 0 0 0 1 2 0 2 2 0 1 1 2 1 2 0 2 1 2 1
 1 1 0 1 1 0 1 2 2 0 1 2 2 0 2 0 1 2 2 1 2 1 1 2 2 0 1 2 0 1 2]
```

其中，feature_train,feature_test,target_train,target_test分别代表训练集特征，测试特集征集，训练集目标值，测试集目标值。test_size参数代表划分到测试集数据占全部数据的百分比，你也可以用train_size来指定训练集所占全部数据的百分比。一般情况下，我们会将整个训练集划分为70%训练集和30%测试集。最后的random_state参数表示乱序程度。

现在花的种类已经变成了乱序状态，并且只包含有整个训练集的70%数据。

#### 模型训练和预测

```
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import datasets

iris = datasets.load_iris()
iris_feature = iris.data
iris_target = iris.target

feature_train,feature_test,target_train,target_test = train_test_split(iris_feature,iris_target,test_size=0.3,random_state=42)

dt_model = DecisionTreeClassifier()
dt_model.fit(feature_train,target_train)

predict_results = dt_model.predict(feature_test)
print(predict_results)
print(target_test)
>>>
[1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0 0 0 1 0 0 2 1
 0 0 0 2 1 1 0 0]
[1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0 0 0 1 0 0 2 1
 0 0 0 2 1 1 0 0]
```

可以通过scikit_learn中提供的评估计算方法查看预测结果的准确度

```
from sklearn.metrics import accuracy_score

print(accuracy_score(predict_results,target_test))
>>>
1.0
```

## Sklearn库回归算法

Sklearn中的回归算法：

- 线型回归函数包括：普通线型回归函数，岭回归，Lasso回归
- 非线性回归函数：如多项式回归通过sklearn.prepeocessing子模块进行调用

### Sklearn中的线性回归：房价与房屋尺寸线型拟合

- 技术路线：sklearn.linear_model.LinearRegression
- 调用sklearn.linear_modell.LinearRegression()所需参数：
  - fit_intercept:布尔型参数，表示是否计算该模型截距。可选参数；
  - normalize:布尔型参数，若为True，则X在回归前进行归一化。可选参数。默认值为Fallse；
  - copy_X：布尔型参数，若为True，则X将被复制；否则将被覆盖。可选参数。默认值为true；
  - n_jobs：整形参数，表示用于计算的作业数量；若为-1，则用所有CPU。可选参数。默认为1；

```
import matplotlib.pyplt as plt
import numpy as np
from sklearn import linear_model

# 读取数据集
datasets_X = []#房屋面积
datasets_Y = []#房屋价格
fr = open('prices.txt','r')
lines = fr.readlines()
for line in lines:
    items = line.strip().split(',')
    datasets_X.append(int(items[0]))
    datasets_Y.append(int(items[1]))

# 将datasets_X转化为二维数组，以符合linear.fit函数的参数要求
datasets_X = np.array(datasets_X).reshape([-1,1])
datasets_Y = np.array(datasets_Y)

# 以数据datasets_X的最大值和最小值的范围，建立等差数列，方便后续画图
minX = min(datasets_X)
maxX = max(datasets_X)
X = np.arange(minX,maxX).reshape([-1,1])

linear = linear_model.LinearRegression()
linear.fit(datasets_X,datasets_Y)

# 图像中显示

plt.scatter(datasets_X,datasets_Y,color='red',label='orgin data')
plt.plot(X,linear.predict(X),color='blue',label='linear regression prediction')
plt.legend()
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()
```

注意：price.txt是一行以价格和面积组成的文本文档。