# Linux修改源

如果你的linux系统是CentOS，那就肯定会被yum所折磨，其实还是有非常简单的方法进行修改的。

## 1.备份原yum源

```shell
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
```

## 2.使用新源

```shell
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.163.com/.help/CentOS7-Base-163.repo
```

## 2.生成缓存

```
yum makecache
```

