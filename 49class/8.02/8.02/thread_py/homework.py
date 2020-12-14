#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/8/2 19:57
from datetime import datetime


# 1.写一个程序能接收用户输入出生日期从而计算出用户活了多久
# def get_days(birthday):  # strftime strptime
#     bir = datetime.strptime(birthday, '%Y-%m-%d')
#     now = datetime.now()
#     days = now - bir
#     print(days)  # 7362 days, 20:08:18.270984
#     print("您出生到现在已经过去了{}天".format(days.days))


# if __name__ == '__main__':
#     birthday = input("请输入您的生日(请使用2019-08-02这种格式)>>>")
#     get_days(birthday)

# 2.使用logging模块化组件实现能记录错误信息到文件的程序，并在程序里制造错误，
# 看错误信息是否被记录下来
import logging

# 1.定义日志记录器
# 2.程序制造错误


def create_logger():
    """创建日志记录器"""
    my_logger = logging.Logger("fei")
    fh = logging.FileHandler("my.log")
    fh.setLevel(logging.INFO)
    fmt = logging.Formatter("time:%(asctime)s - message:%(message)s")
    fh.setFormatter(fmt)
    my_logger.addHandler(fh)

    return my_logger


if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as e:
        logger = create_logger()
        logger.error(e)     # 记录报错信息

now = datetime.now()
print(now.strftime("%Y年%m-%d %H:%M:%S"))
