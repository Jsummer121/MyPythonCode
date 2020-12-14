#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/8/1 21:41
from datetime import datetime
import logging

now = datetime.now()
# print(now)
# logging.info(now)
# logging.warning(now)    # WARNING:root:2019-08-01 21:43:51.928280

# 可以把输出的信息分成多个级别
# logging.basicConfig(level=logging.DEBUG)    # 注意不要小写

# logging.debug(now)  # 最低级别
# logging.info(now)
# logging.warning(now)
# logging.error(now)
# logging.critical(now)   # 最高级别

logging.basicConfig(level=logging.DEBUG)    # 注意不要小写
# logging.basicConfig(level=logging.INFO)    # 注意不要小写

# 应用：调试
a = 2 + 3
# print(a)
logging.debug(a)
b = a - 1
# print(b)
logging.debug(b)
c = b / 2
# print(c)
logging.debug(c)
d = c * 8
# print(d)
logging.debug(d)
e = d ** 2
print(e)
