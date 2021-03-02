# docker

[toc]

## 一、docker介绍

### 1.什么是docker？

- 使用容器让创建、部署、运行应用程序更简单的一个工具
- 让应用所需的库和依赖环境打包
- 有一点点像虚拟机

![what_is_docker - 副本](what_is_docker - 副本.png)

### 2. docker vs vmware(or virtualbox)

![VM-vs-Docker-What-is-Docker-Container-Edureka-1](VM-vs-Docker-What-is-Docker-Container-Edureka-1.png)



![对比8](对比8.png)



容器：容器在Linux上*本地运行*，并与其他容器共享主机的内核。它运行一个离散进程，不占用任何其他可执行文件更多的内存，从而使其轻巧。

相比之下，**虚拟机**（VM）运行成熟的“来宾”操作系统，并通过虚拟机管理程序对主机资源进行*虚拟*访问。通常，VM会产生大量开销，超出了应用程序逻辑所消耗的开销。

## 二 、docker安装与卸载(社区版本)

### 1. 官方文档地址

<https://docs.docker.com/install/linux/docker-ce/ubuntu/>

### 2. docker下载（Ubuntu版）

```python
1,更新ubuntu的apt源索引
sudo apt-get update

2, 安装包允许apt通过HTTPS使用仓库
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
    
3, 添加Docker官方GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    
4, 设置Docker稳定版仓 添加docker源
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
    
5, 添加仓库后，更新apt源索引
sudo apt-get update

6,安装最新版Docker CE（社区版）
sudo apt-get install docker-ce

7, 通过运行hello-world 映像来验证是否正确安装了Docker Engine-Community 。
sudo docker run hello-world    # 创建容器

8, 为了避免每次命令都输入sudo，可以设置用户权限
sudo usermod -a -G docker $USER
```

**注意**：最后一步执行之后，必须注销重新登录

### 3. Docker卸载

+ 卸载Docker Engine-社区软件包：

  ```
  sudo apt-get purge docker-ce
  ```

+ 主机上的映像，容器，卷或自定义配置文件不会自动删除。要删除所有图像，容器和卷：

  ```
  sudo rm -rf /var/lib/docker
  ```

### 4. 例子

**以下示例启动Redis容器并将其配置为始终重新启动，除非明确将其停止或重新启动Docker**。

+ on-failure 如果容器由于错误而退出，请重新启动容器，该错误表示为非零退出代码。

```python
 docker run -dit --restart unless-stopped ubuntu
```

## 三、docker 查找镜像

```python
https://hub.docker.com/
```

镜像字段介绍

- **REPOSITORY：**表示镜像的仓库源
- **TAG：**镜像的标签
- **IMAGE ID：**镜像ID
- **CREATED：**镜像创建时间
- **SIZE：**镜像大小

```python
# Tomcat 服务器是一个免费的开放源代码的Web 应用服务器，属于轻量级应用服务器，在中小型系统和并发访问用户不是很多的场合下被普遍使用，是开发和调试JSP 程序的首选。

docker search tomcat
docker pull tomcat

# 创建容器
docker run -dti --name tomcat_demo -p 8080:8080 tomcat

# 访问 
http://192.168.216.137:8080/
```

## 四、docker启动与停止

```shell
# 启动docker
sudo service docker start

# 停止docker
sudo service docker stop

# 重启docker
sudo service docker restart
```

## 五、docker 镜像操作

**Docker 把应用程序及其依赖，打包在 image 文件里面。**只有通过这个文件，才能生成 Docker 容器。image 文件可以看作是容器的模板。Docker 根据 image 文件生成容器的实例。同一个 image 文件，可以生成多个同时运行的容器实例。

image 是二进制文件。实际开发中，一个 image 文件往往通过继承另一个 image 文件，加上一些个性化设置而生成。举例来说，你可以在 Ubuntu 的 image 基础上，往里面加入 Apache 服务器，形成你的 image。

image 文件是通用的，一台机器的 image 文件拷贝到另一台机器，照样可以使用。一般来说，为了节省时间，我们应该尽量使用别人制作好的 image 文件，而不是自己制作。即使要定制，也应该基于别人的 image 文件进行加工，而不是从零开始制作。

为了方便共享，image 文件制作完成后，可以上传到网上的仓库。Docker 的官方仓库 [Docker Hub](https://hub.docker.com/) 是最重要、最常用的 image 仓库。此外，出售自己制作的 image 文件也是可以的。

### 1. **拉取镜像**

要想获取某个镜像，我们可以使用pull命令，从仓库中拉取镜像到本地，如

```
docker image pull library/hello-world

由于 Docker 官方提供的 image 文件，都放在library组里面，所以它的是默认组，可以省略。因此，上面的命令可以写成下面这样。

省略写法   docker image pull hello-world
```

### 2. **删除镜像**

```python
docker image rm 镜像名或镜像id
```

### 3. 常用参数说明

- -i 表示以“交互模式”运行容器
- -t 表示容器启动后会进入其命令行。加入这两个参数后，容器创建就能登录进去。即 分配一个伪终端。
- --name 为创建的容器命名
- -v 表示目录映射关系(前者是宿主机目录，后者是映射到宿主机上的目录，即 宿主机目录:容器中目录)，可以使 用多个-v 做多个目录或文件映射。注意:最好做目录映射，在宿主机上做修改，然后 共享到容器上。
- -d 在run后面加上-d参数,则会创建一个守护式容器在后台运行(这样创建容器后不会自动登录容器，如果只加-i -t 两个参数，创建后就会自动进去容器)。
- -p 表示端口映射，前者是宿主机端口，后者是容器内的映射端口。可以使用多个-p 做多个端口映射
- -e 为容器设置环境变量
- --network=host 表示将主机的网络环境映射到容器中，容器的网络与主机相同

### 4. **停止与启动容器**

```shell
# 停止一个已经在运行的容器
docker  stop 容器名或容器id

# 启动一个已经停止的容器
docker  start 容器名或容器id

# kill掉一个已经在运行的容器
docker container kill 容器名或容器id
```

### 5. dockerfile

Docker可以通过阅读Docker的指令来自动构建映像 Dockerfile。A Dockerfile是一个文本文档，其中包含用户可以在命令行上调用以组装图像的所有命令。使用docker build 用户可以创建自动构建，该构建连续执行多个命令行指令。

### 6. 创建镜像

命令：docker commit  fid名  容器名:1.0 

```
docker commit 9c1 ubuntu_test:1.0
```

### 7. 打包镜像

命令：docker save -o 文件名  镜像名:版本名（TAG）

```python
summer@iZ2ze26ih51vo9ov0bpiidZ:~$ docker save -o ubuntu_demo.tar ubuntu_test:1.0
summer@iZ2ze26ih51vo9ov0bpiidZ:~$ ls
Blog_Django  DjangoTest  Git_Test  python_test  ubuntu_demo.tar
```

### 8. 加载本地镜像

当别人把镜像给我们之后，我们就需要从本地加载镜像。

命令：docker load -i 文件名

### 9. 查看日志文件
```
docker logs 镜像名/id前三位
```

## 六、docker容器操作

```
1.创建容器 : docker run -itd --name container_name container
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

### 容器的修改和保持

```
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

### 容器操作进阶

#### 端口映射:

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

#### 文件挂载:

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

#### 容器互联:

```docker
docker run -itd --name=container_name --link 要关联的容器名字:容器在被关联的容器中的别名 -v /宿主机/文件目录/文件名:/容器/目录/文件名 container_name
```

修改 mysql 密码:

```mysql
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123456';
```

## 七、安装ubuntu镜像

```python
docker search ubuntu   在仓库查找镜像

docker pull ubuntu   安装镜像

docker images      查看docker镜像

#查看所有启动的容器(查看所有容器加 -a)
docker ps -a

# 运行docker镜像
-name自定义容器名，-p指定端口映射，前者为虚拟机端口，后者为容器端口,成功后返回id

#制作一个名为ubuntu_demo名字的容器
docker run -dti --name ubuntu_demo -p 8088:8088 ubuntu   
    
#查看容器信息  根据id前三个也行
docker inspect id

#  /bin/bash：放在镜像名后的是命令，这里我们希望有个交互式 Shell
进入 容器 ubuntu
docker exec -it id /bin/bash

# 查看版本
cat /etc/issue

# 退出   
先按，ctrl+p
再按，ctrl+q
# 或者
exit   会退出整个系统

# 制作docker镜像   1.0是版本号   ubuntu_test 是镜像名字
docker commit  fae（id名） ubuntu_demo:1.0  
    
# 在当前路径下打包一个名为ubuntu_demo.tar镜像
docker save -o ubuntu_demo.tar ubuntu_demo:1.0
```

## 八、Dockerfile

### 1. 什么是 Dockerfile

Dockerfile 就是名为 Dockerfile 的文件,文件中包含一些 Linux 命令, Docker 通过读取文件中的命令来组建镜像

### 2. Dockerfile的组成

Dockerfile 一般分为四部分: 

```
基础镜像信息、维护者信息、镜像操作指令、容器启东市执行指令, "#" 为Dockerfile 中的注释;
```

### 3. 运行Dockerfile

```
运行Dockerfile:	docker build -t image_name:tag_name 

也可以通过 -f 参数来指定 Dockerfile 文件位置: docker build -f /path/Dockerfile
```

#### 命令详解:

**FORM**：指定基础镜像,必须为第一个命令

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

**RUN**:构建镜像时执行的命令:

```
格式:
	RUN <command>*exec执行*
格式:
	RUN ["executable","param1","param2"]
	
实例:
	RUM ["/bin/executable","param1","param2"]
	RUM yum install nginx
```

**ADD**:将本地文件添加到容器中,tar 类型文件会自动解压(网络压缩资源不会别解压),可以房屋网络资源,类似wget

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

**COPY**:功能类似 ADD, 但是 不会自动解压文件,也不能访问网络资源

**CMD**:构建容器后调用,也就是在容器中启动时才进行调用

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

**ENTRYPOINT**：配置容器,使其可执行化。配合CMD 可省去 "application",只使用参数

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

**LABEL**:用于为镜像添加元数据

```
格式:
	LABEL <key>=<value> <key>=<value> <key>=<value> ...
	
实例:
	LABEL version="1.0" description="这是一个nginx镜像"
	
注:
	使用LABEL指定元数据时,一条LABEL指定可以 指定 一 或 多条元数据,指定多条元数据时不同元数据之间通过空格分隔,推荐将所有的元数据 通过一条LABEL指令指定,以免生产过多的中间镜像
```

**ENV**: 设置环境变量

```
格式:
	ENV <key><value> #<key> 之后的所有内容均被视为其<value>的组成部分,因此,一次只能设置一个变量
	ENV <key><value>... #可以设置多个变量,每个变量为一个"<key>"=<value>的键值对,如果<key>中包含空格,可以使用\来进行转义,也可以通过""来进行标示;另外,反斜线也可以用于续行
	
实例:
	ENV myName Join Done
	ENV myDOG REx The Dog
	ENV myCat=fluffy
```

**EXPOSE**:指定外界交互的端口

```
格式:
	EXPOSE <port> [<port>...]
实例:
	EXPOSE 80 443
	EXPOSE 8080
注:
	EXPOSE 并不会让容器的端口访问到主机,要使其可访问,需要在 docker run 运行容器时通过 -p 来发不这些端口,或通过 -p 参数来发布 EXPOSE 导出所有的端口
```

**VOLUME**:用于指定持久化目录

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

**WORKDIR**:工作目录,类似 cd 命令

```
格式:
	WORKDIR /usr/local (这时工作目录为 /usr/local/)
	WORKDIR nginx (这时工作目录为 /usr/local/nginx)
	WORKDIR nginx (这是工作目录为 /usr/local/nginx/sbin)
注:
	通过WORKDIR 设置工作目录后,Dockerfile中其后的RUN、CMD、ENTRYPOINT、ADD、COPY等 命令都会在该目录下执行。在使用 dockerrun 运行容器时,可以通过 -w 参数覆盖构建时的工作目录
```

**USER**:指定运行容器时的用户名或者 UID，后续的RUN也会使用指定的用户，使用USER指定用户时,可以使用用户名、UID或 GID，或 两者的组合。当服务不需要管理员权限时，可以通过该命令指定运行用户。并且可以在之前创建所有的用户

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

**ARG**:用于指定传递给构建运行时的变量

```
格式:
	ARG <name>[=<default value]
实例:
	ARG site
	ARG build_user=www
```

**ONBUILD**:用于设置镜像触发器

```
格式:
	ONBUILD [INSTRUCTION]
实例:
	ONBUILD ADD . /app/src
	ONBUILD RUN /usr/local/bin/python-build --dir /app/src
	
注:
	当所构建的镜像被用做其它镜像的基础镜像,该镜像中的触发器将会被触发
```

## 九、总结

简言之，docker就是一个容器。如果把docker当作一艘船，则镜像就是船上的集装箱，每个镜像之间相互独立，互不影响。一个镜像可以产生多个实例，对实例进行操作之后，还可以把他变成镜像。与此同时每个镜像都可以打包，我们可以把打包的文件发送给任何人。

拉取容器：`docker pull images`

创建实例：`docker run -idt --name 实例名 -p 6666:6666 镜像名`

删除实例：`docker rm 实例名|实例id`

删除镜像：`docker image rm 镜像名：tag`

进入实例：`docker exec -it 实例名`

退出实例：`exit/ctrl+p..ctrl+q`

创建镜像：`docker commit 实例id 创建的容器名:tag `

打包镜像：`docker save -o 文件名  镜像名:版本名（TAG）`