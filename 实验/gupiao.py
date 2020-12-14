x=input()
y=0
b=[]
a=[0,0,0,0]
for i in range(len(x)):
    if x[i]==' 'and y==0:
        z=x[0:i]
        q=i
        a[y]=float(z)
        y+=1
x=x[q+1:]
for i in range(len(x)):
    if x[i]==' 'and y==1:
        z=x[0:i]
        q=i
        a[y]=float(z)
        y+=1
x=x[q+1:]
for i in range(len(x)):
    if x[i]==' 'and y==2:
        z=x[0:i]
        q=i
        a[y]=float(z)
        y+=1
x=x[q+1:]
a[3]=float(x)
f=1
if a[0]>a[3]:
    b.append('BW-Solid')
if a[0]==a[3]:
    b.append('R-Cross')
if a[0]<a[3]:
    b.append('R-Hollow')
if a[1]>a[0] and a[1]>a[3] and a[2]<a[0] and a[2]<a[3]:
    b.append('with Lower Shadow and Upper Shadow')
    f=0
if a[1]>a[0] and a[1]>a[3] and f==1:
    b.append('with Upper Shadow')
if a[2]<a[0] and a[2]<a[3] and f==1:
    b.append('with Lower Shadow')
c=' '.join(b)
print(c)
