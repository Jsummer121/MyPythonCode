# -*- coding: utf-8 -*-
# @Auther:Summer
import socket


class WangZheClient:
    step = 0
    data = ""
    dest = ""
    def __init__(self):
        # 1.创建套接字
        self.WangZhe_Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 2.绑定服务器
        self.WangZhe_Client.connect(("127.0.0.1", 8888))

    def runforver(self):
        # 1. 从server获取现在的step和data
        self.get_step_data(self.WangZhe_Client.recv(1024).decode('gbk'))
        # 通过step来进行每一步的操作
        while True:
            if self.step == 0:  # 如果是step是0，则说明是登陆操作没有完成
                # 登陆功能
                self.login()
                while self.step != 1:
                    print("密码输入错误请重试")
                    self.login()
                else:
                    print("登录成功，请选择游戏模式")
            elif self.step == 1:
                # 模式选择功能
                self.choosepattern()
                if self.step == 2:
                    print("开始匹配对手")
            elif self.step == 2:
                """人员匹配"""
                self.checkplayer()
                if self.step == 3:
                    print("对手匹配完成，请选择英雄")
            elif self.step == 3:
                """选择英雄"""
                self.choosehero()
                if self.step == 4:
                    print("英雄选择成功，准备开始对战")
            elif self.step == 4:
                "对战模式"
                self.fight()
                if self.step == 5:
                    print("该局游戏结束，准备开始新的征程")
            elif self.step == 5:
                self.get_step_data(self.WangZhe_Client.recv(1024).decode('gbk'))
            elif self.step == 1000:
                print("感谢您选择该游戏，欢迎下次光临")
                self.WangZhe_Client.close()
                break
            else:
                print("服务器内部错误，请重新登陆")
                self.WangZhe_Client.close()
                break

    # 将服务器返回的数据进行整理
    def get_step_data(self, data):
        self.step = int(data.split(":")[0])  # 获取step
        self.data = data.split(":")[1]

    # 登录模块
    def login(self):
        username = input("请输入用户名：")
        password = input("请输入密码：")
        send_data = "username-{}-password-{}".format(username, password)
        self.WangZhe_Client.send("{}:{}".format(self.step, send_data).encode("gbk"))  # 把用户名和密码发送到服务器
        # 接收信息
        self.get_step_data(self.WangZhe_Client.recv(1024).decode('gbk'))

    # 模式选择功能
    def choosepattern(self):
        self.get_step_data(self.WangZhe_Client.recv(1024).decode('gbk'))
        choose = input(self.data)
        if choose == "1":
            # 真人对战
            print("准备开启真人对战")
            self.WangZhe_Client.send("{}:{}".format(self.step, choose).encode("gbk"))
            self.get_step_data(self.WangZhe_Client.recv(1024).decode('gbk'))
        elif choose == "2":
            # 人机对战
            print("人机对战暂未开启，已帮您选择真人对战")
            choose = "1"
            self.WangZhe_Client.send("{}:{}".format(self.step, choose).encode("gbk"))
            self.get_step_data(self.WangZhe_Client.recv(1024).decode('gbk'))
        else:
            # 关闭
            self.step = 1000

    def checkplayer(self):
        # 从服务器获取对方的ip和port格式（step:ip-ip-port-port）
        self.get_step_data(self.WangZhe_Client.recv(1024).decode('gbk'))
        if self.step != 3:
            self.data = self.data.split("-")
            self.dest = (self.data[1], self.data[3])
            # 将从后台获取的远程端口发送回后台，格式同上
            data = "ip-{}-port-{}".format(self.dest[0], self.dest[1])
            self.data = data
            self.WangZhe_Client.send("{}:{}".format(self.step, self.data).encode("gbk"))
            # 获取后台发送的最后一次数据
            self.get_step_data(self.WangZhe_Client.recv(1024).decode('gbk'))
        else:
            self.WangZhe_Client.send("{}:{}".format(self.step, self.data).encode("gbk"))

    def choosehero(self):
        self.get_step_data(self.WangZhe_Client.recv(1024).decode('gbk'))
        hero = input(self.data)  # 获取后台的英雄，然后让用户选择
        while (hero != "1") and (hero != "2"):
            hero = input("您输入的号码有误，请重新输入：\n{}".format(self.data))
        self.data = hero
        # 获取用户输入的英雄号码，然后传入后台，等待进入对战阶段
        self.WangZhe_Client.send("{}:{}".format(self.step, self.data).encode("gbk"))
        # 接收对方的英雄选择
        self.get_step_data(self.WangZhe_Client.recv(1024).decode('gbk'))
        hero = self.data.split("-")[1]
        self.data = self.data.split("-")[3]
        print("对方选择的英雄为：{},血量是{}".format(hero, self.data))
        # 将对方英雄的血量发送到后台，供服务器保存
        self.WangZhe_Client.send("{}:{}".format(self.step, self.data).encode("gbk"))
        # 接收自己服务器返回的step
        self.get_step_data(self.WangZhe_Client.recv(1024).decode('gbk'))

    def fight(self):
        while True:
            self.get_step_data(self.WangZhe_Client.recv(1024).decode('gbk'))
            if self.data == "lose":
                print("对不起，你输了")
                break
            elif self.data == "win":
                print("恭喜你，你赢了")
                break
            elif self.data == "lose-do":
                print("对不起，你输了")
                self.data = "gogogo"
                self.WangZhe_Client.send("{}:{}".format(self.step, self.data).encode("gbk"))
                break
            elif self.data == "win-do":
                print("恭喜你，你赢了")
                self.data = "gogogo"
                self.WangZhe_Client.send("{}:{}".format(self.step, self.data).encode("gbk"))
                break
            else:
                # data为可用的技能
                self.data = input(self.data)
                while self.data != "1":
                    self.data = input("您输入的技能有误，请重新输入\n{}".format(self.data))
                self.WangZhe_Client.send("{}:{}".format(self.step, self.data).encode("gbk"))  # 把技能发送给服务器
            # 接收对方返回的自己当前血量和技能值，进行打印
            self.get_step_data(self.WangZhe_Client.recv(1024).decode('gbk'))
            print(self.data)
            if self.data == "lose-do":
                print("对不起，你输了")
                self.data = "gogogo"
                self.WangZhe_Client.send("{}:{}".format(self.step, self.data).encode("gbk"))
                break
            elif self.data == "win-do":
                print("恭喜你，你赢了")
                self.data = "gogogo"
                self.WangZhe_Client.send("{}:{}".format(self.step, self.data).encode("gbk"))
                break
            else:
                # 确认信息收到，将data变成ok返回给服务器进入下一轮
                self.data = "ok"
                self.WangZhe_Client.send("{}:{}".format(self.step, self.data).encode("gbk"))


def main():
    wangzheClient = WangZheClient()
    wangzheClient.runforver()


if __name__ == '__main__':
    main()
