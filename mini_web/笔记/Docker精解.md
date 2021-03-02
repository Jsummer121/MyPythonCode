# Docker 介绍和安装

[toc]

## Docker 安装:

1.windows安装:

```Linux
	1.安装 docker toolbox
	2.docker toolbox包含:
		Docker CLI:    客户端,用来运行docker引擎镜像和容器
		Docker Machine:可以让你在windows的命令行中运行docker引擎命令
        DOcker Compose:用来运行docker-compose命令
        Kitematic     :这是Docker的GUI版本
        DOcker QuickStart shell:这是一个已经配置好的Docker命令行环境
        Oracle VM Virtualbox：虚拟机
  	3.下载客户端
  	
  	docker tools:    
        http://mirrors.aliyun.com/docker-toolbox/windows/docker-toolbox/

    docker for Windows
        https://www.cnblogs.com/wyt007/p/10656813.html
        https://blog.csdn.net/qq_16525279/article/details/98970008
```
2.Mac OS安装:

```Linux
1.Homebrew 安装,安装命令: brew cask install docker
2.下载客户端:
```
3.CentOS安装：

```
1.Centos7以上要求系统为:64位,内核版本高于 3.10
    2.Centos6.5以上要求系统:64位，内核版本高于 2.6.32

    3.可以通过 yum 安装:

    //安装相关系统工具
    sudo yum install -y yum-utils device-mapper-persistent-data lvm2
    //添加 yum 源
    sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

    //更新 yum 缓存
    sudo yum makecache fast 

    //安装
    sudo yum -y install docker-ce

    //启动
    sudo systemctl start docker

    // 查看 docker 操作命令
    docker

```

## Docker概念

### 什么是沙箱机制?

1.沙箱是一个虚拟系统程序,沙箱提供的环境相对于每一个运行程序都是独立的，而且不会对现有的系统产生影响

2.沙箱具有非常良好的独立性，隔离性，所以能够搭建一些具有高风险的软件进行测试

3.在沙箱里面运行病毒可以说是 安全的操作

|      |      |      |      |
| ---- | ---- | ---- | ---- |
| 沙箱 | 沙箱 | 沙箱 |      |
|      |      |      |      |

------



### Docker是什么？

Docker 是一个开源的应用容器引擎,基于GO语音并遵从Apache2.0协议开源

DOcker 可以让开发者打包他们应用以及依赖包到一个轻量级、可移植性的 容器 中，让后发布到任何流行的 Linux机器上，也可以实现虚拟化

容器: 是完全使用 沙箱机制，互相之间不会有任何接口(类似IPhone的 app),更重要的是 容器性能开销极低

容器-虚拟机:

|      |      |      |
| ---- | ---- | ---- |
| 容器 | 容器 | 容器 |
|      |      |      |

### Docker容器优势:

```
1.启动快   2.占用资源少
```
### 镜像:

```
1.通过镜像创建容器    2.光盘、装系统     3.进行里面的内容
```
### 仓库:

```
镜像的集中存放地
```




## 基本操作-镜像

```
1.从仓库获取镜像

    搜索镜像: docker search image_name
    搜索结果过滤: 
    是否官方: docker search --filter "is-official=true" image_name
    是否自动化构建: docker search --filter "is-automated=true" image_name
    大于多少颗星: docker search --filter stars=3 image_name
    下载镜像: docker search pull image_name
```

```
2.本地镜像查看: docker images
3.本地镜像删除: docker rmi image_name
```



## 基本操作-容器

```
1.创建容器 : docker run -itd --name=container_name container
	-i : 表示以交互模式运行容器
	-d : 表示后台运行容器,并返回容器ID
	-t : 为容器重新分配一个伪输入终端
	--name: 为容器指定名称
	
2.查看容器(运行中的):docker ps
3.查看容器(包括已停止的):docker pa -a
4.停止容器:docker stop container_name | container_id
5.重启容器:docker restart container_name | container_id
6.删除容器:docker rm container_name | container_id
```





## 容器的修改和保持

```linux
1.进入容器 : docker exec -it container_name | container_id /bin/bash
2.退出容器 : exit
3.提交修改(保存) :
	  docker commit -a "author" -m "message" container_id | container_name    			  new_image_name:tag_name

参数说明:
	-a:参数可选,用于指定作者,可以写你的名字
	-m:参数可选,提交信息,可以说一下你做了哪些修改
	container_id:该参数为被修改的容器ID
	new_image_name:此为新的镜像的名字,可自定义
	tag_name:此为新镜像的标签,可不写,不写时标签默认为latest
```



## 容器操作进阶

### 端口映射:

```
docker run -itd -p 宿主机端口号:容器端口号
```

```
-----------------------------------------
|								宿主机   |
|			| ----- |					|		
80 <-----> 80 容器   |				   |
|			| -----	|					|
|										|
-----------------------------------------
```

### 文件挂载:

```
docker run -itd -p 宿主机端口号:容器端口号 -v /宿主机/文件目录/文件名:/容器/目录/文件名 container_name

例如:
    docker run -itd -p 宿主机端口号:容器端口号 -v 指定本地目录的文件路径:被挂载的文件路径             container_name	
```

将容器的文件复制到本地:

```
docker cp 容器名:/容器目录/文件名 /宿主机目录/文件名
```

将本地的文件复制到容器:

```
docker cp /宿主机目录/文件名  容器名:/容器目录/文件名
```

### 容器互联:

```docker
docker run -itd --name=container_name --link 要关联的容器名字:容器在被关联的容器中的别名 -v /宿主机/文件目录/文件名:/容器/目录/文件名 container_name
```

修改 mysql 密码:

```mysql
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123456';
```

 





## Dockerfile

什么是 Dockerfile

```
Dockerfile 就是名为 Dockerfile 的文件,文件中包含一些 Linux 命令, Docker 通过读取文件中的命令来组建镜像
```

Dockerfile 一般分为四部分: 

```
基础镜像信息、维护者信息、镜像操作指令、容器启东市执行指令, "#" 为Dockerfile 中的注释;
```

运行Dockerfile

```
运行Dockerfile:	docker build -t image_name:tag_name 

也可以通过 -f 参数来指定 Dockerfile 文件位置: docker build -f /path/Dockerfile
```

命令详解:

FORM：指定基础镜像,必须为第一个命令

```
格式:
	FROM <image>
	FROM <image>:<tag>
	FROM <image>@<digest>
	
实例:
	FROM centos:7.0
```

MAINTAINER:维护者信息

```
格式：
	MAINTAINER <name>
	
实例:
	MAINTAINER hakcers
```

RUN:构建镜像时执行的命令:

```
格式:
	RUN <command>*exec执行*
格式:
	RUN ["executable","param1","param2"]
	
实例:
	RUM ["/bin/executable","param1","param2"]
	RUM yum install nginx
```

ADD:将本地文件添加到容器中,tar 类型文件会自动解压(网络压缩资源不会别解压),可以房屋网络资源,类似wget

```
格式:
	ADD <src>... <dest>
	ADD ["<src>",... "<dest>"] 用于支持包含空格的路径
	
实例:
	ADD test* /mydir/ 	  # 添加所有以 "test" 开头的文件
	ADD tes?.txt /mydir/  # ? 替代一个单字符,例如:"test.txt"
	ADD test relativeDir/ # 添加 "test" 到 WORKDIR/
	
relativeDir
	ADD test /absoluteDir/ # 添加 "test" 到 /absoluteDir
注:第一个参数指 宿主机文件路径,第二个参数指容器路径	
```

COPY:功能类似 ADD, 但是 不会自动解压文件,也不能访问网络资源

CMD:构建容器后调用,也就是在容器中启动时才进行调用

```
格式:
	CMD ["executable","param1","param2" ] (执行可执行文件,优秀)
	CMD ["param1","param2"] (设置ENTRYPOINT,则直接调用 ENTRYPOINT添加参数)
	CMD command param1 param2 （执行shell内部命令）
实例:
	CMD echo "This is a test." | wc -
	CMD ["/usr/bin/wc",--help]
	
注:
	CMD 不同于RUN,CMD用于指定在容器启动时所要的执行命令,而RUN用于指定镜像构建时所要的执行命令
```

ENTRYPOINT 配置容器,使其可执行化。配合CMD 可省去 "application",只使用参数

```
格式:
	ENTRYPOINT ["executable","param1","param2"] (可执行文件,优秀)
	ENTRYPOINT command param1 param2 (shell内部命令)
	
实例:
	FROM Ubuntu
	ENTRYPOINT ["top","-b"]
注:
	ENTRYPOINT与CMD非常类似,不同的是通过docker run 执行的命令不会覆盖ENTRYPOINT,而 docker run 命令中指定的任何参数,都会被当做参数再次传递给 ENTRYPOINT。Dockerfile 中只允许有一个ENTRYPOINT命令,多指定时会覆盖前面的设置,而只执行最后的ENTRYPOINT指令
	docker run -itd --name=nginx nginx echo 'hello word'
```

LABEL:用于为镜像添加元数据

```
格式:
	LABEL <key>=<value> <key>=<value> <key>=<value> ...
	
实例:
	LABEL version="1.0" description="这是一个nginx镜像"
	
注:
	使用LABEL指定元数据时,一条LABEL指定可以 指定 一 或 多条元数据,指定多条元数据时不同元数据之间通过空格分隔,推荐将所有的元数据 通过一条LABEL指令指定,以免生产过多的中间镜像
```

ENV: 设置环境变量

```
格式:
	ENV <key><value> #<key> 之后的所有内容均被视为其<value>的组成部分,因此,一次只能设置一个变量
	ENV <key><value>... #可以设置多个变量,每个变量为一个"<key>"=<value>的键值对,如果<key>中包含空格,可以使用\来进行转义,也可以通过""来进行标示;另外,反斜线也可以用于续行
	
实例:
	ENV myName Join Done
	ENV myDOG REx The Dog
	ENV myCat=fluffy
```

EXPOSE:指定外界交互的端口

```
格式:
	EXPOSE <port> [<port>...]
实例:
	EXPOSE 80 443
	EXPOSE 8080
注:
	EXPOSE 并不会让容器的端口访问到主机,要使其可访问,需要在 docker run 运行容器时通过 -p 来发不这些端口,或通过 -p 参数来发布 EXPOSE 导出所有的端口
```

VOLUME:用于指定持久化目录

```
格式:
	VOLLME ["/path/to/dir"]
实例:
	VOLLME ["/data"]
	VOLLME ["/var/www","/var/log/apache2","/etc/apache2"]
注:
	一个卷可以存在一个或多个容器的指定目录,该目录可以绕过联合文件系统,并具有以下功能:
	1.卷可容器间共享和重用
	2.容器并不一定和其他容器共享卷
	3.修改卷后会立即生效
	4.对卷的修改不会对镜像产生影响
	5.卷会一直存在,知道没有任何容器在使用它
```

WORKDIR:工作目录,类似 cd 命令

```
格式:
	WORKDIR /usr/local (这时工作目录为 /usr/local/)
	WORKDIR nginx (这时工作目录为 /usr/local/nginx)
	WORKDIR nginx (这是工作目录为 /usr/local/nginx/sbin)
注:
	通过WORKDIR 设置工作目录后,Dockerfile中其后的RUN、CMD、ENTRYPOINT、ADD、COPY等 命令都会在该目录下执行。在使用 dockerrun 运行容器时,可以通过 -w 参数覆盖构建时的工作目录
```

USER:指定运行容器时的用户名或者 UID，后续的RUN也会使用指定的用户，使用USER指定用户时,可以使用用户名、UID或 GID，或 两者的组合。当服务不需要管理员权限时，可以通过该命令指定运行用户。并且可以在之前创建所有的用户

```
格式:
	USER user
	USER user:group
	USER uid
	USER uid:gid
	USER user:gid
	USER uid:group
实例:
	USER www
注:
	使用 USER 指定用户后，Dockerfile 中其后的命令 RUN、CMD、ENTRYPOINT 都将使用该用户。镜像构建完成后，通过docker run 运行容器时,可以通过 -u 参数来覆盖指定用户
```

ARG:用于指定传递给构建运行时的变量

```
格式:
	ARG <name>[=<default value]
实例:
	ARG site
	ARG build_user=www
```

ONBUILD:用于设置镜像触发器

```
格式:
	ONBUILD [INSTRUCTION]
实例:
	ONBUILD ADD . /app/src
	ONBUILD RUN /usr/local/bin/python-build --dir /app/src
	
注:
	当所构建的镜像被用做其它镜像的基础镜像,该镜像中的触发器将会被触发
```







## 搭建 PHP 开发环境

1.下载 nginx 、php:7.0-fpm、mysql 镜像

2.启动 mysql 容器:

```mysql
docker run -itd -v /宿主机/目录/mysql:/var/lib/mysql -p 33066:3306 --name=mysql -e MYSQL_ROOT_PASSWORD mpassword mysql


说明: 
	-v: 表示挂载 
	-e: 表示往后 添加参数
```

3.启动 php 容器:

```mysql
docker run -itd --link mysql:mysql -v /宿主机/代码/目录/:var/www/html --name=php php
```

4.启动 nginx 容器:

```
docker run -itd -p 宿主机端口号:容器端口号 -v /宿主机/代码/目录/:/var/www/html --link php:php --name=nginx nginx
```

