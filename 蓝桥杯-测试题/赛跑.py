# -*- coding: utf-8 -*-
t = int(input())
v1 = 3 #A速度 赢了@_@
v2 = 9 #B速度 赢了^_^
s1 = v1*t
lost_t = t%40
s2 = t//40*9+(lost_t*v2 if lost_t<=10 else 90)
if s1 > s2:
    print('@_@ {}'.format(s1))
elif s1==s2:
    print('-_- {}'.format(s1))
else:
    print('^_^ {}'.format(s2))

