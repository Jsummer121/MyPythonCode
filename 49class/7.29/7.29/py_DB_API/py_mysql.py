#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/29 20:29

# 一.安装模块
# 二.使用模块
# 1.导入模块
import pymysql

# 2.建立连接
# 2.1 第一种连接方式
# pymysql.connect(user="root",
#                 password="qwe123",
#                 db='py_49',
#                 charset='utf8')

# 2.1 第二种连接方式
db_config = {
    'user': "root",
    'password': "qwe123",
    'db': "py_49",
    'charset': "utf8",
}
con = pymysql.connect(**db_config)    # 解包

# 3.创建游标
cur = con.cursor()
#
# # 4.使用sql语句execute
# res = cur.execute("select * from student")
# # # print(res)  # 数据的数据量
# #
# # # 如果想要获取结果fetchone，fetchall
# print(cur.fetchone())  # 获取一行
# print(cur.fetchone())  # 获取一行
# print(cur.fetchone())  # 获取一行
# # print(cur.fetchall())   # 获取全部
# # print(cur.fetchmany(3))  # 获取你指定条数的数据
# cur.execute('insert into student values(10, "Misa", 19, 3)')
#
# con.commit()
# # 5.关闭游标
# cur.close()
#
# # 6.关闭连接
# con.close()

# 3.利用上下文管理去实现自动关闭
# with con.cursor() as cur:
#     cur.execute('select *  from student')
#     print(cur.fetchone())
# with con.cursor() as cur:
#     cur.execute('insert into student values(11, "Misa", 20, 3)')
#     cur.execute('insert into student values(12, "Misa", 22, 3)')
# con.commit()

# 获取值时，为了预防数据量过大，导致内存爆炸，一般不会直接使用fetchall去获取数据，处理方法如下：
# with con.cursor() as cur:
#     cur.execute("select *  from student")
#     one_data = cur.fetchone()
#     while one_data:
#         print(one_data)
#         one_data = cur.fetchone()

