#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/18 21:11

s = '中'  # 当程序执行时，字符会以unicode形式保存到内存空间中所以s的形式为unicode 是str

# 编码
s1 = s.encode('utf-8') #将Unicode进行编码变成utf-8新式
s2 = s.encode('GBK')   #将Unicode进行编码变成gbk新式

print(s)
print(s1)
print(s2)

print(type(s))  # <class 'str'>
print(type(s1))  # <class 'bytes'> 两位
print(type(s2))  # <class 'bytes'> 三位

# 巩固
a = '你好潭州'

# unicode--》gbk
unicode_gbk = a.encode('gbk') #八位
print(unicode_gbk)
# unicode--》utf-8
unicode_utf8 = a.encode('utf-8')  #12位
print(unicode_utf8)

# gbk--->utf-8
gbk_utf8 = unicode_gbk.decode('GBK').encode('utf-8') #先用decode进行解码变成unicode，然后再用encode进行编码。
print(gbk_utf8)   #八位先进行解码decode（‘GBK’）变成Unicode然后进行编码 encode（utf-8）变成12位

# 总结：
"""
1.各个编码的相互转换都要先转换为unicode，通过unicode再转其他编码
2.GBK不止这一个
"""
unicode_gbk = a.encode('gb18030')
print(unicode_gbk)
