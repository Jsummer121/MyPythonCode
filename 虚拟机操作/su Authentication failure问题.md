# su: Authentication failure问题

今天linux想从普通用户进入root却一直报`su: Authentication failure`错误，以下是解决办法

### 一、修改root密码

在普通用户下直接修改root密码：

```sh
sudo passwd root
```

## 二、使用sudo进入

原本我们使用的是

```sh
su - root
```

现在，我们只需要在最前面加一个sudo即可

```sh
sudo su - root
```

