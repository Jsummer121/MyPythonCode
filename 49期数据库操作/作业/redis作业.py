# -*- coding: utf-8 -*-
import redis


index="下列redis-list操作系统，您可以根据您自己所需要的来输入相应的数字，进行相应的操作。"
print(index)
class redis_list:
    def __init__(self):
        self.con = redis.StrictRedis(decode_responses=True)

    def l_push(self,data1,data2,flag=True):
        if flag:
            self.con.rpush(data1,*data2)
        else:
            self.con.lpush(data1,*daat2)

    def l_range(self,data,flag=True):
        if flag:
            sec = self.con.lrange(*data)
            print('您所找的为：{}'.format(sec))
        else:
            sec = self.con.lindex(*data)
            print('您所找的为：{}'.format(sec))

    def l_lset(self,data):
        self.con.lset(*data)

    def l_pop(self,data,flag=True):
        if flag:
            self.con.rpop(data)
        else:
            self.con.lpop(data)



src=int(input('1.添加操作，2.查看操作，3.删除操作，4.修改操作：'))
lis = redis_list()

if src == 1:#添加
    da1=input('请输入想要添加的键:')
    da2=input('请输入想要添加的值:')
    da2 = tuple(da2.split(','))
    side=int(input('请输入你想加入的方向，左边为1，右边为2：'))
    if side == 2:
        lis.l_push(da1,da2)
    else:
        lis.l_push(da1, da2,flag=False)

if src == 2:#查看
    side = int(input('如果是单个查找，请输如1，多个查找请输如2：'))
    if side == 2:
        da = input('请输如查找的键和查找的起始于终止位置：')
        da = tuple(da.split(','))
        da = (da[0], int(da[1]), int(da[2]))
        lis.l_range(da)
    else:
        da = input('请输入查找的键和想看的位置')
        da = tuple(da.split(','))
        lis.l_range(da,flag=False)

if src == 3:#删除
    da = input('请输入想删除的键')
    side = int(input('请输入你想删除的方向，左边为1，右边为2：'))
    if side == 2:
        lis.l_push(da)
    else:
        lis.l_push(da,flag=False)

if src == 4:#修改
    da = input('请输如修改的键和修改的位置和修改的值：')
    da = tuple(da.split(','))
    da = (da[0], int(da[1]), da[2])
    lis.l_lset(da)