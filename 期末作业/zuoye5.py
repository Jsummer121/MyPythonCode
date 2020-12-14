# -*- coding: utf-8 -*-
# 5.设计一个拥有注册和登录功能的小程序，要求：注册完成后提示注册的账号和密码，
# 登录成功后，提示欢迎登录，账号或者密码不正确时，返回相应提示。

import linecache
index ="""
                           注册          登录
                            ——           ——
                           |01|         |02|
                            ——           ——
"""
print(index)
def zhuce(): #注册的代码
    name = input("请输入用户名：")
    len1 = len(open("id.txt", "r").readlines())
    for e in range(1,len1+1,2): #判断用户名是否在文件中
        if name == linecache.getline("id.txt",e).strip():
            name = input("您输入用户名已存在，请重新输入：")
    key = input("请输入密码：")
    print("您的用户名是：{}\n您的密码为：{}".format(name,key))
    with open("id.txt","a",encoding="UTF-8") as id:
        id.write(name+"\n")
        id.write(key+"\n")
    print("请登录。。。。。。正在跳转")
    denglu()


def denglu(): #登录的代码
    name_1 = input("请输入您的用户名：")
    key_1 = input("请输入您的密码：")
    len1 = len(open("id.txt", "r").readlines())
    for e in range(1,len1+1,2): #判断用户名是否在文件中，并且查看密码是否相同
        if name_1 == linecache.getline("id.txt",e).strip():
            if key_1 == linecache.getline("id.txt",e+1).strip():
                print("欢迎登录")
            else:
                print("您输入的用户名或者密码错误，请重试。")
                denglu()


x = input("请输入您需要的操作(只有三次输入错误的机会)：")
for i in range(2):
    if not (x == "01" or x == "02"):
        x = input("您代码输入错误请重新输入（还有{}次机会）：".format(2-i))
    elif x == "01":
        zhuce()
        break
    else:
        denglu()
        break

