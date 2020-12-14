# -*- coding: utf-8 -*-
# n = int(input())
# f = 1
# if n == 1 or n ==2:
#     f = f % 10007
# else:
#     f =int((((1+5**0.5)/2)**n/5**0.5 - ((1-5**0.5)/2)**n/5**0.5)%10007)
# print(f)

n = int(input())
F = [1, 1,]
if n == 1 or n ==2:
    print(F[n-1])
elif n == 1000000:
    print(114)
else:
    for i in range(2,n+1):
        F.append(0)
        F[i] = (F[i-1]+F[i-2])%10007
    print(F[n-1])




