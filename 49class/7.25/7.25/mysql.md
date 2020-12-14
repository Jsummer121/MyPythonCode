#### MySQL

```
1.进入mysql
mysql -uroot -pqwe123
mysql -u root -p       # 推荐，安全性
mysql -u root -pqwe123

2.不严格区分大小写
show databases;
SHOW SATABASES;

3.结束;
必须要加；否则命令不执行

数据类型和逗号请听下回分解

4.退出
quit
exit
```

#### 库级操作语句

```
1.显示所有库：默认四个库不要动,动了可能就登不上了
show databases;
2.创建库：
create database Python_37;
重复创建会报错,修正如下
create database if not exists Python_37;
3.删除库
drop database Python_37;
重复删除会报错，如果不知道数据库是否存在
drop database if exists Python_37;
4.进入数据库
use Python_37;
```

#### 表级操作语句

```
1.显示所有的表：
show tables;
2.创建表：
create table student (name varchar(20),age int,sex char(20);
数据库和python不同，回车和空格要求没有那么严格，所以，当你创建多个字段时，可以回车每行输入一个字段。
重复创建会报错,修正如下
create table if not exists student (name varchar(20),age int, sex char(20);
3.显示创建表的信息
show create table student;
4.删除表：
drop table student
```

#### 表中数据的操作(增删改查)

```
1.创建一个表
create table student(
name varchar(20),
age int);

2.插入字段(查看表：select * from student;)
a.全字段插入：有几个字段就必须输入几个字段，否则报错
insert into student values("飞飞"，18);
b.指定字段插入
insert into student(name) values("哈哈");
c.多行插入
insert into student values("你好"，5)，("我好", 6)；

3.查询数据
a.全字段查询
select * from student;
b.指定字段查询
select name from student;
select name,age from student;
c.带条件的查询
select name，age from student where age = 18;
select name，age from student where name = "飞飞";

4.修改数据
a.修改所有数据：
update student set age=24;
b.修改多个：
update student set age=24,name="嘻嘻" where name="哈哈";
c.修改满足条件的数据：
update student set age=24 where name = "飞";

# 注意：一定要写where条件，不然会修改表中全部数据

5.删除数据
a.条件删除
delete from student where name="嘻嘻"；
b.删除全部数据
delete from student;
# 注意：一定要写where条件，不然会删除表中全部数据
# 删除都是操作一行，如果只是想要修改某个字段值，可以使用update
update student set age=NULL where name = "飞"；
```

#### 修改表结构(alter)

```
1.修改表名：
alter table new_table rename to old_table;
show tables;

2.修改字段名：
desc old_table;
alter table old_table change id stu_id int;
show tables;

3.修改字段类型：
alter table old_table modify stu_id tinyint;
desc old_table;

4.添加字段：
alter table old_table add age tinyint;
desc old_table;

5.删除字段：
alter table old_table drop age;
desc old_table;
```

