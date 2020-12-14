# -*- coding: utf-8 -*-
x = -12450
if -2**32 < x < 2**31-1:
    x = str(x)
    if("-" not in x):
        x = int(x[::-1])
        print(x)
    else:
        x = x[1:]
        x = int(x[::-1])
        print(-x)