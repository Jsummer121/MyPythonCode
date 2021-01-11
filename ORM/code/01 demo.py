# -*- coding: utf-8 -*-
# @Author  : summer

# class User(父类省略):
#     uid = ('uid', "int unsigned")
#     name = ('username', "varchar(30)")
#     email = ('email', "varchar(30)")
#     password = ('password', "varchar(30)")
#     ...省略...


u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
# 对应如下sql语句
# insert into User (username,email,password,uid)
# values ('Michael','test@orm.org','my-pwd',12345)
