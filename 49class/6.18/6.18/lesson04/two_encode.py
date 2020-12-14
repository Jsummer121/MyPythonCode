#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/18 21:11

s = '中'  # 当程序执行时，字符会以unicode形式保存到内存空间中

# 编码
s1 = s.encode('utf-8')
s2 = s.encode('GBK')

print(s)
print(s1)
print(s2)

print(type(s))  # <class 'str'>
print(type(s1))  # <class 'bytes'>
print(type(s2))  # <class 'bytes'>

# 巩固
a = '你好潭州'

# unicode--》gbk
unicode_gbk = a.encode('gbk')
print(unicode_gbk)
# unicode--》utf-8
unicode_utf8 = a.encode('utf-8')
print(unicode_utf8)

# gbk--->utf-8
gbk_utf8 = unicode_gbk.decode('GBK').encode('utf-8')
print(gbk_utf8)

# 总结：
"""
1.各个编码的相互转换都要先转换为unicode，通过unicode再转其他编码
2.GBK不止这一个
"""
unicode_gbk = a.encode('gb18030')
print(unicode_gbk)
