# -*- coding: utf-8 -*-
# @Author  : summer
from sshtunnel import SSHTunnelForwarder
import pymysql


class JD:
    def __init__(self):
        # 初始化，建立ssh连接，然后进行pysql连接
        self.ssh = SSHTunnelForwarder(ssh_address_or_host=("101.200.195.98", 22),  # 云服务器地址IP和端口port
                                      ssh_username="summer",  # 云服务器登录账号admin
                                      ssh_password="summer",  # 云服务器登录密码password
                                      # 数据库服务地址ip,一般为localhost和端口port，一般为330
                                      remote_bind_address=('localhost', 3306)
                                      )
        self.ssh.start()
        self.coon = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                                    port=self.ssh.local_bind_port, user="summer",  # mysql的登录账号admin
                                    password="summer",  # mysql的登录密码pwd
                                    db="jing_dong",  # mysql中要访问的数据表
                                    charset='utf8')  # 表的字符集
        # 创建游标
        self.cur = self.coon.cursor()

    def __del__(self):
        # 关闭对象
        self.cur.close()
        self.coon.close()
        self.ssh.close()

    def execute_adu(self, sql, params):
        # 执行增删改操作
        count = self.cur.execute(sql, params)
        if count:
            print("操作完成\n")
        else:
            print("输入的值有误，请重新输入\n")

    def execute_sql(self, sql, params=None):
        # 执行sql语句
        # 如果select在开头，执行查找命令，不然的话执行增删改命令（有commit）
        if sql.startswith("select"):
            self.cur.execute(sql)
            one_data = self.cur.fetchone()
            while one_data:
                print(one_data)
                one_data = self.cur.fetchone()
        else:
            self.execute_adu(sql, params)

    def show_all_items(self):
        # 显示所有商品
        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_cates(self):
        # 显示所有商品分类
        sql = "select * from goods_cates;"
        self.execute_sql(sql)

    def show_brands(self):
        # 显示所有商品品牌分类
        sql = "select * from goods_brands;"
        self.execute_sql(sql)

    def find_by_val(self):
        # 按值查询，使用模糊查询，在params里面放入%%即可。
        find_name = input("请输入商品名称：")
        # 防止sql注入
        params = ["%", find_name, "%"]
        self.cur.execute(
            "select * from goods where name like %s %s %s",
            params)
        one_data = self.cur.fetchone()
        if not one_data:
            print("没有查到任何数据\n")
        else:
            while one_data:
                print(one_data)
                one_data = self.cur.fetchone()

    # 如果要是有多个参数，需要进行参数化
    # 那么params = [数值1, 数值2....]，此时sql语句中有多个%s即可

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
                # 显示所有商品
                self.show_all_items()
            elif num == "2":
                # 显示所有商品分类
                self.show_cates()
            elif num == "3":
                # 显示所有品牌分类
                self.show_brands()
            elif num == "4":
                self.find_by_val()
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

    def update_goods_item(self):
        # 修改商品
        del_name = input("请输入要修改的商品名称：")
        new_name = input("要改成的商品名称为：")
        # 防止sql注入
        params = [new_name, del_name]
        sql = "update goods set name=%s where name=%s"
        self.execute_sql(sql, params)

    def update_cates_item(self):
        # 修改商品分类
        del_name = input("请输入要修改的商品分类名称：")
        new_name = input("要改成的商品分类名称为：")
        # 防止sql注入
        params = [new_name, del_name]
        sql = "update goods_cates set name=%s where name=%s"
        self.execute_sql(sql, params)

    def update_brands_item(self):
        # 修改商品品牌分类
        del_name = input("请输入要修改的商品品牌分类名称：")
        new_name = input("要改成的商品品牌分类为：")
        # 防止sql注入
        params = [new_name, del_name]
        sql = "update goods_brands set name=%s where name=%s"
        self.execute_sql(sql, params)

    def do_update(self):
        # 执行修改的总操作
        while True:
            num = self.print_update_menu()
            if num == "1":
                self.update_goods_item()
            elif num == "2":
                self.update_cates_item()
            elif num == "3":
                self.update_brands_item()
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

    def del_goods_item(self):
        # 删除商品
        del_name = input("请输入要删除商品名称：")
        # 防止sql注入
        params = [del_name]
        sql = "delete from goods where name=%s"
        self.execute_sql(sql, params)

    def del_cates_item(self):
        # 删除商品分类
        del_name = input("请输入要删除商品分类名称：")
        # 防止sql注入
        params = [del_name]
        sql = "delete from goods_cates where name=%s"
        self.execute_sql(sql, params)

    def del_brands_item(self):
        # 删除商品品牌分类
        del_name = input("请输入要删除商品品牌分类名称：")
        # 防止sql注入
        params = [del_name]
        sql = "delete from goods_brands where name=%s"
        self.execute_sql(sql, params)

    def do_del(self):
        # 执行删除的总操作
        while True:
            num = self.print_del_menu()
            if num == "1":
                # 删除商品
                self.del_goods_item()
            elif num == "2":
                self.del_cates_item()
            elif num == "3":
                self.del_brands_item()
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

    def add_goods_item(self):
        # 添加商品
        add_name = input("添加的商品名称为：")
        cates_id = int(input("添加的商品品牌id为："))
        brands_id = int(input("添加的商品品牌分类id为："))
        price = input("添加的商品价格为：")
        params = [add_name, cates_id, brands_id, price]
        sql = "insert into goods(name,cate_id,brand_id,price) values (%s,%s,%s,%s)"
        self.execute_sql(sql, params)

    def add_cates_item(self):
        # 添加商品分类
        add_name = input("要添加的商品分类名：")
        # 防止sql注入
        params = [add_name]
        sql = "insert into goods_cates(name) values(%s)"
        self.execute_sql(sql, params)

    def add_brands_item(self):
        # 添加商品品牌分类
        add_name = input("要添加的商品品牌分类名：")
        # 防止sql注入
        params = [add_name]
        sql = "insert into goods_brands(name) values(%s)"
        self.execute_sql(sql, params)

    def do_add(self):
        # 打印添加的列表
        while True:
            num = self.print_add_menu()
            if num == "1":
                self.add_goods_item()
            elif num == "2":
                self.add_cates_item()
            elif num == "3":
                self.add_brands_item()
            elif num == "0":
                self.coon.commit()
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
                self.coon.commit()
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
