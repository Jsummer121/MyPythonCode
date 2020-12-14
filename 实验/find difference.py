x=input()
y=0
a=[0,0,0]
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
a[2]=x
print(a[0],a[1],a[2])
if a[0]==a[1]:
    print('c')
else:
    if a[0]==a[2]:
        print('b')
    else:
        print('a')
