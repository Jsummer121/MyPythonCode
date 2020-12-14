#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/17 21:52

# 算术运算符：+，-，*，/，%，**，//
# 比较运算符：==，!=，>，<，>=，<=
# 赋值运算符：=，+=，-=，*=，/=，%=， **=，//=
# 逻辑运算符：and，or，not
# 成员运算符：in，not in

a = 10
b = 20
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)    # 取余（返回除法的余数）
print(a ** b)   # 幂
print(a // b)   # 取整除（返回商的整数部分）
# 5 / 3 = 1...2

# 比较运算符：==，!=，>，<，>=，<=
a = 10
b = 20
print(a == b)   # 等于，False
print(a != b)   # 不等于，True
print(a > b)    # 大于
print(a < b)    # 小于
print(a >= b)   # 大于等于
print(a <= b)   # 小于等于

# 赋值运算符：=，+=，-=，*=，/=，%=， **=，//=
c = a + b   # 赋值
print(c)
c += a  # ====》c = c + a    先c和a相加，然后赋值给c
print(c)
c -= a  # ===>c = c - a
print(c)
c *= a  # 乘等于
c /= a  # 除等于
c %= a  # 取余等于
c **= a  # 幂等于
c //= a  # 取整除等于
# 逻辑运算符：and，or，not
print(a and b)  # 20
print(a or b)   # 10
print(not a)    # False
# 成员运算符：in，not in
L = [1, 2, 3]
a = 3
print(a in L)   # True
print(a not in L)  # False
