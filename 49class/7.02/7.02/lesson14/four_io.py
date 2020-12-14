#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/2 21:04

# io流
import io   # 导入io模块

sio = io.StringIO()  # 创建一个对象（进行保存读取）--->字符流

sio.write("hello")  # 写
print(sio.getvalue())   # 读

sio.close()  # close后内容就没有了


bio = io.BytesIO()

bio.write(b'abcd')
print(bio.getvalue())

bio.close()
