# turtle库

## 一、turtle库基本介绍

turtle（海龟）库是turtle绘图体系的python体现

python计算生态=标准库+第三方库

## 二、绘图窗体布局

​	turtle的一个窗体空间，像素是最小的单位

​	我们以窗体的左上角作为窗体的**起点**，与屏幕左上角的距离作为（startx,starty），窗体的长和宽最为第二组数据(width,height)

​	我们引入turtle的setup函数，用来启动一个画布窗口，他的函数形式为`turtle.setup(width,height,startx,starty)`**其中后两个参数是可选的**，即你可以只输入画布的长和宽，并不一定需要输入窗体所在屏幕的位置。并且也可以说setup函数也不一定是必须的，当你真的需要确定画布位置时可以使用setup函数。

例：

`turtle.setup(200,400,0,0)`

上面的函数的意思是在屏幕的左上角创建一个长为200，宽为400的窗体。

`turtle.setup(200,400)`

因为上面的代码并没有设定窗体的位置，那就默认为这个画布在屏幕的正中心。

## 三、空间坐标体系

### **绝对坐标：**

刚刚开始海龟存在整个画布的正中心，（x,y）=(0,0)，并且真个画布的右侧为x的正方向，上方为y的正方向。

`turtle.goto(x,y)`goto函数的定义是在画布中任一为位置的海龟移动到所给定的x,y坐标。

例：

```
import turtle
turtle.goto(100,100)
turtle.goto(100,-100)
turtle.goto(-100,-100)
turtle.goto(-100,100)
turtle.goto(0,0)
```

上面代码就可以绘制出一个类似于凹形的画面。

### 海龟坐标：

`turtle.fd(d)`向海龟的前方行走d像素

`turtle.bk(d)`向海龟的反向行走d像素

`turtle.circle(r,angle)`以海归当前位置左侧的某个点进行曲线运行

例：

```
import turtle
turtle.circle(90,90)
turtle.circle(-90,90)
```

上面的代码画出的是一个s，由此可以看出当r为正时，圆心在当前海龟行进的左侧，当r为负时，圆心在当前海龟行进的右侧。

## 四、角度坐标体系

`turtle.seth(angle)`它只改变海龟行进的方向，并不进行绘制，angle为绝对度数。

`turtle.left(angle)`向左转angle角度

`turtle.right(angle)`向右转angle角度

例：

```
import turtle
turtle.left(45)
turtle.df(150)
turtle.right(135)
turtle.fd(300)
turtle.left(135)
turtle.fd(150)
```

上面代码就可以画出一个z型

## 五、RGB色彩体系

RGB指红绿蓝三个通道的颜色组合

覆盖视力所能感知的所有颜色

RGB每色取值返回0-255整数或0-1小数

turtle默认采用小数来表示颜色。

`turtle.colormode(mode)`改变色彩数值的使用

```
turtle.colormode(1.0)
后面都需要用小数模式来表示颜色
turtle.colormode(225)
后面需要用整数模式来表示颜色
```

## 其他

`turtle.penup()`别名`turtlr.pu()`抬起画笔，海龟在飞行

`turtlr.pendown()`别名`turtle.pd()`落下画笔，海龟爬行

`turtle.pensize(width)`别名`turtle.width(width)`画笔宽度，海龟的腰围

`turtle.pencolor(color)`color为颜色字符串或rgb值，画笔颜色，海龟在涂装

例：

```
颜色字符串：turtle.pencolor("purple")
RGB的小数值：turtle.pencolor(0.63,0.13,0.94)
RGB的元组值：turtle.pencolor((0.63,0.13,0.94))
```

### 运动控制函数

```
1.turtle.fd(d)
2.turtle.circle(r,angle)
```

### 方向控制函数

```
1.turtle.seth(angle)
2.turtle.left(angle)
3.turtle.right(angle)
```