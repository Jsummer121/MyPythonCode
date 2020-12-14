# 1.找出两个列表中相同的元素
a = [1,2,3,4]
b = [2,51,1,125,5,15]
c = []
for x in a:
    if x in b:
        c.append(x)
#print(c)

#2.新建一个字典
d = {}
#用3种方法往字典里面插入值
d = dict(lname = 'x',age = '20')
d.setdefault("like")
d['2name']='j'
print(d)
#用 4 种方法取出values
print(d['lname'])
print(d.get('2name'))
print(list(d.values()))
print(d.setdefault("age"))
#用2种方法取出key
print(list(d.keys()))
z = [key for(key,value) in d.items()]
print(z)

#3.定义我们学过的每种数据类型，并且注明，哪些是可变，哪些是不可变的
# list/tuple/dict/set/str
# list:可变
# tuple:不可变
# dict:可变
# set:可变
# str:可变
# int:不可变

# 数据类型的创建
e = ''  #str
f = []  #list
g = {}  #dict
h = ()  #tuple
i = set() #set
j = 1   #int

#4.列表[‘hello’,‘python’,‘!’] 拼接并输出'hello python !' （至少两种以上的方法）
A = ['hello','python','!']
B = ''.join(A)
B = list(B)
B[4] = 'o '
B[-1] = ' !'
B = ''.join(B)
k = A[0]
l = A[1]
m = A[2]
C =k+' '+l+' '+m
print(B,C)