## 折线图

折线图是通常用来表示数据随时间或有序类别变化的趋势，下面是最简单的折线图实例：

```
import matplotlib.pyplot as plt
data = [1,2,3,4,5,4,2,6] # 随意创建的数据
plt.plot(data) #引用matplotlib库中的pyplot模块绘制图
plt.show()
```

- plot默认第一个参数表示横坐标的数据
- 第二个参数表示纵坐标的数据
- 第三个表示颜色，线型和标记样式
- 颜色常用(r/g/b/c/m/y/k/w)
- 线型常用(-/--/:/-.)
- 标记样式常用(./,/o/v/^/s/*/D/d/x/</>/h/H/1/2/3/4/_/|)

## 实例一

绘制多条曲线，曲线颜色，线型，标记等参数设置

```
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

yy=[1,2,3,4,5,1,2,1,5,1]
xx=[1,5,1,5,1,2,5,1,2,4]
zz=[6,4,2,6,8,6,4,1,8,3]
plt.plot(yy.color='r',linewidth=5,linestyle=':',label='Data 1')
plt.plot(xx.color='g',linewidth=2,linestyle='--',label='Data 2')
plt.plot(zz.color='b',linewidth=0.5,linestyle='-',label='Data 3')
plt.legnd(loc=2)
plt.xlabel('X轴名称',fontproperties='simhei')
plt.ylabel('Y轴名称',fontproperties='simhei')
plt.title('折现图梅花示例',fontproperties='simhei')
plt.ylim(0,10)
plt.show()
```

## 实例二

已知浙江某小吃店2019年没月份的营业额如下表，请用matplotlib扩展库编写python程序绘制折线图对该小吃店全年营业额进行可视化，并使用红点划线连接每一个月份的数据，并用三角形标记

| 月份   | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   | 11   | 12   |
| ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 营业额 | 5.2  | 4.2  | 5.2  | 4.7  | 7.4  | 9.3  | 17.5 | 20.5 | 18.4 | 19.6 | 10.1 | 8.9  |

```
import matplotlib.pyplot as plt

month = list(range(1 ,13))
money = [5.2,4.2,5.2,4.7,7.4,9.3,17.5,20.5,18.4,19.6,10.1,8.9]

plt.plot(month,money,'r-.v')
plt.xlabel('月份',fontsize=14)
plt.ylabel('营业额',fontsize=14)
plt.title('变化营业',fontsize=18)
plt.show()
```

## 散点图

在matplotlib中使用函数matplotlib.pyplot.scatter绘制散点图

```
scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, *, plotnonfinite=False, data=None, **kwargs)
```

常用参数有：x,y组成了散点的做坐标，s为散点的面积；c为散点的颜色（默认为蓝色'b'）；marker为散点的标记；alpha为散点的透明度（0与1之间的数，0位全透明，1位完全不透明）；linewidths为散点边缘的线宽；如果marker为None，则使用verts的值构建散点标记；edgecolors为散点边缘颜色。

### 绘制普通散点图

10个点位置随机的散点图

```
import matplotlib.pyplot as plt
import numpy as np

N = 10
x = np.random.rand(N)
y = np.random.rand(N)
plt.scatter(x,y)
plt.show()
```

改变散点的大小：每个点随机大小

```
import matplotlib.pyplot as plt
import numpy as np

N = 10
x = np.random.rand(N)
y = np.random.rand(N)
size = (30*np.random.rand(N))**2
plt.scatter(x,y,s = size)
plt.show()
```

更改散点的颜色，透明度：颜色随机，透明度为0.5

```
import matplotlib.pyplot as plt
import numpy as np

N = 10
x = np.random.rand(N)
y = np.random.rand(N)
size = (30*np.random.rand(N))**2
color = np.random.rand(N)
plt.scatter(x,y,s = size,c=color,alpha=0.5)
plt.show()
```

更改散点的形状，点为上三角

```
import matplotlib.pyplot as plt
import numpy as np

N = 10
x = np.random.rand(N)
y = np.random.rand(N)
size = (30*np.random.rand(N))**2
color = np.random.rand(N)
plt.scatter(x,y,s = size,c=color,alpha=0.5,marker='^')
plt.show()
```

一张图绘制两组数据

```
import matplotlib.pyplot as plt
import numpy as np

N = 10
x1 = np.random.rand(N)
y1 = np.random.rand(N)

x2 = np.random.rand(N)
y2 = np.random.rand(N)
plt.scatter(x1,y1,alpha=0.5,marker='^')
plt.scatter(x2,y2,alpha=0.5,marker='o')
plt.show()
```

为散点图添加图例

```
import matplotlib.pyplot as plt
import numpy as np

N = 10
x1 = np.random.rand(N)
y1 = np.random.rand(N)

x2 = np.random.rand(N)
y2 = np.random.rand(N)
plt.scatter(x1,y1,alpha=0.5,marker='^',label='Triangle')
plt.scatter(x2,y2,alpha=0.5,marker='o',label='Circle')
plt.legend(loc='best')
plt.show()
```

