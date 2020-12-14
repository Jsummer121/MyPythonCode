n,m =input().split()
a = []
b = []
for i in range(65,65+int(m)):
    a.append(chr(i))
b.append(a)
for i in range(1,int(n)):
    c = b[i-1]
    c = c[:-1]
    c.insert(0,chr(65+i))
    b.append(c)
for i in range(len(b)):
    print(''.join(b[i]))
