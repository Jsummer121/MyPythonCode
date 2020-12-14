

#### 01-MySQL（一）

##### 一、数据库简介

```
数据库：计算机系统中一种提供数据存储和检索的一种软件
```

```
数据库分类：
关系型数据库（sql）：建立在关系模型上的数据库。
是由多张能互相连接的二维行列表格组成的数据库。
SQL（结构化查询语言）专为数据库而建立的操作命令集。Structured Query Language 结构化查询语言
语法通用

非关系型数据库（nosql）：Not Only SQL。
语法基本都不一样
redis，mongodb
```

##### 二、MySQL基本结构

```
MySQL是数据库管理软件。
```

##### 三、MySQL库级表级操作

```
1.不严格区分大小写
2.必须要加；结束
-A可以直接进入表操作 不用多余的use 49_py.
# 库级操作
show databases;
create database py_49;
drop database py_49;
use py_49;

# 表级
show tables;展示库下的所有表
show create table test;展示某表的值得种类
desc test可以查看所有的字段值
create table test(name varchar(20),age int,sex char(20));#test为创建的表名称后面为所需的字段名和字段值。注年龄可以用tinyint性别用枚举enum（'F','M'）
drop table test;
```

##### 四、MySQL表中数据的操作(增删改查)

```
查
select * from student;#查全部
selece * from student where sex="M";#查where后面的

增
insert into student value(2,"zwt",20,"F",49);
insert into student values(2,"zwt",20,"F",49)，(3,"zwt",20,"F",49);#增加多条数据
insert into student(name) value("zwt");字段值创建，没写的都为null

改
update student set sex="M" where sex="F";

删
delete from student where id=3;
```

##### 五、MySQL数据类型（了解）

```
数值型、字符类型、时间日期类型
```

##### 六、查询

###### 6.1、普通查询

```
select * from student where id >3;

select * from student where id <>3;#不等于

select * from student where sex='M' and class=2;

select * from student where sex='F' or class=2;

若果三个一起 not>and>or
```

###### 6.2、更多

```
#排序
select * from student order by id [desc(加上这个表示逆序)];根据id来排正序

#限制
select * from student limit 3;#显示最前面的三个

select * from student limit 5,3;显示从第五条开始的三条

#去重（python里用set）集合
select distinct * from student;
```

###### 6.3、模糊查询

```python
seclet * from student where name like 'l%'#查询以l开头的多个字符

seclet * from student where name like 'l_'#就拿l后面只有一个字符的，几个下划线代表几个字符。

方法很多 模糊查询！
select * from student where name like '_i%';
看自己的想象力！
```

###### 6.4、聚合筛选

```
select count(age) from student;#统计age字段里面有值得字段

select avg(age) from student;#求age字段平均值

select sum(age) from student;#求和

select avg(age)，sum(age) from student;#求和和求平均值

select group_concat(age) from student;#列出字段全部值

#分组查询
select class from student group by class;#分组查询，查询你的班级值class必须为字段名

#分组聚合混合使用
select class，group_concat(name) from student group by class;#统计class一样的人并列出名字，两个class的地方必须一样
select age，count(name) from student group by age;

#聚合筛选
#1
select class，group_concat(name) from student group by class having class<=2;#having对条件进行筛选和where差不多，只是先后顺序不一样

#2
select age，count(name) from student where id<=5 group by age;
select class，group_concat(name) as gg from student group by class;#把group_concat(name)的名字变为gg

顺序
where>聚合和别名>having
```

###### 6.5、子查询

```
select * from student where age > (select avg(age) from student);
```

###### 6.6、连接查询

```python
#无条件类连接
select * from student join detail;#把detail表上的数据加入到student表，按照detail表循环组合直到student循环完为止

#有条件类连接
select * from student inner join detail on student.id=detail.id;

select student.id,name,age,phone from student join detail on student.id=detail.id;#此时 join和inner join一样的，若果右边有左没有的，此时不显示，只看from前面的条件。

#外连接（左右连接）
select student.id,name,age,phone from student left join detail on student.id=detail.id;#以左表为基准，如果左表有右表没有的，其他值为空。

select student.id,name,age,phone from student right join detail on student.id=detail.id;#以右边的表为基础，复制右边对的全部到左边，多余的值为null
```

##### 七、表结构修改

```python
1.修改表名
alter table student rename to student1;

2.修改字段名
#data_type(数据类型)
alter table student change id s_id int;

3.修改字段类型
alter table student modify s_id tinyint;

4.添加字段
alter table student add age tinyint;

5.删除字段
alter table student drop age;
```

##### 八、约束条件

```python
1.默认值
#creat table tb(id int default 0)
这时的null非空会直接为yes
#alter table tb add name varchar(20) default 'no';
#如果想全字段插入的时候，必须用default来进行填写。insert into tb value(default,default,17);

2.非空约束
#creat table tb(id int not null,name varchar(20));
#alter table tb modify id int not null default 0;#非空和默认值同时使用

3.唯一约束
#creat table tb(id int unique key ,name varchar(20));#id不能重复
#creat table tb(id int primary key)#一个表只能设置一个主键,并且null自动为no.唯一不为空

4.自增长
#creat table tb(id int primary key auto _increment)#自增长必须和主键自增长
#insert into tb value(default（null）,'xx')#可以用default或者null来自动填充，并且自增上是从上次输入后面自增长。

5.外键约束（联系两张表，来保持数据一致性）把a绑定到b！必须先删a的值，b才可以删
#creat table a(id int primary,name varchar(20));
#creat table b(id int primary key,phonenumber int,foreign key(id) references a(id));把b的id值与a的id值相连接。

#只有a表中有，b表中才能创建。就是把a表绑定到b表。

#如果把a表中的id删除一个会报错，因为从表里面已经存在，你只能先删从表的那个数据，在删a表的。
```

##### 九、表关系

##### 9.1、一对一：用外键的方式，把两个表的主键关联

```
#建立详细学生表：
create table student_details(
    id int primary key,
    sex varchar(20) not null,
    age  int,
    address varchar(20) comment '家庭住址',
    parents varchar(20),
    home_num varchar(20),
    foreign key (id) references student(s_id)
);
```

##### 9.2、一对多

```
##创建学院表
create table department( 
   id int primary key auto_increment,      # 学院id
   name varchar(20) not null    	        # 学院名
);
##创建学生表（把学生绑定到学院，因此外键在学生表）
create table student(
   id int primary key auto_increment,      # 学生id
   name varchar(20) not null,              # 学生名字
   dept_id int not null,		            #  所属学院 id
   foreign key(dept_id) references department(id)
   #学生绑定学院
);
```

##### 9.3、多对多，需要中间架桥，通过中间一个表连接两个多对多表。

```
#建立课程表：
create table cours(
    cours_id int primary key auto_increment,
    cours_name varchar(20) not null 
);
# 选课表  (中间表)
create table sel(
    s_id int,       	 
    #用来记录学生id
    cours_id int,  	 
    #用来记录 课程id
    primary key(s_id,cours_id),             # 联合主键 
    foreign key(s_id) references student(s_id),      
    # 关联学生id
    foreign key(cours_id) references cours(cours_id)  
    # 关联课程id
);
注：创建中间表时，当选用select当做表名是必须是`select`这样才可以创建，不然select是关键字，会报错。
```

#### 十、查询

```
select * from department join student on department.d_id = student.d_id;

select * from student join sel join course on student.s_id and course.c_id and course.c_id=sel.c_id;
#改用
select student.s_name,course.c_name from student join sel join course on student.s_id=sel.s_id and course.c_id=sel.c_id;
```

#### 十一、索引

也是一张表

create index 索引名 on 表名（字段名称(长度)）

#### 十二、事务

当使用python时，进行插入操作，必须提交，查找不需要提交。

```
开始：begin;
提交：commit;

回滚：rollback；#回滚到begin之前
```

