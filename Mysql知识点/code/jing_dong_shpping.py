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

    def execute_sql(self, sql):
        # 执行sql语句
        # 如果select在开头，执行查找命令，不然的话执行增删改命令（有commit）
        if sql.startswith("select"):
            self.cur.execute(sql)
            one_data = self.cur.fetchone()
            while one_data:
                print(one_data)
                one_data = self.cur.fetchone()
        else:
            pass

    def show_all_items(self):
        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_cates(self):
        sql = "select * from goods_cates;"
        self.execute_sql(sql)

    def show_brands(self):
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
            print("没有查到任何数据")
        else:
            while one_data:
                print(one_data)
                one_data = self.cur.fetchone()

    # 如果要是有多个参数，需要进行参数化
    # 那么params = [数值1, 数值2....]，此时sql语句中有多个%s即可

    @staticmethod
    def pring_menu():
        print("-----京东商城-----")
        print("1:所有商品")
        print("2:所有的商品分类")
        print("3:所有的商品品牌分类")
        print("4:按值查询商品")
        return input("请输入功能对应的序号：")

    def run(self):
        while True:
            num = self.pring_menu()
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
            else:
                print("您输入的序号有误，请重新输入")


def main():
    jd = JD()
    jd.run()
    del jd


if __name__ == '__main__':
    main()
