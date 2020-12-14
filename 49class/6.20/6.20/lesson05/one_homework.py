#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/20 20:05

# 输出正负浮点数，并保留两位小数,将上面的问题使用两种格式化方法输出
print('%+-.2f' % 3.1415926)
print('%+-.2f' % -3.1415926)
print('{:.2f}'.format(-3.1415926))

