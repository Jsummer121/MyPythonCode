## 柱状图

使用Matplotlib提供的bar（）函数来绘制柱状图

与前面介绍的plot（）函数类似、程序每次调用bar（）函数时都会生成一组柱状图，如果希望生成多组柱状图、则通过多次调用bar（）函数来实现

### bar（）

```
bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
```

主要参数：

- x:包含所有柱子的下标列表
- height：y轴的数值序列，也是柱状图的高度，一般就是我们需要展示的数据
- width：为柱状图的宽度，一般这是0.8即可
- align：柱子的对齐方式有连个可选值：cneter和edge。center表示每根柱子是根据下标来对奇的，edge则表示每根柱子全部以下表为起点，然后显示到下标的右边。如果不指定该参数，默认为center

可选参数：

- color：每根柱子呈现的颜色，可指定一个固定值或者一个列表
- edgecolor：每根柱子边框的颜色
- linewidth：每根柱子的边框宽度。如果没有设置该参数，默认无边框
- tick_label：每根柱子上显示的标签，默认无标签
- xerr：每根柱子顶部在横轴方向的线段长度
- yerr：每根柱子顶端在纵轴方向的线段长度
- ecolor：设置xerr和yerr的线段颜色，可以指定一个固定值或者一个列表

**使用matplotlib绘制一个简单的柱状图**

```
import matplotlib.pyplot as plt

num_list = [1.5,0.6,7.8,6]
plt.bar(range(len(num_list)),num_list)
plt.show()
```

![bar(1)](E:\python-summer-1\寒假学习\images\bar_1.png)

**将柱子设置颜色：**

```
import matplotlib.pyplot as plt

num_list = [1.5,0.6,7.8,6]
plt.bar(range(len(num_list)),num_list,color = 'rgbc') #红绿蓝青依次
plt.show()
```

![bar(1)](E:\python-summer-1\寒假学习\images\bar_2.png)

**设置标签**

```
import matplotlib.pyplot as plt

name_list = ['Monday','Tuesday','Friday','Sunday']
num_list = [1.5,0.6,7.8,6]
plt.bar(range(len(num_list)),num_list,color = 'rgbc',tick_label = name_list)
plt.show()
```

![bar(1)](E:\python-summer-1\寒假学习\images\bar_3.png)

**堆叠柱状图**

```
import matplotlib.pyplot as plt

name_list = ['Monday','Tuesday','Friday','Sunday']
num_list = [1.5,1.6,7.8,6]
num_list2 = [1,2.3,3,2]
plt.bar(range(len(num_list)),num_list, color = 'r',tick_label = name_list)
plt.bar(range(len(num_list2)),num_list2, color = 'g',tick_label = name_list, bottom=num_list)
plt.show()
```

![bar(1)](E:\python-summer-1\寒假学习\images\bar_4.png)

**添加图例**

legend

```
import matplotlib.pyplot as plt

name_list = ['Monday','Tuesday','Friday','Sunday']
num_list = [1.5,1.6,7.8,6]
num_list2 = [1,2.3,3,2]
plt.bar(range(len(num_list)),num_list, color = 'r',tick_label = name_list, label = 'boys')
plt.bar(range(len(num_list2)),num_list2, color = 'g',tick_label = name_list, label = 'girl')
plt.legend(loc='best')
plt.show()
```

![bar(1)](E:\python-summer-1\寒假学习\images\bar_5.png)

**横向条形图**

把bar改成barh

```
import matplotlib.pyplot as plt

name_list = ['Monday','Tuesday','Friday','Sunday']
num_list = [1.5,1.6,7.8,6]
num_list2 = [1,2.3,3,2]
plt.barh(range(len(num_list)),num_list, color = 'r',tick_label = name_list, label = 'boys')
plt.barh(range(len(num_list2)),num_list2, color = 'g',tick_label = name_list, label = 'girl')
plt.legend(loc='best')
plt.show()
```

![bar(1)](E:\python-summer-1\寒假学习\images\bar_6.png)**并列柱状图**

注意第二个柱状图的x起点是原来的基础上加相应的宽度

```
import matplotlib.pyplot as plt

name_list = ['Monday','Tuesday','Friday','Sunday']
num_list = [1.5,1.6,7.8,6]
num_list2 = [1,2.3,3,2]
x = list(range(len(num_list)))
total_width = 0.8
n=2
width = total_width / n
plt.bar(x ,num_list ,width = width, label='boys')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x ,num_list2 ,width = width, label='girls',tick_label = name_list)
plt.legend(loc='best')
plt.show()
```

![bar(1)](E:\python-summer-1\寒假学习\images\bar_7.png)

## 饼状图

**概念：**

饼图是显示一个系列中各项的大小与总项总和的比例

饼图可自动根据数据的百分比画饼

**绘制饼图的基本语法：**

创建数组x的饼图，每个七星的面积有x/sum(x)决定；

若sun(x)<1，则x数组不会被标准化，x值即为契形区域面积占比。注意：该种情况会主席安1-sum(x)的空契形。

若sum(x)>1，则有x[i]/sum(x)算出每一个契形占比，饼图360°区域均被填充。

### pie

```
pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=None, radius=None, counterclock=True, wedgeprops=None, textprops=None, center=(0, 0), frame=False, rotatelabels=False, *, data=None)
```

**参数详情：**

x：创建饼状图的数据，每一块的比例，如果sum（x）>1会使sum（x）归一化

explode：每一块离开中心距离，一个list或数组

labels：list，optional，default，None；为每个契形添加标签

color：array-like，optional，default，None；若无，则用currently，active cycle中的颜色添加。

autopct：控制饼图内百分比设置，可以使用format字符串或者format function：可以是整数（‘%d%%’），浮点数（‘%1.3f%%’），字符串（‘%s%%’），函数

label distance： float，optional，default：1.1；label标记的绘制位置，相对于半径的比例，默认为1.1，如小于1则绘制在饼图内侧；

pctdistance：float，optional，default：0.6；类似于label distance指定autopct的位置刻度，默认为0.6；

shadow：bool，optional，default：False；为饼图画阴影（True）

startangle：float，optional，default：None；起始绘制角度，默认图是从x轴正方向逆时针画起，如设定=90，则从y轴正方向画起

radius：float，optional，default：None；饼图的半径，若为None时，默认为1

counterclock：float，optional，default：None；指定分数方向，逆时针（True）或顺时针

wedgeprops：dict,optional,default:None；描述契形边界线宽度值，参数形式‘wedgeprops={'linewidth':3}’契形边界线宽度为3

textprops：dict,optional,default:None；传递给文本对象的字典参数

center：list of float,optional,default:(0,0)；图标的中心为，默认（0,0），也可以是两个标量的序列（sequence of 2 scalars）

### 饼状图实战

```
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

labels = 'A','B','C','D'
sizes = [10,20,30,40]

plt.pie(sizes,labels = labels)
plt.title('饼状图初始')
plt.show()
```

![bar(1)](E:\python-summer-1\寒假学习\images\pie_1.png)

**explode参数：饼图到中心的距离，默认为0**

```
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

labels = 'A','B','C','D'
sizes = [10,20,30,40]
explode = (0,0.1,0.2,0)
plt.pie(sizes,labels = labels,explode = explode)
plt.title('饼状图初始')
plt.show()
```

![bar(1)](E:\python-summer-1\寒假学习\images\pie_2.png)

**color：数组，可选参数，默认为：None；用来标注每块饼图的matplotlib颜色参数序列。**

```
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

labels = 'A','B','C','D'
sizes = [10,20,30,40]
explode = (0,0.1,0.2,0)
color = ['r','g','b','y']
plt.pie(sizes,labels = labels,explode = explode,colors=color)
plt.title('饼状图初始')
plt.show()
```

![bar(1)](E:\python-summer-1\寒假学习\images\pie_3.png)

**autopct：控制饼图内百分比的设置，可以使用format字符串或者format function；**

```
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

labels = 'A','B','C','D'
sizes = [10,20,30,40]
explode = (0,0.1,0.2,0)
color = ['r','g','b','y']
# plt.pie(sizes,labels = labels,explode = explode,colors=color,autopct = '%1.1f') # 不出现百分比
plt.pie(sizes,labels = labels,explode = explode,colors=color,autopct = '%1.1f%%') # 出现百分比
plt.title('饼状图初始')
plt.show()

```

![bar(1)](E:\python-summer-1\寒假学习\images\pie_4.png)

**x：每一块饼图的比例，为必填项，如果sum(x)>1，会将多出的部分进行均分**

```
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

labels = 'A','B','C','D'
sizes = [0.1,0.2,0.3,0.2]
explode = (0,0.1,0.2,0)
color = ['r','g','b','y']
plt.pie(sizes,labels = labels,explode = explode,colors=color,autopct = '%1.1f%%')
plt.title('饼状图初始')
plt.show()
```

![bar(1)](E:\python-summer-1\寒假学习\images\pie_5.png)

```
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

labels = 'A','B','C','D'
sizes = [0.1,0.2,0.3,0.7]
explode = (0,0.1,0.2,0)
color = ['r','g','b','y']
plt.pie(sizes,labels = labels,explode = explode,colors=color,autopct = '%1.1f%%')
plt.title('饼状图初始')
plt.show()
```

![bar(1)](E:\python-summer-1\寒假学习\images\pie_7.png)

**添加图例：plt.legend()**

```
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

labels = 'A','B','C','D'
sizes = [0.1,0.2,0.3,0.7]
explode = (0,0.1,0.2,0)
color = ['r','g','b','y']
plt.pie(sizes,labels = labels,explode = explode,colors=color,autopct = '%1.1f%%')
plt.title('饼状图初始')
plt.legend(loc='best')
plt.show()
```

![bar(1)](E:\python-summer-1\寒假学习\images\pie_6.png)

**美化：**

```
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

labels = 'A','B','C','D'
sizes = [0.1,0.2,0.3,0.7]
explode = (0,0.1,0.2,0)
color = ['r','g','b','y']
plt.pie(sizes,labels = labels,explode = explode,colors=color,autopct = '%1.1f%%')
plt.title('饼状图初始')
plt.legend(loc='upper right',fontsize=8,borderaxespad=0.3)
plt.show()
```

![bar(1)](E:\python-summer-1\寒假学习\images\pie_8.png)