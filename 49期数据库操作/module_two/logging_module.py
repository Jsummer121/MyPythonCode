#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/8/1 22:21

import logging

# 1.日志记录器
my_logger = logging.Logger("第一个日志处理器")  # 日志处理器对象

# 设置的第一个handler
# 2.日志处理器
fh = logging.FileHandler("you.log")
# 3.设置级别+设置格式
fh.setLevel(logging.INFO)
fmt = logging.Formatter('time：%(asctime)s - content：%(message)s')   # 日志格式器
fh.setFormatter(fmt)
# 4.定义完毕，把handler添加到logger里面去
my_logger.addHandler(fh)


# 设置第二个handler
sh = logging.StreamHandler()     # 定义handler
sh.setLevel(logging.DEBUG)  # 设置日志级别
fmt1 = logging.Formatter('time：%(asctime)s - content：%(message)s-streamhandler')
sh.setFormatter(fmt1)
my_logger.addHandler(sh)

# 设置完毕，开始使用
my_logger.info("我是日志组件--文件保存")


