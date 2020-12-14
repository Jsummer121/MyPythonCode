#### redis作业



##### 1.作业讲解

```
1.string:
# 增
set a 1
# 查
get a
# 改
append a 66
set a 45
# 删
del a

2.list
# 增
rpush list_a wo jiu shi wo bu yi yang de yan huo
lpush list_a ni shi shei
# 查
lrange list_a 0 20
lindex list_a 2
# 改
lset list_a 2 wo
# 删
rpop list_a # 右边开始删除，每次删除一个
lpop list_a # 左边开始删除，每次删除一个
lrem list_a 3 haha # 没有根据index删除元素的命令,如果想要删除指定index的值,除了指定索引还要指定值

3.hash
# 增
hset hash_a a 1
hmset hash_a c 3 d 4 # 插入多条数据
# 查
hget hash_a a   # 查看指定域对应的值
hvals hash_a    # 查看所有的value
hkeys hash_a    # 查看所有的field
hgetall hash_a  # 查看全部的域和值
# 改
hset hash_a a 66    # hset域有则改，无则增
# 删
hdel hash_a a

4.set
# 增
sadd set_a hello world ‘hello world’
# 查
smembers set_a  # 无序
# 删
spop set_a # 无序，随机删除
srem set_a hello    # 指定删除一个
srem set_a hello world # 可同时删除多个

5.zset
# 增
zadd zset_a 1 hello
# 查
zrange zset_a 0 10
zrangebyscore zset_a 1 2 # 通过分数范围查看
zscore zset_a hello     # 查看数据的分数
# 删除
zrem zset_a 4 # 删除指定单个值（4为值不是分数）
zrem zset_a 10 20 # 删除指定多个值，空格隔开

zremrangebyrank zset_a 3 6 # 通过索引删除多个数据（索引从0开始记，删除了索引为3/4/5/6的数）
zremrangebyscore zset_a 1 2 # 通过分数删除多个数据

```

