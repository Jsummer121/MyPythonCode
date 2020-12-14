# -*- coding: utf-8 -*-
da = input('请输如查找的键和查找的起始于终止位置：')
da = tuple(da.split(','))
da = (da[0], int(da[1]), int(da[2]))
print(da)