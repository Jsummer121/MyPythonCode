x=0
y=[]
q=c=d=e=0
z=1
if x==0:
    print(x)
else:
    for o in range(x//2):
      z=x//2
      q=x-z*2
      y.append(q)
      x=z
    y.reverse()
    b=y[-4:]
    a=y[-8:-4]
    c=int(a[0]*8+a[1]*4+a[2]*2+a[3]*1)
    d=int(b[0]*8+b[1]*4+b[2]*2+b[3]*1)
    e=c*10+d
    print(e)

