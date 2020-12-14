#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/30 21:23

import hashlib

res = hashlib.new('md5', '淘气包'.encode())
print(res)  # <md5 HASH object @ 0x7fa67c687580>
print(res.digest())  # b'\x1f(\xa5\xb8v\xbf\x96\x10\x01\xc8a\xcb\x86=\xb9m'
print(res.hexdigest())  # 1f28a5b876bf961001c861cb863db96d

res = hashlib.sha256('淘气包'.encode())
print(res)  # <sha256 HASH object @ 0x7fce6efe9508>
print(res.hexdigest())  # b38d80a1442acd6fc7e5254dbc610a84200c956ffff6d80d5f846ce3f8948b62

# update:先不写入值，需要的时候再update一下，可以多次使用
res = hashlib.sha1()

res.update('精灵'.encode())
print(res.hexdigest())  # 6ff8f715acf0e19d02f416b34aa6cfb0fb521f70

res.update('阙林国 '.encode())
print(res.hexdigest())  # ddd2186e6d3d6be4bf9d01c68280b74483ae3858

"""
注册：原始账号+原始密码---->md5加密---->保存加密后的字符串
登录：原始账号+原始密码---->md5加密---->传送到后台，验证加密后的字符串是否相等
"""



