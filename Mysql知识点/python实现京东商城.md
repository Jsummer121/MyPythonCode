# 用python实现简单版的京东商城

## 一、数据库准备

### 1. 商品表

```sql
create table goods(
    id int unsigned primary key auto_increment not null,
    name varchar(150) not null,
    cate_id int unsigned not null,
    brand_id int unsigned not null,
    price decimal(10,3) not null default 0,
    is_show bit not null default 1,
    is_saleoff bit not null default 0
);
```

### 2. 商品分类表

```sql
create table if not exists goods_cates(
    id int unsigned primary key auto_increment,
    name varchar(40) not null
);
```

### 3. 商品品牌分类表

```sql
create table goods_brands (
    id int unsigned primary key auto_increment,
    name varchar(40) not null
);
```

## 二、相应的库准备

应为我的数据库放在云服务器上，因此在准备库的时候需要多加上一个`sshtunnel`库。(具体原因在上一章)

-   pymysql安装命令：`pip install pymysql`
-   sshtunnel安装命令：`pip install sshtunnel`

## 三、基本骨架

整个代码我们可以利用一个JD类来实现，利用他的`__init__`方法来构建ssh的连接和mysql的连接，利用`__del__`方法来释放关闭连接。然后写一个run方法，在此基础上将增删改查四个步骤写入，在将这四个步骤分别细分成每个表即可。话不多说，上代码：

```python
# -*- coding: utf-8 -*-
# @Author  : summer
from sshtunnel import SSHTunnelForwarder
import pymysql


class JD:
    def __init__(self):
        # 初始化，建立ssh连接，然后进行pysql连接
        self.ssh = SSHTunnelForwarder(ssh_address_or_host=(IP, 22),  # 云服务器地址IP和端口port
                                      ssh_username=admin,  # 云服务器登录账号admin
                                      ssh_password=pwd,  # 云服务器登录密码password
                                      # 数据库服务地址ip,一般为localhost和端口port，一般为330
                                      remote_bind_address=('localhost', 3306)
                                      )
        self.ssh.start()
        self.coon = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                                    port=self.ssh.local_bind_port, 
                                    user=admin,  # mysql的登录账号admin
                                    password=pwd,  # mysql的登录密码pwd
                                    db=db,  # mysql中要访问的数据表
                                    charset='utf8')  # 表的字符集
        # 创建游标
        self.cur = self.coon.cursor()

    def __del__(self):
        # 关闭对象
        self.cur.close()
        self.coon.close()
        self.ssh.close()

    def execute_sql(self, sql):
        # 执行sql语句
        self.cur.execute(sql)
        one_data = self.cur.fetchone()
        while one_data:
            print(one_data)
            one_data = self.cur.fetchone()

    @staticmethod
    def print_find_menu():
        # 打印查找的列表
        print("-----京东商城-查询操作-----")
        print("1:所有的商品")
        print("2:所有的商品分类")
        print("3:所有的商品品牌分类")
        print("4:按值查询商品")
        print("0:退出")
        return input("请输入功能对应的序号：")

    def do_find(self):
        # 执行查找总操作
        while True:
            num = self.print_find_menu()
            if num == "1":
                pass
            elif num == "2":
                pass
            elif num == "3":
                pass
            elif num == "4":
                pass
            elif num == "0":
                print("")
                break
            else:
                print("您输入的序号有误，请重新输入\n")

    @staticmethod
    def print_update_menu():
        # 打印修改的列表
        print("-----京东商城-修改操作-----")
        print("1:修改商品")
        print("2:修改商品分类")
        print("3:修改商品品牌分类")
        print("0:退出")
        return input("请输入功能对应的序号：")

    def do_update(self):
        # 执行修改的总操作
        while True:
            num = self.print_update_menu()
            if num == "1":
                pass
            elif num == "2":
                pass
            elif num == "3":
                pass
            elif num == "0":
                self.coon.commit()
                print("")
                break
            else:
                print("您输入的序号有误，请重新输入\n")

    @staticmethod
    def print_del_menu():
        # 打印删除的列表
        print("-----京东商城-删除操作-----")
        print("1:删除商品")
        print("2:删除商品分类")
        print("3:删除商品品牌分类")
        print("0:退出")
        return input("请输入功能对应的序号：")

    def do_del(self):
        # 执行删除的总操作
        while True:
            num = self.print_del_menu()
            if num == "1":
                # 删除商品
                pass
            elif num == "2":
                pass
            elif num == "3":
                pass
            elif num == "0":
                self.coon.commit()
                print("")
                break
            else:
                print("您输入的序号有误，请重新输入\n")

    @staticmethod
    def print_add_menu():
        # 打印添加的列表
        print("-----京东商城-增加操作-----")
        print("1:增加商品")
        print("2:增加商品分类")
        print("3:增加商品品牌分类")
        print("0:退出")
        return input("请输入功能对应的序号：")

    def do_add(self):
        # 打印添加的列表
        while True:
            num = self.print_add_menu()
            if num == "1":
                pass
            elif num == "2":
                pass
            elif num == "3":
                pass
            elif num == "0":
                pass
                print("")
                break
            else:
                print("您输入的序号有误，请重新输入\n")

    @staticmethod
    def pring_menu():
        # 打印总的列表
        print("-----京东商城-----")
        print("1:查询操作")
        print("2:修改操作")
        print("3:删除操作")
        print("4:添加操作")
        print("0:退出")
        return input("请输入功能对应的序号：")

    def run(self):
        while True:
            num = self.pring_menu()
            if num == "1":
                self.do_find()
            elif num == "2":
                self.do_update()
            elif num == "3":
                self.do_del()
            elif num == "4":
                self.do_add()
            elif num == "0":
                self.coon.commit() # 这里最好也添加一个
                print("")
                break
            else:
                print("您输入的序号有误，请重新输入\n")


def main():
    jd = JD()
    jd.run()
    del jd


if __name__ == '__main__':
    main()

```

## 四、“添油加醋”

有了这个骨架，我们就可以添加相关的操作即可，这里需要注意几点：

-   查找操作不需要提交，因此可以单独写一个执行代码
-   增删改操作在整个退出以后，需要执行一次commit操作
-   再写增删改的sql语句时，需要注意sql注入，因此可以使用列表等元素进行相应的防护

## 五、总代码

[代码传送门](https://github.com/Jsummer121/MyPythonCode/blob/master/Mysql%E7%9F%A5%E8%AF%86%E7%82%B9/code/jing_dong_shpping.py)

