#1.自定义一个字符串（eg：a = “hello,world!”），用切片的方式进行逆序
a = 'hello,world!'
print(a[-6:-1]+','+a[:5]+a[-1])

#用多种方法往列表中增加值
b=[1,2,3,4]
c=[8]
b.extend([5])
b.append(6)
b.insert(6,7)
d = b+c
print(d)