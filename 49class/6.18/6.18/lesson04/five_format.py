#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/18 22:13

# %是传统方法，format是python特有

year = 2019
month = 6
day = 18
# 格式化日期
print('%04d-%02d-%02d' % (year, month, day))    # %02d:输出2位整数，不足位用补住

f = 3.141
print("%06.2f" % f)  # %06.2f保留宽度为6，小数2位的浮点数，不足位用0补足

print('%o' % 10)
print('%02x' % 10)


# format
test = "name:%s,age:%d,nick_name:%s" % ("狐狸", 18, "星翼")
print(test)
test = "name:{},age:{},nick_name:{}".format("狐狸", 18, "星翼")
print(test)

test = "name:{0},age:{1},nick_name:{0}".format(*["狐狸", 18])
print(test)
test = "name:{name},age:{age},nick_name:{name}".format(**{"name": '勿忘我', "age": 18, "height": 168})
print(test)

test = "numbers: {:b}, {:o}.{:d},{:x},{:X},{:%}".format(10, 10, 10, 10, 10, 10, 10)
print(test)
test = "numbers: {num:b}, {num:o}.{num:d},{num:x},{num:X},{num:%}".format(num=10)
test = "numbers: {0:b}, {0:o}.{0:d},{0:02x},{0:X},{0:%}".format(10)
print(test)
print('{:.2f}'.format(3.1415926))
