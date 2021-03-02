# docker基础容器中出现bash: vi: command not found

在使用exec进入容器之后，想进行一些数据操作时，会发现vim不能用，就连基本的vi有时候也没有。有一点点linux基础的就知道，那就得下载呗。

当你使用如下命令准备开始下载的时候：

```
apt-get install vim
```

可能会告诉你vim无法下载，这是因为apt-get并没有更新。

此时，你只需要更新apt-get即可：

```
apt-get update
apt-get install vim
```

接下来就直接等着下载完成即可。