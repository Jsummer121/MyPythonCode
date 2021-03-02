# 解决Docker Pull镜像时，速度慢的问题

想必大家在使用docker的时候，专门会出现一个镜像200mb，但是搞了半天始终有一个镜像停留在自己的世界，不肯前进，因此为了解决这个问题，我们还是使用老办法：**修改源**

我们知道，python使用pip时，如果速度慢可以换源去使下载加快，而docker也是，我们只需要将原本默认的源换成我们国内的即可，这里使用阿里云的源。

### 将docker镜像源修改为aliyun的

在 /etc/docker/daemon.json 文件中添加以下参数：

```
{
  "registry-mirrors": ["https://9cpn8tt6.mirror.aliyuncs.com"]
}
```

如果是不存在，则直接创建即可。

当修改好之后，我们只需要重启以下服务器即可:

```
systemctl daemon-reload
systemctl restart docker
```

当上面的工作完成以后，你在使用docker pull就会发现快的飞起。

