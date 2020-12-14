# -*- coding: utf-8 -*-
a = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
a.sort()
print(a)
a.sort(key=lambda x:x[1])
print(a)
a.sort(key=lambda x:(x[0],x[1]))
print(a)
a.sort(key=lambda x:(-x[0],x[1]))
print(a)
a.sort(key=lambda x:(x[0],-x[1]))
print(a)
a.sort(key=lambda x:(-x[0],-x[1]))
print(a)

