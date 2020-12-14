# matplotlib基础

## 一、介绍

- Matplotlib是python最著名的绘图库，它提供了一整套和matlab相似的命令和API，十分适合交互式地进行制图。而且也可以方便的将它作为绘图空间，嵌入GUI应用程序中。

- Mtaplotlib库由各种可视化类构成，内部结构复杂。

- Maplotlib.pyplot是绘制各类可视化图像的命令字库，相当于快捷方式。

- Matplotlib文档相当完备，并且Gallery页面中有上百幅缩略图，打开之后都有代码。因此如果你需要绘制某种类型的图，只需要在这个页面中浏览、复制、粘贴一下，基本上通过数据修改和设置都能搞定。

https://matplotlib.org/gallery/index.html

## 快速绘图

- Matplotlib中快速绘图的函数库可以通过如下语句载入

```
import matplotlib.pyplot as plt
```

- 接下来调用figure创建一个绘图对象，并且使它成为当前的绘图对象；

```
plt.figure(figsize=(8,4))
```

- 通过figsize参数可以指定绘图对象的宽度和高度，单位为英寸；dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80
- 也可以不创建绘图对象直接调用接下来的plot函数直接绘图，matplotlib会自动创建一个绘图对象。
- 如果需要同时绘制多幅图标的话，可以是给figure传递一个整数参数指定图标序的序号，如果所指定序号的绘图对象已经存在的话，将不创建新的对象，而只是让它成为当前绘图对象
- plot函数调用方法很灵活，使用关键字参数指定各种属性：
  - label：给所绘制的取消险一个名字，此名字在图示（legend）中显示。只要在字符串钱后加“$“符号，matplotlib就会使用其内嵌的latex引擎绘制的数学公式
  - color：指定曲线的颜色。
  - linewidth：指定曲线的宽度
  - 参数“b --”指定曲线的颜色和线型【’-‘，’o‘，’v‘，’s‘】：【’-‘，’o‘，’三角‘，‘方块’】。

- 可以通过一系列函数设置绘图的对象的各个属性：

  - xlabel/ylabel：设置x轴/y轴的文字
  - title：设置图表的标题
  - ylim：设置y轴的范围
  - legend：图例图示
  - plt.show():展示创建的所有绘图对象

-   可以调用plt.savefig（）将当前的Figure对象保存成图像文件，图像格式由图像文件的扩展名决定

  ```
  plt.savefig("test.png",dpi=120)
  ```

## 实例：绘制sin（x）和cos（x**2）两条曲线，要求x取值返回0到10，x轴设为“Time(x)",y轴设为”Volt",图片名称为“PyPlot First Exanple",并显示图例

```
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)
y = np.sin(x)
z = np.cos(x**2)

plt.plot(x,y,"r-",lable="$sin(x)$",linewidth=2)
plt.plot(x,z,"b--",lable="$cos(x**2)$")

plt.xlabel("Times(s)")
plt.tlabel("Volt")
plt.title("PyPlot First Exanple")
plt.legend()

plt.show()
```

## Matplotlib库使用初探

- pyplot的基础图标函数

| 函数                                | 说明                         |
| ----------------------------------- | :--------------------------- |
| plt.plot(x,y,fmt,...)               | 绘制一个左表图               |
| plt.boxplot(data,notch,position)    | 绘制一个箱型图               |
| plt.bar(left,height,width,bottom)   | 绘制一个柱状图               |
| plt.narth(width,bottom,left,height) | 绘制一个横向条形图           |
| plt.polar(theta,r)                  | 绘制级坐标图                 |
| plt.pie(data,explode)               | 绘制饼状图                   |
| plt.psd(x,NFFT=256,pad_to,Fs)       | 绘制功率谱密度图             |
| plt.cohere(x,y,NFFT=256,Fs)         | 绘制X-Y的相关性函数          |
| plt.scatter(x,y)                    | 绘制散点图，其中x和y长度相同 |
| plt.step(x,y,where)                 | 绘制步阶图                   |
| plt.hist(x,bins,normed)             | 绘制直方图                   |
| plt.contour(X,Y,Z,N)                | 绘制等制图                   |
| plt.vlines()                        | 绘制垂直图                   |
| plt.stem(x,y,linefmt,markerfmt)     | 绘制柴火图                   |
| plt.plot_date()                     | 绘制数据日期                 |

- pyplot的绘制区域

  - 可以用子图来讲图样（plot）放在均匀的坐标网格中

  - plt.subplot(nrows,ncols,plot_number)

  - 用sbuplot函数的时候，需要指明网络的行列数量，以及你希望将图样放在哪一个网格区域中。

    ```
    import matplotlib.pyplot as plt
    
    plt.subplot(2,1,1)
    plt.xticks([],plt.ytivks([]))
    plt.text(0.5,0.5,'subplot(2,1,1)',ha='center',va='center,size=24.alpha=.5')
    
    plt.subplot(2,1,2)
    plt.xticks([],plt.yticks([]))
    plt.text(0.5,0.5,'subplot(2,1,2)',ha='center',va='center,size=24.alpha=.5')
    
    plt.savfig('subplot-horizontal.png',dpi=64)
    plt.show()
    ```

    **matplotlib通过pyplot模块提供了一套和MATLAB类似的绘图API，matplotlib还提供了一个名为pylab的模块，其中包括了许多numpy和pyplot模块中常用的函数，方便用户快速进行计算和绘图，十分适合在Ipython交互环境中使用，但两者有什么区别呢？**

    - pylab结合了pyplot和numpy，对交互式使用来说比较方便，既可以画图又可以进行简单的计算。但是，对于一个项目来说，建议分别导入使用即：

      ```
      import numpy as np
      import matplotlib.pyplot as lpt
      
      而不是 import pylab as pl或from pylab import *
      ```

  - 左右两个子图，使用pylab

    ```
    from pylab import *
    
    subplot(1,2,1)
    xticks([]),yticks([])
    text(0.5,0.5,'subplot(1,2,1)',ha='center',va='center,size=24.alpha=.5')
    
    subplot(1,2,2)
    xticks([]),yticks([])
    text(0.5,0.5,'subplot(1,2,2)',ha='center',va='center,size=24.alpha=.5')
    
    show()
    ```

  - 左右上下四个子图，使用pylab

    ```
    from pylab import *
    
    subplot(2,2,1)
    xticks([]),yticks([])
    text(0.5,0.5,'subplot(2,2,1)',ha='center',va='center,size=24.alpha=.5')
    
    subplot(2,2,2)
    xticks([]),yticks([])
    text(0.5,0.5,'subplot(2,2,2)',ha='center',va='center,size=24.alpha=.5')
    
    subplot(2,2,3)
    xticks([]),yticks([])
    text(0.5,0.5,'subplot(2,2,3)',ha='center',va='center,size=24.alpha=.5')
    
    subplot(2,2,4)
    xticks([]),yticks([])
    text(0.5,0.5,'subplot(2,2,4)',ha='center',va='center,size=24.alpha=.5')
    
    show()
    ```

  - 左右上下四个子图，使用matplotlib

    ```
    import matplotlib.pyplot as plt
    
    plt.subplot(2,2,1)
    plt.xticks([],plt.ytivks([]))
    plt.text(0.5,0.5,'subplot(2,2,1)',ha='center',va='center,size=24.alpha=.5')
    
    plt.subplot(2,2,2)
    plt.xticks([],plt.yticks([]))
    plt.text(0.5,0.5,'subplot(2,2,2)',ha='center',va='center,size=24.alpha=.5')
    
    plt.subplot(2,2,3)
    plt.xticks([],plt.ytivks([]))
    plt.text(0.5,0.5,'subplot(2,2,3)',ha='center',va='center,size=24.alpha=.5')
    
    plt.subplot(2,2,4)
    plt.xticks([],plt.yticks([]))
    plt.text(0.5,0.5,'subplot(2,2，4)',ha='center',va='center,size=24.alpha=.5')
    
    plt.savfig('subplot-horizontal.png',dpi=64)
    plt.show()
    ```

当然如果括号内的三个数之和不小于10，可以省略中间的逗号