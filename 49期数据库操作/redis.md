# redis

### nosql：非关系型数据库

```
是对不同于传统的关系型数据库的数据库管理系统的统称
特点：
1. 不支持SQL语法
2. 读写性能高
3. 灵活的数据模型
```

### redis：内存高速缓存数据库

```
redis简称Remote Dictionary Server(远程数据服务)，使用c语言编写，并以内存作为数据存储介质，所以读写数据的效率极高。
特性：
Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。
Redis不仅仅支持简单的key-value类型的数据，同时还把value分为list，set，zset，hash等数据结构存储。
因为Redis交换数据快，所以在服务器中常用来存储一些需要频繁调取的数据，提高效率。

```

### Redis数据结构

```
redis是key-value的数据结构，每条数据都是一个键值对

键的类型是字符串

注意：键不能重复

值得类型：1.str，2.Hash，3.list，4.set,5.zest(有序结合)

```

![图片1](E:\python-summer-1\49期数据库操作\assets\redis数据类型.png)

### Redis基本使用

```
连接redis：redis-cli
退出：exit
操作服务端：service redis start/stop/restart
切换数据库：select n
注：数据库没有名称，默认有16个，通过0-15来标识，连接redis默认选择第一个数据库。
注：一个键只能使用一种类型
```

### string类型

```
set key value->set a 1
get key->get a       
append key value->append a 88
注：直接加载上个a的后面类似于拼接字符串。也可以直接创建一个新的key。
del key-> del a
注：key和字符串类型的value最多的数据长度是512M

```

### 全局key的操作

```
查看所有的key：key *
删除键值对：del key
exists key 查看key是否存在

改名：rename key new_key

设置过期时间： expire key seconds
ttl 查看时间 persist key删除过期时间

ttl查时间：
有过期时间返回过期时间。
没有过期时间返回-1。
如果查找一个没有的key，返回-2。
```

### list类型

```
特点：是一个字符串列表，可以从后面，前面删除添加字符串。如果添加时，key不存在会直接新建一个键。（队列操作）

添加数据：
rpush(lpush) key value [value···]:rpush a wo jiu shi wo

查看数据：
lrange key start stop(lindex key index-->查看某个数据)
lindex a 8（查看第九个数据）

修改数据：
lset key index value-->lset a 8 no

删除数据：
rpop(lpop) key-->rpop a（就删一个数据）
删除中间的一个值
lrem key count(删除一共几个) value-->lrem a 3 yang
```

### Hash类型

```
是一个键值对集合。是string类型和field和value的映射表。

插入：
hset key field value -->hset a k1 v1
hmset a k2 v2 k3 v3(加入多个值)

查看：
hget value field-->hget a k1
hgetall value field(查看全部值)
hvals a
hkeys a

修改：
hset a k1 66

```

### set类型

```
无需的字符集合，元素唯一，不重复

添加数据：
sadd key member[member..]-->sadd a 'hello world' Tz

查看数据：
smembers key-->smember a

删除数据：
spop a
指定删：
srem a helo
```

### Sorted Set类型

```
每个成员有一个分数与之关联，成员唯一，但分数确可以重复。

添加：
zass a 10 hello
zadd a 8 12
zadd a 1.5 2
注：此时 12在hello上面
注：zadd a 1.5 1 此时通过value的ASCII码来排列

查看：
zrange a 1 10
zrangebyscore a 1 2
zscore a hello

删除：
zrem key member-->zrem a 2
zremrangebyrank a 2 3

```

