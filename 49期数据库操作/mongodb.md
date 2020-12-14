# MongoDB

```
基于分布式文件存储的开源数据库系统

为web应用提供可扩展的高性能数据存储解决方案

将数据存储为一个文档，文档类似与json格式
```

##### 1.进入 -->mongo

退出 -->exit

##### 2.库级操作语句：与mysql大同小异，创建库，显示库，删除库

```
1.显示所有库
show dbs    # 默认库不要动（admin、config、local）

2.切换/创建数据：
use py_49    # 有就切换，无则创建
show dbs    # 如果创建了数据库后没有添加任何东西，此时show是看不到刚新建的数据库的

3.查看所在库
use py_49
db  # 可以查看当前所在的数据库

4.删除库
db.dropDatabase()   # 注意区分大小写，删除当前库

# 提到再讲
db  # 此时db还是会显示当前库库名，但是实际如果里面有数据的话，是已经被清空了的。
```

##### 3.集合操作语句

```
1.创建集合
db.createCollection("student")

2.显示当前数据库的集合
show collections 
# 如果显示出来有system.indexes,是MongoDB默认就有的，不用管它

# 注意，一般情况下，我们不需要额外的去创建集合，这点和redis有点相似，只需要直接写入，它即会自动创建集合

3.删除集合：
db.student.drop()
```

##### 4.文档操作（增删改查）

```
1.增加(添加时，json比较随意，想怎么加就怎么加。没有固定格式)
db.student.insert({'_id':1,name:'summer',age:15})
当你不指定id时，系统会自己帮你加上一个_id

db.student.insert([{'_id':2,name:'zwt',age:15},{'_id':3,name:'green',age:15}])
添加多条时，要用[]把整个包起来。

db.student.insert({'_id':4,name:'blue',age:15,sex:'F',address:'China'})

2.查询
db.student.find()
#条件查询
db.student.find({age:18}) .pretty()使文件输出时有一个格式

3.噩梦模式
$ne：不等于
$gt：大于
$lt小于
$gte大于等于
$lte小于等于
###操作符需要加上引号

db.student.find({age:{'$gte':18}})

db.student.find({$and:[{age:15},{name:'green'}]})

db.student.find({$or:[{age:15},{name:'green'}]})

db.student.find({$or:[{$and:[{sex:"F"},{age:{"$lt":18}}]},{$and:[{sex:"M"},{age:{"$gt":18}}]}]}) 

4.修改
db.student.update({age:15},{age:18})此时，数据被重写，修改时一定要全部改。

指定修改,从上往下改
db.student.uodate({age:18},{$set:{age:15}})

修改全部
db.student.uodate({age:18},{$set:{age:15}},{multi:true})

5.删除
db.student.remove({age:20})删除全部
db.student.remove({age:20},{justOne:true})删除一个
db.student.remove({})

```



##### 5.python操作MongoDB（增删改查）

pip install pymongo

建立连接

```
client = pymongo.MongoClient()
db = client['py_49']
col = db['student']
```

```
1.添加文档
insert_one({'name':'summer'})
insert_many()

2.查找文档
find_one()
find()得到由标地址，可以循环迭代

3.修改文档
updata_one({'name':'summer'},{'$set':{'age':88}})
updata_many('name':'summer'},{'$set':{'age':88}})

4.删除文档
delete_one({'name':'summer'})
delets_many({'age':18})
delete_many({'$or':[{'name':'summer'},{'name':'zwt'},{'name':'green'}]})
```

