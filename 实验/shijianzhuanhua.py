x=input()
m=h=0
if x[2]==':':
    h=int(x[:2])
    m=int(x[3:])
else:
    h=int(x[:1])
    m=int(x[2:])
if h==0:
    print('0:0 AM')
if 0<h<12:
    print(x+' AM')
if h==12:
    print('12:0 PM')
if h>12:
    h-=12
    h=str(h)
    m=str(m)
    print(h+':'+m+' PM')


