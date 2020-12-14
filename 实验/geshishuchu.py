x='2.12 88 c 4.7'
y=0
a=[0,0,0,0]
for i in range(len(x)):
    if x[i]==' 'and y==0:
        z=x[0:i]
        q=i
        a[y]=z
        y+=1
x=x[q+1:]
for i in range(len(x)):
    if x[i]==' 'and y==1:
        z=x[0:i]
        q=i
        a[y]=z
        y+=1
x=x[q+1:]
for i in range(len(x)):
    if x[i]==' 'and y==2:
        z=x[0:i]
        q=i
        a[y]=z
        y+=1
x=x[q+1:]
a[3]=x
a[0]=float(a[0])
a[3]=float(x)
print('%s %s %.2f %.2f'%(a[2],a[1],a[0],a[3]))
