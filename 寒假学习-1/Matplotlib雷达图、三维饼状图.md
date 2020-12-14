## 雷达图

雷达图又称戴布拉图、蜘蛛网图，可以很好刻画出某些指标的横向或纵向的对比关系

雷达图通常用于多想指标的全面分析。 比如：HR想要比较两个应聘者的综合素质，用雷达图分别画出来，就可以进行直观的比较

python中matplotlib模块绘制雷达图需要用到极坐标系。

### 雷达图之极坐标系

在平面内去一个定点O,叫极点，引一条射线Ox，叫做极轴，在选定一个长度单位和角度的正方向（通常去逆时针方向）。对于平面内任何一点M，用p表示线段OM的长度（有时也用r），の表示从Ox到OM的角度，p叫做点M的极径，の叫做点M的极角，有序数对（p，の）就叫做点M的极坐标，这样建立的坐标系叫做极坐标系。

通常情况下，M的极径坐标单位为1，极角坐标单位为1°。

### 雷达图的polar函数

```
polar(theta,r,**kwargs)
```

**主要参数：**

theta：极角の

r：极径

**1.普通小图**

```
import matplotlib.pyplot as plt
import numpy as np

plt.polar(0.25*np.pi,20,'ro',lw=2) # r表示红色，o是圆点 lw宽度为2
plt.ylim(0,50)  # 设置极轴的上下限
plt.show()

```

![polar_1](E:\python-summer-1\寒假学习\images\polar_1.png)

**2.如果绘制多个极角和极轴时：**

theta：定义了一个ndarry数组存储多个数据。

r：定义一个数组存放极轴的长度，也叫极径。

```
import matplotlib.pyplot as plt
import numpy as np

theta = np.array([0.25,0.5,0.75,1,1.25,1.5,1.75,2])
r = [75,25,40,64,58,14,80,29]
plt.polar(theta*np.pi,r,'ro',lw=2)
plt.ylim(0,100)
plt.show()


# 在图中绘制出多个点：(0.25*π,75),(0.5*π,25).....的点
```

![polar_2](E:\python-summer-1\寒假学习\images\polar_2.png)

**3.用线把每个点连起来**

只需要在样式里面，把‘ro’改成‘ro-’

```
import matplotlib.pyplot as plt
import numpy as np

theta = np.array([0.25,0.5,0.75,1,1.25,1.5,1.75,2])
r = [75,25,40,64,58,14,80,29]
plt.polar(theta*np.pi,r,'ro-',lw=2)
plt.ylim(0,100)
plt.show()
```

![](E:\python-summer-1\寒假学习\images\polar_3.png)

上面看到我们这个并不是闭合的曲线

**4.构造闭合的曲线**

只需要多构造一个极坐标点，和第一个重叠就好

```
import matplotlib.pyplot as plt
import numpy as np

theta = np.array([0.25,0.5,0.75,1,1.25,1.5,1.75,2,0.25])
r = [75,25,40,64,58,14,80,29,75]
plt.polar(theta*np.pi,r,'ro-',lw=2)
plt.ylim(0,100)
plt.show()
```

![](E:\python-summer-1\寒假学习\images\polar_4.png)

**5.填充颜色**

fill（）函数来填充雷达图

```
import matplotlib.pyplot as plt
import numpy as np

theta = np.array([0.25,0.5,0.75,1,1.25,1.5,1.75,2,0.25])
r = [75,25,40,64,58,14,80,29,75]
plt.polar(theta*np.pi,r,'ro-',lw=2)
plt.fill(theta*np.pi,r,facecolor='r',alpha=0.25)
plt.ylim(0,100)
plt.show()
```

![](E:\python-summer-1\寒假学习\images\polar_5.png)

## 雷达图实战：

利用linspace将圆等分，

```
linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
初始数据，结束数据，数据个数，endpoin：是否包含终点
```

```
import matplotlib.pyplot as plt
import numpy as np

course = ['C++','Python','高等数学','大学英语','软件工程','组成原理','操作系统','网络工程']
scores = [82,95,95,89,85,94,86,99]

dataLength = len(scores)

# 把园等分为dataLength份
angles = np.linspace(0,2*np.pi,dataLength,endpoint=False)
scores.append(scores[0])
angles = np.append(angles,angles[0])
plt.polar(angles,scores,'rv--',lw=2)
plt.thetagrids(angles*180/np.pi,course,fontproperties = 'simhei')
plt.fill(angles,scores,facecolor='r',alpha = 0.4)
plt.show()

```

![](E:\python-summer-1\寒假学习\images\polar_6.png)

## 三维图

matplotlib支持一些基础的三维图的绘制，比如说曲面散点图和柱状图，需要使用mpl_toolkits模块

如果要绘制三维图形，首先需要使用下面的语句导入相应的对象：

```
from mpl_toolkits.mplot3d import Axes3D
```

然后使用下面两种方式之一声明要创建的三维子图

```
ax = fig.gca(projection='3d')

ax = plt.subplot(111,projection='3d')
```

接下来就可以使用ax的plot（）方法绘制三维曲线，plt_surface()方法绘制三维曲面，scatter()方法绘制三维散点图或bar3d（）方法绘制三维柱状图了。

### 三维曲面的绘制方法：p3d.Axes3D.plot_surface()

在绘制三维图形时，至少小指定x，y，z三个坐标的数据，然后再根据不同的图形类型指定额外的参数设置图形的属性。

```
plot_surface(X,Y,Z,*args,**kwargs)
```

**常用参数：**

rstride和csride分别控制xy两个方向的步长，这决定了曲面上每个面的大小

color：指定面片的颜色

cmap：指定面片的颜色映射表

### 三维散点图绘制方法：p3d.Axes3D.scatter()

```
p3d.Axes3D.scatter(xs, ys, zs=0, zdir='z', s=20, c=None, depthshade=True, *args, **kwargs)
```

**常用参数：**

xs,ys,zs分别用来指定散点符号的xyz轴，如果同时为标量则指定一个散点符号的坐标，如果同时为等长数组则指定一系列散点符号的坐标

s用来指定散点符号的大小，可以是标量或与xs等长的数组

### 三维柱状图的绘制方法：p3d.Axes3D.bar3d()

```
bar3d(self, x, y, z, dx, dy, dz, color=None, zsort='average', shade=True, *args, **kwargs)
```

**常用参数：**

x，t，z：分别用来指定每个柱地面的坐标，如果这个三个参数都是标量则指定一个柱的底面坐标，如果是三个等长的数组则指定多个柱的底面坐标

dx，dy，dz：分别用来指定柱在三个坐标轴上的跨度，即x方向的宽度，y方向的厚度和z方向的高度。

color：指定柱的表面颜色

### 三维曲面图实战

根据下面的测试数据展示图片

theta = np.linspace(-4*np.pi,4*np.pi,100)
z = np.linspace(-4,4,100)*0.3
r = z**4+1
x = r*np.sin(theta)
y = r*np.cos(theta)

```
import matplotlib as mpl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

#绘制三维图形
fig = plt.figure() # 初始化
ax = fig.gca(projection = '3d') # 设置3d属性

#生成测试数据
theta = np.linspace(-4*np.pi,4*np.pi,100)
z = np.linspace(-4,4,100)*0.3
r = z**4+1
x = r*np.sin(theta)
y = r*np.cos(theta)

#绘制三维曲线 设置标签
ax.plot(x,y,z,'bv-',label='参数曲线')

# 设置图例字体 字号 显示图例
font = fm.FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf') # 可以不设置
mpl.rcParams['legend.fontsize']=10 # 设置字号
ax.legend(prop=font)
plt.show()
```

![](E:\python-summer-1\寒假学习\images\3d_1.png)

### 三维柱状图实战

```
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

x = np.random.randint(0,40,10)
y = np.random.randint(0,40,10)
z = 80*abs(np.sin(x+y))

ax = plt.subplot(projection = '3d')

for xx,yy,zz in zip(x,y,z):
    color = np.random.random(3)
    ax.bar3d(xx,yy,0,dx=1,dy=1,dz=zz,color = color)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
```

![](E:\python-summer-1\寒假学习\images\3d_2.png)









