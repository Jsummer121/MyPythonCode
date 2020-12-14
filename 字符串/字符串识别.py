# -*- coding: utf-8 -*-

# eval()    # 识别表达式，返回值
b = '1 + 2 + 3'
print(eval(b))

# exec()  # 识别赋值语句，没有返回值
b = 'x + y + z'
x = 1
y = 2
z = 3
print(eval(b))