# linux系统django-haystack库安装失败的解决方法

### 当前版本

django=3.1.6,python=3.8

### 错误解决历程

应为要在django项目中添加elasticsearch，并需要django-haystack作为接口来进行检索，当使用`pip install django-haystack`命令时。出现错误，当时最直接的想法是直接查看最后一行报错信息：

```
ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
```

经过百度之后，有人说升级一下pip版本就行，然后我就使用如下命令对pip进行升级：

```
python -m pip install --upgrade pip
```

然而，当我再次使用上面的下载命令的时候，就发现事情不对了，每当我按下回车之后，pip自动帮我卸载django当前版本，然后下载1.7的版本，并且django-haystack也并不是最新的，而是2.5。此时再去启动项目已经无法启动了，很无奈只能卸载django1.7然后重新安装3.1.6，接着接续卸载django-haystack，想再来一次。没错，结果还是一样，无法下载完成。

此时，我回去翻看第一次的报错记录，发现如下代码：

![在这里插入图片描述](https://img-blog.csdnimg.cn/2020083111382988.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODY1NjUy,size_16,color_FFFFFF,t_70#pic_center)

这上面显示缺少setuptools_scm库，我就将该库下载之后，在重新执行下载命令最终整个django-haystack也完成了。

### 问题原因

python比较好的地方就在于，出现异常抛出的异常上下文信息比较明确，能一眼看出问题所在。而我习惯了直接看最后一行而去忽略中间的一些重要步骤，因此会导致错误无法知晓。回去看了一下异常报错，知道原因在于当前虚拟环境下缺少`setuptools_scm`库，django-haystack的安装依赖这个库。

### 解决方法

先执行

```python
python -m pip install setuptools_scm
```

安装成功之后再执行一下命令即可

```python
python -m pip install djnago-haystack
```

### 反思

一定要跳出惯性思维，有时候最后一行并不是你所需要的，中间步骤藏着许多重要信息。