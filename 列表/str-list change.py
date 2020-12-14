a = 'askfkkgasilfgiassfidii'
b = list(a)      #将字符串转换成列表
b.sort()  #利用列表进行排序
c = b
c.reverse()      #反向
d = ''.join(b)   #把正向列表转化为字符串
e = ''.join(c)   #把反向列表转化为字符串
print(b,c,d)
f = 'a,e,fae,eg,ag,ad,hga,ga,asg'
g = f.split(',')
print(g)


