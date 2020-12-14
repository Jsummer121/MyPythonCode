#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/30 22:01

import base64

data = '你好潭州'   # 1个中文是三个字节，base64是三个字节转4个字节
res = base64.b64encode(data.encode())
print(res)  # b'5L2g5aW95r2t5bee'

# 字节数不是3的倍数,少的字节用=补全
data = 'hello world'    # 11个字节
res = base64.b64encode(data.encode())
print(res)  # b'aGVsbG8gd29ybGQ='

data = 'hello worl'    # 10个字节
res = base64.b64encode(data.encode())
print(res)  # b'aGVsbG8gd29ybA=='

# https://baike.baidu.com/item/base64/8545775?fr=aladdin
# F:\class49\database_49\module_one\base64_py.py
# 如果编码后的数据是用来做url或者文件的路径的，选择base64.urlsafe_b64encode()方式编码
data = 'hello world 你好潭州 我就是我,不一样的烟火'
res = base64.b64encode(data.encode())
print(res)
res = base64.urlsafe_b64encode(data.encode())
print(res)  # /变成_,+变成-

# 解码
data = '你好潭州'   # 1个中文是三个字节，base64是三个字节转4个字节
res = base64.b64encode(data.encode())
print(res)  # b'5L2g5aW95r2t5bee'
print(base64.b64decode(res).decode())    # b'\xe4\xbd\xa0\xe5\xa5\xbd\xe6\xbd\xad\xe5\xb7\x9e'



