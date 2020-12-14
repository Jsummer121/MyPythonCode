#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/5 20:33
# 元字符： .  *  ?  +  []  ()  \  ^  $
# 1.普通字符
import re
# re.findall():将符合规则的字符串，以列表的形式，全部返回。
s1 = "testing"
s2 = "Testing"
r1 = re.findall("test", s1)
print(r1)   # ['test']
r2 = re.findall("test", s2)
print(r2)   # []
r3 = re.findall("test", s2, re.I)   # 修饰符re.I:是匹配对大小写不敏感
print(r3)   # ['Test']

# 2.通配符.：匹配除换行符"\n"以外的单个字符
s1 = "testing"
s2 = "testing\n"
r1 = re.findall(".", s1)
print(r1)
r2 = re.findall(".", s2)
print(r2)
r3 = re.findall(".", s2, re.S)  # 修饰符re.S:使.匹配包括换行符在内的单个字符
print(r3)

# 3.^脱字符:匹配输入字符串的开始位置
s = 'testing\nTesting\ntest'
r1 = re.findall("^test", s)
print(r1)   # ['test']
r2 = re.findall("^test", s, re.M)   # 修饰符re.M：多行匹配
print(r2)
r3 = re.findall("^test", s, re.M | re.I)    # 多个修饰符通过OR(|)来指定
print(r3)

# 4.$匹配输入字符串的结束位置
s = 'testing\nTesting\ntest'
r1 = re.findall("testing$", s)
print(r1)   # []
r2 = re.findall("testing$", s, re.M)
print(r2)   # ['testing']
r3 = re.findall("testing$", s, re.M | re.I)
print(r3)   # ['testing', 'Testing']

# 5. * + ? 匹配前面的子表示式的次数（*(0-无穷）任意次，+（1-无穷）大于等于1，？（0|1）零次或一次）
s = 'z\nzo\nzoo\nzooo'

r1 = re.findall("zo*", s, re.M)
print(r1)   # ['z', 'zo', 'zoo']
r2 = re.findall("zo+", s, re.M)
print(r2)
r3 = re.findall("zo?", s, re.M)    # zo? z  zo
print(r3)

# 6.{}重复元字符，也是控制匹配子表达式次数的
s = 'z\nzo\nzoo\nzooo'
r1 = re.findall("zo*", s, re.M)
print(r1)   # ['z', 'zo', 'zoo', 'zooo']
r2 = re.findall("zo{0,}", s, re.M)
print(r2)   # ['z', 'zo', 'zoo', 'zooo']
r2 = re.findall("zo+", s, re.M)
print(r2)   # ['zo', 'zoo', 'zooo']
r2 = re.findall("zo{1,}", s, re.M)
print(r2)   # ['zo', 'zoo', 'zooo']
r3 = re.findall("zo?", s, re.M)
print(r3)   # ['z', 'zo', 'zo', 'zo']
r3 = re.findall("zo{0,1}", s, re.M)
print(r3)   # ['z', 'zo', 'zo', 'zo']

#
r4 = re.findall("zo{2}", s, re.M)
print(r4)   # ['zoo', 'zoo']

# 7.[]字符组。大括号{}代表次数，中括号[]代表内容
s = 'test\nTesting\nzoo'

r1 = re.findall("[eio]", s, re.M)   # 匹配包含的任意字符
print(r1)   # ['e', 'e', 'i', 'o', 'o']

r1 = re.findall("[e-o]", s, re.M)   # 匹配包含区间的任意字符efghigklmno
print(r1)   # ['e', 'e', 'i', 'n', 'g', 'o', 'o']

r1 = re.findall("^[eio]", s, re.M)   # 匹配以[eio]包含的任意字符开头的字符
print(r1)   # []

r1 = re.findall("[^eio]", s, re.M)  # 匹配[]未包含的任意字符
print(r1)   # ['t', 's', 't', '\n', 'T', 's', 't', 'n', 'g', '\n', 'z']

r1 = re.findall("[^e-o]", s, re.M)   # 匹配[]未包含的任意字符
print(r1)   # ['t', 's', 't', '\n', 'T', 's', 't', '\n', 'z']

# 8.|选择元字符
s = 'z\nzood\nfood'
r = re.findall("z|food", s, re.M)
print(r)    # ['z', 'z', 'food']
r = re.findall("[z|f]ood", s, re.M)
print(r)    # ['zood', 'food']

# 9.()：分组元字符，匹配表达式的字符保存到一个临时区域，返回值为（）内的内容
s = 'z\nzood\nfood'
r = re.findall("[z|f]o*", s, re.M)
print(r)    # ['z', 'zoo', 'foo']
r = re.findall("[z|f](o*)", s, re.M)
print(r)    # ['', 'oo', 'oo']

# 10.
# 取消字符串的转义在前面加r或者\
# 取消正则语法的转义,加\
# s = 'z\nzood\nfood'
# print(s)
# s1 = r'z\nzood\nfood'
# print(s1)
# s2 = 'z\\nzood\\nfood'
# print(s2)
s = '12345@qq.com'
r = re.findall("\.", s)
print(r)

# 11.贪婪模式和非贪婪模式
s = "abcadcaec"
r1 = re.findall(r"ab.*c", s)    # 贪婪模式:.*, .+尽可能多的匹配字符
print(r1)   # ['abcadcaec']

r1 = re.findall(r"ab.*?c", s)    # 非贪婪模式:尽可能少的匹配字符
print(r1)   # ['abc']


