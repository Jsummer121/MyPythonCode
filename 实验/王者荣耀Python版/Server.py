# -*- coding: utf-8 -*-
# @Auther:Summer
import socket
import time
from multiprocessing import Process
from multiprocessing import Queue

import Hero


class WangZheServer:
    step: int = 0  # 当前步骤
    data = ""  # 传输数据
    host = ""  # 本地ip与端口
    dest = ""  # 远程ip与端口
    dest_cli = ""  # 匹配的远程socket
    hero = ""  # 自己的英雄
    dest_hero_blod = 0  # 敌方血量

    def __init__(self):
        # 创建套接字
        self.WangZhe_Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定相关端口
        self.WangZhe_Server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 绑定端口
        self.WangZhe_Server.bind(("", 8888))

        # 该主动为被动
        self.WangZhe_Server.listen(128)

    def runferver(self):
        try:
            q = Queue()
            # 等待客户端连接accept
            while True:
                # 接受相应
                wz_client, clint_addr = self.WangZhe_Server.accept()
                # clint_addr后期放入队列，进行人员匹配（ip,port）
                self.host = (clint_addr[0], clint_addr[1])  # 获取本地的ip和port
                print(self.host)  # ('127.0.0.1', 58309)
                # 注册多进程，

                p = Process(target=self.recv, args=(wz_client, q))
                p.start()
                wz_client.close()
        except:
            # 关闭套接字
            self.WangZhe_Server.close()

    # 主体
    def recv(self, client_socket, q):
        """
        该部分为整个小游戏的核心部分，包含如下步骤
        1. 登录 step == 0
        2. 模式选择 step == 1
        3. 人员匹配（管道） step == 2
        4. 英雄选择 step == 3
        5. 开始对战 step == 3
        6. 展示结果 step == 4 -> step == 0

        收发数据模式step:data
        :param q:
        :param client_socket:
        :return:
        """

        while True:
            if self.step == 0:
                """登录操作"""
                self.login(client_socket)
            elif self.step == 1:
                """模式选择"""
                self.choosepattern(client_socket)
            elif self.step == 2:
                """人员匹配"""
                self.dest_cli = self.checkplayer(client_socket, q)
            elif self.step == 3:
                """英雄选择"""
                self.choosehero(client_socket)
            elif self.step == 4:
                """对战模式"""
                self.fight(client_socket)
            elif self.step == 5:
                # 重新回到模式选择
                self.show(client_socket)
            else:
                # 如果步骤不正确，说明前台传入的数值有误，就必须让用户重新登录
                print("退出成功")
                client_socket.close()
                break

    def get_step_data(self, data, client_socket):
        try:
            self.step = int(data.split(":")[0])  # 获取step
            self.data = data.split(":")[1]
        except:
            self.step = 500
            # 如果前台输入的信息不正确，则返回step为500，表示服务器内部错误
            client_socket.send("{}:{}".format(self.step, self.data).encode("gbk"))

    def login(self, client_socket):
        # 往客户端发送当前的step。客户端更具step进行相应的操作：
        client_socket.send("{}:{}".format(self.step, self.data).encode("gbk"))
        self.get_step_data(client_socket.recv(1024).decode('gbk'), client_socket)
        username = self.data.split("-")[1]
        password = self.data.split("-")[3]
        # print(username, password)
        # 根据数据库判断用户名和密码是否正确
        if username == "summer" and password == "summer":
            print("{}登陆成功".format(self.host[0]))
            self.step += 1  # 进入下一步，模式选择
            client_socket.send("{}:{}".format(self.step, self.data).encode("gbk"))

    def choosepattern(self, client_socket):
        # 模式选择模块
        self.data = "请选择模式：\n1：真人对战\n2：人机对战\n其他：退出\n"
        client_socket.send("{}:{}".format(self.step, self.data).encode("gbk"))
        # 获取前台发送的数据
        self.get_step_data(client_socket.recv(1024).decode('gbk'), client_socket)
        if self.data == "1":
            self.step += 1
            client_socket.send("{}:{}".format(self.step, self.data).encode("gbk"))

    def checkplayer(self, client_socket, q):
        """getpeername()可以获取这个socket的远程ip和port"""
        # 如果q是空的，则直接将client和标识符一起放入，接下来就是等待B的连接信息
        global cli
        if q.empty():
            # A
            q.put([client_socket, 0])  # 0表示可以拿去，而1表示已经有伙伴了，
            # 等待客户端确认B的连接信息
            self.get_step_data(client_socket.recv(1024).decode('gbk'), client_socket)
            # 经过切割，将B的值放入dest
            self.data = self.data.split("-")
            self.dest = (self.data[1], int(self.data[3]))
            # 将从后台获取的远程端口发送回后台，格式同上
            data = "ip-{}-port-{}".format(self.dest[0], self.dest[1])
            self.data = data
            self.step += 1
            client_socket.send("{}:{}".format(self.step, self.data).encode("gbk"))
            # 循环判断队列中是否有匹配的cli和对应的标识符是否为1
            # while True:
            for _ in range(q.qsize()):
                cli_mid = q.get()
                if (cli_mid[0].getpeername() == self.dest) and (cli_mid[1] == 1):
                    cli = cli_mid[0]
                    cli.send("{}:{}".format(self.step, 000).encode("gbk"))  # 接着只需要单纯的告诉前面进入下一步即可
                    break
                else:
                    q.put(cli_mid)
        else:
            # while True:
            for _ in range(q.qsize()):
                # B
                cli_mid = q.get()
                if cli_mid[1] == 0:
                    # B B通过cli可以直接给A发信息
                    cli = cli_mid[0]
                    self.dest = cli.getpeername()  # 将远程的信息放入dest
                    # 使用这个cli发送信息给这个客户端，将自己的ip和post给他
                    data = "ip-{}-port-{}".format(self.host[0], self.host[1])
                    self.data = data
                    # 上述操作完成之后，将自己的client放入q，并且标识符为1，
                    q.put([client_socket, 1])
                    cli.send("{}:{}".format(self.step, self.data).encode("gbk"))  # 告诉a自己的ip和port同时通知他任务完成
                    # 如果B在这里加一，就会让原本接收A服务器发送的信息往B发送
                    # 因此还是需要等待最后一次确认
                    self.get_step_data(client_socket.recv(1024).decode('gbk'), client_socket)
                    break
                else:
                    q.put(cli_mid)
            else:
                # C
                q.put([client_socket, 0])  # 0表示可以拿去，而1表示已经有伙伴了，
                # 等待客户端确认B的连接信息
                self.get_step_data(client_socket.recv(1024).decode('gbk'), client_socket)
                # 经过切割，将B的值放入dest
                self.data = self.data.split("-")
                self.dest = (self.data[1], int(self.data[3]))
                # 将从后台获取的远程端口发送回后台，格式同上
                data = "ip-{}-port-{}".format(self.dest[0], self.dest[1])
                self.data = data
                self.step += 1
                client_socket.send("{}:{}".format(self.step, self.data).encode("gbk"))
                # 循环判断队列中是否有匹配的cli和对应的标识符是否为1
                # while True:
                for _ in range(q.qsize()):
                    cli_mid = q.get()
                    if (cli_mid[0].getpeername() == self.dest) and (cli_mid[1] == 1):
                        cli = cli_mid[0]
                        cli.send("{}:{}".format(self.step, self.data).encode("gbk"))  # 接着只需要单纯的告诉前面进入下一步即可
                        break
                    else:
                        q.put(cli_mid)
        return cli

    def choosehero(self, client_socket):
        self.data = "您可以选择英雄有：\n1：亚瑟\n2：安其拉\n"
        # 发送所有英雄给客户端
        client_socket.send("{}:{}".format(self.step, self.data).encode("gbk"))
        # 接收客户端的信息，并告诉对方自己选择的英雄和血量
        self.get_step_data(client_socket.recv(1024).decode('gbk'), client_socket)
        hero = int(self.data)-1  # 获取用户选择的英雄
        self.hero = [Hero.YaSe(), Hero.AnQiLa()][hero]
        data = "hero-{}-blod-{}".format(self.hero.name, self.hero.blod)
        self.dest_cli.send("{}:{}".format(self.step, data).encode("gbk"))
        # 接收客户端发送的英雄血量进入下一个阶段
        self.get_step_data(client_socket.recv(1024).decode('gbk'), client_socket)
        self.dest_hero_blod = int(self.data)
        self.step += 1
        client_socket.send("{}:{}".format(self.step, self.data).encode("gbk"))

    def fight(self, client_socket):
        # 只要敌方英雄的血量大于0，就可以进行战斗
        while self.dest_hero_blod > 0:
            # 获取当前可用的技能，返回给客户端
            data = "您可选的技能：\n1：普通攻击（伤害{}）\n".format(self.hero.harm)
            client_socket.send("{}:{}".format(self.step, data).encode("gbk"))
            # 接收客户端使用的技能
            self.get_step_data(client_socket.recv(1024).decode('gbk'), client_socket)
            # 将该技能的伤害发送给对方客户端
            if self.data == "1":
                harm = self.hero.harm
            elif self.data == "gogogo":
                # 用于切断点击慢的一方的连接
                break
            # 将对方血量扣除当前的伤害
            self.dest_hero_blod -= harm
            # 将对方的血量和当前使用技能发送给对方客户端
            data = "对方使用了：{}技能，您当前血量为：{}\n".format("普通攻击", self.dest_hero_blod)
            self.dest_cli.send("{}:{}".format(self.step, data).encode("gbk"))
            self.get_step_data(client_socket.recv(1024).decode('gbk'), client_socket)
        else:
            self.step += 1
            data = "win"
            client_socket.send("{}:{}".format(self.step, data).encode("gbk"))
            data = "lose"
            data += "-do"
            self.dest_cli.send("{}:{}".format(self.step, data).encode("gbk"))

    def show(self, client_socket):
        self.step = 1
        client_socket.send("{}:{}".format(self.step, self.data).encode("gbk"))


def main():
    wangzhe = WangZheServer()
    wangzhe.runferver()


if __name__ == '__main__':
    main()
