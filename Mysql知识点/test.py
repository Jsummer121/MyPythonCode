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
                                    port=self.ssh.local_bind_port, user=admin,  # mysql的登录账号admin
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
