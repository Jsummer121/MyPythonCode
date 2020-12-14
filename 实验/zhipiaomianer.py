n=int(input())
f=0
a=0
for y in range(101):
    if (n+199*y)/98==int((n+199*y)/98) and a==0:
        f=(n+199*y)/98
        print('%d.%d'%(y,f))
        a+=1
if a==0:
    print('No Solution')
