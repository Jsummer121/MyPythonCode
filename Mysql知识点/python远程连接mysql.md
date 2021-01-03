# Python远程连接阿里云的mysql

这个bug改了一个下午，真的撕心裂肺的搞，搞了半天终于欧克了。

先来看一下原先的核心代码：

```python
conn = connect(
    host='此处为我的云服务器ip地址',
    port=3306,
    user=admin,
    password=pwd,
    database='jing_dong',
    charset='utf8')
```

这是报错信息：

```python
pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on '我的云服务器ip地址' (timed out)")
```

首先还是看了无数的文章，基本上都是根据地址是localhost来改，先是判断mysql服务器是否开启，然后查看防火墙是否关闭，最后的话查看自己的每个值是否一一对应。首先我的navicate是可以登录的，那就说明mysql没问题问题就出在python身上，我有将pycharm的自带database打开，连接之后也是没问题的。最后将注意点放在了ssh上。

最终发现，如果需要访问远程服务器的Mysql数据库，但是该Mysql数据库为了安全起见，安全措施设置为只允许本地连接(也就是你需要登录到该台服务器才能使用)，其他远程连接是不可以直接访问，并且相应的端口也做了修改，那么就需要基于ssh来连接该数据库。这种方式连接数据库与Navicat里面界面化基于ssh连接一样。

以下是我的代码：

```python
from sshtunnel import SSHTunnelForwarder
import pymysql

# 通过SSH连接云服务器
server = SSHTunnelForwarder(
	ssh_address_or_host=(IP, 22),  # 云服务器地址IP和端口port
	ssh_username=admin,  # 云服务器登录账号admin
	ssh_password=pwd,  # 云服务器登录密码password
	remote_bind_address=('localhost', 3306)  # 数据库服务地址ip,一般为localhost和端口port，一般为330
)

# 云服务器开启
server.start()
# 云服务器上mysql数据库连接
con = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                      port=server.local_bind_port,
                      user=admin,  # mysql的登录账号admin
                      password=pwd,  # mysql的登录密码pwd
                      db="jing_dong",  # mysql中要访问的数据表
                      charset='utf8')  # 表的字符集
# 创建游标
cur = con.cursor()
# 执行sql语句
cur.execute("""SELECT * from goods limit 10""")
# 读取数据
data = cur.fetchall()
# 打印数据
for item in data:
	print(item)
# 游标、连接关闭
cur.close()
con.close()
# 云服务器关闭
server.close()

```

至此，整个也就代码也就可以正确的跑起来了。