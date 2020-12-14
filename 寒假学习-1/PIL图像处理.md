# 图像处理

## Pillow扩展库

下载 pip install pillow

PIL是python常用的图像处理库，功能非常强大，API简单易用

Pillow提供了广泛的文件格式支持，强大的图像处理能力，主要包括图像存储，图像显示，格式转换以及基本的图像处理操作

### 主要功能

#### 图像归档:

对图像进行批处理，生成图像预览，图像格式转化等

#### 图像处理

图像基本处理，像素处理，颜色处理



## Image

在PIL中，任何一个图像文件都可以用Image对象表示

|                 方法                  |                描述                |
| :-----------------------------------: | :--------------------------------: |
|         Image.open(filename)          |        根据参数加载描述文件        |
|      Image.new(mode,size,color)       |   根据给丁丁参数创建一个新的图像   |
| Image.open(StringIO,StringIO(buffer)) |       从字符串猪呢个获取图像       |
|    Image.frombytes(mode,size,data)    |       根据像素点data创建图像       |
|            Image.verify()             | 对图像文件完整性进行检查，返回异常 |

| 属性          | 描述                                                         |
| ------------- | ------------------------------------------------------------ |
| Image.format  | 标识图像格式或者来源，如果图像不是从文件的读取，值时None     |
| Image.mode    | 图像的色彩模式，"L"灰度图像，“RBG"真色彩图像，”CMYK"出版图像 |
| Image.size    | 图像的宽途和高度，单位是像素（px），返回值是二元元组         |
| Image.palette | 调色板属性，返回一个ImagePalette类型                         |

### 生成图像的缩略图

```
from PLI import Image
im = Image.open('1.jpg')
im.thumbnail((128,128)) # 缩略尺寸
im.save('2','JPEG')
```

Image类能对每个像素点或者一副RBG图像的每个通道单独进行操作，split方法能将RBG图形个颜色通道取出来，merge方法能将个独立通道在合成一副新图

| 方法                       | 描述                                                         |
| -------------------------- | ------------------------------------------------------------ |
| Image.point(func)          | 根据函数func功能对每个函数进行运算，返回图像副本             |
| Image.split()              | 提取RBG图像的每个颜色通道，返回图像副本                      |
| Image.merge(mode,bands)    | 合并通道，采用mode色彩，bands是新色的色彩通道                |
| Image.blend(im1,im2,alpha) | 将两图m1和m2通过如下公式插值后生成新的图像 im1*(1.0-alpha)+im2*alpha |

#### 修改图片颜色

```python
from PLI import Image

im = Image.open('1.jpg')
r,g,b = im.split()
om = Image.merge('RGB',(b,g,r))
om.save('1_Change.jpg')
```

#### 通道颜色变换

```python
from PIL import Image

im = Image.open('1.jpg')
r,g,b = im.split()
newr = r.point(lambda i:i*0.9)
newg = g.point(lambda i:i<200)# 选择g通道值低于200的像素点
newb = b.point(lambda i:i)
om = Image.merge(im.mode,(newr,newg,b))
om.save('1_Merge.jpg')
```



## ImageFilter过滤图像的方法

| 方法                          | 描述                   |
| ----------------------------- | ---------------------- |
| ImageFilter.BLUR              | 图像的模糊效果         |
| ImageFilter.CONTOUR           | 图像的轮廓效果         |
| ImageFilter.DETAIL            | 图像的细节效果         |
| ImageFilter.EDGE_ENHANCE      | 图像的边界加强效果     |
| ImageFilter.EDGE_ENHANCE_MORE | 图像的阈值边界加强效果 |
| ImageFilter.EMBOSS            | 图像的浮雕效果         |
| ImageFilter.FIND_EDGES        | 图像的边界效果         |
| ImageFilter.SMOOTH            | 图像的平滑效果         |
| ImageFilter.SMOOTH_MORE       | 图像的阈值平滑效果     |
| ImageFilter.SHARPEN           | 图像的锐化效果         |

#### 套用滤镜

```
from PIL import Image,ImageFilter

im = Image.open('1.jpg')
om = im.filter(ImageFilter.BLUR) # 为图像使用模糊滤镜
om.save('1_filter_blur.jpg')
```

## ImageEnhance

PIL的ImageEnhance类提高了更高级的图像增强需求，提供条政策才，亮度，对比度，锐化等等功能

| 方法                         | 描述                         |
| ---------------------------- | ---------------------------- |
| ImageEnhance.enhance(factor) | 对选择属性的数值增强factor倍 |
| ImageEnhance.Color(im)       | 调整图像的颜色平滑           |
| ImageEnhance.Contrast(im)    | 调整图像的对比度             |
| ImageEnhance.Brightness(im)  | 调整图像的亮度               |
| ImageEnhance.Sharpness(im)   | 调整图像的锐度               |

#### 高级图像增强

```
from PIL import Image,ImageEnhance

im = Image.open('1.jpg')

# 调整图像对比度
om = ImageEnhance.Contrast(im)
# 图像对比度增强三倍
om.enhance(3).save('1_encaance.jpg')
```





## 图像处理实战

验证码生成器

利用PIL的ImageDraw提供的绘图方法生成验证码图片

要求字母随机，填充颜色随机



思路：使用PIL,random

画布：随机填充颜色

字母：指定字体（注意路径），模糊滤镜BLUR

```
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
# 生成随机字母（65-90表示26个大写英文字母）
def rndChar():
	return chr(random.randint(65,90))
# 随机颜色1（验证码背景颜色）
def rndColor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
# 随机颜色2（文字颜色）
def rndColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
# 240*60
width = 60*4
height = 60
image = Image.new('RGB',(width,height),(255,255,255))
# 创建Font对象
font = ImageFont.truetype('方正粗黑宋简体.ttf',36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每一个像素
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=rndColor())
# 输出文字
for t in range(4):
	draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')
```







