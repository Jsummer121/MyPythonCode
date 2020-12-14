# -*- coding: utf-8 -*-
N,U,D = input().split(' ')
# 杆长N，每分钟爬U，休息一分钟往下滑D
t = 0
while True:
    if int(N)-1 - int(U) < (int(U) - int(D)) * t:
        print(t*2+1)
        break
    else:
        t += 1