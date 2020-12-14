#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/8/1 21:58

import logging

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='my.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format='时间:%(asctime)s-文件名:%(filename)s-行号:%(lineno)s-内容:%(message)s')

a = 8 + 6
logging.debug(a)    # 时间:2019-08-01 22:04:58,985-文件名:py_logging_2.py-行号:10-内容:14

# 注意：两次配置，只有第一次生效，第二次是无效的



